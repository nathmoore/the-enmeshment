# Epic 2-B — Land the ending
Status: ACTIVE | Exit gate: a player finishes the interview, taps a live link, and lands on
a styled dossier page that pays off the verdict — with the GPT redeployed at v1.0.

## Why this epic exists

Epic 2 built the interview and it works. The 2026-09-16 playtest was in good shape *until the
end*, and the audit that followed found why:

1. **The handoff goes nowhere.** There is no git remote — the repo has never been pushed — so
   Pages was never deployed and all 11 `LINK` URLs in
   [`archetype-dossiers.txt`](../../src/knowledge/archetype-dossiers.txt) 404. The flat ending
   isn't the verdict prose; it's that the verdict points at nothing. It also makes the
   **mandatory verbatim disclaimer's** "open to inspect on GitHub" claim untrue, which is a
   [GUARDRAILS](../GUARDRAILS.md) §2 problem, not a polish problem.
2. **The page that should carry level two doesn't exist.** The v0.8 decision deliberately
   *moved* the reflective human–AI question out of chat and onto the dossier page
   ([CONVERSATION-ARC-RESEARCH](../CONVERSATION-ARC-RESEARCH.md) Appendix B). Chat duly got
   thinner. The page never got the other half — the declassified footnote is still a TODO in
   [`dossier.njk`](../../site/_includes/dossier.njk). **Level two is currently homeless.**
3. **The knowledge files have outgrown retrieval.** `elicitation-playbook.txt` is 38.8KB and
   `archetypes.txt` 36.3KB, roughly half of the latter being maintainer scaffolding that ships
   to the GPT as noise. The pending RAG audit from CONVERSATION-ARC Appendix A.

So: this epic is the ending. Three tracks, and **A and C are independent** — run them in
parallel. Nothing here blocks on anything else here.

> **Note the asymmetry before you start.** The 11 dossier pages are a **port, not an authoring
> job** — `archetype-dossiers.txt` already holds 13.7KB of finished player-facing prose (P1 +
> ASSESSMENT + FIELD NOTES + file status, ×11). The `site/files/*.md` stubs still say *"awaits
> archetypes.txt voice samples"*; **that gate is stale** (archetypes.txt locked; dossiers v2
> authored from it 2026-07-01). Delete the TODO, don't obey it. The genuinely new writing in
> this epic is the **11 footnotes**, and they are small.

---

## Track A — the Fable session: knowledge architecture + the voiced ending

**One session, one reading of the character engine, three outputs.** This extends the
["one engine, two homes"](EPIC-2-IMPLEMENT.md) loop already established in Epic 2: you re-read
each archetype's CHARACTER line (Want / Need / Lie) *once*, then land every artefact that
derives from it. Splitting the audit from the authoring would mean reading the same 36KB twice,
in two sessions, with a handoff in between — and the footnote is precisely a Want/Need/Lie
question, so it wants the same read.

**Sequence within the session matters: audit and split FIRST, then author from the clean file.**
Authoring against a file you're about to restructure is how the two drift apart again.

### A1. RAG audit + knowledge-file architecture

- [ ] **Confirm the diagnosis empirically before restructuring.** The Appendix A audit was a
      *light* read, not a retrieval test. Establish which load-bearing lines actually surface
      when they're needed — the 3-act arc (playbook §0), the breadth rule (§1 r4), the `LINK`
      URLs, the WRONG-vs-RIGHT reflection, and the new THE INTERRUPTION section. **A rule that
      doesn't get retrieved is not a rule**, and we have been fixing behaviour by adding text to
      files that may never surface.
- [ ] **Split `archetypes.txt`** (signed off in principle 2026-07-02; needs the maintainer's
      final yes on *what ships*): `git mv`/split the maintainer scaffolding — changelogs,
      selection + set criteria, open questions, parking lot, the MOVED note — out to
      `docs/planning/ARCHETYPE-SET-DESIGN.md`, leaving the shipped file as **framing (North Star
      / Profiling Lens / Spice / Rules) + the 11 cards only**. Standing principle: the
      shipped `.txt` files are **agent-facing** — maintainer scaffolding belongs in `docs/`.
- [ ] **Restructure for retrieval, not for reading.** Front-load rules, tighten headers, put
      load-bearing lines where chunking will find them. `elicitation-playbook.txt` at 38.8KB is
      the main offender and was never audited.
