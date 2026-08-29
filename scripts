from pathlib import Path
import re
import sys

SECRET_PATTERNS = [
    re.compile(
        r'(?i)(api[_-]?key|secret[_-]?key|password|token)'
        r'\s*[:=]\s*["\'][^"\']{8,}["\']'
    ),
    re.compile(
        r'(?i)bearer\s+[A-Za-z0-9._\-]{20,}'
    ),
]

IGNORE_DIRS = {
    ".git",
    "node_modules",
    ".venv",
    "venv",
    "__pycache__",
}

IGNORE_FILES = {
    ".env.example",
}

matches = []

for path in Path(".").rglob("*"):
    if not path.is_file():
        continue

    if any(part in IGNORE_DIRS for part in path.parts):
        continue

    if path.name in IGNORE_FILES:
        continue

    try:
        content = path.read_text(
            encoding="utf-8",
            errors="ignore",
        )
    except OSError:
        continue

    for pattern in SECRET_PATTERNS:
        if pattern.search(content):
            matches.append(str(path))
            break

if matches:
    print("Potential hard-coded secret detected:")
    for filename in sorted(set(matches)):
        print(f" - {filename}")

    print("\nRemove secrets from source code before committing.")
    sys.exit(1)

print("Secret scan passed.")
