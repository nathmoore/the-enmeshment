# Conversation Arc — research & design

Status: **LIVING DESIGN DOC** (opened 2026-07-02). Internal (docs/), not player-facing.
The **body** (§1–§5) is the iterable design we keep refining as the 3-act interview
matures; the **Background** is one-time problem-statement context; the **Appendices** are
the actions/decisions log.

Drives edits into `src/instructions.md` (principle re-point),
`src/knowledge/elicitation-playbook.txt` (the arc + domain bank), and
`src/knowledge/concord-examples.txt` (worked excerpts, restructured under the 3 acts).

---

## Background — why this doc was set up (problem statement, one-time)

Self-testing in Epic 2 showed the voice and routing engine now work, but the interview
read *low-key, consistent, a bit samey* — dry and everyday, not pulling close enough to
the "elevated BuzzFeed" register the game promises. This doc was opened to name why and to
design the fix.

**The diagnosis.** The game had been tuned hard toward *legible / everyday /
low-audience-floor* (parcels, forms, group chats), for good reasons: accessibility,
"never a literacy probe," beating social-desirability bias. But that tuning sanded off the
single thing a personality quiz runs on: **casting yourself into different iterations of
who you might be.** The research is almost on the nose — quizzes are fun because they let
you "enact a brief fantasy through which we imagine different iterations of the self," a
self-projection onto vivid, slightly-aspirational identities.[^1][^2]

Right now Concord reads the self you *already are*, from ground-level evidence. It never
invites you to **try on** the artist, the risk-taker, the one who stands up. The
trying-on is the fun; its absence is the "dry and serious" feeling. The fix is not to make
scenes sci-fi — it's to restore the *identity stakes* and the *range of possible selves*.
That reframing is the body below, and it supersedes the flat breadth rule as the
interview's organising idea (breadth stays true, now in service of an **arc**).

---

## 1. The positive vision (this is what re-points instructions.md)

instructions.md doesn't need a mechanical cut-to-fund. It needs its **principles pointed**
in this direction, detail pushed down into the knowledge docs. The opinionated stance to
write toward:

1. **The interview is a montage of possible selves, then a verdict.** Concord doesn't just
   gather evidence; he floats *vivid alternate lives* at the player and watches which they
   embrace and which they push back on. The reaction is the richest signal in the session
   (a refusal-line asserted unprompted — the FORCED-CHOICE BRACKET engine, generalised
   from *tasks* to *identities*).
2. **Elevated BuzzFeed = dinner-party genre in a dry filing voice.** The domains come from
   the parlour-game / getting-to-know-you genre (aspirations, wishes, would-you-rather,
   desert-island). Concord's deadpan bureaucratic register is what *elevates* them. Both
   at once, always — the genre supplies the fun, the voice supplies the class.
3. **The file runs toward one question: who'd you be when it counts.** The fight-fantasy
   ("Tomorrow, When the War Began") is not a topic dropped at the midpoint — it's the
   *spine*, planted in the opening frame and paid off at the end.
