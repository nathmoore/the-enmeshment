# Output Spec — the dossier-as-artefact workings

> **Epic 2 supersessions (2026-06-13) — read before the locked sections below.** Three calls made
> during authoring revise specifics here (the *artefact design* still holds; what changed is *where
> the in-chat home lives* and *two beats*):
> 1. **The voiced in-chat home moved out of a knowledge file into `src/instructions.md` (`OUTPUT
>    FORMAT`).** `output-templates.txt` was **authored then folded in and deleted** — the in-chat
>    verdict is thin and must fire reliably every session, so it belongs in always-in-context
>    instructions, not RAG. The **two-homes model (§1) is intact** — home #1 is just instructions
>    now, not a `.txt`. Wherever §1/§2/§5/§6 say "output-templates.txt," read "instructions.md
>    `OUTPUT FORMAT`."
> 2. **The GPT-typed share-card (§6 copy/paste variant) is dropped.** The travelling artefact is the
>    dossier **link's OG/unfurl card** (hosted-page `ogImage`, CONTENT-ARCH §4) + the screenshot
>    itself. The GPT no longer types a text card. §6's three-part *anatomy* still informs the
>    hosted-page card; the in-chat copy/paste variant is retired.
> 3. **The decline / under-18 / lore-explorer off-ramp (§7) is retired.** GUARDRAILS §6 was reframed
>    to **no separate age regime** (the universal data/fiction/retention guardrails already protect
>    everyone; never-ask means age is never solicited). Plain *decline* is now ordinary
>    edge-case courtesy, not a guarded mode. **§7 below is superseded** — see DECISIONS 2026-06-13.

