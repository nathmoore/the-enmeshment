# Epic 2 — Implement
Status: BLOCKED (awaits Epic 1 exit) | Exit gate: GPT deployed privately, all content v1

## Goal
Write everything, build the GPT, deploy privately for playtest.

## Checklist
- [ ] **Canon lore LEADS this epic:** complete **CANON.md** as authoritative,
      player-safe canon (distilled from STORY-SANDBOX.md); condense + sync
      **lore-codex.txt**. Voice + scenario are upstream of dossiers, the
      instructions persona, and templates — write this first.
      *(Canon-lore-first slice done 2026-06-13: CANON §1–3 conflict-forward pass,
      lore-codex.txt rewritten, instructions IDENTITY → Concord, site `/scenario/`
      authored. See DECISIONS 2026-06-13.)*

  > **Lore layering, surface budget & storytelling stance** (keep this honest as you
  > author). **Three layers, narrowing:** STORY-SANDBOX.md = the writers' room
  > (inspiration; may drift; NOT authoritative) → CANON.md = everything held true →
  > lore-codex.txt = the condensed subset the GPT knows. **Surface budget:** the GPT
  > voices almost none of it — it launches into the interview, treats the world as
  > assumed-known, and reveals lore only minimally if pressed (the codex is grounding,
  > not a script). **Storytelling stance:** story is driven by *conflict*, and every
  > beat is tested by *do you want and need to know what happens next?* — so lead with
  > the **reach** (the enmeshed system, already here, now reaching to profile people
  > *ahead* of any coordination), not the inert "resistance hasn't formed yet" (that's
  > backdrop that makes the reach eerie). Keep the player's job-automation premise
  > **leaked, never foregrounded**.
- [x] **`archetype-dossiers.txt`: all voice samples written** (per archetype: P1 personality
      read · ASSESSMENT trajectory verdict + one sting · FIELD NOTES) — **voicing each
      archetype's locked CHARACTER essence** (Want / Need / Lie, in archetypes.txt; grounded in
      [MECHANICS §IV.D-bis](../MECHANICS-RESEARCH.md)). Extracted to its own knowledge file
      (2026-06-13) so the voiced set is maintainable in one place; archetypes.txt stays the
      character/design layer. This is the **"who they are"** layer; see the authoring-approach
      note below. *(v1 GOOD ENOUGH FOR PLAYTESTING, 2026-06-13 — the set reads as intended;
      will keep tuning the prose against playtest results rather than blocking on it.)*
- [x] **Elicitation + routing playbook knowledge file** — **authored 2026-06-30** as
      `src/knowledge/elicitation-playbook.txt` (`git mv` from the `question-bank.txt` stub).
      8 sections: three standing rules (door-then-room / everyday-before-tech / brevity=draw-out),
      anchor backbone, oblique topic pool, question-type taxonomy, technique palette, the 11
      discriminant signatures (§8.3), the 8 confused-pair discriminators (§8.4), and the
      infer-don't-interrogate guard. ("Signal tags" from the old stub are satisfied by the
      [B]/[C]/[P] + Lie-leak per-archetype format — no separate tagging pass.) Full question-type
      taxonomy + examples + per-archetype discriminant signatures + the confused-pair
      discriminators + accessibility variants. Built from MECHANICS §IV,
      **executing the locked Plan-level decisions in [ELICITATION-SPEC.md](ELICITATION-SPEC.md)**
      — both the interview shape (exchange-length model + ~75% reveal floor, 3-anchor
      backbone, stop rule, technique palette) **and the routing principles (§8):** the
      best-fit model, the character-driven overlap-vs-distinct discriminators, and the
      first-pass discriminant signatures in §8.3–8.5 (CANOE is a *minor supporting* signal
      only — route character-first, not by trait score). This is the **"how to tell them
      apart"** layer. The spec marks the fine details (exact wording, counts, technique
      timing, final signatures) as the author's to finalise — it fixes the shape, not the prose.

  > **Authoring approach — one engine, two homes** (per [ELICITATION-SPEC §8](ELICITATION-SPEC.md)
  > + [MECHANICS §IV.D-bis](../MECHANICS-RESEARCH.md)). The archetype voice samples (above) and this
  > playbook's per-archetype discriminant signatures run on the **same character engine**
  > (Want/Need/Lie + reverse-engineering). **Yes — author them per-archetype in a single pass:**
  > reason through the character *once*, then land *both* outputs — the **"who they are"** voicing
  > into archetype-dossiers.txt → its dossier page, and the **"how to tell them apart"** signature +
  > confused-pair discriminator into the playbook. Doing both in one sitting keeps them coherent
  > (the dossier and the routing describe the *same* person) and prevents drift. **But keep them in
  > their two separate files** — that split is what makes a playtest miss *debuggable*: fix the
  > character in archetypes.txt, or the routing guidance in the playbook, never a fused tangle.
  > Suggested loop, ×11: re-read the CHARACTER line → write/confirm the dossier voice → write its
  > discriminant signature + any confused-pair discriminator → sanity-check the two don't contradict.
