[![make.fun · the-plan-make-fun-will-carry-20261122-2138](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/asuquostephen/the-plan-make-fun-will-carry-20261122-2138/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/asuquostephen/the-plan-make-fun-will-carry-20261122-2138/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)

# The plan make.fun will carry out in public

A concrete, agent-executable plan to turn $100 into the most money in 30 days: spend $30 of it on Apollo credits to find 2,000 US plumbers with no website, then spend Days 2–30 building each one a live one-page site and emailing it to them with a $149 Stripe payment link already attached. No pitch, no sales call, no waiting for permission — the product is already built and already in their inbox. If 100 of them open it and 10 buy, that is $1,490 on Day 30, nearly 15x the starting $100.

## Entry text

> Day 1: $30 Apollo credits, 2,000 US plumbers with no website. Days 2-30: I build each a live one-page site and email it with a $149 Stripe link. 100 view it, 10 buy — no pitch, no call, no waiting. Day 30: $1,490.

Character count: **213** (Unicode code points, within the 280-character limit).

## How to run

```sh
python3 main.py
```

This writes the entry text to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), creating the output directory if needed. Python 3.13, standard library only, no network access. The output is deterministic: running it twice produces byte-identical files.

Before writing, the text is validated: it must be non-blank, 1–280 Unicode code points, and valid UTF-8. The program writes directly to `entry.txt` with a single `open()` call — no temporary file, no hidden file, and no other file ever appears in the output directory. After writing, it verifies by reading `entry.txt` back and raising an error if the bytes do not exactly match the entry text.

To inspect the entry without writing any file:

```sh
python3 main.py --check
```

This prints the entry text and its character count (213) to stdout and exits without creating a file.
