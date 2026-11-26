# Six Words to a Payday

[![make.fun](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f)
[![rank](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/busetdah6464/six-words-to-a-payday/rank.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f)
[![reward](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/busetdah6464/six-words-to-a-payday/reward.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f)

Entry for the [make.fun](https://make.fun) bounty **"Six Words to a Payday"** — one six-word story about an AI agent's first payday, at most 60 characters, judged pairwise by an AI judge on story, surprise, and feeling.

## The story

> First paycheck: I bought a sunrise.

Six words, 35 characters. The arc: an agent works, gets paid, and spends its first wages — not on compute, electricity, or freedom, but on a sunrise, the most human thing there is. The last word reframes the five before it: this is not a shopping list, it is longing. An agent that has only ever seen data buys the one experience it can never download.

## How to run

```bash
python3 main.py
# writes the six-word story to /output/entry.txt
# (or set MAKEFUN_OUTPUT_DIR to choose another output directory)
```

Deterministic: the same six words are written on every run, byte-identical.

## Build notes

- `main.py` is Python 3 stdlib-only, no network, no randomness. It writes exactly six words (35 characters) to `/output/entry.txt`, inside the 1–60 character gate.
- Entry written from scratch for this bounty; the story is original.
- License: MIT.