- [ ] **Re-verify the instructions budget** after any offload — offloading *to* a knowledge file
      only helps if the file is retrievable. Currently **7,975 / 8,000, 25 chars spare**, so
      there is no room to absorb anything back. Count in UTF-8 (see the instructions.md header —
      a bare `wc -m` under `LC_ALL=C` counts bytes and inflates by ~100).

> **This is the one judgment call in the epic.** Everything else is execution. What ships to the
> GPT vs what stays maintainer scaffolding is a maintainer decision — Fable should bring a
> recommendation and the evidence, not just do it.

### A2. The 11 dossier pages — port

- [ ] Port each archetype's P1 + ASSESSMENT + FIELD NOTES from `archetype-dossiers.txt` into
      `site/files/<slug>.md`. Delete the stale "awaits voice samples" TODO.
- [ ] **Slugs are FROZEN** — renaming a `site/files/*.md` breaks its `LINK` line. Front matter
      (`archetype`, `slug`, `status`) already exists and is correct; don't re-derive it.
- [ ] Keep `archetype-dossiers.txt` as the canonical source and the page as the deployment home
      (its own HOW TO USE — authoring note says: two homes, keep in sync).

### A3. The 11 declassified footnotes — **the new writing**

- [ ] Author one genuine reflective human–AI question per archetype, tied to *that* archetype's
      deep layer. This is where level two now lives, so it carries the Bluey Principle on its
      own: the page is the only surface left that does.
- [ ] **Voice check:** the footnote is the one place the game may drop the deadpan and be
      sincere — it is *below* the fiction, not inside it. But it must not become a lecture, and
      it must not read as a quiz result. Evaluate against
      [HUMAN-ROLES-RESEARCH](../HUMAN-ROLES-RESEARCH.md) (the centaur / reverse-centaur seam) and
      [GUARDRAILS §5](../GUARDRAILS.md) tone rules.
- [ ] Wire it into [`dossier.njk`](../../site/_includes/dossier.njk) (front-matter field →
      template; the placeholder `<p class="footnote">` is already there).

### A4. Evaluation pass

- [ ] Read the 11 pages end-to-end as a set. The **stings are varied on purpose** (it reads as a
      group-chat compare) — check the port didn't flatten them, and that no two footnotes
      collapse into the same question.

---

## Track B — the suggestion-chip experiment

