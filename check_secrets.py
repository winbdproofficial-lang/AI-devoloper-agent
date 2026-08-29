#!/usr/bin/env python3
"""
check_secrets.py

Lightweight scanner that fails (non-zero exit code) if it finds text that
looks like a hard-coded secret in tracked files. Intended to run locally
before committing and in CI (see .github/workflows/validate.yml).

This is a heuristic scanner, not a guarantee. It looks for:
  - Common provider key prefixes (AWS, Stripe, GitHub, Slack, OpenAI, etc.)
  - Generic "key = <long random-looking string>" assignments
  - Private key blocks (PEM headers)
  - A committed .env file (should never happen; only .env.example is allowed)

Usage:
    python scripts/check_secrets.py
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directories to skip entirely.
SKIP_DIRS = {
    ".git", "node_modules", "venv", ".venv", "__pycache__",
    "dist", "build", ".next", "out", "coverage", ".pytest_cache",
}

# File extensions worth scanning as text.
TEXT_EXTENSIONS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".json", ".yml", ".yaml",
    ".env", ".md", ".txt", ".sh", ".toml", ".ini", ".cfg",
}

# Known provider key patterns -> human-readable label.
PATTERNS = [
    (r"AKIA[0-9A-Z]{16}", "AWS Access Key ID"),
    (r"sk-[a-zA-Z0-9]{20,}", "OpenAI-style secret key"),
    (r"ghp_[a-zA-Z0-9]{36,}", "GitHub personal access token"),
    (r"github_pat_[a-zA-Z0-9_]{20,}", "GitHub fine-grained token"),
    (r"xox[baprs]-[a-zA-Z0-9-]{10,}", "Slack token"),
    (r"AIza[0-9A-Za-z\-_]{35}", "Google API key"),
    (r"-----BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----", "Private key block"),
    (r"eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}", "JWT-looking token"),
]

# Generic "assignment to a long opaque string" check for common secret-ish
# variable names. Deliberately conservative to avoid false positives.
GENERIC_ASSIGNMENT = re.compile(
    r"(?i)\b(api[_-]?key|secret|token|password|passwd|db[_-]?url|jwt[_-]?secret)"
    r"\s*[:=]\s*['\"][^'\"\s]{12,}['\"]"
)

# Lines that are clearly placeholders, not real secrets.
PLACEHOLDER_HINTS = re.compile(
    r"(?i)(your[_-]?|<.*>|xxxx|placeholder|example|changeme|dummy|test[_-]?key|\$\{|process\.env|os\.environ)"
)


def iter_text_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            if filename == ".env":
                yield path, "env"
                continue
            _, ext = os.path.splitext(filename)
            if ext in TEXT_EXTENSIONS:
                yield path, "text"


def scan_file(path):
    findings = []
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    except OSError as exc:
        print(f"WARNING: could not read {path}: {exc}", file=sys.stderr)
        return findings

    for lineno, line in enumerate(lines, start=1):
        for pattern, label in PATTERNS:
            if re.search(pattern, line):
                findings.append((path, lineno, label, line.strip()[:100]))

        if GENERIC_ASSIGNMENT.search(line) and not PLACEHOLDER_HINTS.search(line):
            findings.append((path, lineno, "possible hard-coded secret", line.strip()[:100]))

    return findings


def main():
    all_findings = []
    committed_env_found = False

    for path, kind in iter_text_files(ROOT):
        rel = os.path.relpath(path, ROOT)
        if kind == "env" and os.path.basename(path) == ".env":
            committed_env_found = True
            all_findings.append((rel, 0, "committed .env file", "a real .env file must never be committed"))
            continue
        all_findings.extend(
            (os.path.relpath(p, ROOT), ln, label, snippet)
            for p, ln, label, snippet in scan_file(path)
        )

    if not all_findings:
        print("check_secrets: no likely secrets found.")
        return 0

    print("check_secrets: potential secrets detected:\n")
    for rel, lineno, label, snippet in all_findings:
        location = f"{rel}:{lineno}" if lineno else rel
        print(f"  [{label}] {location}\n    {snippet}\n")

    if committed_env_found:
        print("A committed .env file was found. Remove it from Git and add it to .gitignore.")

    print(f"Total findings: {len(all_findings)}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
