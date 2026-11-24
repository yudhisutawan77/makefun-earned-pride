"""One Line of Earned Pride.

Writes a single line of text (1-240 characters) to /output/entry.txt
(or the path named by ENTRY_OUT / ENTRY_OUT_DIR when those are set):
a quiet, earned moment of pride for someone in a scene.

The line: after thirty years of shelving other people's books, a
librarian holds the first copy with her own name on the spine, and
runs her thumb across it twice. Long effort, one small gesture,
no trophy, no speech.
"""

import os
import sys

ENTRY_LINE = (
    "After thirty years of shelving other people's books, the librarian "
    "held the first copy with her name on the spine and ran her thumb "
    "across it twice."
)

MIN_CHARS = 1
MAX_CHARS = 240


def check_length(line):
    """The gate counts characters: 1 to 240, no more, no fewer."""
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(line)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )


def check_single_clean_line(line):
    """One line of plain text: not blank, no line breaks, no control chars."""
    if not line.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    for ch in line:
        if ord(ch) < 0x20 and ch not in ("\t",):
            raise ValueError(f"entry holds a control character {ch!r}")


def build_entry():
    """Validate the line against every part of the bounty gate."""
    check_length(ENTRY_LINE)
    check_single_clean_line(ENTRY_LINE)
    return ENTRY_LINE


def resolve_output_path():
    if os.environ.get("ENTRY_OUT"):
        return os.environ["ENTRY_OUT"]
    out_dir = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    text = build_entry()
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
