# AI Coding Agent Rules

## 1. Repository scope

Work only on files inside the authorized repository.

Do not access unrelated computers, accounts, repositories, databases, or services.

## 2. Secrets

Never:

- print secrets
- commit secrets
- hard-code API keys
- hard-code passwords
- expose authentication tokens
- place private keys in source code

Use environment variables instead.

## 3. Existing code

Before making major changes:

1. Inspect the repository structure.
2. Identify the frontend and backend.
3. Identify the database configuration.
4. Identify deployment configuration.
5. Identify existing API integrations.
6. Identify available tests.

Do not replace working systems unnecessarily.

## 4. Changes

Keep changes:

- minimal
- understandable
- reversible
- compatible with the existing architecture

Do not delete important functionality without authorization.

## 5. Security

Do not disable:

- authentication
- authorization
- database security
- rate limiting
- input validation
- HTTPS/security protections

just to make an error disappear.

## 6. API integrations

Credentials must come from environment variables.

Example:

```js
const apiKey = process.env.API_KEY;
```

Never place private API keys, provider tokens, database passwords, JWT
secrets, or service-role keys in frontend/browser code. Private credentials
are used from the backend/server only.

## 7. Testing and validation

Before finishing a task:

1. Run the secret scanner: `python scripts/check_secrets.py`.
2. Run any available project tests or build steps.
3. Run `git diff` and confirm no secret or credential was added.

## 8. Reporting

At the end of every task, report:

- Which files were changed and why.
- Any configuration, credential, or permission that is missing (never invent
  a value to fill the gap — state clearly what is required).
- Any remaining known issue.
