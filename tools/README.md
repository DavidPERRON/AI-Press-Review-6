# Local automation — `run-podcast.command`

A double-clickable macOS script that sets up and runs the AI Press Review
pipeline locally on your Mac, with a menu-driven interface.

## What you get

- **First run**: installs Homebrew packages (Python 3.11, ffmpeg), clones
  the repo to `~/github/AI-Press-Review-5/`, creates a Python venv, installs
  Python deps + Playwright Chromium, and copies `.env.example` to `.env`
  for you to fill in.
- **Subsequent runs**: skips already-installed dependencies (fingerprinted
  via `requirements.txt` SHA), opens straight to the menu.

## Menu options

| # | Mode | LLM | TTS | R2 upload | Auto-commit | Cost |
|---|------|-----|-----|-----------|-------------|------|
| 1 | Dry run EN | ✓ | ✗ | ✗ | ✗ | LLM tokens only |
| 2 | Dry run FR | ✓ | ✗ | ✗ | ✗ | LLM tokens only |
| 3 | Preview EN | ✓ | ✓ | ✗ | ✗ | LLM + Cartesia |
| 4 | Preview FR | ✓ | ✓ | ✗ | ✗ | LLM + Cartesia |
| 5 | Full prod EN | ✓ | ✓ | ✓ | manual | full pipeline |
| 6 | Full prod FR | ✓ | ✓ | ✓ | manual | full pipeline |
| 7 | Test suite | — | — | — | — | free |
| 8 | git pull | — | — | — | — | free |
| 9 | Edit `.env` | — | — | — | — | free |

Even "full prod" mode does NOT auto-commit — you review with `git status` /
`git diff` then commit + push when you're satisfied.

## Install / first use

1. Download this file (`tools/run-podcast.command`) to
   `/Users/davidperron/github/run-podcast.command`.

   From the GitHub UI: open `tools/run-podcast.command`, click "Raw", then
   `Cmd+S` to save as `~/github/run-podcast.command`.

   Or via Terminal:
   ```bash
   mkdir -p ~/github
   curl -L https://raw.githubusercontent.com/DavidPERRON/AI-Press-Review-5/main/tools/run-podcast.command \
     -o ~/github/run-podcast.command
   chmod +x ~/github/run-podcast.command
   ```

2. Double-click `run-podcast.command` from Finder. macOS Terminal opens.

3. The first run will:
   - Ask for your password to install Homebrew packages (sudo).
   - Clone the repo into `~/github/AI-Press-Review-5/`.
   - Install Python deps (one-time, ~2 min).
   - Open `.env` in TextEdit so you can paste your API keys.

4. Subsequent runs are instant: double-click → menu → choose option.

## Logs

Every pipeline run is timestamped and saved to `~/github/podcast-logs/`. If
something fails you can scroll the log file later instead of relying on
Terminal scrollback.

## Cost reality check

- **GitHub Actions**: free for public repos. Running locally saves nothing
  on this front for you currently.
- **LLM (OpenRouter)**: ~$0.07 per EN run (Claude Sonnet 4.5), ~$0.05 per FR
  run (Mistral Large 2411). Bills per token, regardless of where called from.
- **Cartesia TTS**: ~$0.18 per ~12k character episode. Bills per character.
- **R2**: storage is essentially free (first 10 GB free), egress only counts
  when listeners stream the MP3.
- **For truly $0 dry runs**: install Ollama (`brew install ollama && ollama
  pull qwen2.5:32b`), uncomment `LOCAL_LLM_BASE_URL` in `.env`. Quality is
  ~70% of Mistral Large but free.

## When to use this vs GitHub Actions

| You want to... | Use |
|----------------|-----|
| Publish today's episode automatically at 7am | GitHub Actions (cron) |
| Debug a failed run | Local (option 1 or 2 — instant feedback) |
| Test a prompt change | Local dry run (option 1 or 2) |
| Compare two LLM models side by side | Local — change `.env`, re-run |
| Generate a one-off bonus episode on Sunday | Local full prod (option 5/6) |
| Run an episode while traveling without your laptop | GitHub Actions manual dispatch |

## Troubleshooting

- **"command not found: brew"** → install from https://brew.sh
- **"permission denied"** when double-clicking → `chmod +x ~/github/run-podcast.command`
- **macOS "unidentified developer" warning** → right-click the file in
  Finder → "Open", then click "Open" in the dialog. Only needed once.
- **Pipeline crashes mid-run** → check the log in `~/github/podcast-logs/`,
  the full LLM/TTS API responses are captured there.
