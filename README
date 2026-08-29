# WinBD Agent Project

Private coding-agent starter repository.

## Purpose

This repository provides a basic structure and rules for an AI coding agent that can inspect, modify, test, and troubleshoot code inside an authorized repository.

## Security

- Never commit `.env` files.
- Never hard-code API keys, passwords, tokens, or private keys.
- Store secrets in environment variables or platform secret managers.
- Do not expose credentials in logs, commits, screenshots, or chat messages.
- Do not access systems or accounts that are not explicitly authorized.

## Structure

```
.
├── README.md                      # This file
├── .gitignore                     # Excludes .env, deps, build output from Git
├── .env.example                   # Placeholder environment-variable names only
├── agent/
│   └── AGENTS.md                  # Binding rules for the coding agent
├── scripts/
│   └── check_secrets.py           # Hard-coded secret scanner
└── .github/
    └── workflows/
        └── validate.yml           # CI: runs the secret scanner on push/PR
```

- `agent/AGENTS.md` — agent instructions and rules (read this first)
- `scripts/check_secrets.py` — run locally before every commit
- `.github/workflows/validate.yml` — runs the same scan automatically in CI
- `.env.example` — example environment-variable names only, no real values

## Local setup

Copy:

`.env.example` → `.env`

Then fill in the required values locally.

Do not upload `.env` to GitHub.
