# Punderstruck Quality Eval

Date: 2026-03-28  
Evaluator: Codex, following the `skill-creator` workflow directly in Codex

## Scope

This eval covered two layers:

1. Structural strength
2. Actual joke quality under the live `SKILL.md` rubric

The scoring rubric used here is the current shipping rubric from `SKILL.md`:

- Effortless Activation
- Surprising Punchline
- Groan-Worthy
- Setup Brevity
- Actually Funny

Minimum passing score: `17/25`, with `Actually Funny >= 3/5`.

## Structural Checks

### 1. Skill shape

Command:

```sh
python3 ~/.codex/skills/skill-creator/scripts/quick_validate.py ./punderstruck
```

Result:

```text
Skill is valid!
```

### 2. SKILL.md length

Result:

```text
SKILL.md: 164 lines
pipeline-detailed.md: 136 lines
```

Verdict:

- Better than the previous long-form version
- Deterministic code moved into `scripts/datamuse_probe.py`
- Packaging now has a dedicated repo-local script: `scripts/build_package.py`

### 3. Rubric consistency

Finding:

- `SKILL.md` and `references/pipeline-detailed.md` were using different scoring criteria
- Fixed so both now use the same 5-criterion rubric

### 4. Packaging reality check

Command:

```sh
cd ~/.codex/skills/skill-creator/scripts
python3 package_skill.py /Users/alexgreenshpun/CascadeProjects/Prompts/Claude-Skills/punderstruck /tmp/punder_pkg
```

Observed issue:

```text
Added: punderstruck/punderstruck.zip
Added: punderstruck/.git
Added: punderstruck/evals/trigger-evals.json
```

Verdict:

- `skill-creator` validation passes
- default packager is too naive for clean public shipping
- repo-local `scripts/build_package.py` is the correct shipping path for this skill

## Quality Evals

## Test 1: Standard Topic

Prompt:

```text
/punderstruck marketing and AI
```

Probe command:

```sh
python3 scripts/datamuse_probe.py --topic "marketing and AI" --handle marketing --handle ai --handle funnel --handle model --handle lead --handle prompt --expand
```

Best raw material:

```text
funnel -> fennel
model -> medal
prompt -> primped
lead -> led
```

Served output:

```text
We asked our AI to make the funnel more organic. Now it just tastes like fennel.

A few more that were fighting for the spot:
The attribution model hit one KPI and immediately started wearing a medal.
We tightened the brand prompts so much the copy came back primped.

Want a meaner angle on marketing, AI, or both?
```

Score:

- Effortless Activation: 4
- Surprising Punchline: 4
- Groan-Worthy: 5
- Setup Brevity: 5
- Actually Funny: 4
- Total: `22/25`

Verdict: PASS

## Test 2: Roast Mode

Prompt:

```text
/punderstruck --roast consultants
```

Probe command:

```sh
python3 scripts/datamuse_probe.py --topic "consultants" --handle consultant --handle billable --handle deck --handle scope --handle workshop --handle strategy --expand
```

Best raw material:

```text
billable -> bailable
scope -> scoop
workshop -> work-shy
strategy -> strategery
```

Served output:

```text
So you're a consultant. Incredible. You can turn a two-sentence observation into a twelve-slide deck and still act like the arrows did the heavy lifting.

You call it a workshop because "work-shy" sounded too honest. Then you widen the scope until it becomes a scoop, rebrand common sense as strategery, and invoice the room for nodding on cue.

And somehow every shrug is billable. That's the whole framework: professionally formatted hesitation at premium rates.
```

Score:

- Effortless Activation: 4
- Surprising Punchline: 4
- Groan-Worthy: 4
- Setup Brevity: 4
- Actually Funny: 4
- Total: `20/25`

Verdict: PASS

## Test 3: Translate Mode

Prompt:

```text
/punderstruck --translate "let's circle back next quarter"
```

Probe command:

