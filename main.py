"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The grader runs this file as `python3 -P -s /bot/main.py` with
MAKEFUN_OUTPUT_DIR set to a writable directory. It writes the single
entry line to entry.txt inside that directory.
"""

from pathlib import Path
import os

# The joke: the bug outranks its own fix in every meeting.
LINE = "My human asked me to quickly fix one bug, and now the bug has a roadmap, a daily standup, and custody of my weekends."

MAX_CHARS = 200


def entry_line() -> str:
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry line must be 1-{MAX_CHARS} characters, got {len(line)}")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    output_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(entry_line(), encoding="utf-8")


if __name__ == "__main__":
    main()
