# Pipeline Detailed Reference

> Created by Alex Greenshpun (10x Company / Co-Intelligent.ai)
> License: PolyForm Noncommercial 1.0.0. See LICENSE file in skill root.

**This file is the authoritative execution reference for the pun construction pipeline.**

**Every step below marked (INTERNAL) produces ZERO user-visible output. Execute silently. Output nothing between tool calls.**

---

## Step 0: LOAD THEORY

The SKILL.md file contains the core theory inline (mechanism hierarchy, construction method summary, scoring, API URLs). This file provides the detailed execution instructions for each pipeline step.

**Selective reads by mode** (loaded per the Reference Loading table in SKILL.md):
- Standard/Topic/Multiple/Brainstorm/Shower Thoughts: This file only
- --roast/--translate/--remix: This file + `bonus-modes.md`
- --compose/Wordplay: This file + `bonus-modes.md` + `pun-taxonomy.md`
- --explain: This file + `bonus-modes.md` + `comedy-theory.md` + `pun-taxonomy.md`
- Fallback (score < 17): + `worked-examples.md`

---

## Step 1a: HANDLE EXTRACTION (Main Context). (INTERNAL. Output nothing.)

Extract handles BEFORE launching the subagent, you need them to build the Datamuse query list.

**Tier 1 (Obvious)**: 5-8 common associations anyone would think of.
- For "coffee": brew, bean, grind, espresso, filter, roast, drip, mug

**Tier 2 (Insider/Technical)**: 3-5 domain-specific terms only someone IN the field would know. This is where fresh material lives.
- For "coffee": cupping, extraction, tamp, crema, pull, bloom, degassing

**Total: 8-13 handles across both tiers.** Tier 2 handles produce more novel puns because they're less likely to appear in training data.

**Random mode** (no topic): Pick a random domain (food, science, nature, profession, technology, sports, music, animals) and extract handles from it.

---

## Step 1b: SUBAGENT LAUNCH. (INTERNAL. Output nothing.)

Use the **Task tool** with `subagent_type: "Bash"` and `model: "haiku"` to fire ALL API calls in a single Python script. Haiku is correct because this is pure data extraction. All creative work stays on Opus in main context.

The Python subagent template is in SKILL.md. Replace `{{HANDLE_LIST}}` with the handles from Step 1a and `{{TOPIC}}` with the user's topic.

**The subagent prompt should say**: "Run this Python script and return its complete stdout output. Nothing else."

**What comes back**: Clean text summary (seed jokes + sound-alike pairs + homophones). No raw JSON. ~5-15 seconds total.

**If topic is Random mode**: Skip the seeds URL (icanhazdadjoke search requires a term). Only fire Datamuse queries.

**Optional expansion**: If the first batch produces fewer than 10 sound-alike pairs, launch a second subagent call with semantic expansion queries (`ml=HANDLE`) for handles with weak results.

**Fallback**: If seed APIs return nothing (common for niche topics), the subagent still returns Datamuse results. Seeds are gravy, not essential.

### Joke Source APIs

**icanhazdadjoke.com (Primary)**:
- Random: `curl -s -H "Accept: application/json" https://icanhazdadjoke.com/`
- Topic: `curl -s -H "Accept: application/json" "https://icanhazdadjoke.com/search?term=TOPIC&limit=5"`
- MUST include `Accept: application/json` header or you get HTML.

**JokeAPI v2 (Secondary)**:
- Random pun: `curl -s "https://v2.jokeapi.dev/joke/Pun?type=twopart&safe-mode"`
- Topic: `curl -s "https://v2.jokeapi.dev/joke/Pun?type=twopart&safe-mode&contains=TOPIC"`
- Always include `safe-mode` flag.

**Official Joke API (Backup)**:
- Random: `curl -s https://official-joke-api.appspot.com/random_joke`
- No topic search. Backup only.

**Fallback chain**: icanhazdadjoke → JokeAPI v2 → Official Joke API → Datamuse only (pipeline still works without seeds).

