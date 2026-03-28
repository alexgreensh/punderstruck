# Pipeline Detailed Reference

> Created by Alex Greenshpun (linkedin.com/in/alexgreensh)
> License: PolyForm Noncommercial 1.0.0. See LICENSE file in skill root.

**This file is the authoritative execution reference for the pun construction pipeline, upgraded with the CARLIN Method and Greg Dean's Joke Structure.**

**Every step below marked (INTERNAL) produces ZERO user-visible output. Execute silently. Output nothing between tool calls.**

---

## Step 0: LOAD THEORY

The SKILL.md file contains the core theory inline. This file provides the detailed execution instructions for each pipeline step.

**Selective reads by mode** (loaded per the Reference Loading table in SKILL.md):
- Standard/Topic/Multiple/Brainstorm/Shower Thoughts: This file only
- --roast/--translate/--remix: This file + `bonus-modes.md`
- --compose/Wordplay/Dad Joke: This file + `bonus-modes.md` + `pun-taxonomy.md`
- --explain: This file + `bonus-modes.md` + `comedy-theory.md` + `pun-taxonomy.md`
- Fallback (score < 17): + `worked-examples.md`

---

## Step 1: TOPIC DECONSTRUCTION & HANDLE EXTRACTION (INTERNAL)

*The CARLIN method requires deep contextual understanding before attempting humor.*

**1a. Extract Handles:**
Extract handles BEFORE launching the subagent, you need them to build the Datamuse query list.
- **Tier 1 (Obvious)**: 5-8 common associations anyone would think of. (e.g., For "coffee": brew, bean, grind, espresso, filter, roast)
- **Tier 2 (Insider/Technical)**: 3-5 domain-specific terms only someone IN the field would know. (e.g., For "coffee": cupping, extraction, tamp, crema)

**1b. Third-Association Rule:**
Discard the first two obvious associations that come to mind. Dig for the third, more specific association.

**1c. Deterministic Probe:**
Run `python3 scripts/datamuse_probe.py` with the topic and extracted handles.
- Use `--skip-seeds` for random mode.
- Use `--expand` if the first pass returns too few useful sound-alikes.
- **What comes back**: Clean text summary. No raw JSON.

---

## Step 2: THE CONNECTOR SEARCH (INTERNAL)

*A pun relies on a Connector: a word or phrase with two distinct interpretations.*

**2a. Analyze Datamuse Results:**
Look for the highest "cognitive distance" between two meanings.
- **Polysemy (Priority 1):** One word, two entirely different meanings (e.g., "Weight" vs "Wait").
- **Natural Compound Splits (Priority 2):** (e.g., "Bookmark" -> "Book, Mark").
- **Homophones (Priority 3):** (e.g., "Neil" / "Kneel").
- **Syllable Breakdown (For Dad Jokes):** Can a 3-4 syllable word be broken into separate words? (e.g., "African" -> "A-free-can").

**2b. Build Cognitive Distance Table:**
- **LOW**: Both domains in same context (skip).
- **HIGH**: Completely unrelated fields (strong candidate).

---

## Step 3: MAP THE TWO STORIES (Greg Dean's Structure) (INTERNAL)

*Every joke consists of two stories. The Connector links them.*

1. **Define the 1st Story (Target Assumption):** What is the normal, expected context of the topic? What will the audience assume you are talking about?
2. **Define the 2nd Story (Reinterpretation):** What is the surprising, alternate reality created by the second meaning of the Connector?
3. **Check the Incongruity:** Does the 2nd story logically make sense in a weird way? (Suls's Two-Stage Model: Surprise + Logical Resolution).

---

## Step 4: DRAFTING (Chris Head's Beforethought Technique) (INTERNAL)

*This is where most AI jokes fail. You must construct the joke backward.*

1. **Write the Punchline First:** The punchline contains the Connector (the double meaning).
2. **Write the Setup Backward:** Create a setup that establishes the 1st Story (Target Assumption).
3. **THE GOLDEN RULE:** **NEVER put the punchline word, or a close variation of it, in the setup.**
   - *Bad:* "I usually meet my girlfriend at one minute to one because I like one-to-one time." (Spoils the punchline).
   - *Good:* "I usually meet my girlfriend at 12:59 because I like that one-to-one time."

**Construction Provenance Rule (Non-Negotiable):**
Every pun you serve MUST trace back to a specific Datamuse phonetic collision or a seed joke analysis. If you just thought of it, it's a training-data groaner. Discard it.

---

## Step 5: REFINEMENT & TIGHTENING (INTERNAL)

*Stand-up comedy relies on rhythm and brevity.*

1. **Rule of Three:** If listing items, make the first two normal and the third the punchline.
2. **Punchline Placement:** The funny word MUST be the absolute last word of the sentence. Do not add trailing words.
   - *Bad:* "The baker was a kneady guy, so he asked for a raise."
   - *Good:* "The baker asked for a raise because he was too kneady."
3. **Cut the Fat:** Remove unnecessary adjectives and adverbs. Target length: 8-20 words.
4. **Hard Consonant Guide:** Plosive consonants are funnier: K, hard C, hard G, P, T, B, D.
5. **The "Too On-The-Nose" Check:** Is the joke too obvious? Make the connection slightly more indirect so the audience has to bridge the gap themselves.

---

## Step 6: CRITIQUE (INTERNAL)

Score 5 candidates on 5 criteria (1-5 each), matching the rubric in `SKILL.md`:

| Criterion | Question |
|-----------|----------|
| Effortless Activation | Does the double meaning land instantly without explaining itself? |
| Surprising Punchline | Does the turn feel earned but not obvious? |
| Groan-Worthy | Does it trigger the involuntary "ugh, fine" response good puns need? |
| Setup Brevity | Is the setup tight, clean, and free of filler? |
| Actually Funny | Would a human groan, laugh, or text it to someone? **(VETO: below 3/5 = auto-eliminate)** |

**Minimum to serve: 17/25 AND "Actually Funny" >= 3/5.**

**The Bar Test**: Imagine telling this to a stranger at a bar. Laugh/groan = PASS. Blank stare = FAIL.

---

## Step 7: SERVE. (ONLY VISIBLE OUTPUT)

**Conversational delivery. No cards. No tables. No gimmicks.**

### Standard Mode
1. Lead with the winner. Just the joke. No label, no preamble.
2. "A few more that were fighting for the spot:" followed by 2-3 runners-up.
3. Fresh sign-off + go-deeper invitation.

### Dad Joke Mode
1. Deliver the Q&A dad joke based on the Syllable Breakdown formula.
2. Add a classic Dad sign-off (e.g., "I'll see myself out.").

### Session Continuity (Go Deeper)
After serving, end with a brief invitation to iterate:
- **Standard/Topic**: "Want a different angle on [topic]?"
- **Roast**: "Want me to dial it up? Take a different angle?"
- **Dad Joke**: "Ready for another eye-roll?"