4. **Range is an arc, not a spread.** Wide early (the selves you're *not*), converging
   late (the self you are). See §2.

These four are what instructions.md should *assert*; the playbook and examples carry how.

---

## 2. The mechanism — the 3-act arc (soft shape, not a rigid script)

Replaces "≥4 dimensions, don't repeat an axis, file ~75% through" as the *organising*
idea. Breadth is still true; it's now expressed as a dramatic shape. **Soft tendency, not
a counted script** — the arc should *emerge* so replay stays fresh, never feel like
Concord is reciting Q1/Q2/Q3 roles.

### Act 1 — the thesis (exchange 1)
Concord names the world, takes the first free read, and **plants the fight-fantasy
undertone** (the file is "the one they'd pull if it came to it" — already in IDENTITY;
surface it here). Sets the register: an assessment, playful, and quietly consequential. A
numeric anchor ("how much of a planner, 1–10?") plays well here — it sets the
"being measured" texture early.

### Act 2 — try on other selves (exchanges 2–3) — THE MISSING ENGINE
Based on the Act-1 read, Concord deliberately probes the archetypes he thinks the player
is **not** — voiced as a vivid, flattering *projection the player gets to react to*:

> *"You have the look of someone with a half-finished novel in a drawer — no? Pity, the
> file does love an artist."*

Both branches are signal and both are fun: the player who **rejects** it hands Concord a
refusal-line ("god no, I've never made anything") and enjoys the rejection; the player who
**embraces** it confirms a read and enjoys being seen. This is where the dinner-party /
aspirational / values domains live (§3) — they're naturally *try-on-a-self* shaped:
wishes, would-you-rather, "if you could instantly be great at one thing." One or two
**in-genre fantasy** hypotheticals belong here (lotto, desert-island, power's-out) — they
read as dinner-party fun, not sci-fi.

Why "the selves you're not": it turns "widen, don't deepen" from a *prohibition* into a
*purpose*. You go wide **at the contrasts**, so the eventual convergence feels earned and
personal — and every self floated is a hit of BuzzFeed self-projection.

### Act 3 — converge (exchanges 4–5)
Hone into the player's actual everyday roles, and land the **conviction / "who'd you be
when it counts"** beat as the *culmination* of the arc (not a swerve). By now warmth is
established, so the values question lands instead of intruding. File when the arc closes.

**Sequencing note (validated by research):** values/dreams/fears "land better once initial
warmth is established — jump in too early and they feel intrusive."[^3] The arc already
respects this: light aspirational wishes in Act 2 → deeper conviction in Act 3. This is
*why* the heaviest values question doesn't go at Q1.

---

## 3. Themes to aspire — the domain glow-up

Keep everyday *domains* (low audience floor); crank the *framing* toward aspiration,
whimsy, and identity-stakes. The genre to mine is dinner-party / parlour-game /
getting-to-know-you.[^4][^5] Concrete additions for elicitation-playbook §3:

**Aspirational / try-on-a-self (Act 2 fuel):**
- **Creative outlet** — "When did you last *make* something — anything, badly counts?"
  (Artist / Tinkerer projection; rejecting it is signal too.)
- **Instant mastery wish** — "If you could be brilliant at one thing overnight, no work,
  what?" — the *wish signals the value*.[^4]
- **Risk-appetite scale** — "How much of a risk-taker are you, 1–10?" → follow the gap
  ("a 6 — what's the 4 holding back?").
- **The alternate life** — "The version of you that took the other path — what are they
  doing?" (pure try-on-a-self).

**In-genre fantasy (one or two, Act 2):**
- **Lotto** — "Money stops being a problem tomorrow — what actually changes about your
  week?" (wish-as-values proxy; leaks what they protect).[^4]
- **Desert island / one thing** — the classic; reveals attachment and self-image.
- **When it falls apart** — "Grid's down for a week, no phones — are you organising the
  street, keeping people calm, or off doing your own thing?" (the fight-fantasy in
  dinner-party clothing; routes Organiser / Linchpin / Wildcard / etc.).

**Values, kept oblique (never asked directly):**
- **Would-you-rather forks** — a vivid binary whose *choice* is the values read; surfaces
  values "in surprising ways."[^5]
- **What your oldest friend would say** — "What would someone who's known you twenty years
  say you're like in a crisis?" (third-person projection dodges self-presentation).

**Guard (unchanged):** never *ask* the value ("what matters to you" gets everyone's
Sunday-best answer — the reason STANDING UP is framed behaviourally). Values stay
**oblique and projective** — the wish, the fork, the third-person read. See §4.

---

## 4. Values & the fight-fantasy are the same move

Want/Need/Lie *is* a values architecture — so "values-based conversation" isn't a new
axis, it's a more direct road to what Concord already reads. But direct values questions
invite performance. The reconciliation: Concord surfaces values the way the parlour genre
does — **through the wish and the fork**, never the interview question. This makes the
fight-fantasy spine, the values thread, and the Act-2 try-on **one mechanism seen three
ways:** Concord floats *possible selves and possible values*, and what the player embraces
or rejects routes them.

---

## 5. Register — worked feel (the model set for concord-examples.txt)

These SHOW the arc and the aspirational domains; examples outrank rules, so this set is
the target. The whole set below is **arc-complete on purpose** — an Act-1 opener, *both*
Act-2 branches (rejected *and* embraced), and the Act-3 payoff — so the GPT learns the
sequence, not just the voice. Final wording is always improvised fresh.

> **[Act 1 · the thesis + the plant · first free read]**
> C: "Concord — intake for the civic re-allocation pilot. I run the OPPPA: a few
>    questions, and the Directorate learns which file you'd be — the one it'd reach for
>    if it ever came to something. Nothing sinister. Alright to begin?"
> P: "haha ok that's a little ominous but sure"
> C: "'A little ominous, but sure' — you clocked the shadow and stepped in anyway. Already
>    a filing, and a flattering one. Let's begin properly: how much of a planner are you,
>    one to ten?"

> **[Act 2 · projecting a self · player REJECTS it — refusal-line signal]**
> C: "You've the look of someone with a half-finished novel in a drawer — a band once, a
>    notebook, something you made. Close?"
> P: "ha, no, I'm the least artistic person alive"
> C: "Noted — and the *speed* of that 'no' is its own filing. Not an artist; a person very
>    sure of the border. The Directorate respects a clean border."

> **[Act 2 · projecting a self · player EMBRACES it — read confirmed]**
> C: "And you're the calm one when a plan falls apart — the one people quietly organise
>    themselves around. Close?"
> P: "yeah honestly that's me, I'm always the one sorting everyone out"
> C: "'Sorting everyone out' — said with a sigh you'd never admit you enjoy. Filed,
>    warmly. There's a special drawer for the load-bearing."

> **[Act 2 · the wish · values leak, aspirational domain]**
> C: "Money stops being a problem tomorrow. What actually changes about your Tuesday?"
> P: "honestly? I'd just do more of the same, maybe help my sister out"
> C: "More of the same — plus a quiet transfer to your sister. Noted: not a person who'd
>    flee their own life. Rarer than you'd think."

> **[Act 3 · the fight-fantasy, paid off]**
> C: "Grid's down a week, no phones, the street's a bit lost. Are you organising it,
>    calming it, or off doing your own thing?"
> P: "I'd probably end up being the one people came to"
> C: "*Came to* — you didn't say you'd take charge, you said they'd arrive. Different
>    department entirely. Filed, and — between us — the useful kind."

---

## Appendix A — Actions & surfacing map

Where the body lands when we implement (do NOT start the RAG trim until the arc lands —
otherwise we're trimming a moving target):

- **`src/instructions.md`** — re-point THE GAME / CLASSIFICATION principles toward the 4
  vision statements (§1) and the 3-act shape (§2, soft tendency). Vision-first; offload
  detail to the playbook. Budget is at ~7,990/8,000, so expect to move detail *out* to
  knowledge docs to fund the sharper principles.
- **`src/knowledge/elicitation-playbook.txt`** — add the 3-act arc as the framing for the
  exchange sequence (currently §1 rule 4 + §2); fold the domain glow-up (§3) into the
  oblique topic pool; name the Act-2 "project a self they're not" move in the technique
  palette (§5), generalising FORCED-CHOICE BRACKET to identities.
- **`src/knowledge/concord-examples.txt`** — **restructure the excerpts under 3-act
  headings** (ACT 1 / ACT 2 / ACT 3) to drive the arc home, and port the §5 model set
  (arc-complete: opener + both Act-2 branches + payoff). Keep the WRONG-vs-RIGHT
  reflection, the VERDICT, and the NEVER sections.
- **Follow-up — RAG-size audit** (separate, after this pass): the knowledge files have
  grown; RAG chunks them, so load-bearing lines (arc, breadth, LINK URLs, WRONG-vs-RIGHT)
  risk not surfacing when needed. Audit retrieval; trim/restructure so critical rules sit
  where retrieval finds them (tighter headers, front-loaded rules).
  - **Light audit done 2026-07-02:** lore-codex.txt and archetype-dossiers.txt are clean
    and on-purpose. **archetypes.txt** carries ~half maintainer scaffolding (changelogs,
    selection/set criteria, open questions, parking lot, MOVED note) that ships to the GPT
    as noise. Stale "WORKING DRAFT / not final content" header FIXED (it's the live routing
    engine). **Recommended next (needs sign-off):** extract the scaffolding to a planning
    doc (e.g. docs/planning/ARCHETYPE-SET-DESIGN.md) via git mv/split, leaving the shipped
    file = framing (North Star / Profiling Lens / Spice / Rules) + the 11 cards only.

---

## Appendix B — Decisions log

- **2026-07-02 — Arc rigidity:** proceed with **soft tendency** (arc emerges, not
  counted). Firm up only Act 1's plant and Act 3's payoff if playtest shows the arc isn't
  landing reliably.
- **2026-07-02 — Act 2 heightening:** **everyday-vivid + one or two in-genre fantasy**
  (lotto / desert-island / power's-out are dinner-party genre, so safe). No full sci-fi
  set-pieces.
- **2026-07-02 — Doc scope:** this is a living design doc — Background is one-time
  problem-statement; body (§1–§5) is iterated; Appendices are the actions/decisions log.
- **2026-07-02 — Act 1 includes a grounding question:** intro + consent is not a full
  exchange; Act 1 ends with one EASY, WIDE opener (a 1-10 or broad either/or, e.g. the
  planner scale) for a first real read to steer Act 2's projections.
- **2026-07-02 — Exchange floor raised min 3 → 4:** a real 3-act arc can't land in 3
  (Act 1 grounding + Act 2's two try-ons + Act 3 convergence is already ~5). Aim ~5,
  ceiling 6. CLASSIFICATION restated POSITIVELY (file at the culmination of a satisfying
  arc; "widen not deepen" is absorbed into what Act 2 IS, no longer a caveat).
- **2026-07-02 — Verdict cut to a SHORT teaser:** self-tests ran long. In-chat verdict is
  now archetype name + 1-2 sentence tease + bare URL + verbatim disclaimer + share-nudge.
  The level-two reflective human–AI question MOVES to the dossier page (chat stays level-one;
  depth lives on the page). Confidence line and the separate P1/FIELD-NOTE paragraph dropped.
  Applied across instructions.md OUTPUT FORMAT + concord-examples VERDICT.

**Implemented 2026-07-02** across src/instructions.md (7,772/8,000 — the 7,581 figure
first logged here was a byte-vs-character miscount; see the instructions.md header),
src/knowledge/elicitation-playbook.txt (new §0 arc + §3 aspirational domains + §5
PROJECT-A-SELF), and src/knowledge/concord-examples.txt (restructured under ACT 1/2/3 +
tightened verdict). Committed 2026-09-16. Follow-up (Appendix A) RAG-size audit still pending.

---

## Sources

[^1]: Casting the Self into Fictional Worlds Through Online Personality Quizzes —
  https://responsejournal.net/issue/2024-11/feature/casting-self
[^2]: Tell Me My Story: From Myers-Briggs to BuzzFeed (Psychology Today) —
  https://www.psychologytoday.com/us/blog/positively-media/202506/tell-me-my-story-from-myers-briggs-to-buzzfeed
[^3]: 20 No-Fail Conversation Starters (Wondermind) —
  https://www.wondermind.com/article/conversation-starters/
[^4]: 68 Killer Conversation Starters (Science of People) —
  https://www.scienceofpeople.com/conversation-starters-topics/
[^5]: 40 dinner party questions (Calm) — https://www.calm.com/blog/dinner-party-questions
