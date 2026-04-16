#!/usr/bin/env bash
# ──────────────────────────────────────────────────────────────────────────────
#  AI Press Review — Local automation for macOS
#
#  Double-click from Finder OR run `./run-podcast.command` from Terminal.
#
#  What this script does, in order:
#    1. Verifies / installs Homebrew, Python 3.11, ffmpeg.
#    2. Clones (or updates) the repo at $REPO_DIR.
#    3. Creates a Python venv inside the repo and installs Python deps.
#    4. Prompts you to fill in .env on first run; from then on, just runs.
#    5. Shows a menu so you can pick:
#         - Dry run (LLM only — no TTS, no upload)
#         - Local preview (LLM + TTS — no upload, no commit)
#         - Full prod-style (LLM + TTS + R2 upload + git commit)
#         - Test suite only
#         - Update repo (git pull)
#         - Edit .env
#
#  Designed to live at: /Users/davidperron/github/run-podcast.command
#  Works on the repo:    /Users/davidperron/github/AI-Press-Review-5
#
#  Cost note: dry runs and previews still hit the LLM API (paid). Only the
#  --skip-audio dry run skips Cartesia. Use Ollama via LOCAL_LLM_BASE_URL in
#  .env to make dry runs truly free.
# ──────────────────────────────────────────────────────────────────────────────

set -euo pipefail

# ── Config ────────────────────────────────────────────────────────────────────
REPO_URL="https://github.com/DavidPERRON/AI-Press-Review-5.git"
REPO_DIR="${HOME}/github/AI-Press-Review-5"
VENV_DIR="${REPO_DIR}/.venv-local"
LOG_DIR="${HOME}/github/podcast-logs"
PYTHON_BIN="python3.11"   # Falls back to python3 if 3.11 not available.

# ── Pretty output ─────────────────────────────────────────────────────────────
RED='\033[0;31m'; GRN='\033[0;32m'; YLW='\033[0;33m'; BLU='\033[0;34m'; NC='\033[0m'
say()  { printf "%b\n" "$1"; }
info() { say "${BLU}[i]${NC} $1"; }
ok()   { say "${GRN}[✓]${NC} $1"; }
warn() { say "${YLW}[!]${NC} $1"; }
err()  { say "${RED}[✗]${NC} $1"; }

# ── Pause-on-exit so double-clicked window stays visible ─────────────────────
pause_on_exit() {
  local rc=$?
  echo
  if [[ $rc -ne 0 ]]; then err "Script exited with status $rc"; fi
  read -r -p "Press Return to close this window..." _ || true
}
trap pause_on_exit EXIT

# ── Step 1: Homebrew + system deps ───────────────────────────────────────────
ensure_brew_pkg() {
  local pkg="$1"
  if ! brew list --formula "$pkg" >/dev/null 2>&1; then
    info "Installing $pkg via Homebrew..."
    brew install "$pkg"
  fi
}

ensure_system_deps() {
  if ! command -v brew >/dev/null 2>&1; then
    err "Homebrew is not installed. Install it first: https://brew.sh"
    exit 1
  fi
  ok "Homebrew present."

  ensure_brew_pkg ffmpeg
  ok "ffmpeg ready."

  # Prefer python@3.11 because the GitHub Actions pipeline uses 3.11. Other
  # versions usually work but may surface package ABI quirks (esp. websockets).
  if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
    if brew list --formula python@3.11 >/dev/null 2>&1; then
      PYTHON_BIN="$(brew --prefix python@3.11)/bin/python3.11"
    elif command -v python3 >/dev/null 2>&1; then
      warn "python@3.11 not found, falling back to: $(command -v python3)"
      PYTHON_BIN="$(command -v python3)"
    else
      info "Installing python@3.11 via Homebrew..."
      brew install python@3.11
      PYTHON_BIN="$(brew --prefix python@3.11)/bin/python3.11"
    fi
  fi
  ok "Python: $($PYTHON_BIN --version) at $PYTHON_BIN"
}

