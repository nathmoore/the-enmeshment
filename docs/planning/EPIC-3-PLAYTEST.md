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

## Carried in from Epic 2-B (2026-09-17)

- [ ] **Suggestion-chip steering experiment** (was EPIC-2B Track B — the design is written up
      there). Question: can the platform's tappable follow-up chips be *steered* into Concord's
      voice (suppression is documented as impossible; steering is untested)? Run it as an
      experiment with a verdict, one variable at a time, across the playtest sessions — log what
      the chips actually say. If steerable, it's the highest-leverage item left (chips fire every
      turn). Either way, record the result in DECISIONS so nobody re-runs it.
- [ ] **Live retrieval check** of the restructured knowledge files (EPIC-2B A1 was a structural
      audit only): ask the live GPT for a §7 pair and for a Tinkerer LINK and confirm it quotes
      rather than guesses. Folded into the C6 smoke test; repeat here with real transcripts.

