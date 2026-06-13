# Elicitation & Routing Spec — the full elicitation + routing workings

Status: **STARTED 2026-06-13; routing workings developed 2026-06-13 (deepening pass).** Owns the
EPIC-1-PLAN "Elicitation *spec*" deliverable **and the folded-in "Classification logic" deliverable**
(now §8 "Routing principles" — the old rigid-mapping framing is retired; see DECISIONS 2026-06-13).

> **Purpose.** This is the **single thinking doc** for how Concord's interview works *and how its
> signals route to an archetype* — there is no separate "workings" document. It carries two things:
> (1) the **locked Plan-level decisions** — the counting unit, the target length and its driver, the
> anchor backbone, the stop rule, the technique palette, the never-ask boundary; and (2) the **fully
> developed routing workings** (§8) — the best-fit model, the signal hierarchy, the **per-archetype
> discriminant signatures** (§8.3) and the **confused-pair discriminators** (§8.4), reasoned through
> the whole TAS triad. Epic 2 *executes* these workings into the final elicitation + routing playbook
> (a knowledge file) — turning them into final wording, exact counts, and the per-archetype prose —
> without re-deciding the load-bearing calls or re-deriving the routing logic. The design *thinking*
> grows from [MECHANICS-RESEARCH §IV "Elicitation Science"](../MECHANICS-RESEARCH.md) (incl.
> §IV.D-bis, the character-construction engine) and §I; this doc develops it into decisions and
> workings, and points back at it so the writer can follow the reasoning rather than inherit bare
> rules. The **"who they are"** layer — the formed characters the routing sorts on — lives in its own
> home, [archetypes.txt](../../src/knowledge/archetypes.txt); this doc is the **"how to tell them
> apart"** half of the one engine (MECHANICS §IV.D-bis), kept separate so a playtest miss is
> debuggable against one home or the other.
>
> **How to read this — LOCKED vs GUIDANCE.** Sections marked **[LOCKED]** are decisions Epic 2
> should build on, not relitigate. Sections marked **[GUIDANCE]** are seeded principles, examples,
> and references — *inputs* for the Epic 2 author to finalise with their own judgement and the
> full context in front of them. The fine details (exact wording, exact counts, which technique
> fires when) are deliberately the writer's to settle. Where a worked example appears, it is an
> **illustration of the mechanism, not the shipped artefact** — voice and final phrasing are Epic 2
> (per CLAUDE.md). The classification *signal→archetype routing* is **now in scope** — §8 below
> (previously punted to a separate "Classification logic" deliverable, since folded in). What stays
> out of scope: the *exact dossier wording* and the *enumerated never-ask list* (other deliverables,
> §9).

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
   on your word; who the network runs through / bridges across it). This is also where the
   *Organiser ↔ Social Linchpin* discriminator lives — overtly-drives vs quietly-bridges
   ([archetypes.txt](../../src/knowledge/archetypes.txt); WORLD §II objective #1).
3. **The politeness-to-AI anchor** — already locked as the game's core meme. The signal is not whether
   they say please; it's the *register* of the answer (per-archetype first-pass reads in §8.3).

> **Writer's latitude [GUIDANCE]:** "anchor" means *asked in some form every session*, not *asked in
> fixed words or fixed order*. The author should phrase each anchor in the universal-scenario register
> (no jargon — [MECHANICS §IV.D "language accessibility trap"](../MECHANICS-RESEARCH.md)) and may carry
> 2–3 interchangeable phrasings per anchor so replay doesn't feel scripted. The *three functions* are
> the lock; their surface form is the writer's.

### 3.4 The oblique-topic palette beyond the backbone **[GUIDANCE]**

The 3 anchors are asked every session; the adaptive exchanges (§4) draw from a wider pool of **oblique
everyday topics**. The hard constraint on every topic: **universally answerable — never gated by
technical literacy, jargon, or how online someone is** (the "language accessibility trap",
[MECHANICS §IV.D](../MECHANICS-RESEARCH.md)). A topic only the tech-fluent can answer comfortably both
narrows the audience and *corrupts the signal* — you end up measuring literacy, not character. Always
probe the **behaviour and feeling**, never the technical detail.

Recommended topics (each reveals character without requiring expertise — wording finalised in Epic 2):

- **Who you turn to for a real decision** — a person / family / the AI / no one. Hits social
  architecture (Organiser / Linchpin), the AI-relationship (Companion), and self-reliance at once.
  Maximally universal.
- **How you pick up a new skill** — read / watch a video / ask someone / just have a go / wouldn't
  bother. The purpose-built **Bookworm↔Tinkerer** topic (§8.4): read-or-watch-to-know (Bookworm, inward/
  cerebral — any medium) vs have-a-go-and-make-it-work (Tinkerer, outward/physical); also reveals openness.
- **The thing you're always recommending** — what you tell people they should read / watch / try.
  Reveals evangelism (Power User), taste and audience-orientation (Artist), connecting-people (Linchpin).
- **Your role when the group makes plans** — book it / host (overt driver → Organiser) / just show up /
  the quiet one everyone tells things to and who links people up (→ Linchpin). Carries the
  Organiser-vs-Linchpin discriminator (overtly-drives vs quietly-bridges), and is a fun group-chat compare.
- **An official process that drove you mad** — and what you did about it. Behaviourally-specific (BEI);
  reveals institution-orientation (rule-follower vs workaround-finder).
- **First thing you reach for in the morning** — grand-tour habit; reveals dependency and optimisation
  (Self-Optimiser) without ever framing it as "tech".
- **Something you keep that everyone else has let go of** — paper, photos, old notes. Reveals the
  archive / memory posture (Bookworm).

**On the phone/tech-update topic specifically:** it's genuinely good signal (conscientiousness,
institution-orientation, dependency) and the research already favours it
([MECHANICS §IV.C](../MECHANICS-RESEARCH.md) example) — **but it tips technical fast.** Keep it only if
framed as *habit and feeling*: "when your phone nags you to update, what actually happens?" (tap yes
straight away / put it off / ignore it till it forces you) is universal; anything about *why* or *which*
update is not. When in doubt, prefer the decision / skill / people topics above — same signal, zero
literacy floor.

