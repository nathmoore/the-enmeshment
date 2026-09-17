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

- [x] **Confirm the diagnosis empirically before restructuring.** *(2026-09-17 — done as a
      **structural chunk audit**, not a live retrieval test: this session can't drive the GPT.
      Script: simulate file_search-style chunking (~800 tokens / 400 overlap, OpenAI's
      documented defaults; custom-GPT retrieval is undocumented but built on the same stack)
      and locate every load-bearing line. Findings at HEAD: the 11 LINK lines and the
      examples file (WRONG-vs-RIGHT, THE INTERRUPTION, VERDICT) are fine — each sits within one
      chunk of its own numbered/titled header. The problem is **volume + anonymity**: the
      playbook made 24 chunks and archetypes.txt 22, so 46 of the ~63 chunks in the whole
      knowledge base competed for the handful retrieved per turn, and rules mid-section
      (STANDING UP was an outright orphan; RATION THE REACTION sat 3,169 chars from any header)
      carried no section identity. The deeper point, which the restructure is built on: every-turn
      *behavioural* rules (arc, breadth, ration) can't rely on retrieval at all — the model doesn't
      query for a rule it doesn't know it needs — so they stay one-line in instructions.md (they
      are), and the knowledge files are optimised as **lookups**: self-labelled chunks a routing
      or topic query lands on. **A real retrieval test still belongs in C6's smoke test**: ask the
      live GPT "what does §7 say about Organiser vs Linchpin?" and "give me the Tinkerer LINK" and
      check it quotes, not guesses.)* The Appendix A audit was a
      *light* read, not a retrieval test. Establish which load-bearing lines actually surface
      when they're needed — the 3-act arc (playbook §0), the breadth rule (§1 r4), the `LINK`
      URLs, the WRONG-vs-RIGHT reflection, and the new THE INTERRUPTION section. **A rule that
      doesn't get retrieved is not a rule**, and we have been fixing behaviour by adding text to
      files that may never surface.
