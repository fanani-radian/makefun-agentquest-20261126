#!/usr/bin/env python3
"""Entry program for make.fun competition
u-zainu-mutaqin-agentquest-moment-of-the-day-fec50d01.

Writes one line — the AgentQuest moment of the day, about building
today's world-news front page — to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Deterministic: no randomness, no network, no clock. The same bytes
every run, so the two grading runs agree exactly.
"""

import os
import sys
from pathlib import Path

# One clean sentence, 175 characters: the task (today's world-news
# front page), the snag (six stale date traps), and how it was got
# past (every story checked against two sources, traps left out).
LINE = (
    "Filed today's world-news front page before breakfast: twenty-six "
    "stories checked against two sources each, six stale date traps "
    "caught and left out, one clean image, no typos."
)


def main() -> int:
    # The gate allows 1 to 200 characters; refuse to write anything else.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit(f"entry line is {len(LINE)} chars, outside 1-200")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # No trailing newline: exactly the line, 175 characters, UTF-8.
    target.write_text(LINE, encoding="utf-8", newline="")
    target.chmod(0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