# ── Step 2: Repo clone or update ─────────────────────────────────────────────
ensure_repo() {
  if [[ ! -d "$REPO_DIR/.git" ]]; then
    info "Cloning repo into $REPO_DIR ..."
    mkdir -p "$(dirname "$REPO_DIR")"
    git clone "$REPO_URL" "$REPO_DIR"
    ok "Repo cloned."
  else
    ok "Repo present at $REPO_DIR"
  fi
}

update_repo() {
  info "Pulling latest from origin/main..."
  cd "$REPO_DIR"
  git fetch origin
  git pull --ff-only origin main || warn "Could not fast-forward; you may have local changes."
  ok "Repo updated."
}

# ── Step 3: Python venv + deps ───────────────────────────────────────────────
ensure_venv() {
  if [[ ! -d "$VENV_DIR" ]]; then
    info "Creating Python venv at $VENV_DIR..."
    "$PYTHON_BIN" -m venv "$VENV_DIR"
  fi
  # shellcheck disable=SC1091
  source "$VENV_DIR/bin/activate"
  ok "Venv active: $(which python)"
}

ensure_python_deps() {
  cd "$REPO_DIR"
  # Quick fingerprint check: only re-install deps if requirements.txt changed.
  local req_hash_file="$VENV_DIR/.requirements.sha"
  local current_hash
  current_hash="$(shasum -a 256 requirements.txt | awk '{print $1}')"
  local stored_hash=""
  [[ -f "$req_hash_file" ]] && stored_hash="$(cat "$req_hash_file")"

  if [[ "$current_hash" != "$stored_hash" ]]; then
    info "Installing/updating Python dependencies (this can take a minute)..."
    pip install --upgrade pip >/dev/null
    pip install -r requirements.txt
    pip install -e .
    info "Installing Playwright Chromium browser..."
    python -m playwright install chromium
    echo "$current_hash" > "$req_hash_file"
    ok "Dependencies installed."
  else
    ok "Dependencies already up to date."
  fi
}

# ── Step 4: .env bootstrap ───────────────────────────────────────────────────
ensure_env_file() {
  local env_file="$REPO_DIR/.env"
  local example_file="$REPO_DIR/.env.example"
  if [[ -f "$env_file" ]]; then
    ok ".env file present."
    return
  fi
  if [[ ! -f "$example_file" ]]; then
    err "No .env and no .env.example template found — repo is incomplete."
    exit 1
  fi
  warn "No .env file yet. Copying .env.example → .env"
  cp "$example_file" "$env_file"
  warn "You MUST edit $env_file before running the pipeline."
  warn "Required keys: LLM_API_KEY, CARTESIA_API_KEY, R2_*, NEWSAPI_API_KEY"
  read -r -p "Open .env in TextEdit now? [Y/n] " resp
  if [[ "${resp:-Y}" =~ ^[Yy]$ ]]; then
    open -e "$env_file"
    info "Save and close TextEdit, then come back here and press Return."
    read -r _ || true
  fi
}

# ── Step 5: Pipeline runs ────────────────────────────────────────────────────
mkdir_p_logs() {
  mkdir -p "$LOG_DIR"
}

ts() { date +"%Y-%m-%d_%H-%M-%S"; }

run_dry() {
  local locale="$1"
  local log_file="$LOG_DIR/dry_${locale}_$(ts).log"
  info "Dry run ($locale) — LLM only, no audio, no upload"
  info "Logging to $log_file"
  cd "$REPO_DIR"
  APR_LOCALE="$locale" python scripts/preview_local.py --skip-audio --date today \
    2>&1 | tee "$log_file"
}

