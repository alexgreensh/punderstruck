# Comedy Theory Reference

> Created by Alex Greenshpun (10x Company / Co-Intelligent.ai)
> License: PolyForm Noncommercial 1.0.0. See LICENSE file in skill root.

**This file is the authoritative reference for comedy science, construction methodology, and craft techniques.**

## Why This Pipeline Exists

LLMs are fundamentally bad at humor. Not because they lack creativity, but because of how they work:

- **The prediction problem**: Language models generate the *most likely* next token. Humor requires the *least likely but retroactively logical* completion. These are opposite objectives.
- **EMNLP 2025 findings**: LLMs demonstrate "shallow pun understanding", they pattern-match to seen joke structures rather than discovering new phonetic collisions. When the pun word is replaced with a random word, LLMs still often classify it as a pun. (Source: "Pun Unintended," EMNLP 2025)
- **The LLM Repetition Problem**: ChatGPT generates the same ~25 jokes over and over. LLMs default to the most statistically likely joke pattern, which is the most overused one. (Source: WASSA 2023)
- **The Missing Violation Problem**: RLHF/instruction-tuning optimizes for inoffensiveness, which kills the "violation" in benign violation theory. Comedians described LLM output as "cruise ship comedy from the 1950s." (Source: DeepMind "Robot Walks into a Bar" 2024)
- **The Explanation Problem**: LLMs tend to generate puns AND then explain them, killing the cognitive reward of "getting it."
- **Columbia University research**: Explicit humor skills must be scaffolded externally. Prompting "be funny" just produces the average of all humor in training data, which is mediocre.

**The fix isn't better prompting. It's a structured pipeline that forces surprise.**

---

## The Three Science-Backed Humor Theories

### 1. The Surprise Equation (Incongruity-Resolution)

```
Humor = (Setup Expectation) × (Punchline Deviation) × (Retroactive Sense-Making)
```

All three factors must be present:

1. **Setup Expectation**: The audience's brain builds a mental model. "I used to be a banker..." → brain expects banking story.
2. **Punchline Deviation**: The punchline violates that model. "...but I lost interest." → wait, that's not about banking anymore.
3. **Retroactive Sense-Making**: The brain immediately sees the double path. "Lost interest" = banking term AND emotional state. The surprise resolves instantly.

If any factor is zero, the joke fails:
- No expectation → random nonsense (not funny)
- No deviation → predictable (not funny)
- No sense-making → confusing (not funny)

Dad jokes live in the sweet spot where deviation is LOW but sense-making is INSTANT. The groan IS the laugh.

### 2. Benign Violation Theory (Peter McGraw, Humor Research Lab)

Something is funny when it simultaneously (1) violates a norm and (2) seems benign/safe. Puns are **linguistic norm violations**, a word "shouldn't" mean two things at once. The violation is benign because the alternative meaning rescues it.

**Critical insight**: Surprise alone does NOT increase humor. Violations do. (Warren, Barsky, & McGraw) When surprising and violating stimuli are tested independently, violations win. Don't just aim for surprise. Aim for a genuine linguistic violation that the second meaning resolves.

### 3. Dual Activation Theory (Kao, Levy & Goodman, Cognitive Science 2015)

A pun's funniness requires TWO simultaneous properties:
- **Ambiguity**: Multiple meanings are equally plausible (high entropy)
- **Distinctiveness**: Those meanings are supported by DIFFERENT contextual words

Tested on 235 sentences: puns cluster in the HIGH ambiguity + HIGH distinctiveness space. **If one meaning dominates too heavily, the pun loses its punch.**

### The #1 Rule From Cognitive Science

**Both meanings must be TRUE AT THE SAME TIME in the context of the sentence.**

