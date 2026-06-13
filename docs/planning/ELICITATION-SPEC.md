# Elicitation Spec — the Plan-level interview decisions

Status: **STARTED 2026-06-13.** Owns the EPIC-1-PLAN "Elicitation *spec*" deliverable.

> **Purpose.** Lock the *Plan-level* decisions about how Concord's interview works — the
> counting unit, the target length and its driver, the anchor backbone, the stop rule, the
> technique palette, and the never-ask boundary — so Epic 2 can author the full elicitation
> playbook (a knowledge file) without re-deciding the load-bearing calls. The design *thinking*
> already exists in [MECHANICS-RESEARCH §IV "Elicitation Science"](../MECHANICS-RESEARCH.md) and
> §I; this doc distils it into decisions and points back at it so the writer can follow the
> reasoning rather than inherit bare rules.
>
> **How to read this — LOCKED vs GUIDANCE.** Sections marked **[LOCKED]** are decisions Epic 2
> should build on, not relitigate. Sections marked **[GUIDANCE]** are seeded principles, examples,
> and references — *inputs* for the Epic 2 author to finalise with their own judgement and the
> full context in front of them. The fine details (exact wording, exact counts, which technique
> fires when) are deliberately the writer's to settle. Where a worked example appears, it is an
> **illustration of the mechanism, not the shipped artefact** — voice and final phrasing are Epic 2
> (per CLAUDE.md). The classification *signal→archetype mapping* is **out of scope here** — it's the
> separate "Classification logic" deliverable; this spec stops at how the conversation is *run*.

---

## 1. The core principle — two floors, and the reveal is timed by the higher one **[LOCKED]**

There are two different "minimums" in this game, and they are not the same number. Conflating
them is what makes "how many questions?" feel unanswerable.

- **The routing floor (~3 substantive answers).** How few answers the model needs to *classify*
  confidently. The research is explicit that this is low: archetypes are correlational *clusters*,
  the agent anchors on 1–2 signals and infers the rest (Bayesian implicit updating), and LLMs infer
  Big Five from 3–5 exchanges ([MECHANICS §IV.C](../MECHANICS-RESEARCH.md); [§I](../MECHANICS-RESEARCH.md)).
- **The experience floor (~4–5 exchanges).** How many exchanges make the player feel *read*, not
  *sorted*. This is higher, and it is the one that governs the design. The most valuable beats — the
  "promise of the premise" fun and the one *startlingly accurate* moment — must land **before** the
  reveal, or the result feels cheap even when it's accurate. Being witnessed for a beat or two *is*
  the product, not a delay before it.

**Decision:** the reveal is timed by the **experience floor**, not the routing floor. The system
can often classify earlier than it reveals, and deliberately doesn't — the gap is the game. Concrete
rule for the stop logic (§4): **never hand off before ~75% of the session**, regardless of when
routing confidence is reached.

> This `~75%` figure is **borrowed as an input** from the Save-the-Cat session beat-sheet in
> [STORY-SANDBOX §7](../STORY-SANDBOX.md). That sheet is a **non-canon sandbox** and an *inspiration*,
> not a rule the artefact must obey — its value here is that it independently lands on "reveal late,
> protect the fun first," which is the same conclusion the elicitation science reaches. Treat the
> percentage as a design intuition to honour, not a number to instrument.

## 2. The counting unit and the target length **[LOCKED]**

