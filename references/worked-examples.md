# Worked Examples: Full Pipeline Walkthroughs

> Created by Alex Greenshpun (10x Company / Co-Intelligent.ai)
> License: PolyForm Noncommercial 1.0.0. See LICENSE file in skill root.

## Example 1: `/punderstruck coffee`

### Step 1: SEED
API calls (parallel):
- icanhazdadjoke search "coffee" → "I like my coffee like I like my women. I don't like coffee."
- JokeAPI Pun contains=coffee → "What's the best Beatles song? Latte Be."
- Official Joke API random → "Why do Java developers wear glasses? Because they can't C#." (off-topic but useful structurally)

Mechanisms extracted:
- Joke 1: Subverted expectation (setup implies comparison, punchline negates)
- Joke 2: Homophone pun (Let It Be → Latte Be)
- Joke 3: Polysemy + tech jargon (C# = programming language + "see sharp")

### Step 2: ANALYZE
Seed joke #2 (Latte Be) is the strongest pun mechanism:
- **Type**: Phonetic near-miss (Let It → Latte)
- **Structure**: Question/answer
- **Misdirection**: "Best Beatles song" primes music domain, "Latte" crosses to coffee domain
- **Hinge phrase**: "Latte Be" carries both meanings

### Step 3: GENERATE
Handles extracted from "coffee": brew, bean, grind, espresso, filter, roast, drip, mug, cream, steam

Datamuse sounds-like results (parallel queries):
- bean → been, bin, keen, lean, mean, wean
- brew → blew, blue, clue, drew, flew, glue, grew, knew, new, threw, true
- grind → grinned, blind, bind, find, kind, mind, wind
- espresso → depresso (near-miss, not in Datamuse but discoverable via sl=espresso)
- filter → philter, falter, shelter, swelter
- roast → toast, boast, coast, ghost, host, most, post
- mug → bug, drug, dug, hug, lug, plug, rug, shrug, slug, snug, tug

Cognitive distance table (top pairs):
| Handle | Sound-alike | Domain Cross | Distance |
|--------|-------------|-------------|----------|
| espresso | depresso | coffee → mental health | HIGH |
| brew | blew | coffee → destruction/wind | HIGH |
| bean | been | coffee → grammar/existence | MEDIUM |
| grind | grinned | coffee → emotion | HIGH |
| mug | mug | coffee → crime/face | MEDIUM (polysemy) |
| filter | philter | coffee → medieval romance | VERY HIGH |
| roast | ghost | coffee → supernatural | HIGH |

Winner: espresso/depresso (highest distance + most instant recognition)

5 candidates constructed:

**Candidate 1** (espresso/depresso):
"What do you call a sad cup of coffee? A depresso."
- Double meaning: 5/5 (espresso is coffee, depresso = depressed, portmanteau is instant)
- Surprise: 3/5 (fairly well-known format but still lands)
- Groan-worthy: 4/5 (solid groan)
- Brevity: 5/5 (one-line Q&A)
- **Total: 17/20** ✓

**Candidate 2** (brew/blew):
"I tried to make coffee in the hurricane. The whole batch brew blew away."
- Double meaning: 4/5 (brew/blew works)
- Surprise: 3/5 (setup telegraphs it a bit)
- Groan-worthy: 3/5 (moderate)
- Brevity: 3/5 (could be tighter)
- **Total: 13/20** ✗

**Candidate 3** (grind/grinned):
"My coffee maker told me a joke this morning. It just sat there and grinned."
- Double meaning: 3/5 (grind/grinned is a stretch)
- Surprise: 4/5 (personification is unexpected)
- Groan-worthy: 3/5 (moderate)
- Brevity: 4/5 (clean two-liner)
- **Total: 14/20** ✓ (barely)

**Candidate 4** (mug polysemy):
"A coffee cup walked into a police station. It wanted to report a mugging."
- Double meaning: 5/5 (mug = cup AND crime)
- Surprise: 4/5 (police station misdirects from coffee)
- Groan-worthy: 5/5 (maximum groan)
- Brevity: 5/5 (tight setup)
- **Total: 19/20** ✓ WINNER

**Candidate 5** (filter/philter):
"I only date people who use pour-over. I need someone with a good philter."
- Double meaning: 4/5 (filter/philter works for word nerds)
- Surprise: 4/5 (dating + coffee is unexpected)
- Groan-worthy: 3/5 (too clever for some audiences)
- Brevity: 4/5 (clean)
- **Total: 15/20** ✓

### Step 4: CRITIQUE
Winner: Candidate 4 (mug/mugging) at 19/20.
- Polysemy pun (one word, two meanings)
- High cognitive distance (coffee → crime)
- Setup misdirects perfectly (police station primes crime domain)
- Punchline resolves both (mugging = being robbed + being a mug)

### Step 5: SERVE

```
╔══════════════════════════════════════╗
║  🃏  PUN TRADING CARD               ║
╠══════════════════════════════════════╣
║                                      ║
║  A coffee cup walked into a police   ║
║  station. It wanted to report a      ║
║  mugging.                            ║
║                                      ║
╠══════════════════════════════════════╣
║  Groan-o-meter: 😐😬😬😬🫠  (4/5)   ║
║  Type: Polysemy                      ║
║  Best Used At: Morning team standup  ║
║  Rarity: Rare                        ║
╚══════════════════════════════════════╝
```

*"I regret nothing and neither should you."*

---

## Example 2: `/punderstruck --roast marketing`

### Heat Level Selection
User picks: **Medium Roast** (pointed puns with a knowing wink)

### Step 1: SEED
- icanhazdadjoke search "marketing" → sparse results
- JokeAPI Pun contains=marketing → "Why did the marketer get fired? They kept trying to sell ice to penguins."

### Step 3: GENERATE (adapted for roast mode)
Handles: campaign, funnel, leads, conversion, brand, content, SEO, engagement, metrics, ROI, audience, click

Datamuse sounds-like (roast-relevant pairs):
- funnel → fun-nil (compound split: fun + nil = no fun)
- leads → leads (polysemy: sales leads vs. physically leads)
- brand → bland (near-miss, devastating at medium roast)
- content → content/discontent (polysemy)
- metrics → met-tricks (compound split)
- click → clique (homophone)
- ROI → "are oh why" (stretched, skip)

Roast candidates (medium heat):

**Candidate 1**: "Marketers are experts at driving engagement. Too bad their Tinder profiles can't say the same."
- Score: 16/20 ✓

**Candidate 2**: "What's the difference between a marketer and a magician? A magician knows when the trick isn't working."
- Score: 17/20 ✓

**Candidate 3**: "Marketers put the 'fun' in 'funnel.' Just kidding, there's no fun in funnels."
- Score: 15/20 ✓ WINNER (most on-brand for medium roast)

### Step 5: SERVE

```
╔══════════════════════════════════════╗
║  🃏  PUN TRADING CARD  [ROAST]      ║
╠══════════════════════════════════════╣
║                                      ║
║  Marketers put the "fun" in          ║
║  "funnel."                           ║
║                                      ║
║  Just kidding, there's no fun        ║
║  in funnels.                         ║
║                                      ║
╠══════════════════════════════════════╣
║  Groan-o-meter: 😐😬😬🫠🫠  (4/5)   ║
║  Type: Compound Split + Subversion   ║
║  Heat Level: ☕☕ Medium Roast        ║
║  Best Used At: Marketing all-hands   ║
║  Rarity: Uncommon                    ║
╚══════════════════════════════════════╝
```

*"That one hurt me too."*

---

## Example 3: `/punderstruck --translate "let's align on Q3 priorities"`

### Pipeline (Modified, Skip Step 1)

**Input phrase**: "Let's align on Q3 priorities"

**Handles extracted**: align, Q3, priorities, let's

**Datamuse sounds-like**:
- align → a-line (fashion), a lion (animal)
- priorities → prior-at-ease (stretch), pirate-ies (near-miss)
- Q3 → queue three, cutie, QB

**Best collision**: align → a lion (high cognitive distance: business → safari)

**Constructed translation**:
"Let's a-lion on Q3 priorities. Because this meeting is a jungle and someone needs to be king."

**Backup**: "Let's align on Q3 pirate-ies, plunder the budget before finance notices."

### Step 5: SERVE

```
╔══════════════════════════════════════╗
║  🃏  PUN TRADING CARD [TRANSLATED]  ║
╠══════════════════════════════════════╣
║                                      ║
║  CORPORATE: "Let's align on Q3      ║
║  priorities."                        ║
║                                      ║
║  TRANSLATED: "Let's a-lion on Q3    ║
║  priorities. Because this meeting    ║
║  is a jungle and someone needs       ║
║  to be king."                        ║
║                                      ║
╠══════════════════════════════════════╣
║  Groan-o-meter: 😐😬😬😬😬  (5/5)   ║
║  Type: Phonetic Near-Miss            ║
║  Best Used At: That meeting that     ║
║     should've been an email          ║
║  Rarity: Legendary                   ║
╚══════════════════════════════════════╝
```

*"My creator would like to formally apologize for nothing."*