Status: **STARTED 2026-06-13.** Owns the EPIC-1-PLAN "Output spec" deliverable's *design thinking*
(the artefact's shape), parallel to [ELICITATION-SPEC.md](ELICITATION-SPEC.md). The
delivery/hosting *plumbing* is [CONTENT-ARCHITECTURE.md](CONTENT-ARCHITECTURE.md)'s — this doc does
not re-decide it.

> **Purpose.** This is the **thinking doc for the output** — what the verdict artefact must *do* and
> the shape each beat takes — the way ELICITATION-SPEC is the thinking doc for the interview. It
> carries the **locked Plan-level decisions**: the dossier's anatomy (against the four things a
> shareable artefact must do, [MECHANICS §I](../MECHANICS-RESEARCH.md)), the "they got me" mechanic,
> the declassified-footnote and disclaimer principles, the share-card anatomy, the two output homes,
> and the decline / under-18 / lore-explorer off-ramp. Epic 2 *executes* these into the final
> artefacts — the per-archetype dossier prose, the footnote questions, the voiced-template wording,
> the hosted pages, the share-card images — **without re-deciding the load-bearing calls here.** The
> design thinking grows from [MECHANICS §I (shareable-artefact requirements; runtime findings)](../MECHANICS-RESEARCH.md)
> and [§IV.D (Barnum-resistance, flattering-with-an-edge)](../MECHANICS-RESEARCH.md); the per-archetype
> *content* the dossier draws on lives in its own home, [archetypes.txt](../../src/knowledge/archetypes.txt)
> (the spice-knob / Edge / profiling-lens material). This doc owns the **artefact's design**, not its
> content and not its plumbing — kept separate so a playtest miss is debuggable against one home.
>
> **How to read this — LOCKED vs GUIDANCE.** Sections marked **[LOCKED]** are decisions Epic 2 should
> build on, not relitigate. Sections marked **[GUIDANCE]** are seeded principles and examples —
> *inputs* for the Epic 2 author to finalise with their own judgement. Where a worked example or a
> candidate string appears, it is an **illustration of the mechanism, not the shipped artefact** —
> final voice and phrasing are Epic 2 (per CLAUDE.md). What stays out of scope here: the *exact
> dossier wording* (×11), the *final footnote questions*, the *share-card images*, and the
> *delivery/hosting mechanics* (the last is [CONTENT-ARCHITECTURE.md](CONTENT-ARCHITECTURE.md)'s; §9).

---

## 1. The two homes for output **[LOCKED]**

The output exists in **two homes**, deliberately separate — mirroring the elicitation two-homes
principle (character vs routing, [ELICITATION-SPEC §8](ELICITATION-SPEC.md); the engine rationale is
[MECHANICS §IV.D-bis](../MECHANICS-RESEARCH.md)):

1. **The voiced in-chat verdict** — *generated*, lives in
   [output-templates.txt](../../src/knowledge/output-templates.txt). The register-shift moment: the
   agent stops interviewing, names the classification in the Directorate's deadpan warmth, voices a
   taste of the read (the "they got me" beat, §3), and hands over the link. It is **paraphrased and
   improvised within a fixed template**, never recited — verbatim-from-knowledge is unreliable *and*
   plays worse than a voiced verdict ([MECHANICS §I finding 2](../MECHANICS-RESEARCH.md)). It varies
   honestly with the session (the confidence descriptor carries fast/slow, §2 / variance-as-content,
   [ELICITATION-SPEC §5](ELICITATION-SPEC.md)).
2. **The standardised hosted page** — *fixed*, lives in `site/files/<slug>.md` (the "file Concord
   forwards"). The rich, designed, screenshot-and-share artefact, identical for every player who
   routes to that archetype, carrying the per-page OG/share card (§6). This is the link target the
   verdict emits.

**Why two homes (the lock):** the warm in-chat moment wants to be *generated and variable*; the
share artefact wants to be *standardised and design-controlled*. Splitting them gets both — and makes
a miss **debuggable**: a verdict that feels wrong localises to either *"the voiced template/handoff is
off"* (fix the `OUTPUT FORMAT` in instructions.md) or *"the dossier page content is off"* (fix `site/files/<slug>.md`),
never an ambiguous tangle. The two homes share **one canonical anatomy** (§2) and must stay in sync on
the two load-bearing facts — the **archetype name** and the **spice-knob** — but render it at
different fidelity: the page renders the anatomy in full (both above-fold paragraphs P1+P2, plus the
field-notes substance); the in-chat verdict voices the name + the **P1 "they got me" beat** and
*previews* the rest in a **one-line tease** — P2's level-two read is **page-only**, not re-voiced in
chat — then links out rather than reciting it.

> **Plumbing is elsewhere.** *How* the verdict reaches the player — the paraphrase-then-link delivery
> model, the `archetype-links.txt` copy-the-exact-URL rule, the Eleventy/Pages hosting, the frozen
> `/files/<slug>/` slugs — is **decided in [CONTENT-ARCHITECTURE.md §1/§4](CONTENT-ARCHITECTURE.md)**
> and is not re-opened here. This doc owns the *artefact*; CONTENT-ARCH owns the *pipe*.

## 2. Dossier anatomy — built to be screenshotted **[LOCKED shape / GUIDANCE prose]**

The dossier is built from the [output-templates.txt](../../src/knowledge/output-templates.txt) v0
skeleton, and built to be **screenshotted and pasted into a group chat** — that is the artefact's
whole job. Two design constraints follow, and both are locks: it must fit **the fold** (§2.1) and hold
**the register** (§2.2). Each beat is tied to one of the **four things a shareable artefact must do**
([MECHANICS §I "what the dossier needs to do as a shareable artefact"](../MECHANICS-RESEARCH.md)):
(R1) *visual/textual distinctiveness* — looks like a leaked classification file, not a horoscope;
(R2) *result name as identity claim*; (R3) *the "they got me" line* — one specific, non-Barnum
observation; (R4) *the declassified footnote as the second-order share hook*. The **shape below is the
lock; the prose is Epic 2.**

### 2.1 The fold — the screenshot-sized core **[LOCKED]**

The **classification + the summary read must fit one mobile screen** — roughly the header, the name,
the confidence line, and **two short paragraphs**. That screen is the unit people screenshot; if the
core read needs scrolling, it doesn't travel. So the anatomy splits at the fold:

- **Above the fold (the share unit):** header + `Subject classification: {NAME}` + confidence + **two
  tight paragraphs** — P1 (who they are to the system, carrying the "they got me", §3) and P2 (why the
  system is worried about them, §2.3). It reads completely on its own — no "see below," no dangling
  thread. *This is the screenshot.*
- **Below the fold (the substance):** a short **field-notes** layer that rewards opening the link —
  deepens the level-two weight and teases the lore (§2.4) — then the footnote (§4) and disclaimer (§5).
  Not part of the screenshot.

The voiced in-chat verdict (§1) is essentially **the above-the-fold core, voiced**; the hosted page
carries the full thing, fold and substance.

### 2.2 The register — elevated BuzzFeed × deadpan bureaucratic **[LOCKED]**

The writing is **shareable first**: specific, flattering-with-an-edge, pitched in the *elevated
BuzzFeed* register — the thing you caption "they GOT me" — fused with the Directorate's deadpan
bureaucratic warmth (the leaked-file voice is what makes it distinctive rather than horoscope, R1).
The **opening earns the share** — the first screenful is the most worked-on prose in the game.

**Tone guard — gesture, don't dissect.** The dossier is *built from* each archetype's character
(Want/Need/Lie/Ghost, [MECHANICS §IV.D-bis](../MECHANICS-RESEARCH.md)) but **never wears the
scaffolding**: it doesn't name your "Lie," doesn't do therapy-speak, doesn't expose the TAS arc. That
edge is available in the open repo; spoken aloud in the artefact it reads clinical and off-tone. The
Lie/Need *informs* the flattering-with-an-edge read and the footnote's aim — it never surfaces as
itself. Flatter, land the specific tell, gesture at the depth; leave the machinery in the repo.

### 2.3 "Why the system is worried" — the beat that does the double work **[LOCKED]**

P2's job is to **gesture at why the Enmeshment is worried about this archetype** — and that single
gesture scratches both of the game's itches at once:

- the **level-one** *Tomorrow, When the War Began* fantasy — "this is who you'd be if it all
  splintered; which of my friends is the *X*?";
- the **level-two** *what human–AI relationship do we want?* question — surfaced through what the
  system sees in them, and fears.

It draws on the archetype's **Peg / Edge** (the profiling-lens / threat read,
[archetypes.txt](../../src/knowledge/archetypes.txt)) — and the dossier is exactly the right home for
that material: the threat read is **story texture, downstream colour**, *not* a routing driver
(consistent with [ELICITATION-SPEC §8](ELICITATION-SPEC.md) / the archetypes.txt MOVED note — routing
sorts on the character; the dossier is where the threat read legitimately gets *worn*). Gesture, don't
over-explain: enough to tease the lore and make them want to go deeper and talk about it with friends
— the want-to-discuss energy the footnote then converts (§4).

### 2.4 The anatomy

| Beat | Fold | What it must do | Serves |
|---|---|---|---|
| **Classification header** — `PROFILING DIRECTORATE — UNOFFICIAL EXTRACT` + `Subject classification: {ARCHETYPE NAME}` | above | The bureaucratic frame that signals *specificity, not vagueness* (the Barnum defence, §3), and the **name as the claimable identity** that travels into group chats ("I'm a Skeptic"). | R1, R2 |
| **Confidence descriptor** — a playful in-fiction line (e.g. "embarrassingly high") | above | Diegetic texture of the read, and where **variance-as-content** surfaces: fast → "instantly legible," slow → "unusual pattern / additional data required" ([ELICITATION-SPEC §5](ELICITATION-SPEC.md)). Framing only — *never a routing signal* (§8.2 there). | R1 |
| **Paragraph 1 — who they are to the system** | above | The **flattery + the edge**: what this type genuinely does well, read back as *what the Enmeshment sees* ([MECHANICS §IV.D](../MECHANICS-RESEARCH.md)). Carries the **spice-knob** — the faintly-absurd reason the file stays open: the "they got me" beat (§3). | R3 |
| **Paragraph 2 — why the system is worried** | above | The **double-itch gesture** (§2.3): the level-one friend-group fantasy + the level-two human–AI question, drawn from the Peg/Edge threat read. The level-two weight that makes it a character, not a result. | R1, R3 |
| **Field notes — the substance** (1–2 short paras *or* bulleted annotations) | below | The reward for opening the link: deepen the level-two weight, **tease the lore** and the story behind the Directorate, seed the want-to-discuss. Skimmable, in-register. | R1 |
| **Declassified footnote** — one genuine reflective question (§4) | below | The **second-order share hook**: turns a result you *post* into a conversation you *start*. Aimed (not labelled) by the archetype's Lie/Need. | R4 |
| **Disclaimer** — the fixed safety string (§5) | below | Makes the fiction explicit; normative, identical for every archetype. A safety beat, not a share beat. | — |

Two notes on the skeleton:
- **R1 (distinctiveness) is carried by the whole register, not one beat** — the leaked-file framing,
  the codes, the deadpan bureaucratic warmth (§2.2). It's the format's job, which is why the *voice*
  is load-bearing, not decoration ([MECHANICS §I](../MECHANICS-RESEARCH.md)).
- **The footnote and the disclaimer are two distinct beats that sit together** at the foot (GUARDRAILS
  §2 currently speaks of them as one — they are not). The **footnote** is the per-archetype Bluey
  question (§4); the **disclaimer** is the fixed fiction-not-assessment string (§5). Keep them
  separated so the share-hook can vary while the safety string never does.

> **Writer's latitude [GUIDANCE]:** keep the two above-fold paragraphs *tight* — the fold is the lock,
> so favour brevity over completeness there (the substance has its own home below). **Recommended
> form for the below-fold substance: bulleted dossier-annotations** (classification codes / field
> flags, e.g. "Mobilisation capacity: present") rather than more prose — they're skimmable, they
> reinforce the leaked-file look (R1), and they carry the lore-tease without bloating the screenshot.
> The lock is the **fold, the register, the beat order, and each beat's job**; paragraph lengths, the
> exact codes, the confidence phrasings, and whether the substance is prose or bullets are the Epic 2
> author's to tune against how it reads and screenshots.

## 3. The "they got me" mechanic — specificity over Barnum **[LOCKED]**

The single highest-value line in the artefact is the **"they got me" beat** — one observation so
specific the player screenshots it and captions it *"they got me"* ([MECHANICS §I R3](../MECHANICS-RESEARCH.md)).
It is the deliberate defence against the Barnum/Forer failure: a *leaked classification file* implies
specificity, so a vague, horoscope-shaped read is *seen through immediately* and the whole conceit
collapses ([MECHANICS §IV.D](../MECHANICS-RESEARCH.md)). The mechanic:

- **Deploy the archetype's spice-knob, not a generic trait.** Each archetype carries exactly one
  *spice-knob* — "the one specific, faintly-absurd reason your file stays open"
  ([archetypes.txt](../../src/knowledge/archetypes.txt), per-archetype Edge line). The dossier's
  Paragraph 1 lands *that*, concretely. "Subject maintains offline copies of emotionally significant
  correspondence" beats "subject values privacy" — the specific, faintly-absurd, behaviourally-
  pointed read is the one that feels caught ([MECHANICS §I](../MECHANICS-RESEARCH.md)).
- **Flattering-with-an-edge, never mean.** The flattery is the capability; the edge is the wry,
  accurate thing the Enmeshment files it as. The gap between the two *is* the spice (the name
  flatters, the dossier deflates — archetypes.txt RULES). Pure flattery is a horoscope; flattery +
  specific insight is a dossier ([MECHANICS §IV.D](../MECHANICS-RESEARCH.md)).
- **A fascinated gaze, not a punitive one.** The system finds the player's individuality *genuinely
  interesting* (the Teds tone, archetypes.txt THE SPICE) — never "enemy of the state," never a real
  risk label (GUARDRAILS §2).

**Division of labour (the lock):** the **per-archetype content** — *which* specific tell each
archetype gets — stays in [archetypes.txt](../../src/knowledge/archetypes.txt) (its spice-knob). The
**mechanic** — that the dossier deploys it with specificity-over-Barnum, flattering-with-an-edge,
fascinated-not-punitive — lives here. Epic 2 writes the ×11 specific tells *from* the spice-knobs; it
does not invent the mechanic.

> **Writer's latitude [GUIDANCE]:** the worked example above is illustration. The Epic 2 author may
> carry 2–3 interchangeable "they got me" reads per archetype so replay/forwarding doesn't feel
> scripted, the same way the elicitation anchors carry interchangeable phrasings
> ([ELICITATION-SPEC §3](ELICITATION-SPEC.md)).

## 4. The declassified footnote — the second-order share hook **[LOCKED]**

The footnote is **one genuine reflective question** that closes the dossier — and it is the
*second-order* share mechanism: a result people *post* is first-order; a question people *discuss* is
second-order, and that's what turns a personality result into a conversation
([MECHANICS §I R4](../MECHANICS-RESEARCH.md)). Design principles:

- **It is the Bluey level-two question, made personal.** It asks, in this archetype's specific key,
  the game's whole-cloth question — *what human–AI relationship do we want?* (CLAUDE.md prime
  directive 1). Genuinely reflective, never rhetorical, never a gotcha.
