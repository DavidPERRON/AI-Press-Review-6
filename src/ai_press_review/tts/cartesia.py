from __future__ import annotations

import asyncio
import base64
import json
import logging
import math
import re
import time
import uuid
import wave
from pathlib import Path

import websockets

from ..settings import load_settings

logger = logging.getLogger(__name__)

CARTESIA_WEBSOCKET_URL = 'wss://api.cartesia.ai/tts/websocket'

# Phase 8 / T5: raw PCM sample rate for the websocket stream. 44.1kHz matches
# the previous /tts/bytes WAV output (pcm_f32le @ 44100) at half the bandwidth
# (16-bit vs 32-bit) with no audible loss for speech.
WEBSOCKET_SAMPLE_RATE = 44100


# ─────────────────────────────────────────────────────────────────────────────
# Pronunciation normalization
# ─────────────────────────────────────────────────────────────────────────────
#
# Phonetic respelling is applied ONLY to the text sent to the TTS engine. The
# stored script.txt stays canonical ("BERT", "GPT", "TSMC") so transcripts and
# captions remain readable. Tables are SHARED across locales for acronyms that
# share a spelling (GPT, API, TSMC) and EN/FR-specific only when the locales
# pronounce the letters differently (FR "I. A." vs EN "A. I.").
#
# Rules of thumb when adding entries:
#   • An ALL-CAPS acronym pronounced letter-by-letter → use spaced letters with
#     dots ("T. S. M. C.") so Cartesia's prosody respects each letter as its
#     own beat. Without dots the engine often slurs ("teesemsee").
#   • An acronym pronounced as a word (NASA, NVIDIA) → respell phonetically.
#   • Mixed case (iOS, OpenAI) → respell with the camel-case word breaks made
#     explicit ("Open A. I.").
#   • Word boundaries are enforced via \b so "BERTHA" / "ROBERTA" are safe.
#
# 2026-04-16 expansion driven by listener feedback that TSMC, GPT, IPO, USA
# were being spelled letter by letter as if they were words ("tee-ess-em-see"
# instead of "T. S. M. C."). The earlier prompt instruction telling the LLM
# the voice would "read the letters" was misleading — the voice DOES read
# letters but only when they are spaced and dotted. We now do that here at
# normalization time so the LLM doesn't have to think about it.