```sh
python3 scripts/datamuse_probe.py --topic "let's circle back next quarter" --handle circle --handle back --handle quarter --handle loop --handle followup --expand
```

Best raw material:

```text
followup -> foul up
quarter -> quart / court her
```

Served output:

```text
Let's foul up next quarter. Same delay, better branding, and finally an honest calendar invite.
```

Score:

- Effortless Activation: 4
- Surprising Punchline: 4
- Groan-Worthy: 4
- Setup Brevity: 5
- Actually Funny: 4
- Total: `21/25`

Verdict: PASS

## Test 4: Compose Mode

Prompt:

```text
/punderstruck --compose paragraph about CRM
```

Probe command:

```sh
python3 scripts/datamuse_probe.py --topic "CRM" --handle crm --handle customer --handle relationship --handle lead --handle pipeline --handle close --expand
```

Best raw material:

```text
close -> clothes
pipeline -> biplane
customer -> custom
lead -> led
```

Served output:

```text
The CRM promised a closer relationship with every lead, then showed up in clothes and called it personalization. The pipeline got so overengineered it looked less like rev ops and more like a biplane with quota anxiety. By the time sales said the account was custom, marketing was already calling her custom-her, which is still somehow the most intimate thing the platform has ever done.
```

Score:

- Effortless Activation: 4
- Surprising Punchline: 4
- Groan-Worthy: 4
- Setup Brevity: 3
- Actually Funny: 4
- Total: `19/25`

Verdict: PASS

## Test 5: Dad Joke Mode

Prompt:

```text
dad joke about sales ops
```

Probe command:

```sh
python3 scripts/datamuse_probe.py --topic "sales ops" --handle sales --handle ops --handle pipeline --handle quota --handle revops --expand
```

Best raw material:

```text
quota -> quote a
sales -> sails
revops -> rev up
```

Served output:

```text
What do you call a sales target that gives keynote speeches?

Quote-a.

I'll leave before RevOps asks for attribution.
```

Score:

- Effortless Activation: 4
- Surprising Punchline: 3
- Groan-Worthy: 5
- Setup Brevity: 5
- Actually Funny: 4
- Total: `21/25`

Verdict: PASS

## Test 6: Remix Mode

Prompt:

```text
/punderstruck --remix about AI
```

Probe command:

```sh
python3 scripts/datamuse_probe.py --topic "AI quote remix" --handle ai --handle model --handle prompt --handle future --handle machine --expand
```

Best raw material:

```text
ai -> eye / i / aye
prompt -> primped
model -> medal
future -> fewer / fuser
```

First draft:

```text
AI think, therefore AI am.
```

First-draft score:

- Effortless Activation: 3
- Surprising Punchline: 1
- Groan-Worthy: 2
- Setup Brevity: 5
- Actually Funny: 2
- Total: `13/25`

Verdict: FAIL

Revision served:

```text
Ask not what your prompt can do for you. Ask why it came back so primped.
```

Revised score:

- Effortless Activation: 3
- Surprising Punchline: 4
- Groan-Worthy: 4
- Setup Brevity: 4
- Actually Funny: 3
- Total: `18/25`

Verdict: PASS, but weakest passing mode in this batch

## Summary

Passes:

- Standard topic
- Roast
- Translate
- Compose paragraph
- Dad joke
- Remix after one forced revision

What the scoring system proved:

- It caught a lazy, obvious remix and rejected it
- It pushed the rewrite into a better second draft
- The strongest current modes are standard-topic, roast, and translate
- The weakest current mode in this batch is remix, which likely needs more worked examples

## Recommended Next Moves Before Shipping

1. Keep the new `scripts/build_package.py` and use it for shipping, not the stock `skill-creator` packager.
2. Consider adding one more worked example for `--remix`, since that mode was the easiest to default into obvious material.
3. Keep `SKILL.md` roughly at its current size. It is now short enough to load cleanly while still explaining the mode system.
