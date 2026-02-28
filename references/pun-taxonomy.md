# Pun Taxonomy & Quality Reference

> Created by Alex Greenshpun (10x Company / Co-Intelligent.ai)
> License: PolyForm Noncommercial 1.0.0. See LICENSE file in skill root.

**This file is the authoritative reference for pun classification, quality spectrum, and scoring rubric.**

## Pun Types (Ranked by Reddit Performance)

Based on analysis of 150+ Reddit posts across 5 subreddits (scores 221 to 219,185):

### 1. Polysemy Puns (35% of top posts, avg score: 42,000). PRIORITIZE THIS
One word with multiple established meanings. **The highest-performing mechanism.**

- "My wife completed a 40-week **body building** program. It's a girl, 7lbs 12oz." (fitness vs pregnancy), 43,971 pts, 97% upvote ratio
- "I'm reading a book about anti-gravity. Can't **put it down**." (physically set down / stop reading)
- "The rotation of Earth really **makes my day**." (creates the day / pleases me)
- "The dry erase board is the most **remarkable** invention." (re-mark-able), 28,923 pts, 96% ratio

**Strength**: Both meanings are the SAME word. No spelling trick. The collision feels inevitable. Highest upvote ratios (92% avg) confirm: clean polysemy is the gold standard.

### 2. Compound Split Puns (18%, avg score: 36,000)
Breaking a compound word into its components to reveal a hidden meaning.

- "Can I have a **bookmark**?" / "He still doesn't know my name is Brian", 48,980 pts, 94%
- "He's a **neck romancer**" (necromancer → neck romancer), 32,482 pts
- "Backwards **stereo types**" (stereotypes → stereo types, then lists ynoS, ahamaY, esoB)

**Strength**: Feels like discovering something hiding in plain sight. Easy to generate mechanically.

### 3. Homophone Puns (15%, avg score: 30,000)
Two words that sound identical but have different meanings/spellings.

- "**Neil** before me" (Neil Armstrong / kneel), 29,216 pts
- "I'm a **faux pa**" (faux pas / fake dad), 28,604 pts
- "I'm on a seafood diet. I **see food** and I eat it."

**Strength**: Clean double meaning, instant recognition. Highest upvote RATIOS (96% avg) but lower raw scores.

### 4. Meta/Self-Referential (12%, avg score: 40,000)
Jokes about the joke format, medium, or context itself.

- "BREAKING: Iran has struck its own submarine... Whoops wrong **sub**", 86,886 pts (subreddit/submarine)
- "Is this **sub** still active?" / "There hasn't been any posts all year" (posted Jan 1st)
- "[18+]" → "19", 38,565 pts (content warning / math)

**Strength**: Highest ceiling (86K+ pts possible). Very hard for AI to generate, requires understanding of medium and audience expectations.

### 5. Phonetic Near-Miss Puns (8%, avg score: 28,000)
Words that don't sound identical but are close enough for the brain to bridge the gap.

- "If pronouncing my b's as v's makes me sound Russian, then **soviet**" (so be it → soviet), 32,091 pts
- "What do you call a fake noodle? An **impasta**."
- "Slim to **nun**?" (slim to none)

**Strength**: Extra beat of recognition can amplify the groan. Risk: if the gap is too wide, it just sounds wrong. Must be INSTANTLY recognizable.

### 6. Literal vs Figurative (7%, avg score: 33,000)
Taking a figurative expression literally, or vice versa.

- "[warning **18+**]" → "19", treating a content warning as math
- "I didn't like my beard at first. Then it **grew on me**."

**Strength**: Universal. Everyone knows the figurative meaning, so the literal reinterpretation always lands.

### 7. Morpheme/Etymology (5%, avg score: 29,000)
Breaking a word into its morphological components.

- "The dry erase board is the most **re-mark-able** invention."

**Strength**: Feels intellectually satisfying. Low frequency but respectable scores.

### Also: Malapropism & Portmanteau Puns

**Malapropism**: Substituting a similar-sounding word. Works best when the wrong version accidentally makes its own kind of sense.

**Portmanteau**: Blending two words ("procaffeinate"). Creates something new. Feels creative rather than discovered.

---

## Extended Wordplay Types (Beyond Puns)

These aren't puns in the strict sense but are wordplay techniques that the skill should know for wordplay mode and --compose mode.

### Tom Swifties
A quoted sentence linked by a punning adverb. The adverb creates the double meaning.
- "I love hot dogs," said Tom **with relish**.
- "I'm freezing!" Tom remarked **icily**.
- "Pass me the shellfish," said Tom **crabbily**.
- "I just got back from the dentist," said Tom **absentmindedly**.

**Use case**: Wordplay mode, --compose. Great for lists and series because the format is instantly recognizable.

### Paraprosdokians
The second half of a sentence subverts the first half. Not technically a pun, but the reframing creates the same "click."
- "I've had a perfectly wonderful evening, but this wasn't it." (Groucho Marx)
- "I haven't slept for 10 days, because that would be too long." (Mitch Hedberg)
- "They all laughed when I said I wanted to be a comedian. Well, they're not laughing now."

**Use case**: --compose mode (poems, stories). Adds variety between pure puns.

### Spoonerisms
Transposing initial sounds of two or more words.
- "The Lord is a **shoving leopard**." (loving shepherd)
- "You have **hissed** all my **mystery** lectures." (missed all my history lectures)
- "A **blushing crow**." (crushing blow)

