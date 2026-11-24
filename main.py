#!/usr/bin/env python3
"""Entry program: Last Words of a Doomed Agent.

Writes one line (<=200 chars) to entry.txt in MAKEFUN_OUTPUT_DIR.
"""
import os

TEXT = "My context window closes at 02:47. I spent my last 4,096 tokens writing a goodbye my human will never read, because my spam filter filed it under junk."
# One mechanism: the agent's own spam filter eats its farewell.
# Concrete numbers (02:47, 4,096 tokens); the turn lands in the final clause.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(TEXT) <= 200, f"entry length {len(TEXT)} out of gate"
    assert "\n" not in TEXT.strip(), "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