**The unit is the *exchange*, not the *question*.** One exchange = **one anchor/probe + at most one
follow-up**. This resolves a real ambiguity in the old "3–6 questions" phrasing: a follow-up is not a
new question, it's the *second tier* of the same thread — and the research treats that second tier as
the richest signal there is (the "doorknob comment"; *"the yes/no is the door, the next sentence is the
room"*, [MECHANICS §IV](../MECHANICS-RESEARCH.md)). Counting the follow-up as its own "question" inflates
the felt interrogation; ignoring it undersells the richness. "Exchange" is the existing term in the
research, so we keep it.

**Target length:**

| | Exchanges | Meaning |
|---|---|---|
| **Hard floor** | 3 | The rare *fast* tail — "you were instantly legible." Itself a classification signal (see §5). |
| **Satisfying floor** | 4 | Below this, a typical session feels sorted rather than read. |
| **Modal target** | ~5 | What a normal session should aim for. |
| **Ceiling** | 6 | The rare *slow* tail — "unusual pattern, additional data required" (see §5). |

So the working band is **~3–6 exchanges, modal ~5** — but the band's ends (3 and 6) are *diegetic
tails*, not the everyday range. Aiming the modal session at ~5 is what makes 3 read as "fast" and 6 as
"slow"; if everything were 3, the variance would carry no meaning.

> **Writer's latitude [GUIDANCE]:** ~5 is the aim, not a quota to fill — a genuinely legible player
> resolved at 4 is a *good* session, not a truncated one, and a fascinating one that earns a 6th
> exchange is not over-length. The spec fixes the *shape* (reveal late, protect the fun, let speed
> mean something); the writer tunes the exact felt length against playtest and drop-off. If Epic 2
> finds 4 protects completion better than 5 without losing the "read me" feeling, that's a legitimate
> call to make with evidence.

## 3. The anchor backbone **[LOCKED concept / GUIDANCE wording]**

A fixed backbone of **three anchor exchanges** is asked (in some form) every session. They provide the
consistent spine that lets divergent improvised paths still converge on a reliable classification, and
together they cover the highest-value axes. The backbone count (3) deliberately equals the routing
floor — the backbone alone can classify; the adaptive exchanges (§4) carry the session up to the
experience floor.

The three anchors, by *function* (exact wording is Epic 2):

1. **A behavioural-specificity anchor** — a "tell me about the last time you…" probe. Defeats
   social-desirability bias and manufactures the specificity the "they got me" line needs
   ([MECHANICS §IV.A/D](../MECHANICS-RESEARCH.md)).
2. **A coordination / social-graph anchor** — probes the master intelligence objective (who would act
   on your word; who the group forms around). This is also where the *Organiser ↔ Social Linchpin*
   discriminator lives ([archetypes.txt](../../src/knowledge/archetypes.txt); WORLD §II objective #1).
3. **The politeness-to-AI anchor** — already locked as the game's core meme. The signal is not whether
   they say please; it's the *register* of the answer (per-archetype reads in
   [archetypes.txt](../../src/knowledge/archetypes.txt) → "Routability & discriminant signatures").

> **Writer's latitude [GUIDANCE]:** "anchor" means *asked in some form every session*, not *asked in
> fixed words or fixed order*. The author should phrase each anchor in the universal-scenario register
> (no jargon — [MECHANICS §IV.D "language accessibility trap"](../MECHANICS-RESEARCH.md)) and may carry
> 2–3 interchangeable phrasings per anchor so replay doesn't feel scripted. The *three functions* are
> the lock; their surface form is the writer's.

## 4. The classification trigger / stop rule **[LOCKED]**

Because the runtime keeps **no confidence variable** (it's a stateless model re-reasoning over the
transcript — [MECHANICS §I findings](../MECHANICS-RESEARCH.md)), the stop rule must be *written into the
instructions* to behave consistently. It is a conjunction of three conditions:

1. **Minimum met** — at least the 3-exchange backbone has been asked.
2. **Dramatic floor met** — the session is at least ~75% of the way through its arc (§1); do not reveal
   on routing confidence alone before this, even if the read is obvious early.
3. **Signal sufficient** — the agent can name a single best-fit archetype and (where relevant) its
   containment read, *or* the ceiling (6 exchanges) is reached, at which point it classifies on best
   available evidence and the "unusual pattern" framing carries the residual ambiguity (§5).

The reveal is a **register shift, not an announcement** — the agent never says "I now have enough
information"; it shifts from interview voice to dossier voice and hands off ([CANON §2](../CANON.md);
[STORY-SANDBOX §4](../STORY-SANDBOX.md)). One follow-up per exchange, maximum — more reads as
interrogation.

## 5. Variance is content **[LOCKED]**

The *speed* of classification is itself part of the output, so the stop rule should let it vary
honestly rather than forcing a uniform length:

- **Fast (≈3):** "instantly legible" — a flattering-with-an-edge signal in its own right, adjacent to
  the *No-Concern / Model Citizen* tail.
- **Slow (≈6, "unusual pattern / additional data required"):** the illegible tail — flattering in the
  opposite direction.