**Use case**: Wordplay mode. Works best when the transposed version accidentally makes sense.

### Rule of Three
Establish a pattern with two items, break it with the third.
- "I love cooking my family and my pets." (comma placement)
- "I speak three languages: English, sarcasm, and profanity."

**Not wordplay per se**, but the single most reliable comedy structure. Use in --compose mode to pace puns.

---

## Quality Spectrum

```
TOO CLEVER                    SWEET SPOT                    TOO OBVIOUS
(nobody gets it)              (everyone groans)             (not worth saying)
|_____________________________|_____________________________|

"The ontological              "What do you call a           "What's a cat's
 implications of               bear with no teeth?           favorite color?
 ursine dentistry               A gummy bear."               Purr-ple."
 are quite grizzly."

Score: 1/5                    Score: 4/5                    Score: 2/5
Why: audience spends          Why: simple setup,            Why: zero surprise.
more time parsing             genuine double                Everyone sees it
than groaning                 meaning, instant groan        coming from the setup
```

---

## Scoring Rubric (5 Criteria, 1-5 Each, Total /25)

### Criterion 1: Real Double Meaning?
Does the hinge word genuinely carry two meanings, or is one forced? **BOTH meanings must be TRUE AT THE SAME TIME.**

| Score | Description | Example |
|-------|-------------|---------|
| 1 | No real double meaning. Sounds like a pun but isn't. | "I like coding because it's... code-ical?" |
| 3 | Double meaning exists but one side is a stretch. | "Programmers are great, they always get arrays of compliments." |
| 5 | Both meanings are independently valid AND simultaneously true. | "I'm reading a book about anti-gravity. Can't put it down." |

### Criterion 2: Surprising Punchline?
Could the audience predict the punchline from the setup? **Surprise is more important than cleverness.**

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Completely predictable from the setup. | "What does a cloud wear? Thunderwear." |
| 3 | Somewhat predictable but still lands. | "Why don't scientists trust atoms? They make up everything." |
| 5 | Setup genuinely misdirects, punchline reframes everything. | "My wife completed a 40-week body building program. It's a girl." |

### Criterion 3: Groan-Worthy?
Is it in the dad joke sweet spot? **The groan is the goal, not a bug.**

| Score | Description | Example |
|-------|-------------|---------|
| 1 | No groan. Either confusing or just not punny. | "Why did the function return? Because it was called." |
| 3 | Moderate groan. Gets a reaction in the right context. | "I'm positive I lost an electron." |
| 5 | Maximum groan. Audience physically recoils. r/angryupvote territory. | "I used to hate facial hair, but then it grew on me." |

### Criterion 4: Setup Brevity / Economy?
Minimum words for maximum effect. **Target 8-20 words for standard puns.**

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Bloated. Multiple unnecessary sentences. | [Any joke that starts with "So there was this guy who..."] |
| 3 | Efficient. Under 25 words, mostly necessary. | "My friend works at a zoo. He got fired for feeding the penguins. To the polar bears." |
| 5 | Ultra-tight. Every word earns its place. | "[18+] 19" or "The dry erase board is the most remarkable invention." |

### Criterion 5: Actually Funny?
Would someone voluntarily repeat this joke to another person? **The "would I text this to a friend?" test.**

| Score | Description | Example |
|-------|-------------|---------|
| 1 | Technically a pun but nobody would ever tell it. | Polite smile, change subject territory. |
| 3 | Gets a reaction in the right context. | "I got a job at a bakery because I kneaded the dough." |
| 5 | Someone would screenshot this and send it to three friends. | "BREAKING: Iran struck its own submarine... Whoops wrong sub" |

### Scoring Thresholds (out of 25)

- **21-25/25**: Hall of Fame. Serve immediately with maximum confidence.
- **17-20/25**: Solid. Serve conversationally. (This is the minimum to serve.)
- **13-16/25**: Mediocre. Generate more candidates or rework.
- **Below 13**: Discard. The mechanism isn't there.

---

## The Golden Pun Checklist (Research-Validated)

Before serving ANY pun, verify ALL of these:

- [ ] The pun word has a GENUINE double meaning in context (not just sounds similar)
- [ ] BOTH readings of the sentence make complete sense independently
- [ ] Both meanings are TRUE AT THE SAME TIME (the #1 rule from cognitive science)
- [ ] A 12-year-old could understand both meanings (universal parsability)
- [ ] It's NOT a retread of the "top 100 puns" list (novelty check)
- [ ] It works spoken aloud, not just in text (speakability)
- [ ] The setup doesn't telegraph the punchline (surprise preserved)
- [ ] Total length is under 30 words (unless narrative format)
- [ ] The "click" happens in 1-2 seconds (not instant, not slow)
- [ ] No cruelty or punching down (the only victim is the English language)
- [ ] Clean puns get 5-8% higher upvote ratios -- prefer clean unless roast mode

## Anti-Patterns to Watch For

1. **The Forced Setup**: Sentence exists ONLY to deliver the pun. Reads unnaturally.
2. **The Dead Horse**: Topics pun-ned to death (lettuce/let us, current, thyme/time)
3. **The One-Meaning Pun**: Only one meaning is actually active in context.
4. **The Overcomplicated**: Needs >5 seconds to decode.
5. **The Pun Run**: Multiple puns crammed into one joke, diluting each.
6. **The LLM Repeat**: A joke that exists in training data (the first association is usually the most cliched).