_SPELL_OUT_COMMON: dict[str, str] = {
    # Companies / chip houses
    'TSMC': 'T. S. M. C.',
    'AMD': 'A. M. D.',
    'IBM': 'I. B. M.',
    'AWS': 'A. W. S.',
    'GCP': 'G. C. P.',
    'HPE': 'H. P. E.',
    'SAP': 'S. A. P.',
    # Models / families
    'GPT': 'G. P. T.',
    'BERT': 'Burt',   # pronounced as a word in EN
    'LLM': 'L. L. M.',
    'LLMs': 'L. L. M. s',
    'SLM': 'S. L. M.',
    'SLMs': 'S. L. M. s',
    'LLaMA': 'lama',
    'LoRA': 'lora',
    'MoE': 'M. O. E.',
    'RAG': 'rag',     # retrieval-augmented generation — pronounced as a word
    'RLHF': 'R. L. H. F.',
    'PEFT': 'P. E. F. T.',
    # Compute / infra
    'GPU': 'G. P. U.',
    'GPUs': 'G. P. U. s',
    'CPU': 'C. P. U.',
    'CPUs': 'C. P. U. s',
    'TPU': 'T. P. U.',
    'TPUs': 'T. P. U. s',
    'NPU': 'N. P. U.',
    'HPC': 'H. P. C.',
    'API': 'A. P. I.',
    'APIs': 'A. P. I. s',
    'MCP': 'M. C. P.',  # Model Context Protocol
    'SDK': 'S. D. K.',
    'SDKs': 'S. D. K. s',
    'CLI': 'C. L. I.',
    'IDE': 'I. D. E.',
    'CI': 'C. I.',
    'CD': 'C. D.',
    'SaaS': 'sass',
    'PaaS': 'pass',
    'IaaS': 'eye-ass',
    'VPN': 'V. P. N.',
    # Org titles / business
    'CEO': 'C. E. O.',
    'CTO': 'C. T. O.',
    'CFO': 'C. F. O.',
    'COO': 'C. O. O.',
    'CIO': 'C. I. O.',
    'CISO': 'C. I. S. O.',
    'IPO': 'I. P. O.',
    'M&A': 'M. and A.',
    'VC': 'V. C.',
    'PE': 'P. E.',
    'ROI': 'R. O. I.',
    'KPI': 'K. P. I.',
    'KPIs': 'K. P. I. s',
    # AI-specific acronyms
    'AI': 'A. I.',       # English: ay-eye
    'AGI': 'A. G. I.',
    'ASI': 'A. S. I.',
    'NLP': 'N. L. P.',
    'ML': 'M. L.',
    'TTS': 'T. T. S.',
    'ASR': 'A. S. R.',
    'OCR': 'O. C. R.',
    'CV': 'C. V.',       # computer vision in context
    'RL': 'R. L.',
    # Geographies / institutions
    'USA': 'U. S. A.',
    'EU': 'E. U.',
    'UK': 'U. K.',
    'UAE': 'U. A. E.',
    'NATO': 'NATO',  # already pronounced as a word
    'UN': 'U. N.',
    # Tech / formats
    'iOS': 'eye-O. S.',
    'macOS': 'mac-O. S.',
    'PDF': 'P. D. F.',
    'PDFs': 'P. D. F. s',
    'HTML': 'H. T. M. L.',
    'CSS': 'C. S. S.',
    'JSON': 'jay-son',
    'YAML': 'yamel',
    'XML': 'X. M. L.',
    'URL': 'U. R. L.',
    'URLs': 'U. R. L. s',
    'HTTP': 'H. T. T. P.',
    'HTTPS': 'H. T. T. P. S.',
    'ONNX': 'O. N. N. X.',
    # Brands / camelCase
    'OpenAI': 'Open A. I.',
    'NVIDIA': 'en-vidia',
    'NASA': 'NASA',
    # Research jargon
    'arXiv': 'ar-kive',
    'LaTeX': 'Lay-Tech',
    'NeurIPS': 'noor-ips',
    'ICML': 'I. C. M. L.',
    'ACL': 'A. C. L.',
    'ICLR': 'I. C. L. R.',
    'FAISS': 'fais',   # Facebook AI Similarity Search — pronounced as a word
}

_SPELL_OUT_FR_OVERRIDES: dict[str, str] = {
    # FR-specific letter pronunciations and very common French acronyms.
    'AI': 'A. I.',          # FR keeps the English form when it appears in source quotes
    # IA: deliberately NOT dot-spelled — 'I. A.' caused a stiff, mechanical
    # two-beat pause ("I [stop] A [stop]") that sounded unnatural in French.
    # Cartesia's native FR prosody (cartesia_language='fr') pronounces the bare
    # letters "IA" fluidly as "ee-ah" without any override needed.
    # 'IA': removed — handled by native French TTS
    'PDG': 'P. D. G.',      # Président-directeur général (= CEO)
    'DG': 'D. G.',          # Directeur général
    'DSI': 'D. S. I.',      # Directeur des systèmes d'information (= CIO)
    'PME': 'P. M. E.',
    'PMI': 'P. M. I.',
    'TPE': 'T. P. E.',
    'UE': 'U. E.',
    'OTAN': 'OTAN',         # Already pronounced as a word
    'ONU': 'O. N. U.',
    'RGPD': 'R. G. P. D.', # Règlement général sur la protection des données (= GDPR)
    'PIB': 'P. I. B.',      # Produit intérieur brut (= GDP)
    'GAFAM': 'GAFAM',       # Pronounced as a word in French
    'R&D': 'R. et D.',      # Recherche et développement
    # FR letter names differ from EN — explicit dotted spacing keeps both safe
    # because Cartesia respects the locale flag for individual letter prosody.
    'BERT': 'Beurt',
    'LaTeX': 'La-Tek',
}

# Build the per-locale lookup tables once at import time. Patterns use \b so
# token boundaries are enforced (no false-hit on ROBERTA, BERTHA, NASAQ, etc.).
def _compile_pronunciation_table(table: dict[str, str]) -> dict[str, str]:
    return {rf'\b{re.escape(key)}\b': value for key, value in table.items()}


_PRONUNCIATIONS_EN: dict[str, str] = _compile_pronunciation_table(_SPELL_OUT_COMMON)

