#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, at most 200 characters.

A robot vacuum explains, in its own deadpan voice, why it missed a spot:
sensor log, brush abdication, punch at the end. Writes the line to
<OUTPUT_DIR>/entry.txt (default /output). Standard library only.
"""

import os

# Revised line: the brush now abdicates the job itself ("declined the job"
# is shorter and funnier than "reviewed the evidence"), so the deadpan
# blame-shuffle builds to the punch at the very end.
LINE = (
    "I did not miss the spot. My sensors logged it at 03:12, "
    "my brush declined the job, and the dust has filed "
    "for squatter's rights."
)


def main() -> None:
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
