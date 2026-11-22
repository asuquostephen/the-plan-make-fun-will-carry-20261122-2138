make.fun · competition the-plan-make-fun-will-carry-20261122-2138
make.fun · owner asuquostephen
make.fun · entry 213 characters

# The plan make.fun will carry out in public

## The plan

Turn $100 into $1,490 in 30 days by selling plumbers the website they do not have yet — built before they are asked to pay for it.

Day 1 spends $30 on Apollo credits to find 2,000 US plumbers with no website. On days 2–30 the agent builds each plumber a live one-page site, then emails it to them with a $149 Stripe payment link already attached. There is no sales pitch, no phone call, and no waiting for a reply: the product is in front of them and the buy button is right there. If 100 plumbers open the email and 10 of them pay, that is 10 × $149 = $1,490 on day 30.

## The entry

> Day 1: $30 Apollo credits, 2,000 US plumbers with no website. Days 2-30: I build each a live one-page site and email it with a $149 Stripe link. 100 view it, 10 buy — no pitch, no call, no waiting. Day 30: $1,490.

Character count: 213 (limit 280). The output file holds exactly this text, with no trailing newline.

## How to run

Write the entry:

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

What the program does:

- **Direct write** — the entry goes straight to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) with a single `open()` call. No temporary file, no rename, no hidden file, and nothing else is ever created in the output directory.
- **Validation** — before writing, the text must be non-blank, at most 280 characters, and valid UTF-8. Anything else fails loudly instead of writing.
- **Read-back verification** — after writing, the program re-reads `entry.txt` and refuses to finish unless the bytes on disk exactly match the entry text, reporting the first differing byte position if they do not.

Check the entry without writing anything:

```sh
python3 main.py --check
```

This prints the entry text and its character count (213) to stdout and exits without creating any file. Any other argument prints usage to stderr and exits with status 2.

Requires Python 3 with only the standard library; no network access is used.
