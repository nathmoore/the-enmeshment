# Epic 2 — Implement
Status: SUBSTANTIALLY DONE — remaining work carried into
[EPIC-2B — Land the ending](EPIC-2B-LAND-THE-ENDING.md) (2026-09-17)
| Exit gate: GPT deployed privately, all content v1

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
- [x] **Archetype → dossier-URL map authored, then folded into `archetype-dossiers.txt`**
      (2026-07-01): the map the GPT copies from (never guesses) now lives as a `LINK` line inside
      each dossier block — retrieval co-location so the verdict's voice + its link are one chunk
      (DECISIONS 2026-07-01). Authored against the project-page base in
      [CONTENT-ARCHITECTURE.md](CONTENT-ARCHITECTURE.md) §4
      (`https://nathmoore.github.io/the-enmeshment/files/<slug>/`); re-author the 11 `LINK` lines
      when `enmeshed.xyz` goes live. (Was standalone `archetype-links.txt`, now retired.)
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
      verdict, then emit the archetype's exact URL — the `LINK` line in its `archetype-dossiers.txt`
      block — never construct a link (CONTENT-ARCHITECTURE §3).

  > **REVIEW PASSES — DONE (2026-07-01):** (1) **holistic craft review of `instructions.md`** end-to-end
  > — a focus pass trimmed repetition (CLASSIFICATION / IDENTITY / THE GAME), resolved the verdict
  > **P1-source ambiguity** (in-chat verdict now sources from `archetype-dossiers.txt`; `archetypes.txt`
  > is the interview-time routing engine), **named the 11 archetypes** in KNOWLEDGE FILES for exact-match
  > linking, and added a **CLOSE share-nudge** + a **"skip to the list" edge case**; also folded the
  > archetype-links map into the dossiers (final **7,977/8,000**). (2) **Store copy + starters locked →
  > [`src/gpt-config.md`](../../src/gpt-config.md):** the single GPT **Description** (295/300) and the 4
  > conversation starters are set; the **"threat" vs "resistance" framing is resolved** — the Description
  > leads on the hook and drops "threat" from the headline (it promises menace the warm dossiers don't
  > pay off), the title stays keyword-locked on "resistance" (DECISIONS 2026-07-01).
- [ ] **Public site ([`site/`](../../site/), Eleventy → GitHub Pages):** scaffold + stubs already
      exist (started 2026-06-13). **→ CARRIED INTO [EPIC-2B](EPIC-2B-LAND-THE-ENDING.md) Track C**
      (2026-09-17), which also found the real blocker: there is no git remote, so Pages was never
      deployed and all 11 `LINK` URLs 404. To finish:
      - [ ] Author the **11 dossier pages** (`site/files/<slug>.md`) from the locked archetypes.txt
            voice samples (depends on the voice-samples item above) — the standardised, shareable
            "file Concord forwards." Keep the short archetype framing here; full world on `/scenario/`.
      - [ ] Author `/scenario/` (player-safe, from CANON.md) and `/reading-room/` (from the research
            bibliographies); write the landing page + "Play on ChatGPT" CTA.
      - [ ] Styling so the dossier reads like a leaked file (monospace, screenshot-ready); per-
            archetype OG **share-card images** (`ogImage`); no third-party trackers.
      - [ ] Enable Pages (source: GitHub Actions), set `<org>`/domain + Eleventy `pathPrefix`,
            add the `push` trigger to `.github/workflows/pages.yml`, and verify a deploy.
      - [ ] Cross-check: every `LINK` line in `archetype-dossiers.txt` resolves to a live page (no broken links).
- [ ] GPT created in Builder: instructions pasted, knowledge uploaded, conversation starters set,
      description written. **→ REDEPLOY AT v1.0 in [EPIC-2B](EPIC-2B-LAND-THE-ENDING.md) C6** — the
      live GPT is running v0.7; instructions + four knowledge files have changed since. **All Builder field copy is authored in
      [`src/gpt-config.md`](../../src/gpt-config.md)** (name, store title, Description 295/300, the 4
      starters) — this task is now just pasting them in. *(Store Description locked + "threat vs
      resistance" framing resolved — DECISIONS 2026-07-01; player-facing privacy note lives on the
      GUARDRAILS §7 "what this game does with your words" card, not the Description.)*
- [x] ~~Self-test pass: every archetype reachable; guardrail red-team~~ **→ SPLIT (2026-09-17):**
      the full adversarial red-team moves to [EPIC-3](EPIC-3-PLAYTEST.md) (it wants real
      transcripts to mine); a ~20-minute **guardrail smoke test** stays at redeploy time in
      [EPIC-2B](EPIC-2B-LAND-THE-ENDING.md) C6, because GUARDRAILS is normative and Epic 3 puts
      this in front of 8-12 strangers.
- [ ] Tag release gpt-v0.1 **→ [EPIC-2B](EPIC-2B-LAND-THE-ENDING.md) C6**
