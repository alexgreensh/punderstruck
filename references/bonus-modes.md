# Bonus Modes Reference

> Created by Alex Greenshpun (linkedin.com/in/alexgreensh)
> License: PolyForm Noncommercial 1.0.0. See LICENSE file in skill root.

---

## THE IMPRESSIVENESS BAR (Full Version)

Everything this skill produces must genuinely impress. Not "technically correct." Not "pretty good for AI." Actually sharp, actually witty, actually the kind of thing someone would screenshot and send to a friend.

**The Screenshot Test**: Would someone voluntarily share this with another person? Not because it's "cute" or "clever enough" but because it made them feel something: a groan, a laugh, a "holy shit that's good," a moment of genuine surprise.

---

## --roast [topic]

**This is a COMEDY ROAST, a performance piece, not a list of pun-zingers.**

Think Comedy Central Roast, not a pun encyclopedia. The output is a monologue with a narrative arc that a human could actually read at a team meeting and get laughs.

When roast mode is triggered, FIRST use AskUserQuestion to let the user pick their heat level:
**Question**: "Pick your roast level:"
1. **Light Roast ☕** | Playful wordplay, barely a tease. Grandma-safe.
2. **Medium Roast ☕☕** | Pointed puns with a knowing wink. Coworkers gasp-laugh.
3. **Dark Roast ☕☕☕** | Sharp and unapologetic. HR might overhear.
4. **Espresso Shot ☕☕☕☕** | One devastating concentrated line. Maximum damage per word.

### Joe Toplyn's Roast Association Technique

To generate a truly biting roast, do not rely on generic insults. You must use **Specific Associations**.

1. **List Associations:** Brainstorm specific, unflattering, or embarrassing associations with the target/profession.
   - *Target: Tech Bros* -> Associations: Patagonia vests, Soylent, avoiding eye contact, over-engineering simple problems, crypto crashes.
2. **Find the Punch Line Maker:** Find a Connector that links the target's normal trait to the unflattering association.
3. **Draft the Joke:** The setup states the target's normal trait. The punchline reveals the unflattering association using the Connector.

### The Roast Monologue Structure

Every roast (except Espresso) follows this arc:

**1. THE OPENER** (1-2 sentences): Address the topic/profession directly. Establish the comedian's persona.
**2. THE BUILD** (3-5 sentences): Each sentence escalates using Joe Toplyn's Association Technique. Sentences MUST CONNECT to each other. Use callbacks.
**3. THE CALLBACK** (1-2 sentences): Reference something from the opener or build.
**4. THE MIC DROP** (1 sentence): The closer. The hardest-hitting pun of the set.

**No sign-off after roasts.** The mic drop IS the closer.

---

## --standup [topic] (Stand-Up Routine Mode)

**This mode generates a full stand-up comedy bit (1-2 minutes of material).**

### Greg Dean's Routine Structure

A professional routine is not a list of disconnected jokes. It flows naturally.

1. **The Premise (The Setup):** Start with a broad, relatable observation about the topic.
2. **The Joke Mine (The Branches):** Explore 3-4 different angles of the premise using the 5 Mechanisms of Joke Structure.
3. **The Rule of Three:** List two normal things, then make the third thing the punchline.
4. **The Callback:** Near the end of the routine, reference the very first joke you made.
5. **5 LPM (Laughs Per Minute):** The routine must be dense. There should be a punchline or a tag every 2-3 sentences.

---

## --translate "[phrase]"

**Skips Step 1 (SEED).** The corporate phrase IS the seed material.

1. Take the input phrase directly
2. Extract handles from the corporate jargon words
3. Find the best phonetic collision. **The phonetic swap must carry the comedy.**
4. Rebuild the phrase using the sound-alike word, then extend the metaphor into a second sentence.

---

## --remix

**Skips Step 1 (SEED).** Takes a famous quote, lyric, movie line, or proverb.

**Input formats**: `--remix "To be or not to be"` (specific quote) or `--remix about philosophy` (skill picks a well-known quote from the topic).

**THE REMIX MUST CHANGE THE WORDS.** Non-negotiable. A remix that returns the original unchanged is a reframe, not a remix. Every remix must contain at least one phonetic swap, compound split, or word replacement.

---

## --compose [format] about [topic]

The Pun Composer. For when a single joke isn't enough.

**Supported formats**: `poem`, `limerick`, `haiku`, `paragraph`, `story`.

### LIMERICK CONSTRUCTION RULE: Build Backward from Line 5
The AABBA structure means line 5 IS the punchline. Place the highest-scoring pun candidate in line 5 FIRST, then construct lines 1-4 to escalate toward it.

### EVERY LINE MUST CARRY A REAL PUN
Every line must contain genuine wordplay (double meaning, phonetic collision, polysemy). No filler lines. No rhyme-only lines.

---

## Wordplay Mode

Triggered when the user asks for "wordplay on/about [word]".

**The difference**: Jokes have setups and punchlines. Wordplay manipulates THE WORD ITSELF.

### Wordplay Techniques
- **Prefix/suffix swap** (soup -> soup-er)
- **Idiom exploitation** ("in the soup")
- **Compound embedding** (soupsicion)
- **Homophone/sound play** (stock -> soup/finance)
- **Polysemy pivot** ("stock" = soup base AND financial shares)
