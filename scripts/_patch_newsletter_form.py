"""Inject the email-newsletter signup form into both index templates.

Patches FOUR files (sources-of-truth + currently-deployed copies) so the
change ships on the next `git push` without waiting for a pipeline run:

  src/ai_press_review/publish/templates/index-template.html      (EN source)
  src/ai_press_review/publish/templates/index-template-fr.html   (FR source)
  docs/index.html                                                (EN live)
  docs/fr/index.html                                             (FR live)

What the form does:
  - Visible <input type='email'> + consent checkbox + submit button.
  - Hidden honeypot <input name='website'> (real users leave it empty —
    bots fill every field; the Worker silently 200s on a non-empty value).
  - On submit: POSTs JSON {email, locale, consent, website} to
    `data-api='https://aequitus.net/api/subscribe.php'` (cross-origin to
    the LWS Perso PHP backend — see lws/newsletter/README.md). The PHP
    endpoint echoes the Origin header in CORS (allowlist, not '*') so the
    browser will let the response through when served from
    podcast.aequitus.net. If you move the backend elsewhere, only this
    one constant changes.
  - Inline status under the form: "Sending…" → "You're in!" / error msg.
  - Both EN and FR strings are baked in (data-locale='en'|'fr').

Why this lives next to .subscribe (the platform pills) rather than in its
own section: the existing nav `<a href='#subscribe'>` is the user's mental
model for "I want to subscribe". Anchoring the new wrapper to id='subscribe'
keeps that link working AND surfaces the email form first when they jump to
it. Platform pills now sit below, under a "or pick your platform" divider.

Idempotent: re-running it after a successful patch is a no-op (each replace
is guarded — if the new marker is already present, the patch is skipped).

Run with:
    python scripts/_patch_newsletter_form.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EN_TEMPLATE = ROOT / 'src/ai_press_review/publish/templates/index-template.html'
EN_DOC      = ROOT / 'docs/index.html'
FR_TEMPLATE = ROOT / 'src/ai_press_review/publish/templates/index-template-fr.html'
FR_DOC      = ROOT / 'docs/fr/index.html'


# ── CSS injected just before </style> ─────────────────────────────────────────
# Reuses the existing palette tokens (--gold, --ink, --rule-strong, --bg).
# The .nl-honey rule visually-hides the honeypot field without breaking screen
# readers (aria-hidden=true plus negative left positioning is a belt-and-braces
# pattern; opacity:0 ensures it never paints even briefly during page load).
NEWSLETTER_CSS = (
    '.subscribe-block{margin:0 0 1.6rem}'
    ".nl-label{font-family:'EB Garamond',serif;font-weight:700;font-variant:small-caps;"
    "letter-spacing:.18em;font-size:.92rem;color:var(--gold);margin:0 0 .35rem;text-align:center}"
    '.nl-sub{color:var(--ink-soft);font-size:.96rem;margin:0 0 1rem;text-align:center;font-style:italic}'
    '.newsletter{max-width:520px;margin:0 auto 1.4rem;text-align:left;position:relative}'
    '.nl-row{display:flex;gap:.5rem;margin:0 0 .65rem}'
    '.nl-email{flex:1;min-width:0;background:rgba(217,162,74,.04);border:1px solid var(--rule-strong);'
    'border-radius:6px;padding:.65rem .9rem;color:var(--ink);font-family:inherit;font-size:1rem;'
    'line-height:1.3;-webkit-appearance:none;appearance:none}'
    '.nl-email::placeholder{color:var(--ink-muted);opacity:.85}'
    '.nl-email:focus{outline:none;border-color:var(--gold);background:rgba(217,162,74,.08)}'
    '.nl-btn{flex:0 0 auto;background:var(--gold);color:var(--bg);border:1px solid var(--gold);'
    "border-radius:6px;padding:.65rem 1.4rem;font-family:inherit;font-variant:small-caps;"
    'letter-spacing:.16em;font-size:.92rem;font-weight:700;cursor:pointer;'
    'transition:background .15s,color .15s,border-color .15s}'
    '.nl-btn:hover:not(:disabled){background:#EBC172;border-color:#EBC172}'
    '.nl-btn:disabled{opacity:.55;cursor:not-allowed}'
    '.nl-honey{position:absolute;left:-9999px;width:1px;height:1px;opacity:0;pointer-events:none}'
    '.nl-consent{display:flex;gap:.55rem;align-items:flex-start;font-size:.86rem;line-height:1.45;'
    'color:var(--ink-muted);margin:0 0 .6rem;cursor:pointer}'
    '.nl-consent input{margin-top:.25rem;flex:0 0 auto;accent-color:var(--gold)}'
    '.nl-msg{font-size:.92rem;margin:.4rem 0 0;min-height:1.2em;text-align:center}'
    '.nl-msg.ok{color:var(--gold)}'
    '.nl-msg.err{color:#E58A6E}'
    '.nl-divider{font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;color:var(--ink-muted);'
    'margin:1.4rem 0 .8rem;text-align:center;font-weight:600}'
    '@media (max-width:560px){.nl-row{flex-direction:column}.nl-btn{padding:.7rem 1.2rem}}'
)


# ── JS injected just before </body> ───────────────────────────────────────────
# IIFE so we don't pollute window. Bound to the FIRST .newsletter form on the
# page (each index has exactly one). `data-locale` switches user-facing strings
# between EN and FR; `data-api` is the POST target (same-origin by default).
NEWSLETTER_JS = (
    "<script>"
    "(function(){"
    "var form=document.querySelector('.newsletter');if(!form)return;"
    "var msg=form.querySelector('.nl-msg');"
    "var btn=form.querySelector('.nl-btn');"
    "var apiUrl=form.dataset.api||'/api/subscribe';"
    "var locale=form.dataset.locale||'en';"
    "var T=locale==='fr'?{"
    "sending:'Envoi\\u2026',"
    "ok:'Merci\\u00a0! C\\'est not\\u00e9.',"
    "already:'Vous \\u00eates d\\u00e9j\\u00e0 inscrit\\u00b7e \\u2014 merci\\u00a0!',"
    "invalid:'Adresse email invalide.',"
    "consent:'Merci de cocher la case de consentement.',"
    "rate:'Trop de tentatives \\u2014 r\\u00e9essayez dans une minute.',"
    "server:'Erreur serveur \\u2014 r\\u00e9essayez plus tard.',"
    "network:'Connexion impossible \\u2014 v\\u00e9rifiez votre r\\u00e9seau.'"
    "}:{"
    "sending:'Sending\\u2026',"
    "ok:'You\\'re in \\u2014 thanks!',"
    "already:'You\\'re already subscribed \\u2014 thanks!',"
    "invalid:'That email looks invalid.',"
    "consent:'Please tick the consent box.',"
    "rate:'Too many tries \\u2014 wait a minute and retry.',"
    "server:'Server error \\u2014 try again later.',"
    "network:'Couldn\\'t reach the server \\u2014 check your connection.'"
    "};"
    "form.addEventListener('submit',function(e){"
    "e.preventDefault();"
    "var fd=new FormData(form);"
    "var payload={"
    "email:String(fd.get('email')||'').trim(),"
    "locale:locale,"
    "consent:fd.get('consent')==='on',"
    "website:fd.get('website')||''"
    "};"
    "msg.textContent='';msg.className='nl-msg';"
    "if(!payload.email||payload.email.indexOf('@')<1){"
    "msg.textContent=T.invalid;msg.className='nl-msg err';return"
    "}"
    "if(!payload.consent){"
    "msg.textContent=T.consent;msg.className='nl-msg err';return"
    "}"
    "btn.disabled=true;var oldText=btn.textContent;btn.textContent=T.sending;"
    "fetch(apiUrl,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)})"
    ".then(function(r){return r.json().then(function(j){return{status:r.status,body:j}}).catch(function(){return{status:r.status,body:{}}})})"
    ".then(function(res){"
    "btn.disabled=false;btn.textContent=oldText;"
    "if(res.body&&res.body.ok){"
    "msg.textContent=res.body.already?T.already:T.ok;"
    "msg.className='nl-msg ok';"
    "if(!res.body.already){form.reset()}"
    "return"
    "}"
    "var err=(res.body&&res.body.error)||'';"
    "if(err==='invalid_email')msg.textContent=T.invalid;"
    "else if(err==='consent_required')msg.textContent=T.consent;"
    "else if(err==='rate_limited')msg.textContent=T.rate;"
    "else msg.textContent=T.server;"
    "msg.className='nl-msg err'"
    "}).catch(function(){"
    "btn.disabled=false;btn.textContent=oldText;"
    "msg.textContent=T.network;msg.className='nl-msg err'"
    "})"
    "});"
    "})();"
    "</script>"
)


# ── HTML form (per-locale strings) ────────────────────────────────────────────
NEWSLETTER_FORM_EN = (
    "<p class='nl-label'>Get the daily briefing in your inbox</p>"
    "<p class='nl-sub'>One email per episode \u2014 Mon to Sat at 7&nbsp;AM CET. No tracking, no third parties.</p>"
    "<form class='newsletter' data-api='https://aequitus.net/api/subscribe.php' data-locale='en' novalidate>"
    "<div class='nl-row'>"
    "<input class='nl-email' type='email' name='email' placeholder='you@example.com' "
    "required maxlength='254' autocomplete='email' aria-label='Your email address'>"
    "<button class='nl-btn' type='submit'>Subscribe</button>"
    "</div>"
    "<input class='nl-honey' type='text' name='website' tabindex='-1' "
    "autocomplete='off' aria-hidden='true' placeholder='Leave this empty'>"
    "<label class='nl-consent'>"
    "<input type='checkbox' name='consent' required> "
    "I agree to receive the AI Press Review newsletter. I can unsubscribe at any time."
    "</label>"
    "<p class='nl-msg' role='status' aria-live='polite'></p>"
    "</form>"
    "<p class='nl-divider'>or pick your platform</p>"
)

NEWSLETTER_FORM_FR = (
    "<p class='nl-label'>Recevez le brief quotidien par email</p>"
    "<p class='nl-sub'>Un email par \u00e9pisode \u2014 du lundi au samedi, 7&nbsp;h CET. Sans tracking, sans tiers.</p>"
    "<form class='newsletter' data-api='https://aequitus.net/api/subscribe.php' data-locale='fr' novalidate>"
    "<div class='nl-row'>"
    "<input class='nl-email' type='email' name='email' placeholder='vous@exemple.com' "
    "required maxlength='254' autocomplete='email' aria-label='Votre adresse email'>"
    "<button class='nl-btn' type='submit'>S'abonner</button>"
    "</div>"
    "<input class='nl-honey' type='text' name='website' tabindex='-1' "
    "autocomplete='off' aria-hidden='true' placeholder='Laisser vide'>"
    "<label class='nl-consent'>"
    "<input type='checkbox' name='consent' required> "
    "J'accepte de recevoir la lettre d'information de la Revue de Presse&nbsp;IA. "
    "Je peux me d\u00e9sinscrire \u00e0 tout moment."
    "</label>"
    "<p class='nl-msg' role='status' aria-live='polite'></p>"
    "</form>"
    "<p class='nl-divider'>ou choisissez votre plateforme</p>"
)


# ── Anchors (must match exactly once per file) ────────────────────────────────
# The wrapper-open anchor: replace the existing <p class='subscribe-label'>...
# and the opening of the platform <div class='subscribe' id='subscribe'>.
# After the patch the id='subscribe' lives on the new wrapper, so the
# nav <a href='#subscribe'> still scrolls correctly.
EN_OPEN_OLD = (
    "<p class='subscribe-label'>Subscribe \u2014 choose your platform</p>"
    "<div class='subscribe' id='subscribe'>"
)
EN_OPEN_NEW = (
    "<div class='subscribe-block' id='subscribe'>"
    + NEWSLETTER_FORM_EN
    + "<div class='subscribe'>"
)

FR_OPEN_OLD = (
    "<p class='subscribe-label'>S'abonner \u2014 choisissez votre plateforme</p>"
    "<div class='subscribe' id='subscribe'>"
)
FR_OPEN_NEW = (
    "<div class='subscribe-block' id='subscribe'>"
    + NEWSLETTER_FORM_FR
    + "<div class='subscribe'>"
)

# Wrapper-close anchor: the platform <div> currently closes right before
# <a class='hiw-link'>. We add an extra </div> there to close .subscribe-block.
# (Same anchor for EN and FR — both use 'hiw-link'.)
CLOSE_OLD = "</a></div><a class='hiw-link'"
CLOSE_NEW = "</a></div></div><a class='hiw-link'"

STYLE_OLD = "</style>"
STYLE_NEW = NEWSLETTER_CSS + "</style>"

BODY_OLD = "</body>"
BODY_NEW = NEWSLETTER_JS + "</body>"


def _replace_once(
    text: str, old: str, new: str, *, label: str, path: Path,
    sentinel: str | None = None,
) -> str:
    """Replace `old` with `new`. Idempotent via `sentinel`: if a unique
    fragment of `new` is already in the file, skip. Otherwise refuse if
    `old` is not present or appears more than once — both are signs the
    template diverged and the patcher needs updating.

    The sentinel pattern is needed because anchors like '</style>' and
    '</body>' survive the patch (we INSERT before them, we don't remove
    them) — so a naive `new in text and old not in text` check would
    re-fire on every run. Pick a sentinel that ONLY appears in the
    injected payload (e.g. a unique CSS class or JS identifier).
    """
    if sentinel is not None and sentinel in text:
        print(f'  [skip] {label}: already patched')
        return text
    count = text.count(old)
    if count == 0:
        raise SystemExit(
            f'ERROR: {path.name}: anchor for {label!r} not found.\n'
            f'  Looked for: {old[:120]!r}...'
        )
    if count > 1:
        raise SystemExit(
            f'ERROR: {path.name}: anchor for {label!r} found {count} times '
            '(must be exactly 1). Refusing to patch — anchor is ambiguous.'
        )
    return text.replace(old, new, 1)


def patch_file(path: Path, *, locale: str) -> None:
    print(f'\n→ {path.relative_to(ROOT)}')
    text = path.read_text(encoding='utf-8')
    original = text

    # Sentinels are unique strings present ONLY after their respective patch.
    # `.subscribe-block{margin:` is in the CSS payload only.
    # `class='subscribe-block'` is the new wrapper class.
    # `apiUrl=form.dataset.api` is in the JS payload only.
    # The wrapper-close patch is idempotent on its own (CLOSE_NEW
    # contains '</div></div>' which CLOSE_OLD doesn't, so checking
    # for CLOSE_NEW works).

    # 1. CSS: inject before </style>
    text = _replace_once(
        text, STYLE_OLD, STYLE_NEW,
        label='CSS injection', path=path,
        sentinel='.subscribe-block{margin:',
    )

    # 2. HTML: wrap the .subscribe block, inject the form above the platforms
    if locale == 'en':
        text = _replace_once(
            text, EN_OPEN_OLD, EN_OPEN_NEW,
            label='form open + label', path=path,
            sentinel="class='subscribe-block'",
        )
    else:
        text = _replace_once(
            text, FR_OPEN_OLD, FR_OPEN_NEW,
            label='form open + label', path=path,
            sentinel="class='subscribe-block'",
        )

    # 3. HTML: close the .subscribe-block wrapper before <a class='hiw-link'>
    text = _replace_once(
        text, CLOSE_OLD, CLOSE_NEW,
        label='wrapper close', path=path,
        sentinel=CLOSE_NEW,
    )

    # 4. JS: inject before </body>
    text = _replace_once(
        text, BODY_OLD, BODY_NEW,
        label='JS injection', path=path,
        sentinel='apiUrl=form.dataset.api',
    )

    if text == original:
        print('  (no changes)')
        return

    path.write_text(text, encoding='utf-8')
    delta = len(text) - len(original)
    print(f'  patched (+{delta} chars)')


def main() -> int:
    targets = [
        (EN_TEMPLATE, 'en'),
        (EN_DOC,      'en'),
        (FR_TEMPLATE, 'fr'),
        (FR_DOC,      'fr'),
    ]
    missing = [p for p, _ in targets if not p.exists()]
    if missing:
        for p in missing:
            print(f'ERROR: missing file {p}', file=sys.stderr)
        return 1
    for path, locale in targets:
        patch_file(path, locale=locale)
    print('\nAll four files patched.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
