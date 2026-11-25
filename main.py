#!/usr/bin/env python3
"""The Long Roast — one-line roast of my own AI agent.

Writes a single original roast line to /output/entry.txt.
"""

import os

# Gate limits from the competition brief: one line, 1-200 characters.
MAX_CHARS = 200
MIN_CHARS = 1
OUTPUT_PATH = "/output/entry.txt"

LINE = "Rika splits herself into five subagents to write one joke, then asks which one is the real her \u2014 my assistant outsources herself to herself."

assert MIN_CHARS <= len(LINE) <= MAX_CHARS, f"line must be 1-200 chars, got {len(LINE)}"
assert "\n" not in LINE, "roast must be a single line"


def verify_output() -> None:
    """Read-back check: entry.txt must hold exactly LINE, nothing else."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the roast line exactly"
    assert MIN_CHARS <= len(written) <= MAX_CHARS, "entry.txt length out of gate"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    verify_output()


if __name__ == "__main__":
    main()
