# Worked Examples: Full Pipeline Walkthroughs

> Created by Alex Greenshpun (10x Company / Co-Intelligent.ai)
> License: PolyForm Noncommercial 1.0.0. See LICENSE file in skill root.

**Purpose**: These walkthroughs show the INTERNAL pipeline process for calibration. Steps 1-4 happen silently via tool calls. Only Step 5 produces visible output.

**When loaded at runtime (fallback)**: Use the "CORRECT OUTPUT" sections as your delivery template. NEVER reproduce internal analysis in your response.

---

## Example 1: `/punderstruck coffee`

### Steps 1-4: INTERNAL PIPELINE (never shown to user)

**Step 1: SEED**
API calls (parallel):
- icanhazdadjoke search "coffee" -> "I like my coffee like I like my women. I don't like coffee."
- JokeAPI Pun contains=coffee -> "What's the best Beatles song? Latte Be."
- Official Joke API random -> "Why do Java developers wear glasses? Because they can't C#." (off-topic but useful structurally)

Mechanisms extracted:
- Joke 1: Subverted expectation (setup implies comparison, punchline negates)
- Joke 2: Homophone pun (Let It Be -> Latte Be)
- Joke 3: Polysemy + tech jargon (C# = programming language + "see sharp")

**Step 2: ANALYZE**
Seed joke #2 (Latte Be) is the strongest pun mechanism:
- **Type**: Phonetic near-miss (Let It -> Latte)
- **Structure**: Question/answer
- **Misdirection**: "Best Beatles song" primes music domain, "Latte" crosses to coffee domain
- **Hinge phrase**: "Latte Be" carries both meanings

**Step 3: GENERATE**
Handles extracted from "coffee": brew, bean, grind, espresso, filter, roast, drip, mug, cream, steam

Datamuse sounds-like results (parallel queries):
- bean -> been, bin, keen, lean, mean, wean
- brew -> blew, blue, clue, drew, flew, glue, grew, knew, new, threw, true
- grind -> grinned, blind, bind, find, kind, mind, wind
- espresso -> depresso (near-miss, discoverable via sl=espresso)
- filter -> philter, falter, shelter, swelter
- roast -> toast, boast, coast, ghost, host, most, post
- mug -> bug, drug, dug, hug, lug, plug, rug, shrug, slug, snug, tug

Cognitive distance table (top pairs):
| Handle | Sound-alike | Domain Cross | Distance |
|--------|-------------|-------------|----------|
| espresso | depresso | coffee -> mental health | HIGH |
| brew | blew | coffee -> destruction/wind | HIGH |
| bean | been | coffee -> grammar/existence | MEDIUM |
| grind | grinned | coffee -> emotion | HIGH |
| mug | mug | coffee -> crime/face | MEDIUM (polysemy) |
| filter | philter | coffee -> medieval romance | VERY HIGH |
| roast | ghost | coffee -> supernatural | HIGH |

Winner: mug (polysemy, highest instant recognition + both meanings independently valid)

**Step 4: CRITIQUE**
5 candidates scored on 5 criteria (1-5 each, /25). Minimum: 17/25 AND "Actually Funny" >= 3/5.

**Candidate 1** (espresso/depresso):
"What do you call a sad cup of coffee? A depresso."
- Effortless Activation: 5/5 (espresso -> depresso instant)
- Surprising Punchline: 3/5 (familiar format, still lands)
- Groan-Worthy: 4/5 (solid groan)
- Setup Brevity: 5/5 (one-line Q&A)
- Actually Funny: 4/5 (someone would tell this at brunch)
- **Total: 21/25** ✓

**Candidate 2** (brew/blew):
"I tried to make coffee in the hurricane. The whole batch brew blew away."
- Effortless Activation: 4/5 (brew/blew works)
- Surprising Punchline: 3/5 (setup telegraphs it)
- Groan-Worthy: 3/5 (moderate)
- Setup Brevity: 3/5 (could be tighter)
- Actually Funny: 2/5 (minimal reaction) **VETO: auto-eliminate**
- **Total: 15/25** ✗

**Candidate 3** (grind/grinned):
"My coffee maker told me a joke this morning. It just sat there and grinned."
- Effortless Activation: 3/5 (grind/grinned is a stretch)
- Surprising Punchline: 4/5 (personification unexpected)
- Groan-Worthy: 3/5 (moderate)
- Setup Brevity: 4/5 (clean two-liner)
- Actually Funny: 3/5 (gets a reaction in the right context)
- **Total: 17/25** ✓ (barely passes)

**Candidate 4** (mug polysemy):
"A coffee cup walked into a police station. It wanted to report a mugging."
- Effortless Activation: 5/5 (mug = cup AND crime)
- Surprising Punchline: 4/5 (police station misdirects from coffee)
- Groan-Worthy: 5/5 (maximum groan, physical recoil territory)
- Setup Brevity: 5/5 (tight setup, every word earns its place)
- Actually Funny: 5/5 (screenshot-and-send-to-three-friends level)
- **Total: 24/25** ✓ WINNER

**Candidate 5** (filter/philter):
"I only date people who use pour-over. I need someone with a good filter."
- Effortless Activation: 4/5 (coffee filter / personality filter, both active)
- Surprising Punchline: 4/5 (dating + coffee is unexpected)
- Groan-Worthy: 3/5 (too clever for some audiences)
- Setup Brevity: 4/5 (clean one-liner)
- Actually Funny: 3/5 (gets a reaction, niche audience)
- **Total: 18/25** ✓

Winner: Candidate 4 (mug/mugging) at 24/25.
- Polysemy pun (one word, two meanings)
- High cognitive distance (coffee -> crime)
- Setup misdirects perfectly (police station primes crime domain)
- Punchline resolves both (mugging = being robbed + being a mug)

### Step 5: CORRECT OUTPUT (what the user actually sees)

```
A coffee cup walked into a police station. It wanted to report a mugging.

A few more that were fighting for the spot:
What do you call a sad cup of coffee? A depresso.
I only date people who use pour-over. I need someone with a good filter.

I regret nothing and neither should you.
```

---

## Example 2: `/punderstruck --roast marketing`

### Heat Level Selection (pre-pipeline interaction)
User picks: **Medium Roast** (pointed puns with a knowing wink)

### Steps 1-4: INTERNAL PIPELINE (never shown to user)

**Step 1: SEED**
- icanhazdadjoke search "marketing" -> sparse results
- JokeAPI Pun contains=marketing -> "Why did the marketer get fired? They kept trying to sell ice to penguins."

**Step 3: GENERATE (adapted for roast, Steps 1-3 run normally per bonus-modes.md)**
Handles: campaign, funnel, leads, conversion, brand, content, SEO, engagement, metrics, ROI, audience, click

Datamuse sounds-like (roast-relevant pairs):
- funnel -> fun-nil (compound split: fun + nil = no fun)
- leads -> leads (polysemy: sales leads vs. physically leads)
- brand -> bland (near-miss, devastating at medium roast)
- content -> content/discontent (polysemy)
- metrics -> met-tricks (compound split)
- click -> clique (homophone)

**Step 4: CRITIQUE**
Roast candidates scored individually, then ARRANGED into monologue arc per bonus-modes.md structure (opener -> build -> callback -> mic drop).

**Candidate 1**: "Marketers are experts at driving engagement. Too bad their Tinder profiles can't say the same."
- Effortless Activation: 4/5, Surprising Punchline: 4/5, Groan-Worthy: 3/5, Setup Brevity: 4/5, Actually Funny: 4/5
- **Total: 19/25** ✓ (good opener energy)

**Candidate 2**: "You talk about 'conversion rates' like you're saving souls. Buddy, you're selling SaaS."
- Effortless Activation: 4/5, Surprising Punchline: 4/5, Groan-Worthy: 4/5, Setup Brevity: 4/5, Actually Funny: 4/5
- **Total: 20/25** ✓ (strong build material)

**Candidate 3**: "You put the 'fun' in 'funnel,' the 'con' in 'content,' and the 'pain' in 'campaign.'"
- Effortless Activation: 5/5, Surprising Punchline: 3/5, Groan-Worthy: 5/5, Setup Brevity: 5/5, Actually Funny: 4/5
- **Total: 22/25** ✓ (mic drop material, triple compound split)

Arranged: C1 energy in opener -> C2 in build -> callback to impressions -> C3 as mic drop.

### Step 5: CORRECT OUTPUT (what the user actually sees)

```
So you're in marketing. Your whole job is impressions, and honestly? You're not making a great one right now.

You talk about "conversion rates" like you're saving souls. Buddy, you're selling SaaS. Your funnel has more leaks than your strategy has layers, and the best conversion you've ever pulled off is convincing finance to approve another tool.

You put the "fun" in "funnel," the "con" in "content," and the "pain" in "campaign." And somehow, you're still asking for a bigger budget.
```

*Note: No sign-off for roasts. The mic drop IS the closer.*

---

## Example 3: `/punderstruck --translate "let's align on Q3 priorities"`

### Steps 1-4: INTERNAL PIPELINE (never shown to user)

**Pipeline modified: Skip Step 1 (SEED)**. The corporate phrase IS the seed material.

**Input phrase**: "Let's align on Q3 priorities"

**Handles extracted**: align, Q3, priorities, let's

**Datamuse sounds-like**:
- align -> a-line (fashion), a lion (animal)
- priorities -> prior-at-ease (stretch), pirate-ies (near-miss)
- Q3 -> queue three, cutie, QB

**Best collision**: align -> a lion (high cognitive distance: business -> safari)

**Constructed translation**:
"Let's a-lion on Q3 priorities. Because this meeting is a jungle and someone needs to be king."

**Backup**: "Let's align on Q3 pirate-ies, plunder the budget before finance notices."

### Step 5: CORRECT OUTPUT (what the user actually sees)

```
"Let's align on Q3 priorities."

...or as I heard it: "Let's a-lion on Q3 priorities." Because this meeting is a jungle and someone needs to be king.

(Backup in the holster: "Let's align on Q3 pirate-ies, plunder the budget before finance notices.")

My creator would like to formally apologize for nothing.
```
