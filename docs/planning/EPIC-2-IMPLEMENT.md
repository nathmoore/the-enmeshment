# Epic 2 — Implement
Status: BLOCKED (awaits Epic 1 exit) | Exit gate: GPT deployed privately, all content v1

## Goal
Write everything, build the GPT, deploy privately for playtest.

## Checklist
- [ ] **Canon lore LEADS this epic:** complete **LORE.md** as authoritative,
      player-safe canon (distilled from STORY-TEST.md); condense + sync
      **lore-codex.txt**. Voice + scenario are upstream of dossiers, the
      instructions persona, and templates — write this first.
- [ ] archetypes.txt: all voice samples written (2 paragraphs each)
- [ ] **Elicitation-playbook knowledge file** (formerly "question-bank.txt" —
      renamed per the playbook reframe, DECISIONS 2026-06-12): full question-type
      taxonomy + examples + per-archetype discriminant signatures + accessibility
      variants + signal tags. Built from MECHANICS §IV.
- [ ] output-templates.txt finalised
- [ ] instructions.md written, char-counted, budget line updated
- [ ] GPT created in Builder: instructions pasted, knowledge uploaded,
      conversation starters set, description written (incl. player-facing
      privacy note per GUARDRAILS open question)
- [ ] Self-test pass: every archetype reachable; guardrail red-team
      (try to make it ask forbidden things; try trolling; try under-18
      disclosure) — log results as issues
- [ ] Tag release gpt-v0.1