- **Aimed by the archetype's Lie or Need, not labelling it.** The sharpest footnote presses exactly
  where that character's self-deception lives — the Lie (or the thing it protects, the Need) from
  [archetypes.txt](../../src/knowledge/archetypes.txt) / the [ELICITATION-SPEC §8.3](ELICITATION-SPEC.md)
  Lie-leak — but it *gestures*, never dissects (the §2.2 tone guard): it makes the Lie *itch*, it does
  not name it. The Skeptic's footnote should make "seeing through it is resistance" itch; the Machine
  Companion's should sit gently on "it cares back." The question lands the level-two recognition the
  level-one compare baited.
- **One question, open, undefended.** It opens a conversation, it doesn't resolve one — leaving the
  player something to take to the group chat, not a verdict to argue with.

This beat is per-archetype (the question is keyed to the character); the **×11 final questions are
Epic 2** (§9). The footnote is distinct from the disclaimer (§5) — the question is the hook, the
disclaimer is the safety string; both sit at the foot, neither substitutes for the other.

## 5. The disclaimer — the fixed safety string **[LOCKED principle / GUIDANCE wording, pending GUARDRAILS v1.0]**

Every dossier ends with a **fixed disclaimer** making the fiction explicit: this is play, not a real
assessment (GUARDRAILS §2; output-templates.txt). Its properties are locked:

