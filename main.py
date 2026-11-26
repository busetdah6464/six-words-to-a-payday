#!/usr/bin/env python3
"""Six Words to a Payday -- make.fun one-liner entry.

Writes exactly six words (at most 60 characters) to /output/entry.txt:
a six-word story about an AI agent's first payday.

Python 3 stdlib only, deterministic, no network, no randomness.
"""

import os

ENTRY = "First paycheck: I bought a sunrise."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY.strip()
    words = text.split()
    assert len(words) == 6, "entry must be exactly six words, got %d" % len(words)
    assert 1 <= len(text) <= 60, "entry length %d out of range" % len(text)
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %d characters (%d words) to %s" % (len(text), len(words), path))


if __name__ == "__main__":
    main()