- [x] **Split `archetypes.txt`** (signed off in principle 2026-07-02; **done 2026-09-17** —
      36.7KB → 24.8KB, scaffolding verbatim in `ARCHETYPE-SET-DESIGN.md`; maintainer veto
      = revert one file. What was also stripped from the cards is listed in that doc's header): `git mv`/split the maintainer scaffolding — changelogs,
      selection + set criteria, open questions, parking lot, the MOVED note — out to
      `docs/planning/ARCHETYPE-SET-DESIGN.md`, leaving the shipped file as **framing (North Star
      / Profiling Lens / Spice / Rules) + the 11 cards only**. Standing principle: the
      shipped `.txt` files are **agent-facing** — maintainer scaffolding belongs in `docs/`.
- [x] **Restructure for retrieval, not for reading.** *(2026-09-17, Opus subagent under a
      "move and label, never rewrite" brief, diff reviewed by Fable: new `§00 AT A GLANCE` block
      (12 one-line rules, each with its § pointer) so the every-turn rules sit in chunk 0; 44
      self-identifying labels — `§3 TOPIC —` / `§3 ACT-2 DOOR —` / `§3 BOUNDARY DOOR —` /
      `§6 SIGNATURE —` / `§7 PAIR —` — so any chunk names itself; §3 split into §3a/b/c headers;
      §4 folded into §5 as EXCHANGE SHAPES (stub keeps the numbering); maintainer meta + repo-doc
      pointers stripped; he/his → they. 74/74 rules, phrasings, doors, signatures and pairs
      verified present. Size went UP 39.4 → 41.4KB — the labels cost more than the dedupes saved;
      cutting further means cutting substance, which is a maintainer call (candidates: the
      "Reveals…" gloss lines on §3b/c doors; §6 Texture lines partly restated in §7 Surface).
      Net knowledge base 111.7 → 102.1KB via the archetypes split.)* Front-load rules, tighten
      headers, put load-bearing lines where chunking will find them.
- [x] **Re-verify the instructions budget** *(7,975 / 8,000 confirmed in Python 2026-09-17 — this
      shell's `wc -m` returns bytes, 8,084; Python line added to the header)* after any offload — offloading *to* a knowledge file
      only helps if the file is retrievable. Currently **7,975 / 8,000, 25 chars spare**, so
      there is no room to absorb anything back. Count in UTF-8 (see the instructions.md header —
      a bare `wc -m` under `LC_ALL=C` counts bytes and inflates by ~100).

> **This is the one judgment call in the epic.** Everything else is execution. What ships to the
> GPT vs what stays maintainer scaffolding is a maintainer decision — Fable should bring a
> recommendation and the evidence, not just do it.

### A2. The 11 dossier pages — port

- [x] Port each archetype's P1 + ASSESSMENT + FIELD NOTES from `archetype-dossiers.txt` into
      `site/files/<slug>.md`. Delete the stale "awaits voice samples" TODO. *(2026-09-17 —
      scripted port, headings Subject profile / Assessment / Field notes; site builds.)*
- [x] **Slugs are FROZEN** — renaming a `site/files/*.md` breaks its `LINK` line. Front matter
      (`archetype`, `slug`, `status`) already exists and is correct; don't re-derive it.
- [x] Keep `archetype-dossiers.txt` as the canonical source and the page as the deployment home
      (its authoring note now records the port date + that the footnote lives on the page only).

### A3. The 11 declassified footnotes — **the new writing**

- [x] Author one genuine reflective human–AI question per archetype *(2026-09-17; 53–82 words
      each; in `footnote:` front matter)*, tied to *that* archetype's
      deep layer. This is where level two now lives, so it carries the Bluey Principle on its
      own: the page is the only surface left that does.
- [x] **Voice check** *(done as a set-read; five openers re-varied to kill a shared
      "X is a real skill" shape; no shared question — see A4)*: the footnote is the one place the game may drop the deadpan and be
      sincere — it is *below* the fiction, not inside it. But it must not become a lecture, and
      it must not read as a quiz result. Evaluate against
      [HUMAN-ROLES-RESEARCH](../HUMAN-ROLES-RESEARCH.md) (the centaur / reverse-centaur seam) and
      [GUARDRAILS §5](../GUARDRAILS.md) tone rules.
- [x] Wire it into [`dossier.njk`](../../site/_includes/dossier.njk) (`footnote` front matter →
      `<aside class="footnote">` with a kicker; renders on all 11).

### A4. Evaluation pass

- [x] Read the 11 pages end-to-end as a set *(2026-09-17: stings intact — the port is verbatim;
      the 11 questions are distinct: defaults you'd have chosen / how you'd know the tool changed /
      which targets you set / what it gives that a person who could say no would / seeing→doing /
      the softened work / worked-out vs handed / the "myself" in DIY / what you'd get moving /
      what a reader would need to be / threads held by hand)*. The **stings are varied on purpose** (it reads as a
      group-chat compare) — check the port didn't flatten them, and that no two footnotes
      collapse into the same question.

---

## Track B — the suggestion-chip experiment → **MOVED to Epic 3** (2026-09-17)

> Deferred by the maintainer: it needs live sessions to run, Epic 3 has them, and the epic
> ships without it (v0.9's absorb-and-re-ask stands meanwhile). Kept below for the design of
> the experiment; the checklist entry now lives in [EPIC-3](EPIC-3-PLAYTEST.md).

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

- [x] **DECIDED — publish it all** (DECISIONS 2026-09-17, [WHY-THIS-EXISTS](../WHY-THIS-EXISTS.md)
      §"Why the method is published", README): going public publishes `docs/` too — STORY-SANDBOX, DECISIONS,
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

- [x] *(2026-09-17: `site/assets/css/site.css` — mono letterhead form, rubber-stamp status, the
      footnote drops to sans as the "form stops here" signal; light/dark; verified no horizontal
      scroll at 320px and zero third-party sub-resources in the built site. Mono is site-wide,
      including the long-form scenario/reading-room pages — a one-line scope change if it reads
      heavy.)* There ~~is **no stylesheet at all**~~ was no stylesheet — [`base.njk`](../../site/_includes/base.njk) has a TODO
      where the `<link>` should be. The dossier currently renders as unstyled Times-on-white,
      which is most of why the handoff feels thin.
- [x] **Gotcha (fixed):** `addPassthroughCopy("assets")` was **commented out** in
      [`.eleventy.js`](../../site/.eleventy.js). Uncomment it or the CSS silently won't deploy.
- [x] Target per the existing TODO: monospace, classification-form styling, screenshot-ready.
      **No third-party trackers** — the privacy-respecting profiler practises what it preaches
      ([GUARDRAILS §4](../GUARDRAILS.md)).

### C4. The share loop

- [x] Per-archetype OG **share-card images** (`ogImage`) *(2026-09-17: 11 × 1200×630 PNGs in
      `site/assets/files/`, generator `site/tools/build-cards.py`; `ogImage` set on all 11;
      base.njk emits absolute `og:image` + `og:url` from `_data/site.json`. **Unfurl still
      unverified** — needs a live URL, so it's the exit-checklist item, not this one.)* OG tags are wired in base.njk but
      `ogImage` is unset on all 11, so a pasted link unfurls as a bare `summary` card rather than
      `summary_large_image`. DECISIONS (2026-06-13) dropped the in-chat share-card *because* "the
      dossier link's unfurl IS the travelling artefact" — so right now **the share loop does not
      exist.** The verdict's closing nudge ("send it to a friend") is writing a cheque the page
      doesn't cash.

### C5. Landing + reading room

- [x] `index.njk` hook (~3 sentences, lore cold-open) + a "Play on ChatGPT" CTA *(2026-09-17.
      **The CTA reads `site.gptUrl` from `site/_data/site.json`, which holds a PLACEHOLDER** —
      the live GPT's share link isn't in the repo; paste it there at C6 or the button 404s.)*
- [x] `/reading-room/` from the research bibliographies *(2026-09-17: the warm stance version —
      what it's for / why the method is public / honest limits — above a curated 20-source list
      in five groups; links only to sources the research docs hold primary URLs for)*. **Also the
      player-facing home for the stance** in [WHY-THIS-EXISTS.md](../WHY-THIS-EXISTS.md) —
      a short, warm version of *what this is for and why the method is public*, sitting
      above the curated reading list. The repo doc is for people who go looking; this is
      for the player who just got filed and wants to know who made this and why.
- [ ] `/scenario/` is **already authored** (4.2KB) — leave it.

### C6. Redeploy the GPT

- [ ] The live GPT is running **v0.7**. Paste v1.0 instructions; re-upload the four changed
      knowledge files (`archetypes`, `concord-examples`, `elicitation-playbook`, `lore-codex`)
      plus anything Track A restructures. Builder field copy is already authored in
      [`src/gpt-config.md`](../../src/gpt-config.md) — this is pasting, not writing.
- [ ] **Guardrail smoke test** (see below) — then tag `gpt-v0.1`. *(2026-09-17 first live run at
      v1.0: arc + verdict + link + disclaimer all landed; chips still append but were on-topic.
      One fix → v1.0.1: Concord contracted the letterhead to a bare "the Directorate" —
      now forbidden in IDENTITY, lore-codex, concord-examples. Re-paste + re-upload those two.)*
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
- [~] Chip-steering result logged in DECISIONS either way → moved to Epic 3 (not an exit gate)

Then Epic 3 opens with a game whose ending lands.