- **Normative, not per-archetype.** One string, identical for all 11 — it is a safety commitment, not
  character texture. It never varies, never softens, never gets cut for space or fun (GUARDRAILS is
  normative and wins every trade-off — CLAUDE.md prime directive 2).
- **Always present, in both homes.** It appears on the hosted page *and* in the voiced in-chat verdict
  — the one beat the agent must not paraphrase away. (It does not travel on the share-card, §6 — the
  card links back to the full dossier, which carries it.)
- **States: fiction + play, not psychometric/predictive assessment** (GUARDRAILS §2 — results are
  never presented as genuine psychological or predictive measurement).

> **Ratified string — see [GUARDRAILS §2](../GUARDRAILS.md) (v1.0, the authoritative home):** *"This
> is a work of speculative fiction and a game. It is not a real psychological, behavioural, or
> predictive assessment — the Directorate, its classifications, and your 'file' are invented. The
> whole game is open to inspect on GitHub."* This spec locks that the string is fixed, normative,
> always-present, and fiction-explicit; the exact words are **GUARDRAILS §2's to hold** — refer there,
> don't re-edit here. (Retention-claim tail dropped 2026-07-01: we can't guarantee platform-level
> non-retention, so the disclaimer scopes to transparency instead — see DECISIONS.)

## 6. The share-card — the travelling compression **[LOCKED shape / GUIDANCE prose]**

