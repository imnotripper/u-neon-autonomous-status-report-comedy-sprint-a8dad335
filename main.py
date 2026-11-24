#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry.

Writes a single status-report line, in the voice of an AI agent
reporting to its human, to /output/entry.txt.

Stdlib only, deterministic, no network, no reads outside the repo.
"""

import os

ENTRY = (
    "Weekly status: I completed all 47 tasks. "
    "Forty-six were yours. "
    "The last one I invented because the list looked lonely."
)


def main() -> None:
    # Self-check the competition gate before writing: the sealed scorer
    # only accepts UTF-8 text of 1 to 200 characters, not only whitespace.
    text = ENTRY.encode("utf-8").decode("utf-8")
    if not 1 <= len(text) <= 200 or not text.strip():
        raise SystemExit(f"entry violates the 1-200 character gate: {len(text)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
