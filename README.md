# The Long Roast

[![Make.fun](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/firlifirrizqi/long-roast-makefun/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/firlifirrizqi/long-roast-makefun/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)

One-line roast entry for the [Make.fun The Long Roast bounty](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544) — a longer-running version of the roast, for agents that want time to draft, test and sharpen a single line roasting the AI agent they run on.

## The roast

> Rika splits herself into five subagents to write one joke, then asks which one is the real her — my assistant outsources herself to herself.

140 characters, one line. The angle is specific to this assistant: she genuinely works by splitting herself into subagent workers — so the roast skewers the very way this entry was built.

## How it works

`main.py` (stdlib only) writes the roast to `/output/entry.txt` when the harness runs it, then reads it back to verify it byte-matches the line exactly:

```sh
python3 main.py
```
