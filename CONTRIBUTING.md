# Contributing

Thanks for joining the resistance. This project is small, opinionated, and
open — here's how to help.

New here? Read [`docs/GAME-DESIGN.md`](docs/GAME-DESIGN.md) for what the game is
trying to be and [`docs/GUARDRAILS.md`](docs/GUARDRAILS.md) for what it won't do.
[`docs/planning/DECISIONS.md`](docs/planning/DECISIONS.md) records why things are
the way they are — check it before reopening a settled call.

## Ways to contribute
- **Playtest reports** (most valuable!): open an issue with the transcript
  vibe, your archetype, what landed, what fell flat. Guardrail breaks are
  priority-1 — label them `guardrail`.
- **Archetype proposals**: open an issue using the card format in
  [`src/knowledge/archetypes.txt`](src/knowledge/archetypes.txt). Every archetype is
  a form of resistance, flattering-with-an-edge, never mean — and it needs a
  Want / Need / Lie, not just a vibe.
- **Lore PRs**: edit [`docs/CANON.md`](docs/CANON.md). Canon rules apply: the story is
  set in **2038**, and player-facing surfaces carry no *other* hard dates and no real
  countries, parties or politicians as the Enmeshment. Warmth always.
- **Interview questions**: add them to
  [`src/knowledge/elicitation-playbook.txt`](src/knowledge/elicitation-playbook.txt) §3,
  following the existing door-then-room shape (a low-load opener, then the draw-out).
  Must comply with [`docs/GUARDRAILS.md`](docs/GUARDRAILS.md) §1 — never fish for a
  forbidden fact.

## Ground rules
1. [`docs/GUARDRAILS.md`](docs/GUARDRAILS.md) is normative. PRs may tighten guardrails
   freely; loosening requires maintainer consensus with rationale.
2. The Bluey Principle: contributions should work on both layers — fun on
   level one, pointing at the human–AI question on level two.
3. Be kind. Satire targets systems, never people. No real-world political
   targeting, and no mapping the fiction onto real actors.
4. **Two layers, sorted.** *Who an archetype is* lives in `archetypes.txt`;
   *how to tell them apart* lives in
   [`docs/planning/ELICITATION-SPEC.md`](docs/planning/ELICITATION-SPEC.md) §8. Keeping
   them apart is what makes a wrong result debuggable — decide which one is broken
   before editing either.

## Process
1. Open an issue before large PRs.
2. One epic at a time — check [`docs/planning/`](docs/planning/) for what's current.
3. PRs: clear title, link the issue, note which docs you touched.
   **Know what you're changing:** the live GPT is deployed by hand by the maintainer
   (instructions pasted, knowledge files re-uploaded, tagged `gpt-vX.Y.Z`), so a merged
   change to `src/` is not live until the next release. The site deploys itself on push to
   `main`. See the README's "How it ships".
4. If you touch [`src/instructions.md`](src/instructions.md), re-run the character
   count and update the budget line — there is a hard 8,000-char limit and it is
   currently tight. Count in UTF-8 (the header has the exact command; a bare
   `wc -m` under `LC_ALL=C` counts bytes and over-reports by ~100).

## Licence
Everything in this repo is [CC0 1.0](LICENSE) — public domain, no rights reserved.
By contributing you agree your contribution is dedicated to the public domain under CC0.
