#!/usr/bin/env python3
"""One Word, First Thought: write the entry word to the output directory.

The first word that came to mind: petrichor -- the smell of rain on
dry earth. Surprising, vivid, and specific: one word that carries a
whole weather front in it.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
        word = f.read().strip()
    if not word or not (1 <= len(word) <= 24):
        print("entry must be 1-24 characters", file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in word):
        print("entry must be exactly one word", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    tmp_path = out_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(word)
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, out_path)
    print("wrote %s (%d chars)" % (out_path, len(word)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
