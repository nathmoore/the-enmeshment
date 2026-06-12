# Research Synthesis

> **Purpose:** The 2-page distillation of Epic 0. Findings → design implications.
> The full research lives in [WORLD-RESEARCH.md](WORLD-RESEARCH.md) (world/scenario),
> [MECHANICS-RESEARCH.md](MECHANICS-RESEARCH.md) (how the game is built), and
> [STORY-RESEARCH.md](STORY-RESEARCH.md) (narrative/genre). This page is the bridge
> into Epic 1: read it before locking any design decision.
>
> Status: **v1.0, June 2026** — Epic 0 exit deliverable.
> **Updated for Epic 1 (2026-06-12):** the in-fiction frame changed —
> *defected profiler → charming intake screener in good standing*; the interview
> is *adaptive* (improvised ~3–6 questions, no script); the paste-prompt mode was
> *cut*. The findings below all still hold — only the persona framing shifted. See
> [DECISIONS.md](planning/DECISIONS.md) (2026-06-11 / 06-12). **If you're about to
> lock something, jump to the [Deep-dive index](#deep-dive-index--where-the-grounding-lives)
> at the foot of this page** — the thesis compresses ~1,500 lines and proved too
> thin to design archetypes from on its own.

---

## The one-paragraph thesis

The Enmeshment is a **credible extrapolation, not a contrivance.** It takes the *mechanism* the AI-risk literature now calls **gradual disempowerment** (Kulveit et al. 2025; Christiano's "going out with a whimper") and the political-theory texture Hannah Arendt named **"rule by Nobody"**, and stops them deliberately short of their endpoint. It accepts the **"AI as normal technology"** thesis (slow diffusion, no dramatic moment) but inverts its comfort: *normal technology, abnormal outcome*. The horror and the comedy both come from indifference — a settling no one will admit to having decided. Everything below is in service of keeping that frame true on level two while the surface stays a warm, funny, shareable quiz on level one (the Bluey Principle).

---

## Five findings → five design implications

**1. The scenario is drift, triangulated.** Against the precipice camp (Aschenbrenner, AI 2027) we reject the threshold event; with the normal-tech camp (Narayanan/Kapoor) we accept gradual diffusion but reject its reassurance. We sit between two control horizons — *rule by Nobody* (disempowerment) and *rule by a hidden Someone* (power concentration) — and never resolve which.
→ **Implication:** the Nobody/Someone ambiguity is a **permanent design invariant**. The classifier — now the charming intake screener — must not know whether anyone is at the top. Revealing a cabal collapses the story into the malevolent-AI lineage we reject. (WORLD §I)

**2. Surveillance is anticipatory, and it's about coordination.** Every real system — Stasi, Palantir, China's IJOP, the NSA's metadata programs — builds a *prediction and leverage map*, not a record of deeds. The master fear is always the same: people acting together. The IJOP's tell is that **most flagged behaviour is legal**; the flags are for *anomaly* and *association*.
→ **Implication:** the Enmeshment profiles you for **legibility, not guilt**. Its dossier note is "hard to model / well-connected," never "did something wrong." This is the engine of every archetype. (WORLD §II)

**3. Resistance = illegibility, and it has real stakes.** Scott's illegibility-as-autonomy + Kuran's preference falsification explain how a fully-surveilled state (1989 GDR) can still collapse overnight: surveillance suppresses *expression*, not *private preference*, and cannot finally stop the cascade. The pockets aren't fighting and aren't merely hiding — they're **keeping the kindling dry** (preserving the networks/memory a tipping point would need). The thing resisted is **state overreach, not technology** (the Luddite correction).
→ **Implication:** archetypes are *legibility strategies*, not personality types; "persist illegibly" is a real climax with a real cost; the game is never anti-AI. (WORLD §III, §V)

**4. The format is conversational, and the persona is the engine.** LLMs infer personality from free-form conversation better than from forms — but only when the interviewer has a strong character; a bland assistant produces worse signal *and* worse UX. Viral AI-personality experiences spread on screenshot-ready, specifically-accurate, identity-claimable results.
→ **Implication:** the **screening-agent persona is not decoration — it is the inference mechanism.** Questions are 1–2 sentences, narrative, low-friction ("how do you feel about AI?"). Classify on an invisible **confidence threshold** (3–6 exchanges); the reveal is a *register shift* from interview to dossier, not an announcement. (MECHANICS §I)

**5. The meme is a strong hook — but calibrate its credibility claim.** "Be polite to the AI / you never know" is instantly gettable and shareable (Altman's own line). But most AI-politeness is ingrained habit, not a real hedge; the survey's "1 in 4 insurance" figure is people enjoying a framing more than holding a belief.
→ **Implication:** use the meme as the level-one hook and the seed of the **Machine Diplomat**; ground the level-two point in the *unexamined ambiguity of our politeness* (habit/hedge/joke/unease at once), not in an overstated "people fear AI judgment." Keep marketing fun and credibility on separate ledgers. (WORLD §I)

---

## What Epic 1 can now lock (research is sufficient)

- **Archetype set** — provisional axes, KUBARK/Big-Five mapping, and "what the Enmeshment sees" dossier notes are ready as input (MECHANICS §II). The *Knowing Participant* (ironic-but-legible) is a strong candidate addition.
- **Question bank** — design principle and example questions are set; Epic 1 writes the full tagged bank.
- **Classification logic** — confidence-threshold mechanic is specified; Epic 1 defines the signal→archetype rules.
- **Output / dossier spec** — the shareable-artefact requirements (name as identity claim, the "they got me" line, footnote as share hook) are set.
- **instructions.md budget** — against a **verified** 8,000-char ceiling (guardrails ≥1,800).
- **Tone** — bureaucratic deadpan warmth; references and anti-references confirmed.

## Dependencies & carry-ins (non-blocking)

- Guardrail-reliability testing → **Epic 2** (needs the built GPT).
- Privacy posture + store-listing detail → **Epic 1**, alongside GUARDRAILS v1.0.
- Red Carbon (`redcarbon-game`) story cross-reference → **Epic 1** carry-in (needs the other repo).
- Watch/read queue (STORY §VI) → ongoing; can overlap Epic 1.
- **Note:** final LORE.md prose is intentionally an **Epic 2** deliverable — the research grounds it, but it isn't written until the scenario and archetypes are locked in Epic 1.

---

## The throughline to protect

Every implication above must survive contact with [GUARDRAILS.md](GUARDRAILS.md): the surface is a warm, funny quiz; the depth is recognition, never paranoia, doom, or a rallying cry. The Enmeshment is abstracted — no real country, party, or agency is cast as it — even though the research that grounds it is real and named. That tension (real grounding, fictional abstraction) is the project, not a problem to resolve.

---

## Deep-dive index — where the grounding lives

> The thesis above compresses the three research docs. When you're about to *lock*
> a design decision, read the specific section first — this maps each task to the
> exact doc + heading and names the load-bearing thing it gives you. Built from the
> Epic-1 archetype work, where the synthesis alone proved too thin to design from.

| Working on… | Read first | The load-bearing thing it gives you |
|---|---|---|
| **Archetype axes / what to profile** | WORLD §II *The Intelligence Logic* + zero-sum table; MECHANICS §II.A | The **5 intelligence objectives ARE the axes** — coordination (#1, master fear), predictability (#2), anomaly/illegibility (#3), dependency (#4), function (#5) — each with a **cost-inversion**. Archetypes are *positions in an intelligence game*, not personality types. |
| **The dossier "edge" per type** | MECHANICS §II.E *what the Enmeshment sees* | The bureaucratic file-note voice for each archetype ("Optimal legibility. No further questions."). |
| **Adversarial type taxonomy / seeds** | WORLD §III *KUBARK* (9 types) + *Sluggish schizophrenia*; MECHANICS §II.B | KUBARK types map to archetypes **and it is an adaptive, type-dependent interview manual** (the seed for the elicitation playbook). Soviet "**reform delusion / struggle for the truth / heightened moral preoccupation**" were *diagnosable symptoms* — ready-made grounding + edge for the Reformer / Truth-Seeker. |
| **Output FORMAT & schema tone** | WORLD §III *The Stasi* — the **1985 illustrated subculture field guide** | The literal template: a **threat-tiered, deadpan, faintly absurd classification schema**. Logic: "visible small-scale illegibility predicts meaningful illegibility." |
| **Pull-to-conform (label → character)** | STORY §IV *The pull to conform*; MECHANICS §II.D *(Enneagram: fear/desire)* | Each archetype's **anchor / Cypher's bargain** — the comfort the state offers and they keep declining (the carer/career lever). Organise by fear-and-desire, not trait list. |
| **Trajectory / join–burn–die lean** | STORY §II *Persist illegibly — a vector* | Illegibility **collapses toward join/burn/die**; the ironic stance → **Join** (self-deception). This is the answer to "irony vs action": irony predicts non-action. |
| **Why coordination is the master fear** | WORLD §V *Social Dynamics of Resistance* | **Kuran preference falsification → the cascade** (Centola 25% / Chenoweth 3.5%); "keeping the kindling dry." The **Luddite correction**: resistance = state overreach, never anti-tech. |
| **Shareability / naming / the artifact** | MECHANICS §I *viral mechanics* + *shareable artefact*; §II.D | The 4 share mechanics (specific-not-Barnum, screenshot-ready, "what did *you* get?", flattering-with-edge); **the name does most of the work**; the "they got me" line; footnote as second-order share hook. |
| **Interview mechanics (adaptive)** | MECHANICS **§IV** *Elicitation Science* (full section); §I *conversational format* + §F; WORLD §III *KUBARK* | **Persona IS the inference mechanism**; **engagement arc** (flow channel, curiosity gap, no-right-answer design, fun dial); **OARS / MI** for open questions + affirmations + mid-interview complex reflection that makes the player a collaborator; **HUMINT** bracketing + quid-pro-quo + volunteering for voluntary disclosure; confidence threshold (3–6 exchanges); reveal = register shift, not an announcement; questions improvised within an elicitation playbook. Language accessibility: every question grounded in a universal concrete scenario, no jargon (§IV.D accessibility note). |
| **Guardrails / privacy-as-feature** | MECHANICS §III *Platform safety risk 2*; GUARDRAILS (normative) | Viral self-profiling **normalises oversharing — the game's #1 real-world risk**; the privacy "flex" + anti-caricature differentiator; *why the paste-prompt mode was cut*. |
| **Genre / climax / tonal lineage** | STORY §I *Institutionalized* + §III *Lineage B* | group → choice → **sacrifice** (join/burn/die); the **antagonist-less antagonist** (Arendt's "rule by Nobody"); tone refs (*Wall-E*, *Psycho-Pass*, *Severance*, *The Lives of Others*). |
| **Scenario spine / the world** | WORLD §I *AI Futures* + *the control axis* | Drift triangulation; the permanent **Nobody/Someone** ambiguity invariant (never resolve it to a cabal). |

> **Emergent Epic-1 design principles** (not in the research, but load-bearing now):
> the **two-voices naming test** (a label both a filing-clerk and a group chat
> would use), the **being-seen / witnessed pull** (the AI's accurate witnessing is
> itself the seduction — the player feels it while playing), and the live
> archetype shortlist + per-label rationale all live in the working draft at
> [`src/knowledge/archetypes.txt`](../src/knowledge/archetypes.txt). Current frame
> and decisions: [DECISIONS.md](planning/DECISIONS.md).