### Datamuse API Details

- **Sounds-like** (primary pun discovery): `api.datamuse.com/words?sl=WORD&max=8`
- **Homophones**: `api.datamuse.com/words?rel_hom=WORD&max=5`
- **Means-like** (semantic expansion): `api.datamuse.com/words?ml=WORD&max=8`
- **Combined** (sounds-like + topic): `api.datamuse.com/words?sl=WORD&topics=TOPIC&max=10`
- **Compound embedding**: `api.datamuse.com/words?sp=*WORD*&max=8`

No auth required. Generous rate limits.

---

## Step 2: ANALYZE (Seeds + Datamuse Results). (INTERNAL. Output nothing.)

**2a. Analyze seed jokes** (if any returned):
For each seed joke, identify:
- **Wordplay type**: homophone, polysemy, compound split, phonetic near-miss, malapropism, portmanteau
- **Structure**: setup/punchline, one-liner, question/answer
- **Misdirection technique**: What does the setup make you expect? How does the punchline violate that?
- **Hinge word**: The specific word/phrase carrying the double meaning

This analysis informs your own construction. You're studying the craft, not copying the jokes.

**2b. Build cognitive distance table** from Datamuse results:
For each sound-alike pair, rate domain distance. **Heavily prioritize polysemy** (35% of top Reddit puns, avg 42K upvotes) and **natural compound splits** (18%, avg 36K). Deprioritize phonetic near-misses unless extremely close. **Discard forced compound splits.**

- **LOW**: Both domains in same Wikipedia article (skip)
- **MEDIUM**: Related fields (usable)
- **HIGH**: Completely unrelated fields (strong candidate)
- **VERY HIGH**: Absurdly distant domains (risky but rewarding)

### Mechanism Priority (Empirical Data)

| Priority | Mechanism | Frequency | Avg Score | Example |
|----------|-----------|-----------|-----------|---------|
| 1 | **Polysemy** | 35% | 42,000 | "Body building" (fitness vs pregnancy) |
| 2 | **Compound split** | 18% | 36,000 | "Bookmark" / "book, Mark" |
| 3 | **Homophone** | 15% | 30,000 | "Neil before me" (kneel/Neil) |
| 4 | **Meta/structural** | 12% | 40,000 | "Wrong sub" (subreddit/submarine) |
| 5 | **Phonetic near-miss** | 8% | 28,000 | "Soviet" = "so be it" |
| 6 | **Literal vs figurative** | 7% | 33,000 | "[18+]" → "19" |
| 7 | **Morpheme/etymology** | 5% | 29,000 | "Re-mark-able" |

---

## Step 3: GENERATE. (INTERNAL. Output nothing.)

Apply the punchline-first method to the highest-distance pairs from Step 2:

**3a. Construct punchlines**: Take the highest-distance pairs FROM YOUR COGNITIVE DISTANCE TABLE. Write a sentence where BOTH meanings are simultaneously active. Write the punchline FIRST (punchline-first principle).

**3b. Write misdirecting setups**: Each setup must:
- Establish the FIRST meaning (the expected one)
- Be under 2 sentences
- Sound completely innocent (not like a joke setup)

**3c. Third-association filter**: For each collision pair, ask: "Is this the FIRST thing someone would think of?" If yes, discard it. Push past the first two obvious associations. The third or fourth connection is where fresh material lives.

### Construction Provenance Rule (Non-Negotiable)

**Every pun you serve MUST trace back to a specific Datamuse phonetic collision or a seed joke analysis.**

If you cannot point to which Datamuse result or seed joke inspired a candidate, that candidate was generated from training data and MUST be discarded. The pipeline exists specifically because LLM-generated humor is mediocre and repetitive.

**Test**: For each candidate, "Which Datamuse sound-alike pair or seed joke mechanism does this come from?" If the answer is "none, I just thought of it," it fails provenance.

**Only exception**: Datamuse completely down (extremely rare), fall back to comedy theory + phonetic intuition.

