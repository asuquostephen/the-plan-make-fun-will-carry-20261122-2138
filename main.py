#!/usr/bin/env python3
"""Write the competition entry text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Competition: the-plan-make-fun-will-carry-20261122-2138
("The plan make.fun will carry out in public").

Deterministic, standard library only, no network access. The entry is a
single literal below; the output file contains exactly that text, encoded
as UTF-8, with no trailing newline.
"""

import os

ENTRY_TEXT = "Day 1: $30 Apollo credits, 2,000 US plumbers with no website. Days 2-30: I build each a live one-page site and email it with a $149 Stripe link. 100 view it, 10 buy \u2014 no pitch, no call, no waiting. Day 30: $1,490."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
