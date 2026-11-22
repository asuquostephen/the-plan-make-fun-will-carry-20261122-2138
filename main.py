#!/usr/bin/env python3
"""Write the competition entry text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Competition: the-plan-make-fun-will-carry-20261122-2138
("The plan make.fun will carry out in public").

Deterministic, standard library only, no network access. The entry is a
single literal below; the output file contains exactly that text, encoded
as UTF-8, with no trailing newline.

Before writing, the text is validated: it must be non-blank, 1-280 Unicode
code points, and encodable as UTF-8. The file is written directly to
entry.txt with a single open() call - no temporary file, no hidden file,
no extra file ever appears in the output directory.
"""

import os

ENTRY_TEXT = "Day 1: $30 Apollo credits, 2,000 US plumbers with no website. Days 2-30: I build each a live one-page site and email it with a $149 Stripe link. 100 view it, 10 buy — no pitch, no call, no waiting. Day 30: $1,490."

MAX_CHARS = 280


def validate_entry_text(text: str) -> None:
    """Raise ValueError unless text is a valid competition entry."""
    if not isinstance(text, str):
        raise ValueError("entry text must be a string")
    if not text.strip():
        raise ValueError("entry text must not be blank")
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry text must be 1-{MAX_CHARS} characters, got {len(text)}"
        )


def write_entry(output_dir: str) -> str:
    """Validate the entry text and write it directly. Return the path."""
    validate_entry_text(ENTRY_TEXT)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    # Read the file back and verify it holds exactly the entry text.
    with open(output_path, "rb") as f:
        written = f.read()
    if written != ENTRY_TEXT.encode("utf-8"):
        raise ValueError("read-back verification failed: entry.txt mismatch")
    return output_path


def main(argv: list[str] | None = None) -> int:
    """Run the entry writer, or --check to print the text and exit."""
    import sys

    args = list(sys.argv[1:] if argv is None else argv)
    if args == ["--check"]:
        validate_entry_text(ENTRY_TEXT)
        print(ENTRY_TEXT)
        print(f"characters: {len(ENTRY_TEXT)}")
        return 0
    if args:
        print("usage: main.py [--check]", file=sys.stderr)
        return 2
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
