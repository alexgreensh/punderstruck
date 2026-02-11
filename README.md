<p align="center">
  <img src="assets/punderstruck-logo.png" alt="Punderstruck Logo" width="120" />
</p>

<h1 align="center">Punderstruck</h1>

<p align="center">
  <em>Because your AI deserves better material.</em>
</p>

<p align="center">
  <img src="assets/punderstruck-hero.png" alt="Punderstruck Hero" width="600" />
</p>

---

## What Is This?

Most AI pun generators pull from a stale database of jokes your uncle already forwarded in 2019. Punderstruck takes a different approach entirely.

It's a Claude Code skill that *discovers* puns in real time using the [Datamuse API](https://www.datamuse.com/api/) for phonetic analysis, combined with Joe Toplyn's comedy construction methodology. Every pun is built from scratch, scored against five quality criteria, and delivered only if it clears a 17/25 bar.

No recycled jokes. No "why did the chicken" energy. Just genuinely sharp wordplay, built live, every time.

## How It Works (The Short Version)

You give it a topic. It extracts "handles" (the words that matter), queries Datamuse for sound-alikes and homophones, analyzes the collision space for cognitive distance, constructs punchlines using comedy theory, scores them ruthlessly, and serves only the survivors.

You see none of that. You just get the pun.

## Modes

Punderstruck ships with a bunch of ways to get creative:

| Command | What Happens |
|---------|-------------|
| `/punderstruck` | Random pun, full pipeline, no topic constraint |
| `/punderstruck [topic]` | Focused puns on your topic |
| `/punderstruck --roast [topic]` | Pun-based roasts (it asks your preferred heat level first) |
| `/punderstruck --translate "[phrase]"` | Turns corporate jargon into wordplay |
| `/punderstruck --remix` | Famous quotes and lyrics, rebuilt as puns |
| `/punderstruck --compose [format] about [topic]` | Longer-form compositions (limericks, haiku, sonnets, you name it) |
| `/punderstruck --explain` | Delivers the pun, then dissects the comedy mechanics |
| `brainstorm puns for...` | Collaborative pun consulting for your projects |
| `shower thought about [topic]` | Those 2am "wait, actually..." observations |
| `wordplay on [word]` | Manipulates the word itself, phonetically and structurally |

Flags combine freely. Go wild.

## Sample Output

**Standard mode** (`/punderstruck AI`):

> I asked my AI to lose some parameters, but it told me to weight.

**Compose mode** (`/punderstruck --compose limerick about sales`):

> A sales rep obsessed with her funnel,
> Tried closing through some kind of tunnel.
> She said with a grin,
> "I'm piping them in!"
> Now her pipeline's become departmental.

**Roast mode** (`/punderstruck --roast consultants`):

> Consultants don't solve problems. They just bill by the our.

## The Personality

Punderstruck has swagger. It takes the *craft* seriously but never itself. Think: the funniest person at the dinner party who also happens to have studied comedy theory. Sassy, warm, slightly unhinged. If a pun is a stretch, it owns that stretch with confidence, not apology.

## Quality Control

Every pun runs through a five-criteria scoring system:

1. **Effortless Activation** — Does the double meaning land instantly?
2. **Surprising Punchline** — Did you see it coming? (You shouldn't have.)
3. **Groan-Worthy** — The good kind of groan. The involuntary one.
4. **Setup Brevity** — Short setups hit harder. Target: 8-20 words.
5. **Actually Funny** — This one has veto power. Score below 3/5 and the pun is eliminated, no exceptions.

Minimum to serve: **17/25**. If nothing passes, the skill digs deeper rather than serving mediocre material.

## Requirements

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (Claude's agentic coding tool)
- Internet access (for Datamuse API calls)
- A willingness to groan

## Installation

Download this repo and add it as a skill in Claude Code. The SKILL.md file contains the full instruction set, and the `references/` folder has the comedy theory, pipeline details, and taxonomy that make it all work.

## Project Structure

```
punderstruck/
├── SKILL.md                          # The main skill prompt
├── README.md                         # You are here
├── LICENSE                           # Proprietary - personal use only
├── assets/
│   ├── punderstruck-hero.png         # Hero image
│   └── punderstruck-logo.png         # Logo
└── references/
    ├── pipeline-detailed.md          # Full pun construction pipeline
    ├── bonus-modes.md                # Roast, translate, remix, compose specs
    ├── comedy-theory.md              # Joe Toplyn method + theory foundations
    ├── pun-taxonomy.md               # Classification of pun mechanisms
    └── worked-examples.md            # Scored examples for calibration
```

## Built By

**Alex Greenshpun** — AI Strategist, former VP of Marketing, and someone who believes AI should amplify human creativity, not replace it. When she's not building AI-augmented marketing systems at [10x Company](https://the10xcompany.ai), she's apparently teaching Claude how to be funnier.

- [LinkedIn](https://linkedin.com/in/alexgreensh)
- [10x Company](https://the10xcompany.ai)

## License

Proprietary — Personal use only. See [LICENSE](LICENSE) for details.

---

<p align="center">
  <em>Made with equal parts comedy theory and questionable life choices.</em>
</p>