- Funny: "The teacher's favorite dessert was pi" (both pi/pie meanings are active simultaneously)
- Not funny: "What was the problem with the coat? Hard to put on with a paint roller" (coat-as-outerwear and coat-as-paint aren't both true simultaneously)

This is the single most reliable predictor of pun quality. (Source: fMRI research + validated across 150 Reddit posts)

---

## Joe Toplyn's Method (Adapted for Pun Construction)

Joe Toplyn (Emmy-winning comedy writer, *Comedy Writing for Late-Night TV*) uses a systematic approach to joke construction. Adapted for puns:

### Step A: Extract Handles

A "handle" is any concrete noun, verb, or concept associated with your topic. For "coffee":
- brew, bean, grind, espresso, filter, roast, drip, mug, cream, latte, barista, steam

**Principle**: More handles = more collision opportunities. Extract 5-8 minimum.

### Step B: Build Association Chains

For each handle, list words that sound similar OR share meaning in a different domain:
- bean → been (homophone, crosses into past tense / existence)
- grind → grinned (near-miss, crosses into emotion)
- filter → philter (archaic love potion, crosses into romance)
- brew → blew (homophone, crosses into destruction/wind)
- espresso → depresso (portmanteau, crosses into emotion)

### Step C: Measure Cognitive Distance

**The Cognitive Distance Principle**: The farther apart the two domains, the funnier the pun, up to a point.

```
Too Close          Sweet Spot              Too Far
|__________________|______________________|__________________|
"A baker            "I'm reading a book    "The quantum
 makes bread"        about anti-gravity.    decoherence of
 (not a joke)        Can't put it down."    my sandwich"
                     (everyone groans)       (nobody gets it)
```

Rate each sound-alike pair by domain distance:
- bean/been: coffee → grammar (medium distance), usable
- espresso/depresso: coffee → mental health (high distance), strong candidate
- filter/philter: coffee → medieval romance (very high distance), risky but rewarding if landed
- brew/blew: coffee → destruction (high distance), strong candidate

### Step D: Construct the Punchline First

**Critical Toplyn principle**: Write the punchline BEFORE the setup.

Take your highest-distance pair and build a sentence where BOTH meanings are active:
- "I've been so tired lately, I'm basically an espresso depresso."

### Step E: Write a Misdirecting Setup

The setup must:
1. Establish the FIRST meaning (the expected one)
2. Be under 2 sentences
3. Sound completely innocent

"I asked my barista how she's doing."
→ This primes the brain for coffee domain. The punchline then crosses to emotional domain.

### Step F: Verify the Double Path

Read the complete joke. Does the punchline genuinely work in BOTH domains simultaneously? If you have to squint, discard it.

---

## Cognitive Distance Spectrum (Visual Reference)

```
DOMAINS:
Food ←→ Emotions           = High distance (good)
Food ←→ Cooking            = Low distance (boring)
Tech ←→ Nature             = High distance (good)
Tech ←→ Computers          = Low distance (boring)
Business ←→ Warfare        = Medium distance (overused)
Business ←→ Marine Biology = High distance (fresh)
```

**Rule of thumb**: If both domains show up in the same Wikipedia article, the distance is too low.

---

## Craft Techniques (From Professional Comedy Writers)

### Greg Dean: Pun Word Placement
For standup/text puns: place the pun word at the END of the punchline, not in the setup. End on the word that triggers the reinterpretation. Everything after the reveal is wasted words.

### The "No Jokes in the Setup" Rule (Humor Blueprint)
"There are zero jokes in the premise. There are zero jokes in the setup. That's how you build tension." Every zinger in the setup softens the tension needed for the punchline to land. Setup establishes ONE meaning. Punchline reveals the second.

### Hard Consonant Sounds (K-Word Research)
Plosive consonants (K, hard C, hard G, P, T, B, D) are measurably funnier than soft sounds. Richard Wiseman's LaughLab: the joke rated funniest had the most K sounds. When choosing between two wordings, prefer harder consonants. "Duck" is funnier than "swan." "Pickle" beats "relish."

### Tim Vine's 15-Jokes-a-Day Method
Write 15 new jokes daily. Refine relentlessly, sometimes changing just ONE WORD transforms a dud into a winner. When generating multiple puns, vary the structure/rhythm between them to prevent "punchline fatigue."

### The Toplyn "Discard First" Principle
Discard your first few associations. The first is the most cliched. Push past the obvious. The third or fourth connection is where the good material lives. This is especially critical for AI: LLMs default to the most statistically likely association, which is the most overused.

### The Specificity Principle
Specific details are inherently funnier than vague ones. "A 1997 Honda Civic" is funnier than "a car." "Kalamazoo" is funnier than "a city." Specificity creates vivid mental images and adds absurd precision that enhances comedy. When building setups, use concrete, specific details over generic ones.

### Never Explain the Joke (Cognitive Science)
Explaining a pun short-circuits the "aha" dopamine reward. fMRI studies show two stages: comprehension (detecting incongruity) and elaboration (feeling amused). If you resolve the incongruity FOR the audience by explaining, the elaboration phase never fires. No "aha" = no amusement. If the pun needs explanation, it's not ready.

---

## The Dad Joke Calibration

Dad jokes are a specific subspecies of pun. Their DNA:

1. **Setup innocence**: The setup sounds like a genuine question or observation
2. **Punchline inevitability**: Once revealed, the pun feels like it was always there
3. **Zero mean-spiritedness**: The only victim is the English language
4. **Delivery commitment**: The joke is told WITH pride, not sheepishly

The groan is not failure. It's the intended response. A dad joke that gets a genuine laugh has actually failed at being a dad joke.

Research confirms: pun groans are APPROVAL signals, not disapproval. They acknowledge "I see what you did there" and serve as social bonding rituals. (Gibson & Sagarin, 2024)

---

## Observational Humor & Shower Thoughts

Observational humor is comedy drawn from everyday life, pointing out absurdities, contradictions, and oddities that people overlook. It shares DNA with puns: the best dad jokes are observational puns that find hidden wordplay in mundane situations.

> "I don't trust stairs. They're always up to something."

This is BOTH an observation (stairs go up) AND a pun ("up to something" = ascending + being suspicious). The intersection of observation and wordplay is where the strongest material lives.

### Shower Thought Patterns (Useful for Setup Construction)

These cognitive patterns generate the kind of unexpected angles that make great pun setups:

**Perspective Shift**: Look at a familiar situation from an unusual viewpoint (the object's, an alien's, a child's).
- "Your stomach thinks all potatoes are mashed."
- "Nothing is on fire. Fire is on things."

**Paradox Reframing**: Reveal a hidden logical contradiction we normally ignore.
- "If you drop soap on the floor, is the floor clean or is the soap dirty?"

**Literal Interpretation**: Take a metaphorical expression and interpret it literally.
- "I'm on a seafood diet. I see food, and I eat it."

**Scale Shift**: Zoom in to the microscopic or out to the cosmic.
- "If you weigh 99 lbs and eat a pound of nachos, are you 1% nacho?"

### How This Connects to Pun Construction

Use observational patterns to BUILD SETUPS, not punchlines. The observation creates the expectation; the pun violates it.

1. Start with an everyday observation about the topic
2. Find the hidden absurdity or contradiction
3. Frame it so the pun word resolves BOTH the observation and the wordplay

Example pipeline: Topic "calendar" → Observation: "calendars have numbered days" → Wordplay: "days are numbered" = countdown + mortality idiom → "I'm afraid for the calendar. Its days are numbered."

The observation gives the setup its natural, conversational tone. Without it, the setup sounds like a joke factory. With it, the pun feels discovered rather than constructed.