_PRONUNCIATIONS_FR: dict[str, str] = _compile_pronunciation_table(
    {**_SPELL_OUT_COMMON, **_SPELL_OUT_FR_OVERRIDES}
)


# ─────────────────────────────────────────────────────────────────────────────
# Whitespace normalization & trailing-pause cleanup
# ─────────────────────────────────────────────────────────────────────────────
#
# 2026-04-16: a final-paragraph "pause bizarre" (~1 second of dead air at the
# very end of FR episodes) was traced to the tomorrow_concept paragraph being
# preceded by stray whitespace from earlier normalization passes, plus optional
# trailing ellipsis tokens that the engine extends into a long unfilled tail.

_MULTISPACE = re.compile(r'[ \t]{2,}')
_SPACE_BEFORE_NEWLINE = re.compile(r'[ \t]+\n')
_TRIPLE_NEWLINE = re.compile(r'\n{3,}')
_TRAILING_PAUSE_TOKENS = re.compile(r'(?:\.{2,}|\s+\.\s*)+$')
_LONG_SENT_BREAK = re.compile(r'[,;]\s')


def _normalize_tts_whitespace(text: str) -> str:
    """Collapse double-spaces, strip trailing whitespace per line, cap blank lines."""
    text = _MULTISPACE.sub(' ', text)
    text = _SPACE_BEFORE_NEWLINE.sub('\n', text)
    text = _TRIPLE_NEWLINE.sub('\n\n', text)
    return text.strip()


def _strip_trailing_pause_tokens(text: str) -> str:
    """Remove any trailing ellipsis or floating-period tokens at the very end.

    Cartesia treats a final ellipsis as a long awaited-continuation cue and
    stretches the closing silence well past the natural sentence end. The very
    last character we hand the engine should be a single '.', '?' or '!' with
    no whitespace after.
    """
    return _TRAILING_PAUSE_TOKENS.sub('.', text.rstrip())


# Matches remaining ALL-CAPS tokens (3-5 letters) that are still in the script
# after the known-table normalization pass.
# Minimum 3: 2-letter tokens (IA, AI, EU, UK, ML, RL …) are either already
#   handled by the static table OR, like FR "IA", must be left bare so the
#   native TTS engine (cartesia_language=fr) can pronounce them naturally.
#   Auto-spelling "I. A." is exactly the mechanical two-beat we removed.
# Maximum 5: avoids touching proper names written all-caps (SOLARIS, AURORA …).
_UNKNOWN_ACRONYM = re.compile(r'\b[A-Z]{3,5}\b')

# Words that look like acronyms but should never be auto-spelled — either
# because they're already in the pronunciation table or because they sound
# fine when read as words by the TTS engine.
_AUTO_SPELL_SKIP: frozenset[str] = frozenset({
    'NATO', 'NASA', 'FAISS', 'SWIFT', 'OPEC', 'OTAN',
})


def _auto_spell_unknown_acronyms(text: str, locale: str) -> tuple[str, list[str]]:
    """Dot-spell any ALL-CAPS token (3-7 letters) not yet normalized.

    Run AFTER normalize_pronunciations() so already-handled entries are gone.
    Returns (rewritten_text, sorted list of tokens that were auto-spelled).

    This "run-time accumulation" approach means a newly coined acronym (e.g. a
    paper codename, a product launch abbreviation) is automatically spelled out
    letter-by-letter rather than mispronounced, without requiring a table update.
    The returned list is logged by synthesize_script() so you can review and
    optionally promote frequently seen entries to the static table.
    """
    found: list[str] = []

    def replace(m: re.Match) -> str:
        word = m.group(0)
        if word in _AUTO_SPELL_SKIP:
            return word
        spelled = '. '.join(list(word)) + '.'
        found.append(word)
        return spelled

    result = _UNKNOWN_ACRONYM.sub(replace, text)
    return result, sorted(set(found))


def _cap_sentence_length(text: str, max_chars: int = 240) -> str:
    """Break lines longer than max_chars at a natural comma/semicolon pause point.

    Cartesia's prosody model tapers off on very long unbroken utterances — the
    engine predicts a breath point that never arrives and compensates by winding
    down the voice volume ('running out of air' effect). Breaking any sentence
    longer than ~240 chars at its first suitable comma (≥ 80 chars in) gives the
    engine a clear sentence boundary with full volume on the second half too.

    Each split inserts a '\\n' so split_script() sees two separate paragraphs and
    can place them in independent chunks when they overflow. Applied to TTS input
    only; script.txt stays canonical.
    """
    return '\n'.join(_shorten_line(line, max_chars) for line in text.split('\n'))