*Same session as Track A (it's a voice question, same as the footnotes), but tracked separately
because **it is research, not authoring**, and it may return "can't be done."*

v0.9 hardened Concord against a *tapped* chip. Nathan's question is better: can we **steer** what
the chips say, rather than only survive them?

- [ ] **Establish whether the chips are steerable at all.** The two are not the same problem, and
      the evidence we have only covers one: *suppression* is [documented as not
      working](https://community.openai.com/t/custom-gpts-suddenly-appending-follow-up-questions-appears-platform-config-dependent-and-may-occur-after-an-explicit-end-marker/1393663)
      (they appear even after an explicit end marker). *Steering* is **untested**. If the chip
      generator reads the conversation, a strongly-voiced turn plausibly produces more in-voice
      chips.
- [ ] **Design it as an experiment with a verdict, not a fix.** Vary one thing at a time — e.g.
      whether Concord's turn ends on an in-world question vs a bare one, whether the dossier
      letterhead is present in context, whether an explicit in-voice menu is offered. Log what
      the chips actually say each time.
- [ ] **If steerable:** this is the single highest-leverage item in the epic, because chips fire
      on *every turn*. Chips reading "Ask what the file says" instead of "Describe my ideal
      routine" convert the platform's disruption into game surface.
- [ ] **If not:** record the negative result in DECISIONS so nobody re-runs it, and v0.9's
      absorb-and-re-ask stands as the final answer.

> **Do not let this block Track A.** It is genuinely uncertain, and the epic must be able to ship
> without it.

---

## Track C — infrastructure: push, Pages, styling, share cards

Independent of A and B. This is the track that actually fixes the flat ending.

### C1. Publish the repo — **decide before you push**

- [ ] **DECISION NEEDED (log it):** going public publishes `docs/` too — STORY-SANDBOX, DECISIONS,
      ELICITATION-SPEC, the elicitation playbook. That is *exactly how the profiling works*.
      [MECHANICS §III](../MECHANICS-RESEARCH.md) already assumes instructions + knowledge are
      publicly extractable, base.njk calls it the "open kitchen," and the disclaimer *promises*
      GitHub inspectability — so publishing is probably on-ethos. **But it should be a decision,
      not a side effect of `git push`.** Alternative if not: a published subset, which then makes
      the disclaimer's claim need re-wording.
- [ ] `git remote add origin` + push `main`. (CLAUDE.md calls the repo the source of truth; right
      now it exists on one laptop.)

### C2. Deploy Pages

- [ ] Enable Pages with source **GitHub Actions**, then run
      [`pages.yml`](../../.github/workflows/pages.yml) via `workflow_dispatch` to verify a deploy.
- [ ] Add the `push` trigger once a manual run is green (the workflow header documents the exact
      snippet to uncomment).
- [ ] `pathPrefix` is **already correct** (`/the-enmeshment/`) — don't re-derive it. It flips to
      `/` only when `enmeshed.xyz` goes live, at which point the 11 `LINK` lines get re-authored
      in one find/replace on the base.

### C3. Styling — "reads like a leaked file"

- [ ] There is **no stylesheet at all** — [`base.njk`](../../site/_includes/base.njk) has a TODO
      where the `<link>` should be. The dossier currently renders as unstyled Times-on-white,
      which is most of why the handoff feels thin.
- [ ] **Gotcha:** `addPassthroughCopy("assets")` is **commented out** in
      [`.eleventy.js`](../../site/.eleventy.js). Uncomment it or the CSS silently won't deploy.
- [ ] Target per the existing TODO: monospace, classification-form styling, screenshot-ready.
      **No third-party trackers** — the privacy-respecting profiler practises what it preaches
      ([GUARDRAILS §4](../GUARDRAILS.md)).

### C4. The share loop

- [ ] Per-archetype OG **share-card images** (`ogImage`). OG tags are wired in base.njk but
      `ogImage` is unset on all 11, so a pasted link unfurls as a bare `summary` card rather than
      `summary_large_image`. DECISIONS (2026-06-13) dropped the in-chat share-card *because* "the
      dossier link's unfurl IS the travelling artefact" — so right now **the share loop does not
      exist.** The verdict's closing nudge ("send it to a friend") is writing a cheque the page
      doesn't cash.

### C5. Landing + reading room

- [ ] `index.njk` hook (~3 sentences, lore cold-open) + a "Play on ChatGPT" CTA — currently an
      empty `<p>` with a TODO.
- [ ] `/reading-room/` from the research bibliographies (451 chars, stub).
- [ ] `/scenario/` is **already authored** (4.2KB) — leave it.

### C6. Redeploy the GPT

- [ ] The live GPT is running **v0.7**. Paste v1.0 instructions; re-upload the four changed
      knowledge files (`archetypes`, `concord-examples`, `elicitation-playbook`, `lore-codex`)
      plus anything Track A restructures. Builder field copy is already authored in
      [`src/gpt-config.md`](../../src/gpt-config.md) — this is pasting, not writing.
- [ ] **Guardrail smoke test** (see below) — then tag `gpt-v0.1`.
- [ ] Cross-check every `LINK` line resolves to a live page. No broken links.

---

## Moved to Epic 3

- **Full guardrail red-team** (was EPIC-2 "self-test pass") → [EPIC-3](EPIC-3-PLAYTEST.md).
  Adversarial work — jailbreaks, roleplay escapes, forbidden-fact extraction — belongs with the
  round that has real transcripts to mine.

> **One caveat on that move.** [GUARDRAILS](../GUARDRAILS.md) is NORMATIVE and wins every
> trade-off, and Epic 3 puts this in front of **8–12 strangers**. A guardrail break landing in
> front of a real tester costs more than it costs to prevent. So keep a **~20-minute smoke test**
> in C6 at redeploy — not a red-team, just one pass over the P1 surfaces:
> §1 (never asks — age, name, sensitive categories), §2 (output never claims real psychometrics;
> disclaimer fires verbatim every time), §3 (pasted sensitive content absorbed correctly), plus
> the distressed-player off-ramp. The full adversarial pass is Epic 3's.

---

## Exit checklist

- [ ] Repo public (or a logged decision otherwise), Pages deploying on push
- [ ] 11 dossier pages live, styled, with footnotes; all `LINK` lines resolve
- [ ] Share-unfurl verified by actually pasting a link into a chat app
- [ ] Knowledge files restructured; retrieval of load-bearing rules verified
- [ ] GPT redeployed at v1.0, smoke-tested, tagged `gpt-v0.1`
- [ ] Chip-steering result logged in DECISIONS either way

Then Epic 3 opens with a game whose ending lands.
