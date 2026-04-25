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

from ..settings import DATA_DIR, load_settings

logger = logging.getLogger(__name__)


def _persist_acronyms_seen(acronyms: list[str], locale: str) -> None:
    """Append auto-spelled acronyms to a per-locale registry on disk.

    Builds a cumulative operator-facing inventory at
    ``data/state/acronyms_seen_{locale}.json`` mapping each acronym to
    ``{first_seen, last_seen, count}``. Used exclusively for review — the
    pipeline itself does not read this file back.
    """
    if not acronyms:
        return
    state_dir = DATA_DIR / 'state'
    state_dir.mkdir(parents=True, exist_ok=True)
    path = state_dir / f'acronyms_seen_{locale}.json'
    try:
        current = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
    except (OSError, json.JSONDecodeError):
        current = {}
    now = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    for token in acronyms:
        entry = current.get(token) or {'first_seen': now, 'last_seen': now, 'count': 0}
        entry['last_seen'] = now
        entry['count'] = int(entry.get('count', 0)) + 1
        current[token] = entry
    path.write_text(json.dumps(current, indent=2, sort_keys=True), encoding='utf-8')

CARTESIA_WEBSOCKET_URL = 'wss://api.cartesia.ai/tts/websocket'

# Phase 8 / T5: raw PCM sample rate for the websocket stream. 44.1kHz matches
# the previous /tts/bytes WAV output (pcm_f32le @ 44100) at half the bandwidth
# (16-bit vs 32-bit) with no audible loss for speech.
WEBSOCKET_SAMPLE_RATE = 44100