def _shorten_line(line: str, max_chars: int) -> str:
    """Recursively shorten one line until every segment is ≤ max_chars."""
    if len(line) <= max_chars:
        return line
    # Find the first comma/semicolon between positions [80, max_chars]
    for m in _LONG_SENT_BREAK.finditer(line):
        pos = m.start()
        if 80 <= pos <= max_chars:
            first = line[:pos].rstrip() + '.'
            rest = line[pos + 1:].lstrip()
            if rest:
                rest = rest[0].upper() + rest[1:]
            return first + '\n' + _shorten_line(rest, max_chars)
    return line  # no suitable split point — leave as is


def normalize_pronunciations(text: str, locale: str) -> str:
    """Rewrite known-mispronounced acronyms to their spoken-language form.

    Applied right before chunking so Cartesia hears the phonetic version
    while `script.txt` (read by humans, used for transcripts) keeps the
    canonical uppercase/camelcase spelling.

    The 2026-04-16 cleanup also strips the FR sentence-boundary ellipsis
    insertion that previously over-fired (one ellipsis per sentence × ~60
    sentences per episode) and produced an audible drum-roll of pauses.
    Cartesia's native FR prosody at speed 0.82 carries the breath without
    the manual hints.
    """
    is_fr = (locale or '').lower().startswith('fr')
    table = _PRONUNCIATIONS_FR if is_fr else _PRONUNCIATIONS_EN
    for pattern, phon in table.items():
        text = re.sub(pattern, phon, text)
    return text


def split_script(text: str, max_chars: int = 1800) -> list[str]:
    """Split the script into paragraph-aligned chunks under max_chars each.

    Each chunk is sent as a separate transcript within a single shared
    context_id websocket session, so Cartesia keeps prosody and voice state
    across the whole script. There are no per-chunk restart artefacts.
    """
    paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
    chunks: list[str] = []
    current = ''
    for paragraph in paragraphs:
        candidate = f"{current}\n\n{paragraph}".strip() if current else paragraph
        if len(candidate) <= max_chars:
            current = candidate
        else:
            if current:
                chunks.append(current)
            current = paragraph
    if current:
        chunks.append(current)
    return chunks


