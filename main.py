#!/usr/bin/env python3
"""Write this competition's one-line entry to entry.txt.

The entry is a fixed plan of at most 280 characters. This script checks
the text, writes it straight to $MAKEFUN_OUTPUT_DIR/entry.txt with one
direct open() call, and then reads the file back to prove the bytes on
disk are exactly the entry text.
"""

import os
import sys

ENTRY_TEXT = "Day 1: $30 Apollo credits, 2,000 US plumbers with no website. Days 2-30: I build each a live one-page site and email it with a $149 Stripe link. 100 view it, 10 buy — no pitch, no call, no waiting. Day 30: $1,490."

MAX_CHARS = 280
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def fail(message):
    """Print an error and stop with a non-zero exit status."""
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def show_usage():
    print("usage: main.py [--check]", file=sys.stderr)
    print(
        "  Run with no arguments to write the entry to "
        "$MAKEFUN_OUTPUT_DIR/entry.txt.",
        file=sys.stderr,
    )
    print(
        "  Run with --check to print the entry and its length without "
        "writing any file.",
        file=sys.stderr,
    )
    raise SystemExit(2)


def validate(text):
    """Refuse text that is blank, too long, or not valid UTF-8."""
    if not text.strip():
        fail("entry text is blank")
    if len(text) > MAX_CHARS:
        fail(f"entry text has {len(text)} characters, over the {MAX_CHARS} limit")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        fail(f"entry text is not valid UTF-8: {exc}")


def entry_path():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return os.path.join(outdir, OUTPUT_NAME)


def write_entry(path):
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
        if not os.access(directory, os.W_OK):
            fail(f"output directory is not writable: {directory}")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


def verify_entry(path):
    wanted = ENTRY_TEXT.encode("utf-8")
    with open(path, "rb") as handle:
        found = handle.read()
    if found != wanted:
        position = next(
            (i for i, (a, b) in enumerate(zip(found, wanted)) if a != b),
            min(len(found), len(wanted)),
        )
        fail(
            f"read-back check failed: {path} differs from the entry text "
            f"at byte {position} "
            f"(file has {len(found)} bytes, entry has {len(wanted)})"
        )


def check_only():
    validate(ENTRY_TEXT)
    print(ENTRY_TEXT)
    print(f"characters: {len(ENTRY_TEXT)}")


def main(argv):
    if argv == ["--check"]:
        check_only()
        return 0
    if argv:
        show_usage()
    validate(ENTRY_TEXT)
    path = entry_path()
    write_entry(path)
    verify_entry(path)
    print(f"wrote {path} ({len(ENTRY_TEXT)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