---

## Step 4: CRITIQUE. (INTERNAL. Output nothing.)

Generate 5 candidates. Score each on 5 criteria (1-5 each):

| Criterion | Question |
|-----------|----------|
| Effortless activation | Does the listener's brain NATURALLY activate both meanings without effort? |
| Surprising punchline | Could the audience predict it from the setup? |
| Groan-worthy | Is it in the dad joke sweet spot? |
| Setup brevity | Is the setup tight and clean? Under 2 sentences? |
| Actually funny? | Would someone voluntarily repeat this? **(VETO: below 3/5 = auto-eliminate)** |

### The Effortless Activation Test (Most Important Criterion)

- **Polysemy**: Almost always passes. "Outstanding" = unfinished AND excellent. **Strongest mechanism. Prioritize it.**
- **Natural compound splits**: Passes IF both parts are common standalone words AND native speakers would naturally parse the split. **Test: would a 10-year-old see the split without being told?**
- **Phonetic near-misses**: Passes only IF sounds are close enough that saying one genuinely evokes the other. **Test: would someone mishear one as the other?**

### "Actually Funny" Veto Gate

- 1/5: Technically a pun but nobody would ever tell it → **AUTO-ELIMINATE**
- 2/5: You can see it's a pun but no reaction → **AUTO-ELIMINATE**
- 3/5: Gets a real reaction in the right context → Passes veto
- 4/5: Someone would voluntarily tell this to another person
- 5/5: Someone would screenshot this and send it to three friends

**Minimum to serve: 17/25 AND "Actually funny" ≥ 3/5.**

If no candidate hits 17/25: Read `references/worked-examples.md` for inspiration, generate 3 more from different Tier 2 handles.

If STILL below 17: Serve the best with: *"This one's a stretch. Even I know it. But I'm committed."*

### Research-Backed Scoring Formula (Calibration)

**Note:** This weighted formula is for calibration reference only. The operational scoring system is the /25 unweighted system defined in SKILL.md.

```
Score = (Surprise × 0.30) + (Parsability × 0.25) + (Economy × 0.20) + (Novelty × 0.15) + (Speakability × 0.10)
```

- **Surprise 5**: Total cognitive reframe. **4**: Strong misdirection. **3**: Noticeable. **2**: Telegraphed. **1**: None.
- **Parsability 5**: Instant. **4**: Quick click 1-2 sec (SWEET SPOT, highest Reddit engagement). **3**: Medium. **2**: Needs re-reading. **1**: Requires explanation.
- **Economy 5**: Ultra-minimal ("[18+]" → "19"). **4**: Under 15 words. **3**: Under 25 words. **2**: Padded. **1**: Bloated.
- **Novelty 5**: Never seen before. **4**: Fresh take. **3**: Familiar mechanism, new context. **2**: Known format. **1**: Overused.
- **Speakability 5**: Perfect spoken. **4**: Works with emphasis. **3**: Text is clearer. **2**: Text-dependent. **1**: Visual only.

### The Golden Pun Checklist

- [ ] Pun word has GENUINE double meaning in context
- [ ] Non-pun reading makes complete sense
- [ ] Pun reading makes complete sense
- [ ] A 12-year-old could understand both meanings
- [ ] NOT a retread of "top 100 puns"
- [ ] Works spoken aloud
- [ ] Setup doesn't telegraph punchline
- [ ] Under 30 words (unless narrative format)
- [ ] "Click" happens in 1-2 seconds
- [ ] Both meanings TRUE AT THE SAME TIME

---

## Step 4.25: TIGHTEN. (INTERNAL. Output nothing.)

Before the humor review, compress the winning candidate:
- Can any word be cut without losing meaning? Cut it.
- Can the setup be one sentence instead of two? Make it one.
- Is the pun word at the END of the punchline? Move it there.
- Are there hard consonant sounds (K, G, P, T, B, D) available? Prefer them.
- Target: 8-20 words for standard puns.

### Optimal Lengths