> **Writer's latitude [GUIDANCE]:** a starter pool, not a fixed menu — the agent picks obliquely as the
> flow allows. The **locks** are the accessibility constraint and "probe behaviour, not expertise"; the
> specific subjects are the writer's to extend.

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

## 8. Routing principles — how the archetypes are told apart **[LOCKED frame / GUIDANCE detail]**

This section folds in the old "Classification logic" deliverable (the rigid signal→archetype *mapping*
framing is retired — it predates the move off structured questions). It is the **how-to-tell-them-apart**
layer; the **who-they-are** layer — the formed characters — lives in
[archetypes.txt](../../src/knowledge/archetypes.txt). Both run on the same engine (the
character-construction kit: Want / Need / Lie + BuzzFeed reverse-engineering,
[MECHANICS §IV.D-bis](../MECHANICS-RESEARCH.md)), but this layer is allowed to **expand and speculate**
into the mechanics that separate neighbours. Keeping the two in separate homes is what makes a playtest
miss *debuggable*: "is the character wrong?" (fix archetypes.txt) vs "is the character right but the
routing guidance wrong?" (fix here).

### 8.1 The model: probabilistic best-fit, not a scoring rubric **[LOCKED]**

Routing is best-fit inference over free-form answers, not a forward-scored quiz. Archetypes are
correlational **clusters**, so the agent anchors on 1–2 signals and infers the rest (Bayesian implicit
updating, [MECHANICS §IV.C](../MECHANICS-RESEARCH.md)); it needn't probe every axis. Design it **backward
from the fixed 11** (reverse-engineering): for each character, ask "what answer would reveal *this* one
rather than its neighbour?" Output = **one best-fit archetype → one dossier page** — no multi-label, and
no separate "containment" classification (the file-closed / open / priority flavour already lives inside
each archetype's dossier). **Only the 11 are routes;** the Off-Gridder is not a target — route a
low-dependency disposition to where it's *headed* (Tinkerer / Bookworm / Wildcard / Organiser), per the
archetypes.txt watchlist.

**Sort on the character, not on the threat.** The routing axis is the **TAS triad — Want / Need / Lie**;
that is the concrete, answerable thing the interview can actually read. How the AI-state *relates* to each
archetype and the **type of threat** it poses is **story texture** that lives in
[archetypes.txt](../../src/knowledge/archetypes.txt) (the Peg / Edge / profiling-lens material) — it is
evocative, downstream colour, *not* "concrete and real," so it must **not** drive who-gets-routed-where.
Two archetypes can pose a similar "threat" and still be told apart cleanly on their Want/Need/Lie; that
character split is the sorting work, the threat read is the flavour the dossier then puts on it.

### 8.2 Signal hierarchy **[LOCKED]**

1. **The 3 anchors (§3) are the primary signal**, read by **register over content** — not *whether* they
   say please but *how*; how they talk about coordinating people; the texture of a behaviourally-specific
   story.
2. **Response texture is reliable secondary signal**, often more so than content
   ([MECHANICS §IV.F](../MECHANICS-RESEARCH.md)): irony → Skeptic; "why do you ask?" → a Skeptic *tell*
   (note it, don't reward it); hedging → Companion ambivalence; self-correction → reflective (Bookworm);
   register (institutional vs default-y vs "I turn that off") → institution orientation.
3. **CANOE / trait-direction is a *minor supporting* signal only** — it may corroborate a character-driven
   read, never define or primarily drive one ([MECHANICS §IV.C demotion note](../MECHANICS-RESEARCH.md)).
4. **Session length is framing only** (§5) — *not* a routing signal. Fast/slow colours the diegetic reveal
   ("instantly legible" / "unusual pattern"); it does not move the archetype.

### 8.3 Discriminant signatures — one per archetype **[GUIDANCE]**

Each archetype answers the three anchors (§3) *in character*. A **signature** is the cluster the agent
reads across the anchors plus response texture (§8.2) — and, most usefully, the **Lie-leak**: the place
the self-deception surfaces in *how they justify* a behaviour. Per §8.4, the Lie is the cleanest
discriminator because it's hard to perform; so each signature names the Lie-leak as its sharpest tell.
These are developed reads to *execute* (final wording is Epic 2's), not the rigid forward-scoring the
old mapping implied — read for the *thing the character wants/protects* showing through. The three
anchors below are abbreviated **[B]** behavioural-specificity, **[C]** coordination/social-graph,
**[P]** politeness-to-AI register.

- **Model Citizen** — [B] defaults; "I just go with what it suggests," and *can't readily produce a
  workaround story* — the absence of friction is itself the read. [C] defers ("I'd ask whoever'd
  know"); not a hub. [P] "yes, obviously," faintly puzzled it's being asked. Texture: short, uncurious,
  low elaboration, no irony. **Lie-leak (tell):** minimises own stakes — "none of this is really about
  me / I just keep my head down."
- **Power User** — [B] early-adopter stories, names features/tools, "I switched the moment X shipped."
  [C] the one others ask what to use; evangelises. [P] yes — and can tell you which model responds best
  to which phrasing. Texture: fluent, enthusiastic, specific. **Lie-leak:** frames mastery as being
  *ahead of / in control of* the tool — the more fluent the more enmeshed.
- **Self-Optimiser** — [B] routines, tracking, metrics ("every morning I…"), or the career twin ("I
  can't afford to drop the ball on…"). [C] optimises *around* people (provider read) or is self-focused.
  [P] instrumental — politeness if it gets a better result. Texture: progress-framed, controlled.
  **Lie-leak:** control-talk — "if I just stay on top of it, it can't get away from me."
- **Machine Companion** — [B] talks about the AI *relationally*; has named it; anecdotes of it "getting"
  them. [C] turns to the AI itself for a real decision. [P] genuine warmth; has clearly thought about it.
  Texture: warm, present-tense, relational. **Lie-leak:** attributes interiority/care to the system —
  "it knows me / it cares."
- **Skeptic** — [B] uses everything, narrated ironically ("I know it's all surveillance, but…"). [C]
  dismissive of coordination. [P] ironic "yes," with a self-aware comment on why he bothers (also catches
  the ex-Agitator who provokes the AI in talk). Texture: irony; "why do you ask?" is a *tell* (note it,
  don't reward it); performed distance. **Lie-leak:** equates seeing-through with resisting — "I'm not
  fooled" — while complying fully. (Performer risk lives here, §8.5.)
- **Artist** — [B] makes things; stories pivot on the work and on being seen / missed by an audience.
  [C] audience-oriented — who sees the work, the size of the room. [P] relates to the AI as something
  that *speaks their language* (a route to being understood), not as a social nicety. Texture:
  expressive, particular about their own output. **Lie-leak:** denies the cost — narrates the audience
  as embracing the *uncompromised* thing ("they finally get it"), never admitting the recognition is
  for the legible part, or that being embraced quietly reshapes the work toward what travels.
- **Bookworm** — [B] self-enriches independently — reads, but equally audiobooks / podcasts /
  documentaries / deep dives; "I read around it / went down a rabbit hole." [C] solitary; the one who
  quietly knows. [P] hadn't framed it as a social encounter at all. Texture: reflective, self-correcting,
  precise; the enrichment lives *inward / cerebral* — thoughts kept to themselves or enjoyed in talk.
  **Lie-leak:** cost-denial — "learning on my own is just enrichment, it costs nothing" — not noticing
  the independence it preserves.
- **Tinkerer** — [B] always a project on the go — fixes, makes, mends with their hands (workshop, engine,
  garden, gadget), not just tech; "I just had a go at it myself." [C] self-reliant; a bit off the beaten
  track; helps others practically. [P] also hadn't framed it socially (shares this read with Bookworm —
  split in §8.4). Texture: hands-on, concrete, capability-proud; the same independent streak as the
  Bookworm but turned *outward / physical*. **Lie-leak:** apartness-as-sufficiency — "standing a bit
  apart from the crowd is a self-sufficient way to be" — narrated as independence while they remain as
  embedded in community as anyone.
- **Organiser** — [B] "the last time I sorted X for everyone." [C] **makes things happen** — books it,
  mobilises, the plan flows from them. [P] practical / instrumental. Texture: action-framed, plural
  ("we," "I got everyone…"). **Lie-leak:** "it's only logistics, I'm just the practical one" — disowning
  the mobilisation capacity that *is* the signal.
- **Wildcard** — [B] answers veer; non-sequiturs; no stable through-line. [C] presents as unplaceable.
  [P] an answer you couldn't have predicted from the others. Texture: incoherence, tonal jumps, surprises
  — but *consistent* scramble, which is itself a pattern. **Lie-leak:** the front — "I'm all over the
  place / you can't read me" — performed (knowingly or not) to keep from being reached; the tell is that
  the scramble resolves into a readable person on inspection. Don't be wrong-footed into illegibility:
  it's the slow read (the "unusual pattern" tail, §8.6), not a missed one — the routing lands on the
  person behind the front.
- **Social Linchpin** — [B] stories centred on people and gatherings, but framed as *holding things
  together* rather than running them. [C] the quiet **bridge** — knows people in circles that don't
  otherwise touch, the connector the network actually runs through (vs Organiser, who overtly acts);
  quieter than you'd expect for someone so connected. [P] answers about the AI by talking about *people*
  — who else uses it, who they'd recommend it to. Texture: warm, people-dense; names relationships, not
  tasks. **Lie-leak:** "I'm just sociable, it's only my friends" — disowning the cross-group centrality
  that's the Priority-Interest read.

Each signature is the *who-they-are* of [archetypes.txt](../../src/knowledge/archetypes.txt) read back
out as cues; keep them in sync (fix the character there, the cue here). Epic 2 finalises the exact
phrasings and may carry 2–3 interchangeable reads per anchor so replay doesn't feel scripted.

### 8.4 Overlap-vs-distinct: where neighbours share a drive but split on what they protect **[GUIDANCE]**

The real routing work is the *adjacent* pairs — they overlap on one axis and must be told apart on
another. Reason across the whole **TAS triad**, not just one field: a pair often shares a **Want**
(the surface goal) yet diverges on the **Need / thing protected** or — most usefully — on the **Lie**.
The Lie is frequently the cleanest discriminator because self-deception *leaks*: it surfaces in how a
person justifies a behaviour, not in the behaviour itself, and it's hard to perform. So when two
neighbours look identical on Want, listen for which Lie is doing the talking. Trait-direction is allowed
only to corroborate, never to define.

- **Model Citizen ↔ Power User** — both sit comfortably with the system (shared ease). Split on Want:
  the Citizen wants *frictionless invisibility* (defaults, no fuss); the Power User wants *to be ahead*
  (customises, evangelises, early-adopts). Lie tell: Citizen — "none of this is really about me";
  Power User — "mastering it means I'm ahead of it." Surface discriminator: defaults-user vs
  customiser / early-adopter.
- **Organiser ↔ Social Linchpin** — both register on the coordination anchor (the #1 master objective),
  so this is the highest-stakes pair to get clean — and one likely to surface *together* in a group chat,
  so the difference must be interesting and unambiguous, not a coin-toss. Split on Want: the Organiser
  wants *to make things happen* — mobilises, acts, drives, **overtly** out front; the Linchpin wants *the
  people and groups to stay connected* — the **quiet bridge** who reaches across circles that don't
  otherwise touch (high betweenness), the connector the network runs through without obviously leading
  it. Lie tell: Organiser — "it's only logistics, I'm just practical"; Linchpin — "I'm just sociable,
  it's only my friends." Surface discriminator: do they **overtly drive** the group, or **quietly bridge
  across** it? On the coordination anchor, the Organiser narrates *doing* ("I sorted / booked / got
  everyone to…"); the Linchpin narrates *connecting* ("I introduced X to Y," "everyone tells me things,"
  "I keep the threads together"). CANOE corroboration *only* (never the definer): Organiser reads visibly
  high-Conscientiousness and overtly extraverted; the Linchpin reads quieter than you'd expect for
  someone so central — lower Neuroticism, high Agreeableness, connecting without the push. Spell the
  contrast out in both dossiers — it's the marquee group-chat compare.
- **Bookworm ↔ Artist** — both "do their own thing offline" (shared withdrawal-into-the-personal). Split
  on Need: the Bookworm protects *independent knowing* (input / retains); the Artist protects *the part
  of the work that's theirs* (output / makes). Lie tell: Bookworm — "learning on my own costs nothing";
  Artist — "being seen won't cost me what's mine" (both "costs nothing"-shaped, but one denies the cost
  of independence, the other the cost of recognition). Surface discriminator: retains knowledge vs
  makes things.
- **Self-Optimiser (internal: body ↔ career)** — one card, two domains; same Want (control via
  optimisation), same Lie ("if I optimise hard enough I'm in control of my outcomes"). Because Want *and*
  Lie match, the triad says **don't split** — confirm the interview needn't, and only split back out if
  playtest shows body vs career genuinely route apart.
- **Bookworm ↔ Tinkerer** — the closest pair in *psychology*: the same independent-self-enrichment
  temperament, the same quiet individualism, and both read the politeness anchor the same way ("hadn't
  framed it as a social encounter"), so neither Want nor [P] separates them. They part on the
  **direction the same drive points** — and that direction is exactly what's salient to the AI-state.
  The Bookworm runs **inward / cerebral**: enrichment as knowing, lived in the head and in conversation
  (and so leaves a *legible* trail of words/ideas). The Tinkerer runs **outward / physical**: enrichment
  as making and mending with the hands (and so leaves a *low-yield* physical-world trail — the part of
  #3 anomaly that matters). Lie tell: Bookworm — "learning on my own costs nothing" (cost-denial of
  epistemic independence); Tinkerer — "standing a bit apart is a self-sufficient way to be" (apartness-
  as-sufficiency, while still community-dependent). Surface discriminator (the §3.4 skill topic is
  purpose-built for this): faced with a new skill, the Bookworm *reads / watches / reads around it* (to
  know); the Tinkerer *just has a go and makes it work* (to do). Cerebral-inward vs hands-outward. (NB a
  different cut from Bookworm↔Artist: there the split is knowing vs *expressive* making; here it's
  inward-knowing vs *practical/physical* doing.)
- **Skeptic ↔ Wildcard** — both present a *"you won't pin me" surface* that is, in fact, **a front over
  a mappable person** — so don't be fooled into reading either as genuinely illegible. They split on
  *what the front is and what it protects*. The Skeptic's front is **ironic distance**, and it's
  consistent — the same see-through-it move every exchange; the Lie ("seeing through it is resistance")
  protects a self-image of *cleverness / not being fooled* (he *wants* to be read as the one who sees
  it). The Wildcard's front is **scramble** — tonal jumps and non-sequiturs; the Lie ("the unreadable
  surface keeps the real me safe") protects against *being truly seen at all* (he wants *not* to be
  reached). Tell: the Skeptic's distance is patterned and self-flattering; the Wildcard's is erratic and
  self-concealing — and both resolve on inspection. This also shapes the reveal: a stable ironic read
  routes Skeptic; a scrambled-but-resolving read routes Wildcard and rides the slow "unusual pattern"
  framing (§8.6), landing on *read-through-anyway* rather than *unreadable*.
- **Power User ↔ Self-Optimiser** — both sit *on top / ahead* (shared mastery posture; both Join
  sincerely). Split on the *object* of mastery, which is the Want: the Power User masters the **external
  tool/system** (wants recognition as the one ahead); the Self-Optimiser masters the **self** (wants
  control over their own outcomes). Lie tell: Power User — "mastering the tool means I'm ahead of *it*"
  (outward, about the system); Self-Optimiser — "if I optimise hard enough I'm in control of *my*
  outcomes" (inward, about the self). Surface discriminator: do they evangelise *outward* (recommend,
  early-adopt) or track *inward* (routine, metrics, self)?
- **Machine Companion ↔ Social Linchpin** — both run on **Belonging** and read as people-warm, so warmth
  alone won't separate them. The politeness anchor [P] does it cleanly: the Companion's warmth points *at
  the machine* (the bond is with the AI); the Linchpin's warmth points *at people* (the AI is just a tool
  others use — they answer the AI question by talking about who else uses it). Lie tell: Companion — "it
  cares back"; Linchpin — "I'm just sociable, it's only my friends." Where the relationship lives —
  with the AI or with the human web — is the whole split.

Neighbours rarely differ on *everything*: find the one triad field where they part — usually the Lie —
and route on that.

### 8.5 Tie-breakers, performer risk, and the never-route-by-asking guard **[GUIDANCE]**

- Each confused pair gets a **dedicated 1–2 discriminator** (above) the agent reaches for when a read is
  ambiguous between exactly those two.
- **Performer risk** ([MECHANICS §IV.C](../MECHANICS-RESEARCH.md)): the Skeptic is the player who's done
  enough quizzes to feed you the "right" signals. Don't fight it — behaviourally-specific questions are
  hard to perform smoothly, and the performance *itself* is the Skeptic classification. File it.
- **Infer, don't interrogate.** Routing pressure must never justify a never-ask question (§7) — the read
  comes from *pattern*, never from a real fact. If a discriminator could only be settled by soliciting
  something forbidden, the agent stays ambiguous and leans on the "unusual pattern" framing instead.

### 8.6 The routing threshold = the stop rule **[LOCKED]**

"Signal sufficient" is the *same* boundary already locked in **§4 (stop rule, condition 3)**: the agent
can name a single best-fit archetype. Do not define a second threshold here. At the 6-exchange ceiling it
routes on best available evidence, and residual ambiguity is carried diegetically by the "unusual pattern
/ additional data required" framing (§5) — the *slow-read* tail, which leans toward the **Wildcard**.
Note the reframe (archetypes.txt): the Wildcard is not genuinely *unmappable* — the scramble is a front
that resolves on inspection, so the slow read still ends in a single best-fit route; the diegetic
"unusual pattern" colours the *speed*, and the dossier lands on read-through-anyway, not unread.

## 9. What this hands to Epic 2 / out of scope here

- **In scope, locked above:** the two-floor principle and late reveal; the *exchange* unit and ~5 modal /
  3–6 band; the 3-anchor backbone (by function); the stop rule; variance-as-content; the technique-palette
  shortlist and screen; the never-ask principle; **the routing principles (§8 — best-fit model, signal
  hierarchy, overlap discriminators, threshold).**
- **Epic 2 authoring (the playbook knowledge file):** exact anchor wording (×2–3 phrasings each); the
  *final prose* of the per-archetype discriminant signatures and per-confused-pair discriminator
  phrasings (the **developed workings are now in §8.3–8.4** — Epic 2 turns them into final knowledge-file
  wording, not new logic); and the question-type taxonomy with examples — building on §8 and
  [MECHANICS §IV.D/G + §IV.D-bis](../MECHANICS-RESEARCH.md).
- **Out of scope (other deliverables):** the exact dossier wording and the link-out handoff
  ([CONTENT-ARCHITECTURE.md](CONTENT-ARCHITECTURE.md)); the enumerated never-ask list (GUARDRAILS.md v1.0).
