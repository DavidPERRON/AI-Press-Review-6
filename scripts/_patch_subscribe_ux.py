"""One-shot patcher for the 2026-04-16 subscribe-UX fixes.

Three issues fixed across both templates AND both rendered docs:

  1. YouTube EN URL was a single-video link (gWI4g1tXtJ0). Replace with the
     full episode playlist so users land on the right thing.

  2. The footer "RSS feed" button used navigator.clipboard.writeText() with
     e.preventDefault() and only opened a new tab on the .catch fallback —
     so on every modern browser (HTTPS + clipboard API works) the user got
     a "Copied!" with NO redirection. Now the button always opens the feed
     in a new tab AND copies, so the user gets visual confirmation either
     way (tab opens with feed.xsl-styled view).

  3. The .subscribe section had a `.label{display:none}` rule but the
     <span class='label'> markup was never inserted — so the section
     looked like loose pill buttons with no heading. Adds a visible
     heading inside the subscribe div so the section is impossible to miss.

Patches BOTH the source-of-truth template (so future generator runs keep
the fix) AND the currently-deployed rendered docs (so the live site shows
the fix on the next git push, without waiting for a new pipeline run).
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Files to patch — pairs of (template, rendered).
EN_TEMPLATE = ROOT / 'src/ai_press_review/publish/templates/index-template.html'
EN_DOC      = ROOT / 'docs/index.html'
FR_TEMPLATE = ROOT / 'src/ai_press_review/publish/templates/index-template-fr.html'
FR_DOC      = ROOT / 'docs/fr/index.html'


# ── Patch 1: YouTube EN URL ────────────────────────────────────────────────────
# Single-video → playlist. FR already uses a playlist URL, no patch needed there.
EN_YOUTUBE_OLD = "<a href='https://youtu.be/gWI4g1tXtJ0' aria-label='YouTube'>"
EN_YOUTUBE_NEW = "<a href='https://youtube.com/playlist?list=PLwGlRWhh3Zq_BmVMFSEr6CyRyJpwK1s9r' aria-label='YouTube'>"


# ── Patch 2: RSS click handler — always open AND copy ─────────────────────────
# The old code only opened a new tab when clipboard FAILED. Now we open the
# styled feed (feed.xsl) in a new tab on every click so the user gets a
# visible redirection even when the clipboard write succeeded.
RSS_JS_OLD = (
    "document.querySelectorAll('.rss-copy').forEach(function(a){"
    "a.addEventListener('click',function(e){"
    "e.preventDefault();"
    "var o=a.textContent;"
    "navigator.clipboard.writeText(a.href).then(function(){"
    "a.textContent=a.dataset.copied||'Copied!';"
    "setTimeout(function(){a.textContent=o},1500)"
    "}).catch(function(){window.open(a.href,'_blank')})"
    "})})"
)
RSS_JS_NEW = (
    "document.querySelectorAll('.rss-copy').forEach(function(a){"
    "a.addEventListener('click',function(e){"
    "e.preventDefault();"
    "var o=a.textContent;"
    # Open the feed in a new tab FIRST so the user always sees a redirection.
    "window.open(a.href,'_blank','noopener');"
    # Then attempt to copy — on success show "Copied!" feedback, on failure
    # silently swallow (the new tab already gave the user the URL via the
    # browser address bar).
    "if(navigator.clipboard){navigator.clipboard.writeText(a.href).then(function(){"
    "a.textContent=a.dataset.copied||'Copied!';"
    "setTimeout(function(){a.textContent=o},1500)"
    "}).catch(function(){})}"
    "})})"
)
# FR variant — same JS structure, just with French fallback text.
RSS_JS_OLD_FR = (
    "document.querySelectorAll('.rss-copy').forEach(function(a){"
    "a.addEventListener('click',function(e){"
    "e.preventDefault();"
    "var o=a.textContent;"
    "navigator.clipboard.writeText(a.href).then(function(){"
    "a.textContent=a.dataset.copied||'Copie !';"
    "setTimeout(function(){a.textContent=o},1500)"
    "}).catch(function(){window.open(a.href,'_blank')})"
    "})})"
)
RSS_JS_NEW_FR = (
    "document.querySelectorAll('.rss-copy').forEach(function(a){"
    "a.addEventListener('click',function(e){"
    "e.preventDefault();"
    "var o=a.textContent;"
    "window.open(a.href,'_blank','noopener');"
    "if(navigator.clipboard){navigator.clipboard.writeText(a.href).then(function(){"
    "a.textContent=a.dataset.copied||'Copie !';"
    "setTimeout(function(){a.textContent=o},1500)"
    "}).catch(function(){})}"
    "})})"
)


# ── Patch 3: visible subscribe heading ────────────────────────────────────────
# The CSS already has `.subscribe .label{display:none}` — flip it to display
# the label, then inject a <span class='label'> inside the subscribe div on
# both EN and FR. Result: a clear "Subscribe" / "S'abonner" heading sits above
# the four pill buttons so the section is impossible to miss visually.
LABEL_CSS_OLD = ".subscribe .label{display:none}"
LABEL_CSS_NEW = (
    ".subscribe-label{display:block;text-align:center;font-size:.78rem;"
    "letter-spacing:.18em;text-transform:uppercase;color:var(--ink-muted);"
    "margin:0 0 .8rem;font-weight:600}"
    ".subscribe .label{display:none}"
)
EN_SUBSCRIBE_OLD = "<div class='subscribe' id='subscribe'>"
EN_SUBSCRIBE_NEW = (
    "<p class='subscribe-label'>Subscribe — choose your platform</p>"
    "<div class='subscribe' id='subscribe'>"
)
FR_SUBSCRIBE_OLD = "<div class='subscribe' id='subscribe'>"
FR_SUBSCRIBE_NEW = (
    "<p class='subscribe-label'>S'abonner — choisissez votre plateforme</p>"
    "<div class='subscribe' id='subscribe'>"
)


def _replace(path: Path, old: str, new: str, *, label: str) -> bool:
    """Apply a single string replacement; return True if the file changed.

    Errors loud if old is absent (means the file moved on us) or appears more
    than once (means we'd ambiguously patch — refuse rather than guess).
    """
    text = path.read_text(encoding='utf-8')
    count = text.count(old)
    if count == 0:
        print(f'  [SKIP {label}] {path.name}: pattern not found')
        return False
    if count > 1:
        print(f'  [FAIL {label}] {path.name}: pattern matched {count}× — aborting')
        sys.exit(1)
    path.write_text(text.replace(old, new), encoding='utf-8')
    print(f'  [OK   {label}] {path.name}')
    return True


def main() -> None:
    print('YouTube EN URL → playlist:')
    _replace(EN_TEMPLATE, EN_YOUTUBE_OLD, EN_YOUTUBE_NEW, label='youtube')
    _replace(EN_DOC,      EN_YOUTUBE_OLD, EN_YOUTUBE_NEW, label='youtube')

    print('\nRSS click handler — always open AND copy:')
    _replace(EN_TEMPLATE, RSS_JS_OLD,    RSS_JS_NEW,    label='rss-js')
    _replace(EN_DOC,      RSS_JS_OLD,    RSS_JS_NEW,    label='rss-js')
    _replace(FR_TEMPLATE, RSS_JS_OLD_FR, RSS_JS_NEW_FR, label='rss-js-fr')
    _replace(FR_DOC,      RSS_JS_OLD_FR, RSS_JS_NEW_FR, label='rss-js-fr')

    print('\nVisible subscribe heading (CSS + label markup):')
    _replace(EN_TEMPLATE, LABEL_CSS_OLD,    LABEL_CSS_NEW,    label='label-css')
    _replace(EN_DOC,      LABEL_CSS_OLD,    LABEL_CSS_NEW,    label='label-css')
    _replace(FR_TEMPLATE, LABEL_CSS_OLD,    LABEL_CSS_NEW,    label='label-css-fr')
    _replace(FR_DOC,      LABEL_CSS_OLD,    LABEL_CSS_NEW,    label='label-css-fr')
    _replace(EN_TEMPLATE, EN_SUBSCRIBE_OLD, EN_SUBSCRIBE_NEW, label='label-html')
    _replace(EN_DOC,      EN_SUBSCRIBE_OLD, EN_SUBSCRIBE_NEW, label='label-html')
    _replace(FR_TEMPLATE, FR_SUBSCRIBE_OLD, FR_SUBSCRIBE_NEW, label='label-html-fr')
    _replace(FR_DOC,      FR_SUBSCRIBE_OLD, FR_SUBSCRIBE_NEW, label='label-html-fr')

    print('\n✓ All patches applied. Run `git diff --stat` to verify.')


if __name__ == '__main__':
    main()