def synthesize_script(script: str, output_path: Path, local_preview: bool = False) -> dict:
    """Render the full script as a single continuous MP3 via websocket continuity.

    Phase 8 / T5: replaced /tts/bytes per-chunk POSTs (plus post-hoc pydub
    crossfade) with /tts/websocket on a shared context_id. Test C user
    ear-test confirmed seams are inaudible under continuity mode — the
    model treats the whole script as one utterance, so there are no
    independent "chunk restart" transients and no inter-chunk level mismatch.
    """
    from pydub import AudioSegment

    settings = load_settings(local_preview=local_preview)
    if not settings.cartesia_api_key:
        raise ValueError('CARTESIA_API_KEY is required for TTS')
    if not settings.cartesia_voice_id:
        raise ValueError('CARTESIA_VOICE_ID is required for TTS')

    # Phonetic respelling for acronyms Cartesia otherwise spells letter by
    # letter (LaTeX → "L-A-T-E-X" instead of "Lay-Tech", etc.). Only affects
    # what the TTS hears; script.txt stays canonical.
    spoken_script = normalize_pronunciations(script, settings.locale or 'en')
    # Auto-spell any ALL-CAPS tokens not covered by the static table.
    spoken_script, auto_spelled = _auto_spell_unknown_acronyms(spoken_script, settings.locale or 'en')
    if auto_spelled:
        logger.info(
            'TTS auto-spelled %d unknown acronym(s): %s — '
            'add to _SPELL_OUT_COMMON if pronunciation is wrong',
            len(auto_spelled), ', '.join(auto_spelled),
        )
    spoken_script = _normalize_tts_whitespace(spoken_script)
    spoken_script = _strip_trailing_pause_tokens(spoken_script)
    # Cap long sentences so Cartesia never tapers volume on a single utterance.
    # Splits any line > 240 chars at its first usable comma/semicolon ≥ 80 chars in.
    spoken_script = _cap_sentence_length(spoken_script)
    chunks = split_script(spoken_script, max_chars=settings.tts_chunk_max_chars)
    if not chunks:
        raise ValueError('Script is empty — cannot synthesize audio')

    # Final guard: the last chunk should not end on a pause token either.
    chunks[-1] = _strip_trailing_pause_tokens(chunks[-1])

    output_path.parent.mkdir(parents=True, exist_ok=True)

    start = time.monotonic()
    tts_mode = getattr(settings, 'tts_mode', 'websocket')
    if tts_mode == 'chunks':
        # FR mode: each chunk is a fully independent WebSocket session whose
        # audio is then crossfaded with its neighbours. Avoids the quality
        # degradation (noise, volume drop) that accumulates in a single long
        # WebSocket continue=true session beyond ~2 minutes.
        crossfade_ms = getattr(settings, 'tts_chunk_crossfade_ms', 80)
        raw_pcm = asyncio.run(_render_chunks_crossfade(chunks, settings, crossfade_ms))
    else:
        # EN mode: one WebSocket session with continue=true — seamless prosody
        # across the full script, validated on sessions up to ~15 min.
        raw_pcm = asyncio.run(_render_script_websocket(chunks, settings))
    elapsed = time.monotonic() - start

    # Wrap raw PCM (int16 little-endian mono) into a WAV, then transcode to MP3.
    tmp_wav = output_path.parent / 'tts_raw.wav'
    with wave.open(str(tmp_wav), 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # pcm_s16le = 2 bytes per sample
        wf.setframerate(WEBSOCKET_SAMPLE_RATE)
        wf.writeframes(raw_pcm)

    segment = AudioSegment.from_file(tmp_wav, format='wav')
    segment.export(output_path, format='mp3', bitrate=settings.tts_bitrate)
    tmp_wav.unlink(missing_ok=True)

    duration_seconds = math.ceil(len(segment) / 1000)
    logger.info(
        'TTS synthesized: chunks=%d raw_bytes=%d duration=%ds elapsed=%.1fs',
        len(chunks), len(raw_pcm), duration_seconds, elapsed,
    )

    return {
        'chunk_count': len(chunks),
        'duration_seconds': duration_seconds,
        'bytes': output_path.stat().st_size,
        'auto_spelled_acronyms': auto_spelled,
    }


async def _render_script_websocket(chunks: list[str], settings, max_retries: int = 3) -> bytes:
    """Retry the whole session up to max_retries times on failure.

    Partial audio from a dropped session isn't useful — a seam-free episode
    requires a single uninterrupted websocket session from start to finish.
    Retries back off exponentially (capped at 15s).
    """
    last_exc: Exception | None = None
    for attempt in range(1, max_retries + 1):
        try:
            return await _render_session(chunks, settings)
        except Exception as exc:
            last_exc = exc
            logger.warning('Cartesia websocket attempt %d/%d failed: %s', attempt, max_retries, exc)
            if attempt < max_retries:
                await asyncio.sleep(min(2 ** attempt, 15))
    raise ValueError(f'Cartesia websocket failed after {max_retries} attempts: {last_exc}')


async def _render_single_chunk_ws(chunk: str, settings, context_id: str | None = None) -> bytes:
    """Render one text chunk as a complete, self-contained WebSocket session.

    Unlike _render_session (which sends all chunks under one context_id with
    continue=True), each call here opens a fresh connection for a single chunk
    and closes it after the 'done' frame. This prevents the audio-quality
    degradation that accumulates over long WebSocket sessions (noise, volume
    creep) at the cost of a per-chunk connection overhead (~0.2 s each).
    """
    ctx = context_id or f'aipr-{uuid.uuid4()}'
    url = (
        f'{CARTESIA_WEBSOCKET_URL}'
        f'?cartesia_version={settings.cartesia_version}'
        f'&api_key={settings.cartesia_api_key}'
    )
    async with websockets.connect(url, max_size=None) as ws:
        request = {
            'model_id': settings.cartesia_model_id,
            'transcript': chunk,
            'voice': {'mode': 'id', 'id': settings.cartesia_voice_id},
            'language': settings.cartesia_language,
            'context_id': ctx,
            'continue': False,   # standalone — no continuation expected
            'output_format': {
                'container': 'raw',
                'encoding': 'pcm_s16le',
                'sample_rate': WEBSOCKET_SAMPLE_RATE,
            },
            'generation_config': {
                'volume': settings.cartesia_volume,
                'speed': settings.cartesia_speed,
                'emotion': settings.cartesia_emotion,
            },
        }
        await ws.send(json.dumps(request))

        audio = bytearray()
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('context_id') != ctx:
                continue
            mtype = msg.get('type')
            if mtype == 'chunk':
                audio.extend(base64.b64decode(msg['data']))
            elif mtype == 'done':
                break
            elif mtype == 'error':
                raise RuntimeError(f'Cartesia error: {msg}')
    return bytes(audio)


async def _render_chunks_crossfade(
    chunks: list[str], settings, crossfade_ms: int = 80, max_retries: int = 3,
) -> bytes:
    """Render each chunk independently, then crossfade all segments together.

    Used for FR (tts_mode='chunks') where a single long WebSocket session
    accumulates noise and volume instability after ~2 minutes. Independent
    connections keep each segment at full quality; the crossfade_ms overlap
    smooths the boundary so the join is inaudible at normal listening volume.

    Retry logic: each chunk backs off exponentially and retries up to
    max_retries times before raising, so a transient WebSocket hiccup on
    chunk 8/20 doesn't abort the whole episode.
    """
    from pydub import AudioSegment

    segments: list[AudioSegment] = []
    for i, chunk in enumerate(chunks, 1):
        last_exc: Exception | None = None
        for attempt in range(1, max_retries + 1):
            try:
                pcm = await _render_single_chunk_ws(chunk, settings)
                break
            except Exception as exc:
                last_exc = exc
                logger.warning(
                    'Chunk %d/%d attempt %d/%d failed: %s',
                    i, len(chunks), attempt, max_retries, exc,
                )
                if attempt < max_retries:
                    await asyncio.sleep(min(2 ** attempt, 10))
        else:
            raise ValueError(
                f'Cartesia chunk {i}/{len(chunks)} failed after {max_retries} attempts: {last_exc}'
            )
        seg = AudioSegment(
            data=pcm,
            sample_width=2,                # pcm_s16le = 2 bytes per sample
            frame_rate=WEBSOCKET_SAMPLE_RATE,
            channels=1,
        )
        segments.append(seg)
        logger.debug('Chunk %d/%d: %.1fs audio', i, len(chunks), len(seg) / 1000)

    # Merge with a short crossfade to hide any micro-silence at boundaries.
    combined = segments[0]
    for seg in segments[1:]:
        combined = combined.append(seg, crossfade=crossfade_ms)
    return combined.raw_data


async def _render_session(chunks: list[str], settings) -> bytes:
    context_id = f'aipr-{uuid.uuid4()}'
    url = (
        f'{CARTESIA_WEBSOCKET_URL}'
        f'?cartesia_version={settings.cartesia_version}'
        f'&api_key={settings.cartesia_api_key}'
    )

    # max_size=None lifts the default 1 MiB per-frame cap — audio frames for
    # long scripts can exceed that. Default ping_interval (20s) is fine since
    # Cartesia streams audio frames continuously to keep the connection live.
    async with websockets.connect(url, max_size=None) as ws:
        for i, chunk in enumerate(chunks, start=1):
            is_last = (i == len(chunks))
            request = {
                'model_id': settings.cartesia_model_id,
                'transcript': chunk,
                'voice': {'mode': 'id', 'id': settings.cartesia_voice_id},
                'language': settings.cartesia_language,
                'context_id': context_id,
                'continue': not is_last,
                'output_format': {
                    'container': 'raw',
                    'encoding': 'pcm_s16le',
                    'sample_rate': WEBSOCKET_SAMPLE_RATE,
                },
                'generation_config': {
                    'volume': settings.cartesia_volume,
                    'speed': settings.cartesia_speed,
                    'emotion': settings.cartesia_emotion,
                },
            }
            await ws.send(json.dumps(request))

        audio = bytearray()
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('context_id') != context_id:
                continue  # ignore any stale frames from a prior session
            mtype = msg.get('type')
            if mtype == 'chunk':
                audio.extend(base64.b64decode(msg['data']))
            elif mtype == 'done':
                break
            elif mtype == 'error':
                raise RuntimeError(f'Cartesia error: {msg}')
    return bytes(audio)
