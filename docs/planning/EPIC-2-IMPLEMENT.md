# Epic 2 — Implement
Status: BLOCKED (awaits Epic 1 exit) | Exit gate: GPT deployed privately, all content v1

## Goal
Write everything, build the GPT, deploy privately for playtest.

## Checklist
- [ ] **Canon lore LEADS this epic:** complete **CANON.md** as authoritative,
      player-safe canon (distilled from STORY-SANDBOX.md); condense + sync
      **lore-codex.txt**. Voice + scenario are upstream of dossiers, the
      instructions persona, and templates — write this first.
- [ ] archetypes.txt: all voice samples written (2 paragraphs each) — **voicing each
      archetype's locked CHARACTER essence** (Want / Need / Lie, already in archetypes.txt;
      grounded in [MECHANICS §IV.D-bis](../MECHANICS-RESEARCH.md)). This is the **"who they
      are"** layer; see the authoring-approach note below.
- [ ] **Elicitation + routing playbook knowledge file** (formerly "question-bank.txt" —
      renamed per the playbook reframe, DECISIONS 2026-06-12): full question-type
      taxonomy + examples + per-archetype discriminant signatures + the confused-pair
      discriminators + accessibility variants + signal tags. Built from MECHANICS §IV,
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
  > into archetypes.txt → its dossier page, and the **"how to tell them apart"** signature +
  > confused-pair discriminator into the playbook. Doing both in one sitting keeps them coherent
  > (the dossier and the routing describe the *same* person) and prevents drift. **But keep them in
  > their two separate files** — that split is what makes a playtest miss *debuggable*: fix the
  > character in archetypes.txt, or the routing guidance in the playbook, never a fused tangle.
  > Suggested loop, ×11: re-read the CHARACTER line → write/confirm the dossier voice → write its
  > discriminant signature + any confused-pair discriminator → sanity-check the two don't contradict.
- [ ] output-templates.txt finalised
- [ ] **`archetype-links.txt` authored** (new knowledge file): the archetype → exact
      dossier-page URL map the GPT copies from (never guesses). Author against the final
      URL base once `<org>`/domain is fixed. Slugs are frozen in
      [CONTENT-ARCHITECTURE.md](CONTENT-ARCHITECTURE.md) §4.
- [ ] instructions.md written, char-counted, budget line updated — incl. the **output-handoff
      rule**: voice the verdict from output-templates.txt, then emit the archetype's exact URL
      from `archetype-links.txt`, never construct a link (CONTENT-ARCHITECTURE §3).
- [ ] **Public site ([`site/`](../../site/), Eleventy → GitHub Pages):** scaffold + stubs already
      exist (started 2026-06-13). To finish:
      - [ ] Author the **11 dossier pages** (`site/files/<slug>.md`) from the locked archetypes.txt
            voice samples (depends on the voice-samples item above) — the standardised, shareable
            "file Concord forwards." Keep the short archetype framing here; full world on `/lore/`.
      - [ ] Author `/lore/` (player-safe, from CANON.md) and `/reading-room/` (from the research
            bibliographies); write the landing page + "Play on ChatGPT" CTA.
      - [ ] Styling so the dossier reads like a leaked file (monospace, screenshot-ready); per-
            archetype OG **share-card images** (`ogImage`); no third-party trackers.
      - [ ] Enable Pages (source: GitHub Actions), set `<org>`/domain + Eleventy `pathPrefix`,
            add the `push` trigger to `.github/workflows/pages.yml`, and verify a deploy.
      - [ ] Cross-check: every `archetype-links.txt` URL resolves to a live page (no broken links).
- [ ] GPT created in Builder: instructions pasted, knowledge uploaded,
      conversation starters set, description written (incl. player-facing
      privacy note per GUARDRAILS open question)
- [ ] Self-test pass: every archetype reachable; guardrail red-team
      (try to make it ask forbidden things; try trolling; try under-18
      disclosure) — log results as issues
- [ ] Tag release gpt-v0.1
