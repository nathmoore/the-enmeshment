# Game Design & Philosophy

> Status: **stub** — core pillars locked, details developed in Epics 0–1

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

Seed list (to be developed in `src/knowledge/archetypes.txt`):

| Archetype | One-liner | Deep layer |
|---|---|---|
| The Conventional User | Compliant, comfortable, quietly indispensable to the system's legitimacy | Convenience as consent |
| Off-Grid Capable | Would be fine. Knows which mushrooms. Owns a paper map. | Resilience & analogue skill loss |
| The Renaissance Generalist | Knows a worrying amount about a worrying range of things | Generalism vs. automated expertise |
| The Machine Diplomat | Says please. Negotiates with chatbots. The AI *likes* them. | Anthropomorphism & moral status of AI |
| The Quiet Archivist | Backs things up. Keeps receipts. Remembers what the feed forgot. | Memory, records & who controls history |
| The Network Weaver | Knows everyone; the human mesh network | Social capital that can't be automated |
| *(4–6 more TBD)* | | |

Design rule: **every archetype is a form of resistance** — including the Conventional User (the twist: the system needs them most, which is its own kind of leverage).

## 4. Question & signal design

Signals we profile (persona-level only — see GUARDRAILS.md):
- Big 5 *tendencies* (as expressed in writing style / choices, framed playfully)
- Politeness-to-AI habits (the meme, operationalised)
- Analogue & survival-adjacent skills (self-reported, tongue-in-cheek)
- Generalist vs. specialist knowledge shape
- Digital usage *style* (not history): customiser vs. defaults-user, lurker vs. poster
- Relationship-to-institutions disposition (rule-follower ↔ workaround-finder), kept apolitical

TODO (Epic 1): build the elicitation playbook — oblique, open-ended question *types* (not fixed multiple-choice), interview techniques, and the signal each answer reveals. The agent improvises within it; see DECISIONS 2026-06-12.

## 5. Tone references & anti-references

- ✅ Bureaucratic-absurdist: *Severance*, SCP Foundation field reports, *Welcome to Night Vale* memos
- ✅ Warm satire: classic BuzzFeed-quiz joy, but written by someone who's read the futures literature
- ❌ Doomer content, partisan digs, real-world political targeting, genuine psychometric claims

## 6. Open design questions

- [ ] Does the player get a "resistance cell assignment" (faction flavour) as a second axis?
- [ ] Rarity/edge archetypes for delight ("we have… never seen this combination")?
- [ ] Replayability: does answering as your *workplace self* vs *weekend self* change the result (it should)?
