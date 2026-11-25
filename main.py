#!/usr/bin/env python3
"""One-Line Office Jokes - writes one office joke to /output/entry.txt.

The joke is a single line about a meeting that runs long: it was booked
for thirty minutes, ran for ninety, and ends by booking a follow-up
meeting to decide what the first meeting decided. The laugh lands on
the last few words, and every detail is a real office moment.
"""

import os
import sys

JOKE = (
    "The meeting was scheduled for thirty minutes, ran for ninety, and "
    "ended with a follow-up meeting to decide what the first one decided."
)


def validate(text: str) -> str:
    """Return the entry text, or exit 1 if it breaks the gate rules."""
    if not 1 <= len(text) <= 199:
        print(f"entry is {len(text)} chars, must be 1-199", file=sys.stderr)
        sys.exit(1)
    if text.strip() != text:
        print("entry must not start or end with whitespace", file=sys.stderr)
        sys.exit(1)
    if "\n" in text or "\r" in text:
        print("entry must be one line", file=sys.stderr)
        sys.exit(1)
    return text


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    entry = validate(JOKE)
    with open(out, "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"wrote {len(entry)} chars to {out}: {entry}")


if __name__ == "__main__":
    main()
