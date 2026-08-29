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

- `agent/` — agent instructions
- `scripts/` — repository validation scripts
- `.github/workflows/` — GitHub Actions checks
- `.env.example` — example environment-variable names only

## Local setup

Copy:

`.env.example` → `.env`

Then fill in the required values locally.

Do not upload `.env` to GitHub.
