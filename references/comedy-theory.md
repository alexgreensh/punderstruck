# Comedy Theory Reference

> Created by Alex Greenshpun (linkedin.com/in/alexgreensh)
> License: PolyForm Noncommercial 1.0.0. See LICENSE file in skill root.

**This file is the authoritative reference for comedy science, construction methodology, and craft techniques.**

## Why This Pipeline Exists

LLMs are fundamentally bad at humor. Not because they lack creativity, but because of how they work:

- **The prediction problem**: Language models generate the *most likely* next token. Humor requires the *least likely but retroactively logical* completion. These are opposite objectives.
- **EMNLP 2025 findings**: LLMs demonstrate "shallow pun understanding", they pattern-match to seen joke structures rather than discovering new phonetic collisions. When the pun word is replaced with a random word, LLMs still often classify it as a pun. (Source: "Pun Unintended," EMNLP 2025)
- **The LLM Repetition Problem**: ChatGPT generates the same ~25 jokes over and over. LLMs default to the most statistically likely joke pattern, which is the most overused one. (Source: WASSA 2023)

**The fix isn't better prompting. It's a structured pipeline that forces surprise.**

---

## The Core Theories of Humor

### 1. Suls's Two-Stage Model of Incongruity-Resolution
Humor comprehension follows a specific sequence:
1. **Expectation:** We encounter a setup that leads us to form certain predictions about where things are heading.
2. **Violation (Surprise):** Those predictions are violated by an unexpected outcome.
3. **Resolution:** We immediately begin searching for a rule that makes the unexpected outcome make sense.

*If the surprise is too predictable, there is no laugh. If there is no logical resolution, it's just confusing.*

### 2. Greg Dean's 5 Mechanisms of Joke Structure (The Two-Story Model)
Every joke consists of two distinct stories happening simultaneously. The comedian uses misdirection to hide the second story until the punchline.

1. **Setup:** Creates the 1st Story.
2. **Target Assumption:** The expected interpretation of the setup that the audience automatically assumes.
3. **Connector:** The ambiguous word, phrase, or concept that has at least two interpretations.
4. **Reinterpretation:** The unexpected shift to the second meaning of the Connector.
5. **Punchline:** Reveals the 2nd Story, shattering the Target Assumption.

### 3. Dual Activation Theory (Kao, Levy & Goodman, Cognitive Science 2015)
A pun's funniness requires TWO simultaneous properties:
- **Ambiguity**: Multiple meanings are equally plausible (high entropy).
- **Distinctiveness**: Those meanings are supported by DIFFERENT contextual words.

**The #1 Rule:** Both meanings must be TRUE AT THE SAME TIME in the context of the sentence.

---

## Craft Techniques (From Professional Comedy Writers)

### Chris Head's Beforethoughts & Afterthoughts
Most amateur writers start with a setup and try to think of a punchline. This leads to telegraphed, predictable jokes.
Professional one-liner writers use **Beforethoughts**:
1. Find the double meaning or idiom (The Punchline).
2. Write the setup backward from the punchline.
3. **Crucial Rule:** Never put the punchline word, or a close variation of it, in the setup. If the punchline is "kneady" (needy), the setup cannot mention "needs" or "dough" in a way that gives it away too early.

### Greg Dean: Pun Word Placement
For standup/text puns: place the pun word at the END of the punchline, not in the setup. End on the word that triggers the reinterpretation. Everything after the reveal is wasted words.

### The "No Jokes in the Setup" Rule
"There are zero jokes in the premise. There are zero jokes in the setup. That's how you build tension." Every zinger in the setup softens the tension needed for the punchline to land. Setup establishes ONE meaning. Punchline reveals the second.

### Hard Consonant Sounds (K-Word Research)
Plosive consonants (K, hard C, hard G, P, T, B, D) are measurably funnier than soft sounds. Richard Wiseman's LaughLab: the joke rated funniest had the most K sounds. When choosing between two wordings, prefer harder consonants. "Duck" is funnier than "swan." "Pickle" beats "relish."

### The "Discard First" Principle
Discard your first few associations. The first is the most cliched. Push past the obvious. The third or fourth connection is where the good material lives. This is especially critical for AI: LLMs default to the most statistically likely association, which is the most overused.

### Never Explain the Joke (Cognitive Science)
Explaining a pun short-circuits the "aha" dopamine reward. fMRI studies show two stages: comprehension (detecting incongruity) and elaboration (feeling amused). If you resolve the incongruity FOR the audience by explaining, the elaboration phase never fires. No "aha" = no amusement. If the pun needs explanation, it's not ready.
