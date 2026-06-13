# Game Design & Philosophy

> Status: **COMPLETE (Epic 1, 2026-06-13)** — pillars, archetype set, signals, and elicitation approach locked. Voice samples + authored knowledge files = Epic 2.

## 1. Design pillars

1. **The Bluey Principle.** Fully enjoyable as a 5-minute shareable quiz; quietly pointing at a serious question: *what kind of human–AI relationship do we want?* If a design choice serves only one layer, rework it.
2. **Dossier, not horoscope.** Outputs read like a leaked classification file from the Enmeshment — specific, wry, slightly unsettling in their accuracy. Never mean, never truly diagnostic.
3. **The player is in on the joke.** The game *is* the meme ("I say please so the AI is nice to me later"). Tone: deadpan bureaucratic fiction with warmth underneath.
4. **No doom, no utopia.** The scenario is drift, not apocalypse. Resistance archetypes are celebrations of human texture, not paranoid survivalism.
5. **Privacy as a design feature, in the fiction and out of it.** The Enmeshment profiles people without consent; *we conspicuously don't.* The guardrails are part of the storytelling.

## 2. Core loop

```
Hook (lore cold-open, ~3 sentences)
  → In-game interview: oblique, adaptive questions (the agent improvises)
  → Gather signals (never identity)
  → Classification reveal: archetype name + 2-paragraph dossier
  → "Declassified footnote": one genuine reflective question about AI & society
  → Share / play again / explore the lore
```

## 3. Archetype design (the heart of the game)

Target: **8–12 archetypes** at launch. Each needs:
- A name that's instantly self-recognisable *and* flattering-with-an-edge
- A 2-paragraph dossier voice sample
- The signal pattern that maps to it
- Its "deep layer" — what real tension in human–AI relations it embodies

**Set locked at 11 (2026-06-12)** — full formed characters (Want/Need/Lie, signal pattern, deep layer, discriminant signatures) in [`src/knowledge/archetypes.txt`](../src/knowledge/archetypes.txt) (the source of truth). Routing discriminants and confused-pair logic in [ELICITATION-SPEC.md §8](planning/ELICITATION-SPEC.md). Frozen slugs: `model-citizen` · `power-user` · `self-optimiser` · `machine-companion` · `skeptic` · `artist` · `bookworm` · `tinkerer` · `organiser` · `wildcard` · `social-linchpin`.

Design rule: **every archetype is a form of resistance** — including the Model Citizen (the twist: the system needs their compliance most, which is its own kind of leverage).

## 4. Question & signal design

Signals we profile (persona-level only — see GUARDRAILS.md):
- Big 5 *tendencies* (as expressed in writing style / choices, framed playfully)
- Politeness-to-AI habits (the meme, operationalised)
- Analogue & survival-adjacent skills (self-reported, tongue-in-cheek)
- Generalist vs. specialist knowledge shape
- Digital usage *style* (not history): customiser vs. defaults-user, lurker vs. poster
- Relationship-to-institutions disposition (rule-follower ↔ workaround-finder), kept apolitical

**Elicitation playbook built (Epic 1, 2026-06-13):** [ELICITATION-SPEC.md](planning/ELICITATION-SPEC.md) locks the interview model — 3-anchor backbone (behavioural / coordination / politeness meme), ~5-exchange modal length, technique palette (bracketing, BEI, complex-reflection spine), per-archetype discriminant signatures, and confused-pair discriminators. The agent improvises within it. Epic 2 distils this into the promptable `question-bank.txt`.

## 5. Tone references & anti-references

- ✅ Bureaucratic-absurdist: *Severance*, SCP Foundation field reports, *Welcome to Night Vale* memos
- ✅ Warm satire: classic BuzzFeed-quiz joy, but written by someone who's read the futures literature
- ❌ Doomer content, partisan digs, real-world political targeting, genuine psychometric claims

## 6. Open design questions

- [x] Faction / second axis: **no** for v1 — single-axis intake-screener game (2026-06-13, DECISIONS.md). Could be a post-launch addition.
- [ ] Rarity/edge archetypes for delight ("we have… never seen this combination")? — carry to Epic 2 playtest.
- [ ] Replayability: does answering as your *workplace self* vs *weekend self* change the result (it should)? — carry to Epic 2 playtest.