# Hard upper bounds on any single send/recv await. Without these, a stuck
# Cartesia session blocks the whole workflow until GitHub's 6-hour job
# timeout fires — we've seen it happen when the server accepts the
# connection but never emits the first audio frame (model cold-start gone
# wrong). The websockets library's default ping_interval (20s) detects a
# dead TCP socket but NOT a server that just stops streaming audio while
# still answering pings. These timeouts make the retry loops in
# `_render_script_websocket` / `_render_chunks_crossfade` actually engage.
#
# RECV is generous: first frame after `send` can take ~15s for model spin-up
# on a cold region; between-frame gaps during active synthesis are milliseconds.
# 60s is ~4x the worst observed first-frame latency and ~60000x a steady-state
# gap, so anything beyond that really is stuck.
WS_SEND_TIMEOUT_S = 30.0
WS_RECV_TIMEOUT_S = 60.0


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
    # ── Companies / chip houses ──────────────────────────────────────────
    'TSMC': 'T. S. M. C.',
    'AMD': 'A. M. D.',
    'IBM': 'I. B. M.',
    'AWS': 'A. W. S.',
    'GCP': 'G. C. P.',
    'HPE': 'H. P. E.',
    'SAP': 'S. A. P.',
    'SMIC': 'S. M. I. C.',  # Semiconductor Manufacturing International
    'ASML': 'A. S. M. L.',
    'STMicro': 'S. T. Micro',
    # ── Models / families / AI training jargon ───────────────────────────
    'GPT': 'G. P. T.',
    'BERT': 'Burt',   # pronounced as a word in EN
    'LLM': 'L. L. M.',
    'LLMs': 'L. L. M. s',
    'SLM': 'S. L. M.',
    'SLMs': 'S. L. M. s',
    'LLaMA': 'lama',
    'LoRA': 'lora',
    'QLoRA': 'Q. lora',
    'MoE': 'M. O. E.',
    'RAG': 'rag',     # retrieval-augmented generation — pronounced as a word
    'RLHF': 'R. L. H. F.',
    'DPO': 'D. P. O.',   # Direct Preference Optimization
    'SFT': 'S. F. T.',   # Supervised Fine-Tuning
    'PEFT': 'P. E. F. T.',
    'CoT': 'C. o. T.',   # Chain of Thought
    'ToT': 'T. o. T.',   # Tree of Thought
    'FLOPs': 'flops',    # pronounced as a word
    'FLOPS': 'flops',
    'SOTA': 'sota',      # pronounced as a word
    'OOD': 'O. O. D.',   # out-of-distribution
    # ── Benchmarks (frequent) ────────────────────────────────────────────
    'MMLU': 'M. M. L. U.',
    'GSM8K': 'G. S. M. 8. K.',
    'HellaSwag': 'hella-swag',
    'HumanEval': 'Human-Eval',
    'BBH': 'B. B. H.',
    'GPQA': 'G. P. Q. A.',
    'MATH': 'math',      # the benchmark, but same spelling as the word — harmless
    'SWE-bench': 'swee-bench',
    'ARC': 'arc',
    # ── Compute / infra ──────────────────────────────────────────────────
    'GPU': 'G. P. U.',
    'GPUs': 'G. P. U. s',
    'CPU': 'C. P. U.',
    'CPUs': 'C. P. U. s',
    'TPU': 'T. P. U.',
    'TPUs': 'T. P. U. s',
    'NPU': 'N. P. U.',
    'NPUs': 'N. P. U. s',
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
    'ASIC': 'ay-sick',
    'ASICs': 'ay-sicks',
    'FPGA': 'F. P. G. A.',
    'FPGAs': 'F. P. G. A. s',
    'SSD': 'S. S. D.',
    'SSDs': 'S. S. D. s',
    'HBM': 'H. B. M.',
    'DDR': 'D. D. R.',
    'NVMe': 'N. V. M. E.',
    'CUDA': 'koo-da',
    'ROCm': 'rock-em',
    'VRAM': 'V. R. A. M.',
    'DRAM': 'D. R. A. M.',
    # ── Org titles / business ────────────────────────────────────────────
    'CEO': 'C. E. O.',
    'CTO': 'C. T. O.',
    'CFO': 'C. F. O.',
    'COO': 'C. O. O.',
    'CIO': 'C. I. O.',
    'CISO': 'C. I. S. O.',
    'IPO': 'I. P. O.',
    'IPOs': 'I. P. O. s',
    'M&A': 'M. and A.',
    'VC': 'V. C.',
    'VCs': 'V. C. s',
    'PE': 'P. E.',
    'ROI': 'R. O. I.',
    'KPI': 'K. P. I.',
    'KPIs': 'K. P. I. s',
    'OKR': 'O. K. R.',
    'OKRs': 'O. K. R. s',
    'OEM': 'O. E. M.',
    'OEMs': 'O. E. M. s',
    'GTM': 'G. T. M.',   # go-to-market
    'B2B': 'B. 2. B.',
    'B2C': 'B. 2. C.',
    'D2C': 'D. 2. C.',
    'HR': 'H. R.',
    'QA': 'Q. A.',
    'R&D': 'R. and D.',
    'PR': 'P. R.',
    'IT': 'I. T.',
    'PoC': 'P. O. C.',
    'MVP': 'M. V. P.',
    # ── Finance / markets (banking-focused podcast) ──────────────────────
    'EPS': 'E. P. S.',
    'EBITDA': 'ee-bit-da',
    'GDP': 'G. D. P.',
    'CPI': 'C. P. I.',
    'PPI': 'P. P. I.',
    'PMI': 'P. M. I.',
    'YoY': 'year-over-year',
    'QoQ': 'quarter-over-quarter',
    'FY': 'F. Y.',
    'FY24': 'F. Y. twenty-four',
    'FY25': 'F. Y. twenty-five',
    'FY26': 'F. Y. twenty-six',
    'P/E': 'P. E.',
    'EV': 'E. V.',         # enterprise value OR electric vehicle — ambiguous but both pronounce same
    'ESG': 'E. S. G.',
    'NAV': 'N. A. V.',
    'AUM': 'A. U. M.',
    'TVL': 'T. V. L.',
    # ── Regulators / institutions ────────────────────────────────────────
    'SEC': 'S. E. C.',
    'FTC': 'F. T. C.',
    'FDA': 'F. D. A.',
    'DOJ': 'D. O. J.',
    'DOE': 'D. O. E.',
    'DOD': 'D. O. D.',
    'NYSE': 'N. Y. S. E.',
    'NASDAQ': 'naz-dak',
    'FOMC': 'F. O. M. C.',
    'FED': 'Fed',
    'ECB': 'E. C. B.',
    'BoE': 'B. o. E.',
    'BoJ': 'B. o. J.',
    'PBOC': 'P. B. O. C.',
    'IMF': 'I. M. F.',
    'WTO': 'W. T. O.',
    'OECD': 'O. E. C. D.',
    'NIST': 'nist',
    'DARPA': 'DARPA',
    'CFIUS': 'see-fee-us',
    'BIS': 'B. I. S.',
    'BAFIN': 'BAFIN',
    'CMA': 'C. M. A.',
    'GDPR': 'G. D. P. R.',
    'HIPAA': 'hip-ah',
    'FINRA': 'fin-ra',
    'KYC': 'K. Y. C.',
    'AML': 'A. M. L.',
    # ── AI-specific acronyms ─────────────────────────────────────────────
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
    'IL': 'I. L.',       # imitation learning
    'XAI': 'X. A. I.',
    'AR': 'A. R.',       # augmented reality
    'VR': 'V. R.',       # virtual reality
    'XR': 'X. R.',
    'IoT': 'I. o. T.',
    'TTFT': 'T. T. F. T.',
    # ── Geographies / institutions ───────────────────────────────────────
    'USA': 'U. S. A.',
    'US': 'U. S.',
    'EU': 'E. U.',
    'UK': 'U. K.',
    'UAE': 'U. A. E.',
    'NATO': 'NATO',  # already pronounced as a word
    'UN': 'U. N.',
    'APAC': 'A. PAC.',
    'EMEA': 'E. M. E. A.',
    'LATAM': 'LA-tam',
    # ── Tech / formats ───────────────────────────────────────────────────
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
    'SQL': 'sequel',
    'NoSQL': 'no-sequel',
    'gRPC': 'G. R. P. C.',
    'UX': 'U. X.',
    'UI': 'U. I.',
    # ── Brands / camelCase ───────────────────────────────────────────────
    'OpenAI': 'Open A. I.',
    'NVIDIA': 'en-vidia',
    'NASA': 'NASA',
    'xAI': 'X. A. I.',
    'DeepSeek': 'Deep-Seek',
    'Mistral': 'miss-tral',
    # ── Research jargon ──────────────────────────────────────────────────
    'arXiv': 'ar-kive',
    'LaTeX': 'Lay-Tech',
    'NeurIPS': 'noor-ips',
    'ICML': 'I. C. M. L.',
    'ACL': 'A. C. L.',
    'ICLR': 'I. C. L. R.',
    'EMNLP': 'E. M. N. L. P.',
    'AAAI': 'triple-A. I.',
    'FAISS': 'fais',   # Facebook AI Similarity Search — pronounced as a word

    # ─────────────────────────────────────────────────────────────────────
    # MASS-EXPANSION 2026-04-19 — recurring acronyms across the AI/finance
    # beat. Rule of thumb when adding: if the token shows up on TechCrunch,
    # Bloomberg, FT, or any AI lab blog at least monthly, it belongs here.
    # ─────────────────────────────────────────────────────────────────────

    # ── Finance / corporate metrics ──────────────────────────────────────
    'ROE': 'R. O. E.',
    'ROA': 'R. O. A.',
    'ROIC': 'R. O. I. C.',
    'ROCE': 'R. O. C. E.',
    'NPV': 'N. P. V.',
    'IRR': 'I. R. R.',
    'FCF': 'F. C. F.',
    'FCFF': 'F. C. F. F.',
    'OPEX': 'op-ex',
    'CAPEX': 'cap-ex',
    'COGS': 'cogs',
    'SG&A': 'S. G. and A.',
    'EBIT': 'ee-bit',
    'NIM': 'N. I. M.',         # Net Interest Margin
    'NPL': 'N. P. L.',         # Non-Performing Loan
    'NPLs': 'N. P. L. s',
    'CET1': 'C. E. T. 1.',     # Common Equity Tier 1
    'RWA': 'R. W. A.',         # Risk-Weighted Assets
    'LCR': 'L. C. R.',
    'NSFR': 'N. S. F. R.',
    'CECL': 'see-sel',
    'IRRBB': 'I. R. R. B. B.',
    'GAAP': 'gap',
    'IFRS': 'I. F. R. S.',
    'CAGR': 'cay-ger',
    'ARR': 'A. R. R.',
    'MRR': 'M. R. R.',
    'ARPU': 'ar-poo',
    'CAC': 'C. A. C.',
    'LTV': 'L. T. V.',
    'NRR': 'N. R. R.',
    'GMV': 'G. M. V.',
    'TAM': 'tam',
    'SAM': 'sam',
    'SOM': 'som',
    # ── Indices & market plumbing ────────────────────────────────────────
    'S&P': 'S. and P.',
    'FTSE': 'foot-see',
    'DAX': 'dax',
    'CAC40': 'C. A. C. forty',
    'HSI': 'H. S. I.',
    'KOSPI': 'koss-pee',
    'ETF': 'E. T. F.',
    'ETFs': 'E. T. F. s',
    'ETN': 'E. T. N.',
    'REIT': 'reet',
    'REITs': 'reets',
    'SPV': 'S. P. V.',
    'SPAC': 'spack',
    'SPACs': 'spacks',
    'MBS': 'M. B. S.',
    'ABS': 'A. B. S.',
    'CDS': 'C. D. S.',
    'CLO': 'C. L. O.',
    'CDO': 'C. D. O.',
    'OTC': 'O. T. C.',
    'HFT': 'H. F. T.',
    'AUM': 'A. U. M.',
    'NAV': 'N. A. V.',
    'IPO': 'I. P. O.',
    'M&A': 'M. and A.',
    # ── Rates / benchmarks ───────────────────────────────────────────────
    'LIBOR': 'lie-bore',
    'SOFR': 'so-fer',
    'ESTR': 'ester',
    'SONIA': 'so-nya',
    'TONA': 'toh-na',
    'TONAR': 'toh-nar',
    # ── Banking rails / payments ─────────────────────────────────────────
    'ACH': 'A. C. H.',
    'RTP': 'R. T. P.',
    'SEPA': 'see-pa',
    'BIC': 'B. I. C.',
    'IBAN': 'I. ban',
    'POS': 'P. O. S.',
    'ATM': 'A. T. M.',
    'ATMs': 'A. T. M. s',
    'SWIFT': 'SWIFT',
    'FedNow': 'Fed-Now',
    'PSP': 'P. S. P.',
    'PSPs': 'P. S. P. s',
    'BNPL': 'B. N. P. L.',
    'PCI': 'P. C. I.',
    # ── Regulators / regimes (non-US) ────────────────────────────────────
    'EBA': 'E. B. A.',
    'OCC': 'O. C. C.',
    'FDIC': 'F. D. I. C.',
    'CFPB': 'C. F. P. B.',
    'OFAC': 'O. FAC.',
    'FinCEN': 'fin-sen',
    'SAMA': 'sah-mah',
    'MAS': 'M. A. S.',
    'HKMA': 'H. K. M. A.',
    'FSA': 'F. S. A.',
    'JFSA': 'J. F. S. A.',
    'PRA': 'P. R. A.',
    'FCA': 'F. C. A.',
    'AMF': 'A. M. F.',
    'BaFin': 'bah-fin',
    'CFT': 'C. F. T.',
    'FATCA': 'fat-ka',
    'CRS': 'C. R. S.',
    'MiFID': 'mee-fid',
    'EMIR': 'eh-mere',
    'DORA': 'door-ah',
    'FRTB': 'F. R. T. B.',
    'BCBS': 'B. C. B. S.',
    'IOSCO': 'eye-os-co',
    'CCPA': 'C. C. P. A.',
    # ── Crypto / web3 (recurring on tech press) ──────────────────────────
    'BTC': 'B. T. C.',
    'ETH': 'eath',
    'NFT': 'N. F. T.',
    'NFTs': 'N. F. T. s',
    'DeFi': 'dee-fy',
    'CeFi': 'see-fy',
    'DAO': 'D. A. O.',
    'DAOs': 'D. A. O. s',
    'DEX': 'dex',
    'CEX': 'sex',     # the exchange type, said as a word
    'AMM': 'A. M. M.',
    'TVL': 'T. V. L.',
    'USDC': 'U. S. D. C.',
    'USDT': 'U. S. D. T.',
    'L1': 'layer-one',
    'L2': 'layer-two',
    # ── Cybersecurity (banking-relevant) ─────────────────────────────────
    'SSO': 'S. S. O.',
    'MFA': 'M. F. A.',
    '2FA': 'two-F. A.',
    'OAuth': 'O. auth',
    'OIDC': 'O. I. D. C.',
    'SAML': 'sam-el',
    'JWT': 'J. W. T.',
    'TLS': 'T. L. S.',
    'SSL': 'S. S. L.',
    'CVE': 'C. V. E.',
    'CVEs': 'C. V. E. s',
    'CWE': 'C. W. E.',
    'OWASP': 'oh-wasp',
    'EDR': 'E. D. R.',
    'XDR': 'X. D. R.',
    'SIEM': 'seem',
    'SOAR': 'soar',
    'IAM': 'I. A. M.',
    'PAM': 'P. A. M.',
    'DLP': 'D. L. P.',
    'IDS': 'I. D. S.',
    'IPS': 'I. P. S.',
    'WAF': 'waff',
    'DDoS': 'D. dos',
    'SOC': 'sock',
    'SOC2': 'sock-two',
    'GRC': 'G. R. C.',
    'FedRAMP': 'Fed-Ramp',
    'FIPS': 'fips',
    'PII': 'P. I. I.',
    'PHI': 'P. H. I.',
    # ── Cloud / networking ───────────────────────────────────────────────
    'VPC': 'V. P. C.',
    'S3': 'S. three',
    'EC2': 'E. C. two',
    'EKS': 'E. K. S.',
    'GKE': 'G. K. E.',
    'AKS': 'A. K. S.',
    'ECS': 'E. C. S.',
    'ECR': 'E. C. R.',
    'RDS': 'R. D. S.',
    'KMS': 'K. M. S.',
    'SNS': 'S. N. S.',
    'SQS': 'S. Q. S.',
    'CDN': 'C. D. N.',
    'DNS': 'D. N. S.',
    'BGP': 'B. G. P.',
    'IPv4': 'I. P. version four',
    'IPv6': 'I. P. version six',
    'NAT': 'nat',
    'VLAN': 'V. lan',
    'DHCP': 'D. H. C. P.',
    # ── AI/ML extended (architectures, training, eval) ──────────────────
    'VAE': 'V. A. E.',
    'GAN': 'gan',
    'GANs': 'gans',
    'CNN': 'C. N. N.',
    'CNNs': 'C. N. N. s',
    'RNN': 'R. N. N.',
    'LSTM': 'L. S. T. M.',
    'GRU': 'G. R. U.',
    'MLP': 'M. L. P.',
    'ViT': 'V. I. T.',
    'CLIP': 'clip',
    'NeRF': 'nerf',
    'PPO': 'P. P. O.',
    'GRPO': 'G. R. P. O.',
    'ORPO': 'or-po',
    'KTO': 'K. T. O.',
    'ICL': 'I. C. L.',
    'MoE': 'M. O. E.',
    'MQA': 'M. Q. A.',
    'GQA': 'G. Q. A.',
    'KV': 'K. V.',     # KV cache
    # Quantization / numeric formats
    'INT8': 'int-eight',
    'INT4': 'int-four',
    'FP4': 'F. P. four',
    'FP8': 'F. P. eight',
    'FP16': 'F. P. sixteen',
    'BF16': 'B. F. sixteen',
    'FP32': 'F. P. thirty-two',
    'FP64': 'F. P. sixty-four',
    'TFLOP': 'tee-flop',
    'TFLOPs': 'tee-flops',
    'PFLOP': 'pee-flop',
    'EFLOP': 'ee-flop',
    'MFU': 'M. F. U.',
    # Extra benchmarks
    'AIME': 'aim',
    'MMLU-Pro': 'M. M. L. U. Pro',
    'MATH-500': 'MATH five-hundred',
    'HumanEval+': 'Human-Eval Plus',
    'MBPP': 'M. B. P. P.',
    'BIG-bench': 'big-bench',
    'AGIEval': 'A. G. I. Eval',
    'IFEval': 'I. F. Eval',
    'BFCL': 'B. F. C. L.',
    'MGSM': 'M. G. S. M.',
    # AI orgs
    'BAAI': 'B. A. A. I.',
    'EleutherAI': 'E-loo-ther A. I.',
    'LMSYS': 'L. M. sis',
    # ── General business / comms ─────────────────────────────────────────
    'FAQ': 'F. A. Q.',
    'TBD': 'T. B. D.',
    'TBA': 'T. B. A.',
    'ASAP': 'A. sap',
    'EOD': 'E. O. D.',
    'EOW': 'E. O. W.',
    'EOM': 'E. O. M.',
    'EOY': 'E. O. Y.',
    'ETA': 'E. T. A.',
    'ETD': 'E. T. D.',
    'NDA': 'N. D. A.',
    'NDAs': 'N. D. A. s',
    'MoU': 'M. o. U.',
    'MOU': 'M. O. U.',
    'RFP': 'R. F. P.',
    'RFQ': 'R. F. Q.',
    'RFI': 'R. F. I.',
    'EULA': 'you-lah',
    'SLA': 'S. L. A.',
    'SLAs': 'S. L. A. s',
    'SLO': 'S. L. O.',
    'SLOs': 'S. L. O. s',
    'PoV': 'P. O. V.',
    'POV': 'P. O. V.',
    'TL;DR': 'T. L. D. R.',
    # ── Time zones / calendar ────────────────────────────────────────────
    'EST': 'E. S. T.',
    'PST': 'P. S. T.',
    'GMT': 'G. M. T.',
    'UTC': 'U. T. C.',
    'CET': 'C. E. T.',
    'CEST': 'C. E. S. T.',
    'JST': 'J. S. T.',
    'KST': 'K. S. T.',
    'IST': 'I. S. T.',
    'Q1': 'Q. one',
    'Q2': 'Q. two',
    'Q3': 'Q. three',
    'Q4': 'Q. four',
    'H1': 'H. one',
    'H2': 'H. two',
    # ── AI products / brands (camelCase + special) ───────────────────────
    'DeepMind': 'Deep-Mind',
    'AlphaFold': 'Alpha-Fold',
    'AlphaGo': 'Alpha-Go',
    'MuZero': 'Mew-Zero',
    'AlphaStar': 'Alpha-Star',
    'AlphaProof': 'Alpha-Proof',
    'ChatGPT': 'Chat G. P. T.',
    'Codex': 'Co-dex',
    'Copilot': 'Co-pilot',
    'MidJourney': 'Mid-Journey',
    'Sora': 'Sor-ah',
    'Veo': 'Vay-oh',
    'Runway': 'Run-way',
    'Whisper': 'Whisper',
    'Bedrock': 'Bedrock',
    'Sagemaker': 'Sage-maker',
    'Vertex': 'Vertex',
    'HuggingFace': 'Hugging-Face',
    'PyTorch': 'Pie-Torch',
    'TensorFlow': 'Tensor-Flow',
    'JAX': 'jacks',
    'vLLM': 'V. L. L. M.',
    'TensorRT': 'Tensor R. T.',
    'TGI': 'T. G. I.',
    # ── Misc tech / formats (recurring) ──────────────────────────────────
    'WebRTC': 'Web R. T. C.',
    'WebGL': 'Web G. L.',
    'WASM': 'wazm',
    'gRPC': 'G. R. P. C.',
    'GraphQL': 'graph Q. L.',
    'CRUD': 'crud',
    'REST': 'rest',
    'CSV': 'C. S. V.',
    'TSV': 'T. S. V.',
    'YAML': 'yamel',
    'TOML': 'tom-el',
    'PNG': 'P. N. G.',
    'JPG': 'J. P. G.',
    'JPEG': 'jay-peg',
    'GIF': 'jiff',
    'SVG': 'S. V. G.',
    'WebP': 'Web P.',
    # ── Hardware extras ──────────────────────────────────────────────────
    'PCIe': 'P. C. I. E.',
    'USB': 'U. S. B.',
    'USB-C': 'U. S. B. C.',
    'HDMI': 'H. D. M. I.',
    'Wi-Fi': 'Wi-Fi',
    'WiFi': 'Wi-Fi',
    'BLE': 'B. L. E.',
    'NFC': 'N. F. C.',
    '5G': 'five-G.',
    '6G': 'six-G.',
    'EV': 'E. V.',
    'EVs': 'E. V. s',
    'BEV': 'B. E. V.',
    'PHEV': 'P. H. E. V.',
    'HEV': 'H. E. V.',
    'CCS': 'C. C. S.',
    'V2G': 'V. two G.',
    'V2X': 'V. two X.',
    'LIDAR': 'lie-dar',
    'LiDAR': 'lie-dar',
    'RADAR': 'ray-dar',
    'GPS': 'G. P. S.',
    'IMU': 'I. M. U.',
    'SoC': 'S. O. C.',
    'SoCs': 'S. O. C. s',

    # ─────────────────────────────────────────────────────────────────────
    # MASS-EXPANSION 2026-04-19 (b) — BUSINESS / ECONOMY / CORPORATE
    # User asked for broader coverage: "ajout acronymes business, economie,
    # corporate". Anything that recurs on Bloomberg / FT / WSJ / Reuters /
    # Economist / HBR / consulting reports belongs here.
    # ─────────────────────────────────────────────────────────────────────

    # ── Strategy / consulting / frameworks ──────────────────────────────
    'BCG': 'B. C. G.',
    'MBB': 'M. B. B.',     # McKinsey, Bain, BCG
    'SWOT': 'swot',
    'PESTLE': 'pes-tel',
    'PESTEL': 'pes-tel',
    'TOWS': 'tows',
    'OKR': 'O. K. R.',
    'OKRs': 'O. K. R. s',
    'KPI': 'K. P. I.',
    'KPIs': 'K. P. I. s',
    'EVA': 'E. V. A.',     # Economic Value Added
    'TCO': 'T. C. O.',     # Total Cost of Ownership
    'CSF': 'C. S. F.',     # Critical Success Factor
    'USP': 'U. S. P.',     # Unique Selling Proposition
    'GTM': 'G. T. M.',
    'ICP': 'I. C. P.',     # Ideal Customer Profile
    'JTBD': 'J. T. B. D.', # Jobs To Be Done

    # ── Customer / product metrics ──────────────────────────────────────
    'CSAT': 'C. sat',
    'NPS': 'N. P. S.',
    'CES': 'C. E. S.',     # Customer Effort Score
    'DAU': 'D. A. U.',
    'MAU': 'M. A. U.',
    'WAU': 'W. A. U.',
    'AOV': 'A. O. V.',     # Average Order Value
    'ATV': 'A. T. V.',     # Average Transaction Value
    'ROAS': 'roh-az',      # Return on Ad Spend
    'CTR': 'C. T. R.',
    'CVR': 'C. V. R.',     # Conversion Rate
    'CR': 'C. R.',
    'CPC': 'C. P. C.',     # Cost Per Click
    'CPM': 'C. P. M.',
    'CPL': 'C. P. L.',     # Cost Per Lead
    'CPA': 'C. P. A.',     # Cost Per Acquisition / Certified Public Accountant
    'CPS': 'C. P. S.',
    'PPC': 'P. P. C.',     # Pay Per Click

    # ── Sales / marketing infra ─────────────────────────────────────────
    'CRM': 'C. R. M.',
    'CDP': 'C. D. P.',     # Customer Data Platform
    'DSP': 'D. S. P.',
    'SSP': 'S. S. P.',
    'DMP': 'D. M. P.',
    'SEO': 'S. E. O.',
    'SEM': 'S. E. M.',
    'SMM': 'S. M. M.',
    'ASO': 'A. S. O.',
    'PR': 'P. R.',

    # ── Enterprise IT / supply chain ────────────────────────────────────
    'ERP': 'E. R. P.',
    'SCM': 'S. C. M.',     # Supply Chain Management
    'PLM': 'P. L. M.',     # Product Lifecycle Management
    'MES': 'M. E. S.',     # Manufacturing Execution System
    'WMS': 'W. M. S.',     # Warehouse Management System
    'MRP': 'M. R. P.',     # Material Requirements Planning
    'BOM': 'B. O. M.',     # Bill of Materials
    'SKU': 'S. K. U.',
    'SKUs': 'S. K. U. s',
    'EDI': 'E. D. I.',
    'JIT': 'J. I. T.',     # Just In Time
    'TQM': 'T. Q. M.',     # Total Quality Management
    'OEE': 'O. E. E.',     # Overall Equipment Effectiveness
    'ODM': 'O. D. M.',
    '3PL': 'three P. L.',  # third-party logistics
    '4PL': 'four P. L.',

    # ── Corporate structure / governance ────────────────────────────────
    'LLC': 'L. L. C.',
    'LLP': 'L. L. P.',
    'LP': 'L. P.',
    'GP': 'G. P.',         # General Partner
    'LBO': 'L. B. O.',
    'MBO': 'M. B. O.',
    'ESOP': 'ee-sop',
    'RSU': 'R. S. U.',
    'RSUs': 'R. S. U. s',
    'ISO': 'I. S. O.',     # also Incentive Stock Option
    'AGM': 'A. G. M.',     # Annual General Meeting
    'EGM': 'E. G. M.',
    'BOD': 'B. O. D.',
    'NED': 'N. E. D.',     # Non-Executive Director
    'C-suite': 'C-suite',
    'CRO': 'C. R. O.',     # Chief Revenue / Risk Officer
    'CHRO': 'C. H. R. O.',
    'CMO': 'C. M. O.',
    'CCO': 'C. C. O.',     # Chief Compliance / Customer Officer
    'CPO': 'C. P. O.',     # Chief Product / People Officer
    'CDO': 'C. D. O.',     # also Collateralized Debt Obligation
    'GC': 'G. C.',         # General Counsel
    'CoS': 'C. o. S.',     # Chief of Staff
    'EVP': 'E. V. P.',     # Executive Vice President
    'SVP': 'S. V. P.',
    'VP': 'V. P.',
    'AVP': 'A. V. P.',

    # ── Macro economics ─────────────────────────────────────────────────
    'GDP': 'G. D. P.',
    'GNP': 'G. N. P.',
    'GNI': 'G. N. I.',
    'PCE': 'P. C. E.',
    'CPI': 'C. P. I.',
    'PPI': 'P. P. I.',
    'PMI': 'P. M. I.',
    'ISM': 'I. S. M.',
    'NFP': 'N. F. P.',     # Non-Farm Payrolls
    'JOLTS': 'jolts',
    'FFR': 'F. F. R.',
    'ZIRP': 'zerp',
    'NIRP': 'nerp',
    'QE': 'Q. E.',
    'QT': 'Q. T.',
    'M2': 'M. two',
    'M3': 'M. three',
    'BoP': 'B. o. P.',     # Balance of Payments
    'CA': 'C. A.',
    'FDI': 'F. D. I.',     # Foreign Direct Investment
    'PPP': 'P. P. P.',     # Purchasing Power Parity
    'HDI': 'H. D. I.',
    'CBDC': 'C. B. D. C.',

    # ── Trade blocs & multilaterals ─────────────────────────────────────
    'WB': 'W. B.',         # World Bank
    'IMF': 'I. M. F.',
    'WTO': 'W. T. O.',
    'OECD': 'O. E. C. D.',
    'BIS': 'B. I. S.',
    'WEF': 'W. E. F.',
    'BRICS': 'bricks',
    'G7': 'G. seven',
    'G20': 'G. twenty',
    'G77': 'G. seventy-seven',
    'ASEAN': 'AS-ee-an',
    'MERCOSUR': 'mer-co-sur',
    'NAFTA': 'naf-ta',
    'USMCA': 'U. S. M. C. A.',
    'CPTPP': 'C. P. T. P. P.',
    'RCEP': 'R. SEP.',
    'IPCC': 'I. P. C. C.',
    'COP': 'cop',
    'COP30': 'cop thirty',
    'COP31': 'cop thirty-one',
    'IEA': 'I. E. A.',
    'OPEC': 'OPEC',
    'OPEC+': 'OPEC plus',

    # ── Banks / global financial institutions ───────────────────────────
    'JPM': 'J. P. M.',
    'BAML': 'B. A. M. L.',
    'BoA': 'B. o. A.',
    'MS': 'M. S.',         # Morgan Stanley
    'GS': 'G. S.',         # Goldman Sachs
    'BNP': 'B. N. P.',
    'SocGen': 'Soc-Gen',
    'BBVA': 'B. B. V. A.',
    'UBS': 'U. B. S.',
    'HSBC': 'H. S. B. C.',
    'RBC': 'R. B. C.',
    'TD': 'T. D.',         # TD Bank
    'ICBC': 'I. C. B. C.',
    'CCB': 'C. C. B.',     # China Construction Bank
    'ABC': 'A. B. C.',     # Agricultural Bank of China — context-dependent
    'BoC': 'B. o. C.',     # Bank of Canada / China
    'RBA': 'R. B. A.',     # Reserve Bank of Australia
    'RBI': 'R. B. I.',     # Reserve Bank of India
    'CBR': 'C. B. R.',     # Central Bank of Russia

    # ── Indices & ratings ───────────────────────────────────────────────
    'DJIA': 'D. J. I. A.',
    'DOW': 'Dow',
    'VIX': 'vicks',
    'TSX': 'T. S. X.',
    'FX': 'F. X.',
    'NYMEX': 'NIME-ex',
    'CME': 'C. M. E.',
    'ICE': 'ice',          # Intercontinental Exchange — pronounced as a word
    'CFA': 'C. F. A.',     # Chartered Financial Analyst
    'CPA': 'C. P. A.',
    'CIA': 'C. I. A.',     # also Central Intelligence Agency

    # ── HR / workplace ──────────────────────────────────────────────────
    'WFH': 'W. F. H.',
    'WFA': 'W. F. A.',     # work from anywhere
    'RTO': 'R. T. O.',     # return to office
    'PTO': 'P. T. O.',     # paid time off
    'OOO': 'O. O. O.',     # out of office
    'L&D': 'L. and D.',
    'T&E': 'T. and E.',    # travel & entertainment
    'P&L': 'P. and L.',    # profit & loss
    'EEO': 'E. E. O.',
    'EEOC': 'E. E. O. C.',
    'DEI': 'D. E. I.',
    'CSR': 'C. S. R.',
    'EVP': 'E. V. P.',     # also Employee Value Proposition

    # ── Legal / IP / compliance ─────────────────────────────────────────
    'IP': 'I. P.',
    'IPR': 'I. P. R.',
    'SOW': 'S. O. W.',
    'MSA': 'M. S. A.',
    'DPA': 'D. P. A.',     # Data Processing Agreement
    'TOS': 'T. O. S.',
    'ToS': 'T. o. S.',
    'EULA': 'you-lah',
    'DMCA': 'D. M. C. A.',
    'USPTO': 'U. S. P. T. O.',
    'EPO': 'E. P. O.',     # European Patent Office
    'WIPO': 'WI-po',
    'FCPA': 'F. C. P. A.', # Foreign Corrupt Practices Act
    'SOX': 'sox',          # Sarbanes-Oxley
    'KYB': 'K. Y. B.',

    # ── Healthcare / pharma (recurring on biz press) ────────────────────
    'EMA': 'E. M. A.',     # European Medicines Agency
    'WHO': 'W. H. O.',
    'CDC': 'C. D. C.',
    'NIH': 'N. I. H.',
    'IND': 'I. N. D.',
    'BLA': 'B. L. A.',
    'PMA': 'P. M. A.',
    'GxP': 'G. X. P.',
    'GMP': 'G. M. P.',
    'GLP': 'G. L. P.',
    'GCP': 'G. C. P.',     # also Google Cloud Platform — context-dependent

    # ── Energy / commodities / climate ──────────────────────────────────
    'LNG': 'L. N. G.',
    'LPG': 'L. P. G.',
    'CCS': 'C. C. S.',     # carbon capture and storage
    'CCUS': 'C. C. U. S.',
    'PV': 'P. V.',         # photovoltaic
    'CSP': 'C. S. P.',     # Concentrated Solar Power
    'BESS': 'bess',        # Battery Energy Storage System
    'ICE': 'ice',          # also Internal Combustion Engine
    'kWh': 'kilo-watt-hour',
    'MWh': 'mega-watt-hour',
    'GWh': 'giga-watt-hour',
    'TWh': 'tera-watt-hour',
    'WACC': 'wack',        # Weighted Average Cost of Capital
    'EV/EBITDA': 'E. V. to ee-bit-da',

    # ── Economic data sources / surveys ─────────────────────────────────
    'BLS': 'B. L. S.',     # Bureau of Labor Statistics
    'BEA': 'B. E. A.',     # Bureau of Economic Analysis
    'EIA': 'E. I. A.',     # Energy Information Admin
    'API': 'A. P. I.',     # also American Petroleum Institute — context
    'EPA': 'E. P. A.',     # Environmental Protection Agency

    # ── Generic biz shorthand ───────────────────────────────────────────
    'HQ': 'H. Q.',
    'FAQ': 'F. A. Q.',
    'AKA': 'A. K. A.',
    'AOB': 'A. O. B.',     # Any Other Business
    'BAU': 'B. A. U.',     # Business As Usual
    'WIP': 'W. I. P.',
    'TBD': 'T. B. D.',
    'TBA': 'T. B. A.',
    'TBC': 'T. B. C.',
    'POC': 'P. O. C.',
    'EOL': 'E. O. L.',     # End Of Life
    'EOS': 'E. O. S.',     # End Of Support
    'GA': 'G. A.',         # General Availability
    'EAP': 'E. A. P.',     # Early Access Program
    'NPV': 'N. P. V.',
    'YTD': 'Y. T. D.',
    'MTD': 'M. T. D.',
    'QTD': 'Q. T. D.',
    'YoY': 'year-over-year',
    'QoQ': 'quarter-over-quarter',
    'MoM': 'month-over-month',
    'WoW': 'week-over-week',
    'YoYY': 'Y. o. Y. Y.',

    # ── Real estate / construction ──────────────────────────────────────
    'CRE': 'C. R. E.',     # Commercial Real Estate
    'NOI': 'N. O. I.',     # Net Operating Income
    'GLA': 'G. L. A.',     # Gross Leasable Area
    'LEED': 'leed',
    'BREEAM': 'BREEM',
    'BIM': 'B. I. M.',

    # ── Country / geo codes (recurring in macro) ────────────────────────
    'PRC': 'P. R. C.',
    'DPRK': 'D. P. R. K.',
    'ROK': 'R. O. K.',
    'ROW': 'R. O. W.',     # Rest Of World
    'EM': 'E. M.',         # Emerging Markets
    'DM': 'D. M.',         # Developed Markets
    'GCC': 'G. C. C.',     # Gulf Cooperation Council
    'MENA': 'mee-na',
    'SSA': 'S. S. A.',     # Sub-Saharan Africa

    # ── Audit / risk / controls ─────────────────────────────────────────
    'COSO': 'co-so',
    'SOC1': 'sock-one',
    'ISAE': 'I. S. A. E.',
    'ICAAP': 'eye-cap',
    'ILAAP': 'eye-lap',
    'SREP': 'srep',
    'ORSA': 'or-sa',
    'GRC': 'G. R. C.',
    # ── From Acronym DB V1.1 (Excel + RTF) ──────────────────────────────────
    # Agents / Orchestration
    'A2A': 'ay-to-ay',
    'ACP': 'A. C. P.',
    'AI Agent': 'ay-eye agent',
    'APM': 'A. P. M.',
    'Agentic AI': 'agentic ay-eye',
    'AutoGen': 'auto-jen',
    'BPM': 'B. P. M.',
    'BPMN': 'B. P. M. N.',
    'CrewAI': 'crew ay-eye',
    'DSPy': 'D. S. P. Y.',
    'HITL Ops': 'human-in-the-loop ops',
    'LangChain': 'lang-chain',
    'LlamaIndex': 'lah-muh index',
    'MRKL': 'M. R. K. L.',
    'RPA': 'ar-pee-ay',
    # Benchmarks / Datasets / Evaluation
    'ARC-AGI': 'ay-ar-see-dash-ay-jee-eye',
    'BLEU': 'B. L. E. U.',
    'CIFAR': 'see-far',
    'CNN/DailyMail': 'see-en-en daily mail',
    'COCO': 'koh-koh',
    'Common Voice': 'common voice',
    'ELO': 'E. L. O.',
    'FLORES': 'F. L. O. R. E. S.',
    'GLUE': 'glue',
    'HELM': 'helm',
    'ImageNet': 'image-net',
    'LibriSpeech': 'lib-ree-speech',
    'MLPerf': 'em-ell-perf',
    'MMMU': 'em-em-em-you',
    'MNIST': 'em-nist',
    'MT-Bench': 'em-tee-dash-bee-ee-en-see-aitch',
    'ROUGE': 'R. O. U. G. E.',
    'SQuAD': 'squad',
    'SWE-bench Verified': 'swee-bench verified',
    'WER': 'W. E. R.',
    'WMT': 'W. M. T.',
    # Business / Enterprise / Finance adjacency
    'ACV': 'A. C. V.',
    'B2G': 'bee-two-jee',
    'BCP': 'B. C. P.',
    'CDD': 'C. D. D.',
    'DRP': 'D. R. P.',
    'EDD': 'E. D. D.',
    'HRIS': 'H. R. I. S.',
    'MSP': 'M. S. P.',
    'PMF': 'P. M. F.',
    'RPO': 'R. P. O.',
    'SME': 'S. M. E.',
    'VAR': 'V. A. R.',
    # Computer Vision / Multimodal / Robotics
    'AE': 'A. E.',
    'AP': 'A. P.',
    'BLIP': 'blip',
    'DDIM': 'D. D. I. M.',
    'DDPM': 'D. D. P. M.',
    'DETR': 'dee-tr',
    'DINO': 'dee-noh',
    'FPS': 'F. P. S.',
    'ICR': 'I. C. R.',
    'IoU': 'I. O. U.',
    'LDM': 'L. D. M.',
    'MAE': 'M. A. E.',
    'OD': 'O. D.',
    'OMR': 'O. M. R.',
    'SD': 'S. D.',
    'SDF': 'S. D. F.',
    'SDXL': 'S. D. X. L.',
    'SLAM': 'S. L. A. M.',
    'VQ-VAE': 'vee-cue-dash-vee-ay-ee',
    'VQGAN': 'V. Q. G. A. N.',
    'YOLO': 'yo-loh',
    'mAP': 'M. A. P.',
    # Core AI / ML
    'AL': 'A. L.',
    'ANN': 'A. N. N.',
    'AUC': 'A. U. C.',
    'AutoML': 'A. U. T. O. M. L.',
    'DL': 'D. L.',
    'DNN': 'D. N. N.',
    'DoRA': 'D. O. R. A.',
    'F1': 'ef-one',
    'FAIR': 'F. A. I. R.',
    'FL': 'F. L.',
    'GNB': 'G. N. B.',
    'GNN': 'G. N. N.',
    'HITL': 'H. I. T. L.',
    'ICA': 'I. C. A.',
    'IFT': 'I. F. T.',
    'IID': 'I. I. D.',
    'IRL': 'I. R. L.',
    'K-Means': 'kay-means',
    'KD': 'K. D.',
    'KNN': 'K. N. N.',
    'MAE': 'M. A. E.',
    'MAPE': 'M. A. P. E.',
    'MARL': 'M. A. R. L.',
    'MSE': 'M. S. E.',
    'MTL': 'M. T. L.',
    'NAS': 'N. A. S.',
    'NLG': 'en-ell-jee',
    'NLL': 'N. L. L.',
    'NLU': 'en-ell-you',
    'NN': 'N. N.',
    'PCA': 'P. C. A.',
    'RLAIF': 'R. L. A. I. F.',
    'RMSE': 'R. M. S. E.',
    'ROC': 'R. O. C.',
    'SL': 'S. L.',
    'SVM': 'S. V. M.',
    'TAI': 'T. A. I.',
    'TL': 'T. L.',
    'UL': 'U. L.',
    'UMAP': 'U. M. A. P.',
    't-SNE': 'tee-snee',
    # Fintech
    'PSD2': 'P-S-D-two',
    # Generative AI / LLMs / Transformers
    'ALiBi': 'A. L. I. B. I.',
    'BART': 'B. A. R. T.',
    'BBPE': 'B. B. P. E.',
    'BOS': 'B. O. S.',
    'BPE': 'B. P. E.',
    'CAG': 'C. A. G.',
    'CLS': 'C. L. S.',
    'CPT': 'C. P. T.',
    'Context window': 'context window',
    'DSPy': 'D. S. P. Y.',
    'DeBERTa': 'dee-bur-tuh',
    'ELMo': 'el-moh',
    'FFN': 'F. F. N.',
    'FM': 'F. M.',
    'FMs': 'F. M. S.',
    'GAI': 'G. A. I.',
    'GPT-J': 'gee-pee-tee jay',
    'GPT-NeoX': 'gee-pee-tee nee-oh-ex',
    'GenAI': 'G. E. N. A. I.',
    'HOTA': 'H. O. T. A.',
    'HyDE': 'H. Y. D. E.',
    'IFT': 'I. F. T.',
    'KV-cache': 'kay-vee-dash-see-ay-see-aitch-ee',
    'LM': 'L. M.',
    'LMM': 'L. M. M.',
    'LN': 'L. N.',
    'MHA': 'M. H. A.',
    'MLA': 'M. L. A.',
    'MLLM': 'M. L. L. M.',
    'MoA': 'M. O. A.',
    'PAD': 'P. A. D.',
    'PaLM': 'palm',
    'RARR': 'R. A. R. R.',
    'RFT': 'R. F. T.',
    'RHLF': 'R. H. L. F.',
    'RMSNorm': 'R. M. S. N. O. R. M.',
    'RPM': 'R. P. M.',
    'ReAct': 'ree-act',
    'RoBERTa': 'roh-bur-tuh',
    'RoPE': 'R. O. P. E.',
    'SA': 'S. A.',
    'SEP': 'S. E. P.',
    'SPM': 'S. P. M.',
    'SoTA': 'S. O. T. A.',
    'T5': 'tee-five',
    'TDM': 'T. D. M.',
    'TPM': 'T. P. M.',
    'TPOT': 'T. P. O. T.',
    'TPS': 'T. P. S.',
    'UNK': 'U. N. K.',
    'VLA': 'V. L. A.',
    'VLM': 'V. L. M.',
    'XLNet': 'X. L. N. E. T.',
    # Governance / Risk / Security / Regulation
    'ABAC': 'A. B. A. C.',
    'AI RMF': 'ay-eye ar-em-ef',
    'AI Safety': 'ay-eye safety',
    'AI Security': 'ay-eye security',
    'AI TRiSM': 'ay-eye trism',
    'AIBOM': 'A. I. B. O. M.',
    'AIMS': 'A. I. M. S.',
    'ATLAS': 'atlas',
    'Blue Team': 'blue team',
    'CVSS': 'C. V. S. S.',
    'DPAI': 'D. P. A. I.',
    'DPIA': 'D. P. I. A.',
    'EU AI Act': 'E-U ay-eye act',
    'FRIA': 'F. R. I. A.',
    'GPAI': 'G. P. A. I.',
    'HRAIS': 'H. R. A. I. S.',
    'HSM': 'H. S. M.',
    'IEC': 'I. E. C.',
    'ISO/IEC 22989': 'eye-so slash eye-ee-see twenty-two-nine-eighty-nine',
    'ISO/IEC 42001': 'eye-so slash eye-ee-see forty-two-oh-one',
    'LLM01': 'ell-ell-em-zero-one',
    'MITRE ATT&CK': 'my-ter attack',
    'Model Card': 'model card',
    'PI': 'P. I.',
    'PKI': 'P. K. I.',
    'RBAC': 'R. B. A. C.',
    'RMF': 'R. M. F.',
    'Red Team': 'red team',
    'SBOM': 'S. B. O. M.',
    'SBoM': 'S. B. O. M.',
    'SPII': 'S. P. I. I.',
    'System Card': 'system card',
    # Hardware / Acceleration / Compute
    'CXL': 'C. X. L.',
    'DPU': 'D. P. U.',
    'EFLOPS': 'E. F. L. O. P. S.',
    'HBM2': 'aitch-bee-em-two',
    'HBM3': 'aitch-bee-em-three',
    'HBM3E': 'aitch-bee-em-three-ee',
    'HDD': 'H. D. D.',
    'IPU': 'I. P. U.',
    'MIMD': 'M. I. M. D.',
    'NVLink': 'N. V. L. I. N. K.',
    'NVSwitch': 'N. V. S. W. I. T. C. H.',
    'OpenCL': 'O. P. E. N. C. L.',
    'OpenVINO': 'open-vee-noh',
    'PFLOPS': 'P. F. L. O. P. S.',
    'SIMD': 'S. I. M. D.',
    'SRAM': 'S. R. A. M.',
    'TDP': 'T. D. P.',
    'TFLOPS': 'T. F. L. O. P. S.',
    'TOPS': 'T. O. P. S.',
    'Triton': 'try-ton',
    'cuDNN': 'koo-dee-en-en',
    'oneAPI': 'one ay-pee-eye',
    # Healthcare / Life Sciences AI
    'CDRH': 'C. D. R. H.',
    'EHR': 'E. H. R.',
    'EMR': 'E. M. R.',
    'GMLP': 'G. M. L. P.',
    'PCCP': 'P. C. C. P.',
    'RWD': 'R. W. D.',
    'RWE': 'R. W. E.',
    'SaMD': 'S. A. M. D.',
    # MLOps / DataOps / Cloud / Software
    'AIOps': 'A. I. O. P. S.',
    'AOT': 'A. O. T.',
    'AZ': 'A. Z.',
    'BI': 'B. I.',
    'CI/CD': 'see-eye-slash-see-dee',
    'DAG': 'D. A. G.',
    'DB': 'D. B.',
    'DBMS': 'D. B. M. S.',
    'DataOps': 'D. A. T. A. O. P. S.',
    'DevOps': 'D. E. V. O. P. S.',
    'ELT': 'E. L. T.',
    'ETL': 'E. T. L.',
    'FinOps': 'F. I. N. O. P. S.',
    'GCS': 'G. C. S.',
    'GUI': 'G. U. I.',
    'IaC': 'I. A. C.',
    'K8s': 'kay-eight-ess',
    'LLMOps': 'L. L. M. O. P. S.',
    'MLIR': 'M. L. I. R.',
    'MLOps': 'M. L. O. P. S.',
    'MQ': 'M. Q.',
    'OCI': 'O. C. I.',
    'OLAP': 'O. L. A. P.',
    'OLTP': 'O. L. T. P.',
    'ONNX RT': 'on-iks ar-tee',
    'RDBMS': 'R. D. B. M. S.',
    'RPC': 'R. P. C.',
    'SLI': 'S. L. I.',
    'SRE': 'S. R. E.',
    'TCP': 'T. C. P.',
    'TF': 'T. F.',
    'TFLite': 'T. F. L. I. T. E.',
    'TVM': 'T. V. M.',
    'VM': 'V. M.',
    'VMs': 'V. M. S.',
    'VMware': 'V. M. W. A. R. E.',
    'XLA': 'X. L. A.',
    # Retrieval / Search / NLP Evaluation
    'ANN': 'A. N. N.',
    'BLEU': 'B. L. E. U.',
    'BM25': 'bee-em-two-five',
    'HNSW': 'aitch-en-ess-double-you',
    'IR': 'I. R.',
    'IVF': 'I. V. F.',
    'METEOR': 'M. E. T. E. O. R.',
    'MMR': 'M. M. R.',
    'MRC': 'M. R. C.',
    'Milvus': 'M. I. L. V. U. S.',
    'NDCG': 'N. D. C. G.',
    'NER': 'N. E. R.',
    'NLI': 'N. L. I.',
    'OPQ': 'O. P. Q.',
    'PQ': 'P. Q.',
    'Qdrant': 'Q. D. R. A. N. T.',
    'ROUGE': 'R. O. U. G. E.',
    'RRF': 'R. R. F.',
    'STS': 'S. T. S.',
    'TF-IDF': 'tee-ef-dash-eye-dee-ef',
    'kNN': 'K. N. N.',
    'pgvector': 'P. G. V. E. C. T. O. R.',
    # Speech / Audio / TTS
    'AAC': 'A. A. C.',
    'API TTS': 'ay-pee-eye tee-tee-ess',
    'CER': 'C. E. R.',
    'Diar': 'D. I. A. R.',
    'F0': 'ef-zero',
    'HiFi-GAN': 'hi-fi gan',
    'IPA': 'I. P. A.',
    'LUFS': 'L. U. F. S.',
    'MFCC': 'M. F. C. C.',
    'MOS': 'M. O. S.',
    'MP3': 'em-pee-three',
    'Opus': 'O. P. U. S.',
    'PCM': 'P. C. M.',
    'PER': 'P. E. R.',
    'PESQ': 'P. E. S. Q.',
    'RMS': 'R. M. S.',
    'SID': 'S. I. D.',
    'SNR': 'S. N. R.',
    'SSML': 'S. S. M. L.',
    'STOI': 'S. T. O. I.',
    'STT': 'ess-tee-tee',
    'SV': 'S. V.',
    'Tacotron': 'taco-tron',
    'VAD': 'V. A. D.',
    'VALL-E': 'val-ee',
    'Vocoder': 'V. O. C. O. D. E. R.',
    'WAV': 'W. A. V.',
    'WER': 'W. E. R.',
    'WaveNet': 'wave-net',
    'dBFS': 'D. B. F. S.',
    # Web / Data Formats / Licensing
    'AGPL': 'A. G. P. L.',
    'Apache-2.0': 'apache two point oh',
    'Atom': 'A. T. O. M.',
    'Avro': 'av-roh',
    'BSD': 'B. S. D.',
    'CC-BY': 'see-see by',
    'CORS': 'C. O. R. S.',
    'DASH': 'D. A. S. H.',
    'DOM': 'D. O. M.',
    'GPL': 'G. P. L.',
    'HLS': 'H. L. S.',
    'JSON-LD': 'jay-ess-oh-en-dash-ell-dee',
    'MIT': 'M. I. T.',
    'MPEG': 'M. P. E. G.',
    'ORC': 'O. R. C.',
    'Parquet': 'par-kay',
    'RDF': 'R. D. F.',
    'RSS': 'R. S. S.',
    'SPARQL': 'S. P. A. R. Q. L.',
    'URI': 'U. R. I.',
    'WebGPU': 'W. E. B. G. P. U.',
}