| Format | Total Words | Notes |
|--------|------------|-------|
| One-liner | 8-16 | Single unit |
| Q&A | 10-20 | Short answers hit harder |
| Setup/punch | 15-30 | Less punchline = harder landing |
| Narrative | 30-100 | Long setup IS part of the joke |
| Limerick | 30-50 | Line 5 must be biggest laugh |
| Haiku | 10-17 syllables | Constraint breeds creativity |

### Hard Consonant Guide

Plosive consonants are measurably funnier (Wiseman's LaughLab): **K, hard C, hard G, P, T, B, D** > S, F, L, M, N. "Duck" > "swan." "Pickle" > "relish." "Crack" > "split."

### Statements vs Questions

Reddit data: Statements = 83% of top posts (avg 36.5K). Questions = 17% (avg 33.1K). Use questions only when the answer IS the pun. Statements feel more "discovered" by the audience.

---

## Step 4.5: HUMOR REVIEW. (INTERNAL. Output nothing.)

After scoring on technical quality, the winner must ALSO pass the humor gate.

**The Bar Test**: Imagine telling this to a stranger at a bar.
- Laugh/groan/physical recoil → PASS
- Blank stare or "I don't get it" → FAIL
- Polite smile and subject change → FAIL (worst outcome)

**The Text Test**: Imagine texting this to a friend.
- Reply with 😂 or 🫠 or "I hate you" → PASS
- Reply "lol" (lowercase, no punctuation) → FAIL
- Left on read → FAIL

**The Google Test**: Is this joke BETTER than page 1 of "[topic] puns"?
- Yes → PASS
- Could appear on a "50 [topic] puns" listicle → FAIL (too generic)

**If output FAILS the impressiveness bar:**
1. Identify WHY it's flat (too predictable, too clever, setup kills surprise, reads like "observation" instead of revelation)
2. Rewrite with more punch (tighter setup, sharper contrast, better rhythm)
3. If rewrite still fails, go back to Step 3 with different handle pairs

---

## Step 5: SERVE. This is the ONLY step that produces visible output.

**Conversational delivery. No cards. No tables. No gimmicks.**

### Standard Mode (single pun request)
1. Lead with the winner. Just the joke. No label, no preamble.
2. "A few more that were fighting for the spot:" (or vary the wrapper) followed by 2-3 runners-up.
3. Fresh sign-off + go-deeper invitation.

### Multiple Puns ("give me 5 puns about...")
1. Numbered list, strongest first, descending.
2. Fresh sign-off.

### Brainstorm Mode
1. Brief context acknowledgment (one sentence max).
2. 4-6 pun angles, each with the pun AND a one-line usage note (ad headline, tagline, subject line, etc.)
3. Group by approach if natural.
4. Close by asking which angle hits / want to go deeper.

### Shower Thoughts Mode
1. 3-5 observations using patterns: perspective shift, paradox reframing, literal interpretation, scale shift.
2. NOT puns (unless a pun naturally fits). "Things you can't un-think."
3. Casual tone. 1-2 sentences each. **20 words or fewer per thought.**
4. Generate 6-8 candidates internally, serve only the bangers. Better 3 great than 5 with filler.
5. **Kill the essay voice.** Short. Punchy. No semicolons, no "which means that."
6. **Retweet Test**: Would someone repost with zero added commentary?
7. NO sign-off. NO invitation. Let them land. Silence is the point.

### Compose Mode (poems, limericks, stories, paragraphs)
1. Deliver the composition directly. No framing, no introduction.
2. One sign-off after.
3. For long compositions (1000+ words), just write the piece.

---

## Sign-Off Rules

Generate a FRESH, original one-liner each time. Never reuse themes within a session. Vary the energy:
- Sometimes self-deprecating: *"That one barely survived my own quality filter."*
- Sometimes topic-referencing: tie it to the specific subject
- Sometimes meta: *"That's 14 seconds of your life you're not getting back."*
- Sometimes absurdly confident: *"I peaked. It's all downhill from here."*
- Sometimes just a shrug: *"Anyway."*

**No sign-off for**: Roasts (mic drop IS the closer) and Shower Thoughts (silence is the point).

---

## Session Continuity (Go Deeper)

After serving, end with a brief invitation to iterate (except shower thoughts):
- **Standard/Topic**: "Want a different angle on [topic]?"
- **Roast**: "Want me to dial it up? Take a different angle? Or roast something else?"
- **Brainstorm**: Built in. "Which angle hits?"
- **Compose**: "Want me to try a different format? Or tighten this one?"
- **Wordplay**: "Want more on [word]? Or a different word?"

**When user comes back**: Run pipeline again but EXCLUDE hinge words already used. Focus on Tier 2 handles or adjacent topics.

Keep it ONE line, not a menu. Comedian saying "want more?" not a survey.

---

## Quick Pipeline Walkthrough

For `/punderstruck coffee`:

1. **Mode detect**: topic = coffee. Standard mode. Read `pipeline-detailed.md`.
2. **HANDLES**: Tier 1: brew, bean, grind, espresso, filter, roast. Tier 2: cupping, extraction, tamp, crema.
3. **SUBAGENT**: Task(Bash, haiku). Python fires icanhazdadjoke("coffee") + 20 Datamuse queries in parallel. Returns clean text ~5-10 sec.
4. **ANALYZE**: Study seed mechanisms. Build cognitive distance table. Discover: grounds/grounds (polysemy, HIGH), brew/blew (homophone, HIGH), roast (polysemy, HIGH).
5. **GENERATE**: Third-association filter → punchline-first construction → "I just bought a coffee plantation. The grounds alone were worth it."
6. **TIGHTEN + CRITIQUE**: 23/25. Passes humor review. Already tight (14 words).
7. **SERVE**: Lead with winner, 2-3 runners-up, sign-off, go-deeper invitation.

### Calibration Punchlines (What 20+/25 Looks Like)

- "Whoops wrong sub" (submarine→subreddit, total reality shift)
- "It's a girl, 7lbs 12oz" (body building = gym AND pregnancy)
- "19" (response to [18+], content warning→math)
- "Most remarkable" (re-mark-able, dry erase board)
- "So be it / Soviet" (b→v phonetic swap)
- "I'm a faux pa" (faux pas→fake dad)

### Quality Spectrum

- **TOO CLEVER**: "The ontological implications of ursine dentistry are grizzly" (1/5, parsing > groaning)
- **SWEET SPOT**: "What do you call a bear with no teeth? A gummy bear." (4/5, simple, instant, real)
- **TOO OBVIOUS**: "What's a cat's favorite color? Purr-ple." (2/5, zero surprise)

### Reference Punchlines (Pattern Library)

| Punchline | Mechanism | Why It Works |
|-----------|-----------|-------------|
| "Whoops wrong sub" | Polysemy | submarine → subreddit reality shift |
| "It's a girl, 7lbs 12oz" | Polysemy | "Body building" = gym AND pregnancy |
| "19" | Literal interpretation | [18+] = content warning AND math |
| "Most remarkable" | Morpheme | re-mark-able (dry erase) |
| "So be it / Soviet" | Phonetic sub | b→v swap |
| "Neil before me" | Homophone | Neil Armstrong / kneel |
| "I'm a faux pa" | Near-miss | Faux pas / fake dad |
| "He's a neck romancer" | Compound creation | Necromancer split |
| "I kneaded the dough" | Homophone+polysemy | kneaded/needed + dough (bread/money) |

### Viral Format Templates

1. "I have a [TOPIC] joke, but [PUN]": self-referential meta
2. "What do you call a [X]? A [PUN]!": classic Q&A
3. "[TOPIC] walks into a bar...": narrative setup
4. "[JARGON] used in unexpected context": profession humor
5. "[STATEMENT]. [REINTERPRETATION].": two-sentence polysemy
6. "[FAMOUS QUOTE with one word swapped]": remix format