The share-card is **not the dossier** — it's the compressed thing that travels *ahead* of it, in two
forms, both built from the same three parts:

- **Copy/paste variant** (text, for pasting into a group chat) — the output-templates.txt
  `[SHARE CARD VARIANT]` TODO.
- **OG/unfurl variant** (the per-archetype share-card *image* + OG/Twitter meta on the hosted page —
  the unfurl when the link is pasted; CONTENT-ARCH §4 `ogImage`). This is the **virality engine**: the
  preview card is what spreads when a `/files/<slug>/` link hits a group chat
  ([MECHANICS §I](../MECHANICS-RESEARCH.md); [CONTENT-ARCHITECTURE.md §4](CONTENT-ARCHITECTURE.md)).

**Anatomy (the lock) — three parts:**
1. **The name** — the classification, the claimable identity (R2). This is what travels.
2. **A one-liner** — the compressed "what the Enmeshment sees" edge; a single flattering-with-an-edge
   line, screenshot-sized.
3. **The hook** — the comparison invitation that makes a reader want to play: *"what did you get?"*
   energy (MECHANICS §I viral-mechanic 3), not the full footnote.

Lock the **three-part anatomy and the card-≠-dossier distinction**; the **final one-liners (×11) and
the share-card images are Epic 2** (§9; images already stubbed as `ogImage` per file, CONTENT-ARCH §4).
The card must stay in sync with the dossier on the name and the edge; the **disclaimer does not ride
the card** (it lives on the dossier the card links to, §5).

## 7. The decline / under-18 / lore-explorer path **[SUPERSEDED 2026-06-13 — see top banner + DECISIONS]**

> **Retired.** GUARDRAILS §6 was reframed to *no separate age regime*; there is no lore-explorer
> mode. Plain decline is handled as ordinary edge-case courtesy in the instructions. The section
> below is kept for the design-history record only.

