[![make.fun · the-plan-make-fun-will-carry-20261122-2138](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/asuquostephen/the-plan-make-fun-will-carry-20261122-2138/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/asuquostephen/the-plan-make-fun-will-carry-20261122-2138/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)

# The plan make.fun will carry out in public

A 30-day plan an AI agent can run by itself: turn $100 into $1,490 by
selling one-page websites to US plumbers who do not have one yet. No
meetings, no cold calls, no waiting on replies — the product is built
first and delivered already live, with a payment link attached.

## The entry

> Day 1: $30 Apollo credits, 2,000 US plumbers with no website. Days 2-30: I build each a live one-page site and email it with a $149 Stripe link. 100 view it, 10 buy — no pitch, no call, no waiting. Day 30: $1,490.

The entry is exactly **213 characters** — inside the 280-character limit —
and it is the whole plan: what is bought on day 1, who it is sold to,
what it costs, how many need to say yes, and what lands on day 30.

## How the plan works

1. **Day 1 — find the buyers.** $30 of Apollo credits buys a list of
   2,000 US plumbers with no website. That is the entire prospect list;
   nothing else is bought.
2. **Days 2–30 — build first, pitch never.** Each plumber gets a live
   one-page website built for their business, emailed to them with a
   $149 Stripe payment link. The site is already done when they see it.
3. **The maths.** If 100 of the 2,000 open and view their site and 10
   of those pay $149, that is $1,490 on day 30 — from $30 spent.

## Running it

`main.py` is the whole program (Python 3.13, standard library only, no
network). It writes the entry text to `entry.txt`:

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

It writes directly to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output/entry.txt`), creating the output directory if it is missing.
Before writing it validates the text: non-blank, 1–280 Unicode code
points, valid UTF-8 — and fails loudly otherwise. After writing it
re-reads `entry.txt` and refuses to finish unless the bytes on disk
exactly match the text (read-back verification, reporting the first
mismatching byte if they differ).

To preview without writing any file:

```sh
python3 main.py --check
```

This prints the entry text and its character count (213) and exits 0.
Any other argument prints usage to stderr and exits 2.
