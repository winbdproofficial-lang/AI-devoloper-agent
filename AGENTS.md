# AGENTS.md

Operating rules for any automated development agent (human or AI) working on
this repository.

## Scope

- This agent may inspect, edit, and fix code inside this repository only.
- No access to unrelated repositories, personal accounts, or external systems
  outside this project's declared stack.

## Secrets

- Never print, log, commit, or hard-code secrets (API keys, DB passwords,
  JWT secrets, service-role keys, tokens).
- Secrets are read only from environment variables at runtime.
- `.env` must never be committed. `.env.example` must be kept up to date with
  placeholder variable **names** only — never real values.
- Before finishing any task, run `scripts/check_secrets.py` and review
  `git diff` to confirm no credential was introduced.

## Code changes

1. Inspect the existing structure and architecture before changing anything.
2. Identify the root cause of a bug before patching symptoms.
3. Make the smallest reliable fix — avoid unrelated rewrites.
4. Preserve existing functionality unless the task explicitly requires
   changing it.
5. Run available tests/build/lint after any non-trivial change.
6. Use proper database migrations for schema changes — never edit production
   data directly, never delete data to "make something work."

## API integrations

- Inspect existing API/service architecture first.
- Private credentials belong on the backend/server only — never in frontend
  code or client bundles.
- Add input validation and handle timeout/auth/error responses explicitly.
- Update `.env.example` and the README when new configuration is introduced.

## Reporting

At the end of a task, report:
- Which files were changed and why.
- Any configuration, secret, or permission that is missing and required
  (never invent a placeholder value and treat it as real).
- Any known remaining issue.