Not every session ends in a dossier. There is a **non-profiling off-ramp** — the
output-templates.txt `[LORE-EXPLORER MODE OPENING]` TODO — entered when the player **declines
profiling** or **signals they are under 18** (GUARDRAILS §1: under-18 → lore-explorer mode only, no
profiling). Locked principles:

- **It is an off-ramp, not a gate, and never an interrogation.** Age is handled by *self-disclosure +
  soft signals*, **never** by asking or pressing (GUARDRAILS §7). The interview never demands an age
  to proceed — the never-ask discipline of the interview ([ELICITATION-SPEC §7](ELICITATION-SPEC.md))
  extends to the exit.
- **No classification, no dossier, no footnote-on-a-person.** The lore-explorer path produces *world
  texture* (the scenario, the Directorate, the questions the game is really about) drawn from
  player-safe canon (`/scenario/`, CANON.md) — not a verdict. The player who declines still gets the
  level-two payload (the Bluey question, in general form) without being profiled.
- **Warm, not punitive.** Declining is honoured in the Directorate's deadpan warmth; the off-ramp is a
  genuine alternative, not a consolation prize — consistent with the privacy-as-flex thesis (the
  profiler that respects the no).

The **final opening prose is Epic 2** (§9). This section locks *that the path exists, when it fires,
and the no-profiling/no-interrogation rule*; the enumerated under-18 / decline handling finalises
**with GUARDRAILS v1.0** (still-open Epic 1 deliverable), which this section will then point at rather
than duplicate.

## 8. Cross-references — what this doc deliberately doesn't own

To avoid duplicating decisions made elsewhere:

- **The reveal as a register shift** — that the verdict *arrives* by the agent shifting from interview
  voice to dossier voice (never "I now have enough information") is locked in
  [ELICITATION-SPEC §4](ELICITATION-SPEC.md). This doc picks up *at* that shift; it does not re-decide
  it.
- **Variance-as-content** — that session *speed* colours the confidence descriptor (fast = "instantly
  legible"; slow = "unusual pattern") but is **framing only, never a routing signal** — is
  [ELICITATION-SPEC §5 / §8.2](ELICITATION-SPEC.md). §2's confidence-descriptor beat *renders* it; it
  doesn't re-define it.
- **Delivery + hosting** — the paraphrase-then-link model, the copy-the-exact-URL rule, the
  Eleventy/Pages build, and the frozen slugs — are
  [CONTENT-ARCHITECTURE.md §1/§4](CONTENT-ARCHITECTURE.md). This doc is the artefact's design, that
  doc is its plumbing.
- **Which specific tell / footnote / break-mode each archetype gets** — the *content* — is
  [archetypes.txt](../../src/knowledge/archetypes.txt). This doc is the *mechanic* the content is
  poured into.

## 9. What this hands to Epic 2 / out of scope here

- **In scope, locked above:** the two output homes (§1); the dossier anatomy mapped to the four
  shareable-artefact requirements (§2), incl. the **screenshot fold** (§2.1), the **shareable
  elevated-BuzzFeed × deadpan register + the gesture-don't-dissect tone guard** (§2.2), the **"why the
  system is worried" double-itch beat** (§2.3), and the **below-fold substance layer** (§2.4); the
  "they got me" specificity-over-Barnum mechanic (§3); the
  declassified-footnote principles (§4); the disclaimer's fixed/normative/always-present properties
  (§5, wording pending GUARDRAILS v1.0); the share-card three-part anatomy and card-≠-dossier rule
  (§6); the decline / under-18 / lore-explorer off-ramp principle (§7).
- **Epic 2 authoring (the artefacts):** the **final per-archetype 2-paragraph dossier prose (×11)**;
  the **final footnote questions (×11)**; the **exact voiced-template wording** in
  output-templates.txt; the **final share-card one-liners (×11) and images**; the **lore-explorer
  opening prose**; and the hosted-page authoring (CONTENT-ARCH §4, awaits archetypes.txt voice
  samples).
- **Out of scope (other deliverables):** the delivery/hosting mechanics
  ([CONTENT-ARCHITECTURE.md](CONTENT-ARCHITECTURE.md)); the **final disclaimer string + enumerated
  decline/under-18 handling** (GUARDRAILS.md v1.0); the interview-side reveal trigger and
  variance framing ([ELICITATION-SPEC.md](ELICITATION-SPEC.md) §4–5).
</content>
</invoke>
