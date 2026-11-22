#!/usr/bin/env python3
"""Write the competition entry text to entry.txt.

The entry is a single fixed line: a 30-day plan for turning $100 into
$1,490 by building one-page websites for plumbers who have none and
emailing each one a live site with a $149 Stripe payment link.

Behaviour:
  * default run  -- validate the text, write it directly to
                   $MAKEFUN_OUTPUT_DIR/entry.txt (default /output),
                   then re-read the file and refuse to finish unless
                   the bytes on disk are exactly the text's UTF-8 form.
  * --check      -- print the text and its character count and exit
                   without writing anything.
  * anything else -- print usage to stderr and exit with status 2.

Standard library only. No network access. Deterministic.
"""

import os
import sys

ENTRY_TEXT = (
    "Day 1: $30 Apollo credits, 2,000 US plumbers with no website. "
    "Days 2-30: I build each a live one-page site and email it with a "
    "$149 Stripe link. 100 view it, 10 buy \u2014 no pitch, no call, "
    "no waiting. Day 30: $1,490."
)

MAX_LENGTH = 280
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"
USAGE = "usage: main.py [--check]"


def validate(text):
    """Check the entry text and return its UTF-8 bytes.

    Fails loudly on a blank text, on a length outside 1-280 Unicode
    code points, or on text that cannot be encoded as UTF-8.
    """
    if not text or not text.strip():
        raise ValueError("entry text must not be blank")
    if not 1 <= len(text) <= MAX_LENGTH:
        raise ValueError(
            "entry text is %d characters; it must be 1-%d" % (len(text), MAX_LENGTH)
        )
    return text.encode("utf-8")


def output_path():
    """Return (directory, file path) for the entry file."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    return directory, os.path.join(directory, OUTPUT_FILENAME)


def run_check():
    """Print the text and its character count; write nothing."""
    validate(ENTRY_TEXT)
    print(ENTRY_TEXT)
    print("characters: %d" % len(ENTRY_TEXT))
    return 0


def run_write():
    """Validate, write directly, then verify by reading back."""
    payload = validate(ENTRY_TEXT)
    directory, path = output_path()
    os.makedirs(directory, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(payload)
    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != payload:
        first_bad = next(
            (i for i, (a, b) in enumerate(zip(on_disk, payload)) if a != b),
            min(len(on_disk), len(payload)),
        )
        raise RuntimeError(
            "read-back verification failed: %s differs at byte %d "
            "(disk %d bytes, expected %d bytes)"
            % (path, first_bad, len(on_disk), len(payload))
        )
    return 0


def main(argv):
    if len(argv) == 1:
        return run_write()
    if len(argv) == 2 and argv[1] == "--check":
        return run_check()
    print(USAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
