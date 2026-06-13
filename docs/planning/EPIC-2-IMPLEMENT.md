# Epic 2 — Implement
Status: BLOCKED (awaits Epic 1 exit) | Exit gate: GPT deployed privately, all content v1

## Goal
Write everything, build the GPT, deploy privately for playtest.

## Checklist
- [ ] **Canon lore LEADS this epic:** complete **CANON.md** as authoritative,
      player-safe canon (distilled from STORY-SANDBOX.md); condense + sync
      **lore-codex.txt**. Voice + scenario are upstream of dossiers, the
      instructions persona, and templates — write this first.
- [ ] archetypes.txt: all voice samples written (2 paragraphs each)
- [ ] **Elicitation-playbook knowledge file** (formerly "question-bank.txt" —
      renamed per the playbook reframe, DECISIONS 2026-06-12): full question-type
      taxonomy + examples + per-archetype discriminant signatures + accessibility
      variants + signal tags. Built from MECHANICS §IV.
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
