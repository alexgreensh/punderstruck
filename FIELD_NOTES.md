# Punderstruck Field Notes

Accumulated insights from real usage. Updated as patterns emerge.

## Bug Fixes
- **Roast 3-level bug (2026-02-19)**: Users only got 3 roast levels (Light/Medium/Dark) because SKILL.md didn't define levels inline. Claude improvised a natural coffee-roast scale and dropped "Espresso Shot." Fixed by adding the 4-level table directly into SKILL.md.
- **Trading card output**: worked-examples.md and pun-taxonomy.md still referenced the old PUN TRADING CARD format after SKILL.md was updated to conversational delivery. Aligned all files.
- **Scoring mismatch**: pun-taxonomy.md used different criterion names ("Real Double Meaning" vs "Effortless Activation") and worked-examples.md scored on /20 instead of /25. Aligned to 5 criteria, /25, matching names everywhere.

## Observations
- When reference files don't load (or load partially), Claude falls back on training data patterns. Any critical instruction that lives ONLY in a reference file is at risk. Defensive fix: duplicate key specs inline in SKILL.md.
- The Espresso Shot level is the most likely to be dropped because it's structurally different from the other three (one line vs monologue). Always needs explicit instruction.