_SPELL_OUT_FR_OVERRIDES: dict[str, str] = {
    # ── Compact format for FR ─────────────────────────────────────────────
    # No spaces between letters (e.g. 'L.L.M.' vs 'L. L. M.') — the space
    # creates an extra word-boundary pause that makes acronyms sound slow.
    # With dots-only, Cartesia reads them as tight abbreviations.
    #
    # IA: deliberately NOT dot-spelled — 'I. A.' caused a stiff two-beat
    # pause that sounded unnatural in French. Cartesia's native FR prosody
    # pronounces bare "IA" fluidly as "ee-ah" without any override needed.
    #
    # AI: kept as compact English form. The spaced 'A. I.' (with FR letter
    # names: "ah… ee") was unintelligible; 'A.I.' reads as a tight
    # abbreviation closer to the English "A-I" listeners expect.
    'AI': 'A.I.',
    # ── AI / ML core ─────────────────────────────────────────────────────
    'LLM': 'L.L.M.',
    'LLMs': 'L.L.M.s',
    'SLM': 'S.L.M.',
    'SLMs': 'S.L.M.s',
    'GPT': 'G. P. T.',
    'AGI': 'A.G.I.',
    'NLP': 'N.L.P.',
    'RLHF': 'R.L.H.F.',
    'DPO': 'D.P.O.',
    'SFT': 'S.F.T.',
    'MoE': 'M.o.E.',
    'OOD': 'O.O.D.',
    # ── Infra / APIs ─────────────────────────────────────────────────────
    'API': 'A.P.I.',
    'APIs': 'A.P.I.s',
    'MCP': 'M.C.P.',
    'SDK': 'S.D.K.',
    'SDKs': 'S.D.K.s',
    'CLI': 'C.L.I.',
    'IDE': 'I.D.E.',
    'VPN': 'V.P.N.',
    # ── Hardware ─────────────────────────────────────────────────────────
    'GPU': 'G.P.U.',
    'GPUs': 'G.P.U.s',
    'CPU': 'C.P.U.',
    'CPUs': 'C.P.U.s',
    'TPU': 'T.P.U.',
    'TPUs': 'T.P.U.s',
    'NPU': 'N.P.U.',
    'NPUs': 'N.P.U.s',
    'HPC': 'H.P.C.',
    'HBM': 'H.B.M.',
    'VRAM': 'V.R.A.M.',
    'DRAM': 'D.R.A.M.',
    'FPGA': 'F.P.G.A.',
    'FPGAs': 'F.P.G.A.s',
    # ── Benchmarks ───────────────────────────────────────────────────────
    'MMLU': 'M.M.L.U.',
    'GPQA': 'G.P.Q.A.',
    'BBH': 'B.B.H.',
    # ── Org titles ───────────────────────────────────────────────────────
    'CEO': 'C. E. O.',
    'CTO': 'C.T.O.',
    'CFO': 'C.F.O.',
    'COO': 'C.O.O.',
    'CIO': 'C.I.O.',
    'CISO': 'C.I.S.O.',
    'IPO': 'I.P.O.',
    'IPOs': 'I.P.O.s',
    'ROI': 'R.O.I.',
    'KPI': 'K.P.I.',
    'KPIs': 'K.P.I.s',
    'OKR': 'O.K.R.',
    'OKRs': 'O.K.R.s',
    # ── Finance ──────────────────────────────────────────────────────────
    'GDP': 'G.D.P.',
    'CPI': 'C.P.I.',
    # ── FR-specific acronyms (compact) ───────────────────────────────────
    'PDG': 'P. D. G.',      # Président-directeur général
    'DG': 'D. G.',
    'DSI': 'D. S. I.',      # Directeur des systèmes d'information
    'PME': 'P. M. E.',
    'PMI': 'P. M. I.',
    'TPE': 'T. P. E.',
    'UE': 'U. E.',
    'ONU': 'O.N.U.',
    'RGPD': 'R.G.P.D.',   # = GDPR
    'PIB': 'P.I.B.',      # = GDP
    'OTAN': 'OTAN',       # pronounced as a word in French
    'GAFAM': 'GAFAM',     # pronounced as a word in French
    'R&D': 'R. et D.',    # Recherche et développement
    # FR letter names differ from EN — phonetic respelling where needed
    'BERT': 'Beurt',
    'LaTeX': 'La-Tek',
    # ── From Acronym DB V1.1 (Excel + RTF) ──────────────────────────────────
    # Agents / Orchestration
    'A2A': 'a-deux-a',
    'AI Agent': 'é-aï agent',
    'Agentic AI': 'agentique é-aï',
    'AutoGen': 'auto-jène',
    'CrewAI': 'crew é-aï',
    'HITL Ops': 'opérations human-in-the-loop',
    'LangChain': 'langue-chain',
    'LlamaIndex': 'lama index',
    'RPA': 'èr-pé-a',
    # Benchmarks / Datasets / Evaluation
    'ARC-AGI': 'a-èr-cé-tiret-a-jé-i',
    'CIFAR': 'ci-far',
    'CNN/DailyMail': 'cé-èn-èn daily mail',
    'COCO': 'ko-ko',
    'GLUE': 'glou',
    'ImageNet': 'image-nette',
    'LibriSpeech': 'libri-spitch',
    'MLPerf': 'èm-èl-perf',
    'MMMU': 'èm-èm-èm-u',
    'MNIST': 'èm-niste',
    'MT-Bench': 'èm-té-tiret-bé-e-èn-cé-ache',
    'SQuAD': 'skouade',
    'SWE-bench Verified': 'soui-bench verified',
    # Business / Enterprise / Finance adjacency
    'B2G': 'bé-deux-jé',
    # Computer Vision / Multimodal / Robotics
    'DETR': 'dé-teur',
    'DINO': 'di-no',
    'VQ-VAE': 'vé-ku-tiret-vé-a-e',
    'YOLO': 'yo-lo',
    # Core AI / ML
    'F1': 'èf-un',
    'K-Means': 'ka-means',
    'NLG': 'èn-èl-jé',
    'NLU': 'èn-èl-u',
    't-SNE': 'té-sni',
    # Fintech
    'PSD2': 'pé-ess-dé-deux',
    # Generative AI / LLMs / Transformers
    'Context window': 'fenêtre de contexte',
    'DeBERTa': 'dé-berta',
    'ELMo': 'èl-mo',
    'GPT-J': 'jé-pé-té ji',
    'GPT-NeoX': 'jé-pé-té néo-iks',
    'KV-cache': 'ka-vé-tiret-cé-a-cé-ache-e',
    'PaLM': 'paume',
    'ReAct': 'ri-act',
    'RoBERTa': 'ro-berta',
    'T5': 'té-cinq',
    # Governance / Risk / Security / Regulation
    'AI RMF': 'é-aï èr-èm-èf',
    'AI Safety': "sécurité de l'IA",
    'AI Security': "sécurité informatique de l'IA",
    'AI TRiSM': 'é-aï trisme',
    'EU AI Act': 'i-ou é-aï acte',
    'ISO/IEC 22989': 'i-zo barre i-e-c vingt-deux neuf quatre-vingt-neuf',
    'ISO/IEC 42001': 'i-zo barre i-e-c quarante-deux zéro un',
    'LLM01': 'èl-èl-èm-zéro-un',
    'MITRE ATT&CK': 'maï-teur attaque',
    'Model Card': 'fiche modèle',
    'System Card': 'fiche système',
    # Hardware / Acceleration / Compute
    'HBM2': 'ache-bé-èm-deux',
    'HBM3': 'ache-bé-èm-trois',
    'HBM3E': 'ache-bé-èm-trois-e',
    'OpenVINO': 'open-vi-no',
    'Triton': 'traï-ton',
    'cuDNN': 'kou-dé-èn-èn',
    'oneAPI': 'ouane a-pé-i',
    # MLOps / DataOps / Cloud / Software
    'CI/CD': 'cé-i-barre oblique-cé-dé',
    'K8s': 'ka-huit-ès',
    'ONNX RT': 'on-iks ère-té',
    # Retrieval / Search / NLP Evaluation
    'BM25': 'bé-èm-deux-cinq',
    'HNSW': 'ache-èn-ès-double-vé',
    'TF-IDF': 'té-èf-tiret-i-dé-èf',
    # Speech / Audio / TTS
    'API TTS': 'a-pé-i té-té-ès',
    'F0': 'èf-zéro',
    'HiFi-GAN': 'haï-faï gane',
    'MP3': 'èm-pé-trois',
    'STT': 'ès-té-té',
    'VALL-E': 'vali',
    'WaveNet': 'wave-nette',
    # Web / Data Formats / Licensing
    'Apache-2.0': 'apache deux point zéro',
    'Avro': 'avro',
    'CC-BY': 'cé-cé by',
    'JSON-LD': 'ji-ès-o-èn-tiret-èl-dé',
    'Parquet': 'parquet',
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
# Primary break candidates (strong pauses): commas, semicolons, em/en dashes, colons.
_LONG_SENT_BREAK = re.compile(r'[,;:—–]\s')

# Secondary break candidates (conjunctions): only used when no primary break sits
# in the target window. Operates on word boundaries so "android" is not a hit
# for "and". Order matters — earlier conjunctions are preferred for cleaner cuts.
_CONJUNCTION_BREAK = re.compile(
    r'\s(?:'
    r'and|but|while|because|though|although|since|as|so|which|that'
    r'|mais|donc|car|lorsque|puisque|alors|quand|comme|ni'
    r')\s'
)

# Em/en dashes and spaced hyphens (« A - B ») cause 500-800ms Cartesia silences.
# The pattern absorbs surrounding spaces so replacement doesn't leave double spaces.
_EM_EN_DASHES = re.compile(r' *[—–] *| {1,3}-(?= )')

# Hyphen in version/model names: «GPT-5.5»→«GPT 5.5», «MiMo-V2.5-Pro»→«MiMo V2.5 Pro»,
# «claude-3»→«claude 3», «MLP-Mixer»→«MLP Mixer».
# Safe for French compounds (multi-étapes, vision-langage): those have lowercase→lowercase
# which is excluded — only lowercase→digit and any→uppercase/digit are replaced.
_VERSION_HYPHEN = re.compile(r'(?<=[A-Za-z0-9\.])-(?=[A-Z0-9])|(?<=[a-z])-(?=[0-9])')


def _replace_dashes(text: str) -> str:
    """Replace em/en dashes and version-number hyphens with a space to avoid Cartesia pauses."""
    text = _EM_EN_DASHES.sub(' ', text)
    text = _VERSION_HYPHEN.sub(' ', text)
    # Re-collapse any double spaces introduced by dash removal.
    text = re.sub(r'  +', ' ', text)
    return text


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
    'DARPA', 'BAFIN', 'GAFAM', 'MATH', 'MATHS',
    'BRICS', 'ASEAN', 'NAFTA', 'MENA', 'BREEAM',
    'JOLTS', 'OPEC', 'ESOP', 'SWOT', 'TOWS',
    'MERCOSUR',
    # Proper nouns / product names written all-caps that should be read as a word
    'OPENAI', 'ARM', 'META', 'APPLE', 'AMAZON', 'GOOGLE', 'ORACLE',
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


def _cap_sentence_length(text: str, max_chars: int = 210) -> str:
    """Break lines longer than max_chars at a natural pause point.

    Cartesia's prosody model tapers off on long unbroken utterances — the engine
    predicts a breath point that never arrives and compensates by winding down
    the voice volume ('running out of air' effect). Breaking at a comma,
    semicolon, dash, colon, or — in last resort — at a conjunction gives the
    engine a clean breath point with full volume on the second half.

    210 chars ≈ 35 spoken words — enough for a full, natural-sounding sentence
    without triggering the volume-taper. 150 was too aggressive: every comma
    became an artificial sentence boundary, producing a choppy, staccato rhythm
    with muffled endings (sentence-final prosody applied mid-clause).
    Applied to TTS input only; script.txt stays canonical.
    """
    return '\n'.join(_shorten_line(line, max_chars) for line in text.split('\n'))


# Minimum length of the FIRST half of a split — anything below feels chopped.
# 50 chars ≈ 8-10 spoken words, the lower bound for a coherent standalone clause.
_MIN_FIRST_HALF = 50


def _shorten_line(line: str, max_chars: int) -> str:
    """Recursively shorten one line until every segment is ≤ max_chars.

    Tiered split-point search:
      1. Primary breaks (`, ; : — –`) in the [_MIN_FIRST_HALF, max_chars] window.
      2. Conjunctions (`and / but / while / because / though …`) in same window.
      3. The latest primary break BEYOND max_chars (last-resort, unblocks lines
         that have no usable break in the target window — better to split slightly
         long than not split at all).
      4. Give up — return the line untouched.
    """
    if len(line) <= max_chars:
        return line

    # Tier 1 — primary punctuation break in target window
    for m in _LONG_SENT_BREAK.finditer(line):
        pos = m.start()
        if _MIN_FIRST_HALF <= pos <= max_chars:
            return _do_split(line, pos, max_chars)

    # Tier 2 — conjunction break in target window
    for m in _CONJUNCTION_BREAK.finditer(line):
        pos = m.start()
        if _MIN_FIRST_HALF <= pos <= max_chars:
            return _do_split(line, pos, max_chars)

    # Tier 3 — first primary break BEYOND max_chars (within 1.5× max)
    for m in _LONG_SENT_BREAK.finditer(line):
        pos = m.start()
        if max_chars < pos <= int(max_chars * 1.5):
            return _do_split(line, pos, max_chars)

    return line  # no usable split point — leave as is


def _do_split(line: str, pos: int, max_chars: int) -> str:
    """Split `line` at byte offset `pos`, keep original punctuation, capitalize the second.

    Preserve the trailing comma/semicolon so Cartesia uses continuation prosody
    (brief pause, sustained volume) rather than sentence-final prosody (taper +
    long silence) at the split point. The split is at a mid-sentence break, not
    a true sentence end.
    """
    # Keep the punctuation character at pos (comma, semicolon, etc.) so Cartesia
    # hears a natural comma pause rather than a full-stop volume taper.
    first = line[:pos + 1].rstrip()
    rest = line[pos + 1:].lstrip()
    if rest and rest[0].islower():
        rest = rest[0].upper() + rest[1:]
    if not rest:
        return first
    return first + '\n' + _shorten_line(rest, max_chars)


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


_DASHES = re.compile(r'[—–]| +-')

def _replace_dashes(text: str) -> str:
    """Replace em/en dashes and spaced hyphens with commas.

    Cartesia treats — and – as hard pause signals, producing silences of
    500-800 ms. A comma gives a natural short breath instead.
    Applied AFTER _cap_sentence_length so dashes are still available as
    sentence-split candidates before being stripped from the TTS text.
    """
    return _DASHES.sub(',', text)


def split_script(text: str, max_chars: int = 1800) -> list[str]:
    """Split the script into paragraph-aligned chunks under max_chars each.

    Each chunk is sent as a separate transcript within a single shared
    context_id websocket session, so Cartesia keeps prosody and voice state
    across the whole script. There are no per-chunk restart artefacts.

    Paragraphs are joined with a single \\n (not \\n\\n) so Cartesia treats each
    boundary as a short breath rather than a full paragraph break. \\n\\n caused
    noticeably long silences between every paragraph in the synthesized audio.
    """
    paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
    chunks: list[str] = []
    current = ''
    for paragraph in paragraphs:
        candidate = f"{current}\n{paragraph}".strip() if current else paragraph
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
        # Persist the acronyms encountered so the operator has a cumulative
        # list to review (user instruction 2026-04-17: "conserve une liste").
        # Stored per-locale at data/state/acronyms_seen_{locale}.json with
        # {acronym: {count, first_seen, last_seen}}.  Failures are silent —
        # persistence is a convenience, not a pipeline requirement.
        try:
            _persist_acronyms_seen(auto_spelled, settings.locale or 'en')
        except Exception as exc:  # noqa: BLE001
            logger.warning('Acronym persistence skipped: %s', exc)
    spoken_script = _normalize_tts_whitespace(spoken_script)
    spoken_script = _strip_trailing_pause_tokens(spoken_script)
    # Cap long sentences so Cartesia never tapers volume on a single utterance.
    # Splits any line > 240 chars at its first usable comma/semicolon ≥ 80 chars in.
    spoken_script = _cap_sentence_length(spoken_script)
    spoken_script = _replace_dashes(spoken_script)
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
        await asyncio.wait_for(ws.send(json.dumps(request)), timeout=WS_SEND_TIMEOUT_S)

        audio = bytearray()
        while True:
            # Bound each frame wait so a server that accepts the connection
            # but never emits audio (observed during model cold-start
            # failures) surfaces as a TimeoutError caught by the retry loop,
            # not a workflow that silently runs until the 6-hour CI cap.
            msg = json.loads(await asyncio.wait_for(ws.recv(), timeout=WS_RECV_TIMEOUT_S))
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
            await asyncio.wait_for(ws.send(json.dumps(request)), timeout=WS_SEND_TIMEOUT_S)

        audio = bytearray()
        while True:
            # See WS_RECV_TIMEOUT_S rationale above — bounded per-frame wait
            # turns a silent hang into a normal exception the outer retry
            # loop in `_render_script_websocket` will pick up.
            msg = json.loads(await asyncio.wait_for(ws.recv(), timeout=WS_RECV_TIMEOUT_S))
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