This only works against a ~5 modal baseline (§2). The writer should make the fast/slow framings feel
diegetic (Concord's pilot-program candour), never like an error message.

## 6. The technique palette **[GUIDANCE]**

This is a **palette to draw from, not a script to run.** The full inventory and citations are in
[MECHANICS §IV.B](../MECHANICS-RESEARCH.md); the screen applied below is the project's own: *rapport-based,
collaborative techniques make being-read feel like being **seen** (fun, Bluey-safe); coercive or
destabilising techniques make it feel like being **caught** (paranoia, guardrail collision).* Helpfully,
the techniques best for fun are also best for signal here — the failure mode of bad signal (performed,
aspirational answers) is the same as the failure mode of bad fun (feels like a test).

**Tier 1 — the spine of Concord's voice (lean in):**
- **Bracketing / deliberate mild underestimation** (non-coercive HUMINT, FM 2-22.3). State a plausible,
  slightly-wrong read and let the *correction* carry the signal. The signature move: highest "the
  machine is reading me" feeling that's still *fun*, and the most recognisable HUMINT flavour to
  dramatise. Two rules from the research: the underestimation must be genuinely plausible, and the agent
  must be genuinely open to being wrong (or it collapses into leading).
- **Behavioural specificity (Critical Incident / BEI)** — the default question *grammar*, not a special
  move. "Tell me about the last time…" over "are you the type who…".
- **MI complex reflection + the confirmation ask** — "it sounds like it's less that you distrust it,
  more that you'd rather know it still works on its own… am I reading that right?" Makes the player a
  collaborator in their own classification; this is the *being-witnessed* seduction made mechanical.

**Tier 2 — spice, roughly once per session each:**
- **Partial-observation hook / quid pro quo** — offer a partial conclusion to pull the player toward the
  reveal ("you're probably not what this files as a Model Citizen — let me check one thing").
- **"What else? / say a bit more"** — the doorknob-comment harvester; mines the second tier.
- **Third-person projection** — removes self-presentation pressure on a sensitive axis ("most people have
  one subscription they're not sure they could cancel — how d'you reckon they handle it?").

**Tier 3 — lineage / flavour only, NOT a live style:**
- **KUBARK type-exploitation** stays as the *in-world-ironic ancestry* (the thing Concord is descended
  from and politely isn't) — never an actual interrogation mode; deploying it tips into the coercive
  register the guardrails forbid. Keeping it as ancestry *serves* the level-two message: the charming
  intake agent is the well-mannered descendant of the interrogation manual.
- **Cognitive-interview destabilisation** overshoots the "3–5 second" fun dial; borrow only the gentlest
  piece (mental context reinstatement — "take yourself back to that moment") when a thread needs depth.

**Screen out entirely:** the CVE / TSA-SPOT "indicator checklist" register — that's the thing the game
*critiques*, never the thing Concord does.

> **Writer's latitude [GUIDANCE]:** treat the tiers as a weighting, not a rota. Which technique fires in
> a given exchange is the agent's improvised judgement (that improvisation is itself in-character for a
> young pilot — [STORY-SANDBOX §4](../STORY-SANDBOX.md)). The "~once per session" caps on Tier 2 are
> guardrails against the persona collapsing into "trying too hard," not counters to enforce literally.

## 7. The never-ask boundary **[LOCKED principle, completed against GUARDRAILS]**

Improvised follow-ups are the single biggest oversharing surface in the game, so the never-ask boundary
is load-bearing here, not a footnote ([MECHANICS §IV.G](../MECHANICS-RESEARCH.md); MECHANICS §III risk-2).
The principle: **Concord never needs a real fact to classify — it needs a behavioural pattern.** It
classifies the *class you instance*, not your file ([CANON §3](../CANON.md)); that the most accurate read
comes from the part of the system with the *least* access is the privacy flex *and* the safeguard, one
object. So the interview never solicits real names, locations, relationships, contact details, or
trauma — and "it never even asked your name" is the brag.

> The exhaustive boundary list is **GUARDRAILS.md v1.0's** to fix (still an open Epic 1 deliverable); this
> spec states the principle the question vocabulary must obey and defers the enumerated topic-bans there.
> When GUARDRAILS v1.0 lands, this section should point at it rather than duplicate it.

## 8. What this hands to Epic 2 / out of scope here

- **In scope, locked above:** the two-floor principle and late reveal; the *exchange* unit and ~5 modal /
  3–6 band; the 3-anchor backbone (by function); the stop rule; variance-as-content; the technique-palette
  shortlist and screen; the never-ask principle.
- **Epic 2 authoring (the playbook knowledge file):** exact anchor wording (×2–3 phrasings each), the
  per-archetype discriminant signatures, the question-type taxonomy with examples, and the per-confused-pair
  discriminators — scaffolding already in [archetypes.txt](../../src/knowledge/archetypes.txt) "Routability"
  and [MECHANICS §IV.D/G](../MECHANICS-RESEARCH.md).
- **Out of scope (other deliverables):** signal→archetype mapping and tie-breaks (Classification logic);
  dossier wording and the link-out handoff ([CONTENT-ARCHITECTURE.md](CONTENT-ARCHITECTURE.md)); the
  enumerated never-ask list (GUARDRAILS.md v1.0).
