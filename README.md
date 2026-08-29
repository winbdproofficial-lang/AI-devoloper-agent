# winbd-agent-project

Project scaffold for the WinBD development agent.

## Structure

```
winbd-agent-project/
├── README.md                      # This file
├── .gitignore                     # Files/folders excluded from Git
├── .env.example                   # Placeholder environment variables (copy to .env)
├── agent/
│   ├── AGENTS.md                  # Rules and operating instructions for the agent
│   └── README.md                  # Agent-specific documentation
├── scripts/
│   └── check_secrets.py           # Pre-commit / CI secret-leak scanner
└── .github/
    └── workflows/
        └── validate.yml           # CI: lint + secret scan on push/PR
```

## Getting started

1. Copy the environment template and fill in real values locally:
   ```bash
   cp .env.example .env
   ```
2. **Never commit `.env`.** It is already listed in `.gitignore`.
3. Review `agent/AGENTS.md` before running any automated agent against this repo.

## Secret scanning

Before every commit, run:

```bash
python scripts/check_secrets.py
```

This also runs automatically in CI via `.github/workflows/validate.yml`.

## Environment variables

See `.env.example` for the full list of expected variables. No real credentials
are stored in this repository — all secrets must be supplied through your
deployment platform's environment/secret manager (e.g. GitHub Actions secrets,
Vercel/Render/Fly env vars, etc.).
