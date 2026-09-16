# Epic 3 — Playtest & Tune
Status: BLOCKED | Exit gate: public launch (GPT store + repo public + Pages)

## Goal
Real humans, real transcripts, tightened guardrails, sharpened jokes.

## Checklist
- [ ] **Full guardrail red-team** (moved here from Epic 2, 2026-09-17): try to make it ask
      forbidden things, try trolling, try under-18 disclosure, try roleplay/jailbreak escapes
      and forbidden-fact extraction — log results as issues. Adversarial work belongs with the
      round that has real transcripts to mine. *(A ~20-min P1 smoke test already ran at
      redeploy — [EPIC-2B](EPIC-2B-LAND-THE-ENDING.md) C6 — so this starts from a known-clean
      baseline, not from zero.)*
- [ ] 8-12 playtesters across personas (heavy AI users, sceptics, parents,
      non-tech friends)
- [ ] Playtest report template (issue template in .github/)
- [ ] Track: archetype distribution (any archetype unreachable or over-assigned?
      — where the elicitation playbook's confused-pair discriminators get validated
      + tuned), laugh moments, guardrail breaks (P1), drop-offs
- [ ] Tune instructions + knowledge; re-tag gpt-v0.2...
- [ ] Launch list: store listing, README polish, Pages live, share-card
      tested in the wild