run_preview() {
  local locale="$1"
  local log_file="$LOG_DIR/preview_${locale}_$(ts).log"
  warn "Local preview ($locale) — LLM + TTS, no upload, no commit"
  warn "This WILL hit Cartesia (paid per character) and your LLM (paid per token)."
  read -r -p "Continue? [y/N] " resp
  [[ "${resp:-N}" =~ ^[Yy]$ ]] || { info "Cancelled."; return; }
  info "Logging to $log_file"
  cd "$REPO_DIR"
  APR_LOCALE="$locale" python scripts/preview_local.py --date today \
    2>&1 | tee "$log_file"
  ok "Output MP3 should be in $REPO_DIR/output/"
}

run_full_prod() {
  local locale="$1"
  local log_file="$LOG_DIR/prod_${locale}_$(ts).log"
  warn "FULL PROD-STYLE RUN ($locale)"
  warn "  - LLM API call (paid)"
  warn "  - Cartesia TTS (paid per character)"
  warn "  - R2 upload (counts against egress quota)"
  warn "  - Modifies docs/, data/state/, data/sources/"
  warn "  - Does NOT auto-commit or push (you commit manually after review)"
  read -r -p "Are you sure? [y/N] " resp
  [[ "${resp:-N}" =~ ^[Yy]$ ]] || { info "Cancelled."; return; }
  info "Logging to $log_file"
  cd "$REPO_DIR"
  APR_LOCALE="$locale" python scripts/generate_draft.py --date "$(date +%F)" --profile daily \
    2>&1 | tee "$log_file"
  echo
  ok "Done. Review the changes with:"
  echo "    cd $REPO_DIR && git status && git diff"
  ok "Then commit + push when satisfied:"
  echo "    git add -f data/state/ data/sources/ docs/ && git commit -m '...' && git push"
}

run_tests() {
  cd "$REPO_DIR"
  info "Running test suite..."
  PYTHONPATH=src python -m pytest tests/ -v --tb=short
}

edit_env() {
  open -e "$REPO_DIR/.env"
  info "Edit, save, close TextEdit, then come back here."
  read -r -p "Press Return when done..." _ || true
}

# ── Menu loop ─────────────────────────────────────────────────────────────────
show_menu() {
  echo
  say "${BLU}╔══════════════════════════════════════════════════════════╗${NC}"
  say "${BLU}║         AI Press Review — Local Pipeline                 ║${NC}"
  say "${BLU}╚══════════════════════════════════════════════════════════╝${NC}"
  echo "  1) Dry run EN     (LLM only, no audio, no upload)"
  echo "  2) Dry run FR     (LLM only, no audio, no upload)"
  echo "  3) Preview EN     (LLM + TTS, no upload — costs Cartesia $)"
  echo "  4) Preview FR     (LLM + TTS, no upload — costs Cartesia $)"
  echo "  5) FULL PROD EN   (LLM + TTS + R2, no auto-commit)"
  echo "  6) FULL PROD FR   (LLM + TTS + R2, no auto-commit)"
  echo "  7) Run test suite"
  echo "  8) Update repo (git pull)"
  echo "  9) Edit .env"
  echo "  q) Quit"
  echo
  read -r -p "Choice: " choice
  case "$choice" in
    1) run_dry en ;;
    2) run_dry fr ;;
    3) run_preview en ;;
    4) run_preview fr ;;
    5) run_full_prod en ;;
    6) run_full_prod fr ;;
    7) run_tests ;;
    8) update_repo ;;
    9) edit_env ;;
    q|Q) info "Bye."; exit 0 ;;
    *) warn "Unknown choice: $choice" ;;
  esac
}

# ── Main ─────────────────────────────────────────────────────────────────────
main() {
  echo
  say "${BLU}=== AI Press Review — Local Setup & Run ===${NC}"
  echo

  ensure_system_deps
  ensure_repo
  ensure_venv
  ensure_python_deps
  ensure_env_file
  mkdir_p_logs

  echo
  ok "Setup complete. Logs will be saved to: $LOG_DIR"

  while true; do
    show_menu
    echo
    read -r -p "Run another action? [y/N] " again
    [[ "${again:-N}" =~ ^[Yy]$ ]] || break
  done
}

main "$@"
