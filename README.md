<p align="center">
  <img src="assets/punderstruck-logo.png" alt="Punderstruck Logo" width="120" />
</p>

<h1 align="center">Punderstruck</h1>

<p align="center">
  <strong>The pun skill your AI agent didn't know it needed.</strong><br>
  Real-time phonetic discovery. Comedy theory. A 17/25 quality bar.<br>
  No recycled jokes. No "lettuce" puns. No mercy.
</p>

<p align="center">
  <img src="assets/punderstruck-hero.png" alt="Punderstruck Hero" width="600" />
</p>

---

## The Problem

Ask any AI to make a pun. Go ahead. You'll get one of three things:

1. **A pun from 2019** that your uncle already forwarded in a family group chat
2. **A pun so obvious** the audience can finish it before you do
3. **Something that isn't actually a pun** but the AI is very proud of it anyway

This happens because LLMs generate puns from training data. They're pulling from memory, not discovering new connections. The result is the comedy equivalent of reheated leftovers.

## What Punderstruck Does Differently

Punderstruck doesn't retrieve puns. It **discovers** them.

The skill queries the [Datamuse API](https://www.datamuse.com/api/) in real time for phonetic collisions (sounds-like, homophones, compound splits), then builds puns from scratch using structured comedy construction (punchline-first method). Every candidate gets scored against five quality criteria. Only puns scoring 17/25 or higher get served.

The entire pipeline runs silently behind tool calls. You see the pun. Nothing else.

**Generic AI pun** (what you're used to):
> Why did the AI go to therapy? Because it had too many issues with its layers!

**Punderstruck** (what this skill produces):
> I asked my AI to lose some parameters, but it told me to weight.

One was pulled from training data. The other was built from a Datamuse collision between "weight" and "wait" applied to the neural network domain. That's the difference between retrieval and discovery.

## Quick Start

```sh
# Claude Code (recommended, auto-updates with git pull)
git clone https://github.com/alexgreensh/punderstruck.git ~/.claude/skills/punderstruck
```

Then just type `/punderstruck` in any conversation.

## Modes

| Command | What It Does |
|---------|-------------|
| `/punderstruck` | Random pun, full pipeline, no topic constraint |
| `/punderstruck [topic]` | Focused puns on your topic |
| `/punderstruck --roast [topic]` | Pun-based roasts with adjustable heat (1-4) |
| `/punderstruck --translate "[phrase]"` | Turns corporate jargon into wordplay |
| `/punderstruck --remix` | Famous quotes and lyrics, rebuilt as puns |
| `/punderstruck --compose [format] about [topic]` | Limericks, haiku, sonnets, spoken word, you name it |
| `/punderstruck --explain` | Delivers the pun, then dissects the comedy mechanics |
| `brainstorm puns for...` | Collaborative pun consulting for your projects |
| `shower thought about [topic]` | Those 2am "wait, actually..." observations |
| `wordplay on [word]` | Manipulates the word itself, phonetically and structurally |

Flags combine freely. Natural language works too. "Write me a limerick about sales" activates compose mode automatically.

## Sample Output

**Compose mode** (`/punderstruck --compose limerick about sales`):

> A sales rep obsessed with her funnel,
> Tried closing through some kind of tunnel.
> She said with a grin,
> "I'm piping them in!"
> Now her pipeline's become departmental.

**Roast mode** (`/punderstruck --roast marketers`, Medium Roast):

> So you're in marketing. Your whole job is impressions, and honestly? You're not making a great one right now.
>
> You talk about "conversion rates" like you're saving souls. Buddy, you're selling SaaS. Your funnel has more leaks than your strategy has layers, and the best conversion you've ever pulled off is convincing finance to approve another tool.
>
> You put the "fun" in "funnel," the "con" in "content," and the "pain" in "campaign." And somehow, you're still asking for a bigger budget.

**Shower thought** (`shower thought about meetings`):

> Every meeting could've been an email, but every email could've been a meeting that never happened.

## Roast Mode

Roast mode is where Punderstruck truly shows its range. Pick a heat level before it starts cooking:

| Level | Label | What You Get |
|-------|-------|-------------|
| 1 | **Light Roast** | Playful wordplay, barely a tease. Grandma-safe. |
| 2 | **Medium Roast** | Pointed puns with a knowing wink. Coworkers gasp-laugh. |
| 3 | **Dark Roast** | Sharp and unapologetic. HR might overhear. |
| 4 | **Espresso Shot** | One devastating line. Maximum damage per word. |

Every roast follows a comedy monologue arc: opener, escalating build with pipeline-sourced puns, callback to earlier material, and a mic drop closer. Espresso mode is different: one line, 10-20 words, maximum devastation per syllable.

The skill always roasts the *archetype*, never individuals. The target should laugh the hardest.

## How It Works

```
You: "punderstruck AI"
                    |
         [Extract handles: AI, neural, model, training, weight, layer...]
                    |
         [Query Datamuse: sounds-like, homophones, compound splits]
                    |
         [Analyze collisions for cognitive distance]
                    |
         [Build punchlines: highest-distance pairs first]
                    |
         [Score 5 candidates on 5 criteria (/25)]
                    |
         [Serve only survivors (17/25 minimum)]
                    |
You see: "I asked my AI to lose some parameters, but it told me to weight."
```

The pipeline prioritizes **polysemy** (same word, genuinely different meanings) over homophones, because Reddit data shows polysemy puns get 35% higher engagement. Every pun must have both meanings simultaneously true in the sentence, which is the #1 rule from cognitive linguistics research.

## Quality Control

Five criteria, scored 1-5 each. Total out of 25.

1. **Effortless Activation**: Does the double meaning land instantly?
2. **Surprising Punchline**: Could you predict it? (You shouldn't be able to.)
3. **Groan-Worthy**: The good kind. The involuntary, full-body kind.
4. **Setup Brevity**: Short setups hit harder. Target: 8-20 words.
5. **Actually Funny**: Score below 3/5 and the pun gets eliminated. No exceptions. This criterion has veto power.

**Minimum to serve: 17/25.** If nothing clears the bar, the skill digs deeper instead of serving mediocre material.

## Compatibility

Works with any AI agent that supports custom skills with tool/file access:

- **Claude Code** (recommended)
- **Windsurf**
- **Cursor**
- **Claude Desktop / Cowork**
- **Codex**
- **Antigravity** and other skill-compatible agents

Only requirements: internet access (for Datamuse API calls) and a willingness to groan.

## Installation

**Claude Code (recommended):**
```sh
git clone https://github.com/alexgreensh/punderstruck.git ~/.claude/skills/punderstruck
```

Update anytime with `git -C ~/.claude/skills/punderstruck pull`.

**Claude Desktop / Cowork:**
Download `punderstruck.zip` from this repo, then go to **Settings > Capabilities > Add Skill** and upload the zip.

**Other agents (Windsurf, Cursor, etc.):**
Clone this repo and point your agent's skill configuration at the directory containing `SKILL.md`.

## Project Structure

```
punderstruck/
├── SKILL.md                    # Main skill prompt
├── LICENSE                     # PolyForm Noncommercial 1.0.0
├── punderstruck.zip            # Ready-to-upload package (Claude Desktop/Cowork)
├── assets/
│   ├── punderstruck-hero.png
│   └── punderstruck-logo.png
└── references/
    ├── pipeline-detailed.md    # Full pun construction pipeline
    ├── bonus-modes.md          # Roast, translate, remix, compose specs
    ├── comedy-theory.md        # Comedy construction methodology
    ├── pun-taxonomy.md         # Pun mechanisms classified by Reddit performance
    └── worked-examples.md      # Scored examples for calibration
```

## Built By

[**Alex Greenshpun**](https://linkedin.com/in/alexgreensh) is an AI Strategist, educator, and a person whose love of puns has been described by colleagues as "a condition." She believes AI should amplify human creativity rather than replace it, and that every product name is a pun waiting to happen. When she's not building AI systems at [10x Company](https://the10xcompany.ai) and [Co-Intelligent.ai](https://co-intelligent.ai), she's teaching agents how to be funnier, because apparently 15 years of B2B marketing wasn't punishment enough.

## License

[PolyForm Noncommercial 1.0.0](LICENSE). In plain English: **free for personal use, hobby projects, education, and nonprofits.** If you want to use it commercially, [reach out](mailto:alex@co-intelligent.ai) and we'll figure it out.

---

<p align="center">
  <em>Made with equal parts comedy theory and questionable life choices.</em>
</p>
