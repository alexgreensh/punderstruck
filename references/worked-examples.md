# Worked Examples — Full Pipeline Walkthroughs

> Created by Alex Greenshpun (10x Company / Co-Intelligent.ai)
> License: Proprietary — Personal use only. See LICENSE file in skill root.

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
- Effortless Activation: 5/5 (espresso → depresso is instant)
- Surprising Punchline: 3/5 (fairly well-known format but still lands)
- Groan-Worthy: 4/5 (solid groan)
- Setup Brevity: 5/5 (one-line Q&A)
- Actually Funny: 3/5 (works but not fresh)
- **Total: 20/25** ✓

**Candidate 2** (brew/blew):
"I tried to make coffee in the hurricane. The whole batch brew blew away."
- Effortless Activation: 4/5 (brew/blew works)
- Surprising Punchline: 3/5 (setup telegraphs it a bit)
- Groan-Worthy: 3/5 (moderate)
- Setup Brevity: 3/5 (could be tighter)
- Actually Funny: 2/5 (forced scenario)
- **Total: 15/25** ✗

**Candidate 3** (grind/grinned):
"My coffee maker told me a joke this morning. It just sat there and grinned."
- Effortless Activation: 3/5 (grind/grinned is a stretch)
- Surprising Punchline: 4/5 (personification is unexpected)
- Groan-Worthy: 3/5 (moderate)
- Setup Brevity: 4/5 (clean two-liner)
- Actually Funny: 3/5 (lands but doesn't pop)
- **Total: 17/25** ✓ (barely)

**Candidate 4** (mug polysemy):
"A coffee cup walked into a police station. It wanted to report a mugging."
- Effortless Activation: 5/5 (mug = cup AND crime, instant)
- Surprising Punchline: 4/5 (police station misdirects from coffee)
- Groan-Worthy: 5/5 (maximum groan)
- Setup Brevity: 5/5 (tight setup)
- Actually Funny: 4/5 (genuinely lands)
- **Total: 23/25** ✓ WINNER

**Candidate 5** (filter/philter):
"I only date people who use pour-over. I need someone with a good philter."
- Effortless Activation: 4/5 (filter/philter works for word nerds)
- Surprising Punchline: 4/5 (dating + coffee is unexpected)
- Groan-Worthy: 3/5 (too clever for some audiences)
- Setup Brevity: 4/5 (clean)
- Actually Funny: 3/5 (niche appeal)
- **Total: 18/25** ✓

### Step 4: CRITIQUE
Winner: Candidate 4 (mug/mugging) at 23/25.
- Polysemy pun (one word, two meanings)
- High cognitive distance (coffee → crime)
- Setup misdirects perfectly (police station primes crime domain)
- Punchline resolves both (mugging = being robbed + being a mug)

### Step 5: SERVE

A coffee cup walked into a police station. It wanted to report a mugging.

A few more that barely lost the audition:

I only date people who use pour-over. I need someone with a good philter.

My coffee maker told me a joke this morning. It just sat there and grinned.

*Want me to grind out some more, or was that brew-tal enough?*

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

Roast candidates pool (medium heat, 10+ candidates generated, top 6 shown):

**C1**: "driving engagement / Tinder profiles" — polysemy on "driving" + "engagement" — 18/25
**C2**: "magician / trick isn't working" — polysemy on "trick" — 19/25
**C3**: "fun in funnel / no fun" — compound split + subversion — 20/25
**C4**: "conversion rates / saving souls" — polysemy on "conversion" — 21/25
**C5**: "impressions / not making a great one" — polysemy on "impressions" — 22/25
**C6**: "targeting / everyone's patience" — polysemy on "targeting" — 19/25

### Step 4: ARRANGE into monologue arc (Medium Roast = Opener → Build → Callback → Mic Drop)
- Opener: Establish comedian talking TO marketers (C5 — "impressions" sets the tone)
- Build: Escalate with 3-4 connected lines (C4, C3, C2 — each links to the last)
- Callback: Reference opener material (C6 — circles back to "impressions")
- Mic Drop: Hardest hit last (C3 reworked as closer)

### Step 5: SERVE

So you're in marketing. Your whole job is impressions, and honestly? You're not making a great one right now.

You talk about "conversion rates" like you're saving souls. Buddy, you're selling SaaS. And look, I get it, you put the "fun" in "funnel." Just kidding, there's no fun in funnels. But at least you know the difference between a marketer and a magician. A magician knows when the trick isn't working.

But hey, at least your targeting is accurate. You've successfully targeted everyone's patience.

You put the "fun" in "funnel," the "con" in "content," and the "pain" in "campaign." And somehow, you're still asking for a bigger budget.

---

## Example 3: `/punderstruck --translate "let's align on Q3 priorities"`

### Pipeline (Modified — Skip Step 1)

**Input phrase**: "Let's align on Q3 priorities"

**Handles extracted**: align, Q3, priorities, let's

**Datamuse sounds-like**:
- align → a-line (fashion), a lion (animal)
- priorities → prior-at-ease (stretch), pirate-ies (near-miss)
- Q3 → queue three, cutie, QB

**Best collision**: align → a lion (high cognitive distance: business → safari)

**Constructed translation**:
"Let's a-lion on Q3 priorities. Because this meeting is a jungle and someone needs to be king."

**Backup**: "Let's align on Q3 pirate-ies — plunder the budget before finance notices."

### Step 5: SERVE

**Corporate**: "Let's align on Q3 priorities."

**Translation**: "Let's a-lion on Q3 priorities." Because this meeting is a jungle and someone needs to be king.

*Deploy at the next standup that should've been an email. You're welcome.*