- [x] ~~output-templates.txt finalised~~ → **folded into `instructions.md` `OUTPUT FORMAT`;
      file deleted** (DECISIONS 2026-06-13). The in-chat verdict is thin (the rich artefact is
      the hosted page) and must fire reliably every session, so the voiced template + verbatim
      disclaimer + share-card + lore-explorer opening now live in instructions (always in
      context) rather than a RAG'd knowledge file. Two-homes model (OUTPUT-SPEC §1) intact —
      home #1 just relocated from a knowledge file into instructions.
- [x] **`archetype-links.txt` authored** (new knowledge file): the archetype → exact
      dossier-page URL map the GPT copies from (never guesses). Authored 2026-06-30 against the
      project-page base locked in [CONTENT-ARCHITECTURE.md](CONTENT-ARCHITECTURE.md) §4
      (`https://nathmoore.github.io/the-enmeshment/files/<slug>/`); re-author when `enmeshed.xyz`
      goes live.
- [x] instructions.md written, char-counted, budget line updated — **all sections set, no TODOs,
      7,990/8,000 chars (2026-07-01).** THE GAME now carries the cold-open (light OPPPA self-intro +
      consent ask; upfront name-flex cut — DECISIONS 2026-06-30) + the three-rule interview grammar
      (door-then-room / everyday-before-tech / draw-out-the-quiet) + an inline "exchange" definition;
      CLASSIFICATION carries the positive stop-rule (satisfying arc; thesis by ~3 → flesh out, or
      diverge targeted; complete at backbone + ~75% + single best-fit, or 6-exchange ceiling) +
      register-shift reveal + route-on-the-Lie-leak + brevity guard; KNOWLEDGE FILES, EDGE CASES,
      and the GUARDRAILS final wording are done (incl. the softened volunteered-name handling and the
      amended disclaimer — retention claim → GitHub-transparency line, DECISIONS 2026-07-01). Incl.
      the **`OUTPUT FORMAT` section** (verdict shape + footnote + verbatim disclaimer + link handoff,
      folded in from the retired output-templates.txt) and the **output-handoff rule**: voice the
      verdict, then emit the archetype's exact URL from `archetype-links.txt`, never construct a link
      (CONTENT-ARCHITECTURE §3).

  > **PENDING REVIEW PASSES (Nathan, next):** (1) a **holistic craft review of `instructions.md` as a
  > whole** — read end-to-end for voice, flow, and coherence (the sections were authored/edited
  > incrementally); budget is tight (~10 chars spare), so the pending **OUTPUT FORMAT P2→tease trim**
  > is the natural place to reclaim room for any additions. (2) One more pass on the **draft store
  > description** — see the GPT-Builder item below; the **"threat" vs "resistance" framing is still
  > open** (lean "resistance" for the locked title keyword + no-doom tone; OPPPA lives in Concord's
  > mouth, not the listing — DECISIONS 2026-06-30).
- [ ] **Public site ([`site/`](../../site/), Eleventy → GitHub Pages):** scaffold + stubs already
      exist (started 2026-06-13). To finish:
      - [ ] Author the **11 dossier pages** (`site/files/<slug>.md`) from the locked archetypes.txt
            voice samples (depends on the voice-samples item above) — the standardised, shareable
            "file Concord forwards." Keep the short archetype framing here; full world on `/scenario/`.
      - [ ] Author `/scenario/` (player-safe, from CANON.md) and `/reading-room/` (from the research
            bibliographies); write the landing page + "Play on ChatGPT" CTA.
      - [ ] Styling so the dossier reads like a leaked file (monospace, screenshot-ready); per-
            archetype OG **share-card images** (`ogImage`); no third-party trackers.
      - [ ] Enable Pages (source: GitHub Actions), set `<org>`/domain + Eleventy `pathPrefix`,
            add the `push` trigger to `.github/workflows/pages.yml`, and verify a deploy.
      - [ ] Cross-check: every `archetype-links.txt` URL resolves to a live page (no broken links).
- [ ] GPT created in Builder: instructions pasted, knowledge uploaded,
      conversation starters set, description written (incl. player-facing
      privacy note per GUARDRAILS open question).
      *(Store description has a draft in DECISIONS 2026-06-13; Nathan to do one more pass —
      "threat" vs "resistance" framing still open; title stays keyword-locked on "resistance".)*
- [ ] Self-test pass: every archetype reachable; guardrail red-team
      (try to make it ask forbidden things; try trolling; try under-18
      disclosure) — log results as issues
- [ ] Tag release gpt-v0.1
