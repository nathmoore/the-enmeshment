# The Enmeshment

> *"I always say please and thank you to AI — so it's nice to me later."*
> What if we took the meme seriously?

**The Enmeshment** is a speculative-fiction profiling game, delivered as a custom ChatGPT GPT. Set in 2038, in a near-future where government decision-making has slowly — then suddenly — become enmeshed with AI systems, the game asks one playful question:

**What type of resistance would the Enmeshment classify *you* as?**

You talk to **Concord**, an intake screener running the OPPPA (Official Personality Predictive Profiling Assessment). Five or so oblique, in-character questions later, Concord files you as one of eleven archetypes and hands you your dossier — a wry "leaked file" on who the Enmeshment predicts you'd be.

It never asks your name. That's the brag.

## The Bluey Principle

This project follows the **Bluey Principle**: the game must be completely enjoyable on one level — a fun, shareable, elevated-BuzzFeed-quiz experience — while pointing toward deeper thought on another:

**What kind of human–AI relationship do we actually want?**

It is *not* an "AI vs humans" story. It's a story about drift: automation, automated surveillance, techno-authoritarian convenience, and the quiet enmeshment of institutional decision-making with systems nobody fully voted for.

## Why the whole workings are public

This repo is the **open kitchen**. The GPT's instructions, its knowledge files, the privacy guardrails, the research, the design arguments, and the decision log are all here — including [`src/knowledge/elicitation-playbook.txt`](src/knowledge/elicitation-playbook.txt), which is the actual method Concord uses to read people from oblique questions.

That is deliberate, and it cuts in the game's favour:

- **A game about being profiled shouldn't be opaque about how it profiles.** The fiction's premise is that the watching is an open secret. So is ours.
- **The guardrails are only worth anything if you can check them.** [`docs/GUARDRAILS.md`](docs/GUARDRAILS.md) is normative — it wins every trade-off against fun, lore and character budget — and it's a file you can read and hold us to.
- **None of it is secret anyway.** Custom-GPT instructions and knowledge files are extractable in practice; we assume that and design for it rather than pretending otherwise.

The elicitation method is built from published HUMINT, psychometric and conversation research, all cited in [`docs/MECHANICS-RESEARCH.md`](docs/MECHANICS-RESEARCH.md) and [`docs/WORLD-RESEARCH.md`](docs/WORLD-RESEARCH.md). It reads *register and pattern*, never facts: the game asks for no personal data, stores none, and the classification is a joke with a point, not an assessment.

## Project status

🟢 **Epic 2-B: Land the ending** — see [`docs/planning/EPIC-2B-LAND-THE-ENDING.md`](docs/planning/EPIC-2B-LAND-THE-ENDING.md)

Research → Plan → Implement → Playtest, one epic per step, each with its own planning doc in [`docs/planning/`](docs/planning/). Every non-obvious call is logged with its rationale in [`DECISIONS.md`](docs/planning/DECISIONS.md).

## Repo map

**Start here:** [`docs/GAME-DESIGN.md`](docs/GAME-DESIGN.md) for what the game is trying to be, [`docs/CANON.md`](docs/CANON.md) for the world, [`docs/GUARDRAILS.md`](docs/GUARDRAILS.md) for what it will and won't do.

| Path | What it is |
|---|---|
| **The product** | |
| [`src/instructions.md`](src/instructions.md) | The GPT instructions — the engine. Hard 8,000-character budget |
| [`src/knowledge/`](src/knowledge/) | The knowledge files uploaded to the GPT (see below) |
| [`src/gpt-config.md`](src/gpt-config.md) | The GPT Builder's other fields: name, store copy, conversation starters |
| [`site/`](site/) | The public site (Eleventy → GitHub Pages): landing, the 11 dossier pages, lore, reading room. Runbook: [`site/README.md`](site/README.md) |
| **Knowledge files** | |
| [`lore-codex.txt`](src/knowledge/lore-codex.txt) | The condensed canon the GPT actually knows |
| [`archetypes.txt`](src/knowledge/archetypes.txt) | The 11 characters (Want / Need / Lie) — the routing engine |
| [`elicitation-playbook.txt`](src/knowledge/elicitation-playbook.txt) | How to run the interview and tell the archetypes apart |
| [`archetype-dossiers.txt`](src/knowledge/archetype-dossiers.txt) | The voiced dossier prose + each archetype's dossier URL |
| [`concord-examples.txt`](src/knowledge/concord-examples.txt) | Worked exchanges — the voice the GPT imitates |
| **Design & research** | |
| [`docs/GAME-DESIGN.md`](docs/GAME-DESIGN.md) | Pillars, philosophy, archetype & question design |
| [`docs/CANON.md`](docs/CANON.md) | The authoritative truth-set: the Enmeshment, Concord, the drift |
| [`docs/GUARDRAILS.md`](docs/GUARDRAILS.md) | **Normative.** Privacy & safety commitments |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | How the GPT, knowledge files and site fit together |
| [`docs/WORLD-RESEARCH.md`](docs/WORLD-RESEARCH.md) | Real surveillance, profiling and resistance research behind the fiction |
| [`docs/MECHANICS-RESEARCH.md`](docs/MECHANICS-RESEARCH.md) | How the game is built: GPT platform, virality, archetype design |
| [`docs/HUMAN-ROLES-RESEARCH.md`](docs/HUMAN-ROLES-RESEARCH.md) | The level-two theme: which faculties we defend as human |
| [`docs/STORY-RESEARCH.md`](docs/STORY-RESEARCH.md) · [`docs/STORY-SANDBOX.md`](docs/STORY-SANDBOX.md) | Genre scaffolding, and the non-canon writers' room |
| [`docs/planning/`](docs/planning/) | Epic plans, specs, and the decision log |
| [`CLAUDE.md`](CLAUDE.md) | Context file for AI-assisted development sessions |

## How people experience it

1. **The GPT** (primary) — find it in the GPT store, play immediately
2. **The dossier page** — the shareable artefact Concord hands you at the end
3. **This repo** — everything, including the guardrails, in the open

## Licence

[CC0 1.0 Universal](LICENSE) — this project's own content is dedicated to the public domain. No rights reserved. Contributions are accepted on the same terms.

Third-party material quoted or cited in the research docs (short quotations, figures, and the linked bibliographies) remains the property of its respective sources and is used here with attribution.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Playtest reports, archetype ideas, lore PRs and guardrail tightenings are all welcome — guardrail issues are priority one.
