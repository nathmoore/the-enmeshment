# Epic 1 — Plan
Status: READY (Epic 0 core complete; awaits synthesis sign-off) | Exit gate: all specs locked & reviewed

## Goal
Lock every design decision so Epic 2 is pure execution.

> **Research readiness:** [RESEARCH-SYNTHESIS.md](../RESEARCH-SYNTHESIS.md) §"What Epic 1
> can now lock" confirms the research supports every deliverable below. Design seeds
> (archetype axes, "what the Enmeshment sees" notes) live in MECHANICS-RESEARCH §II.
> Carry-ins from Epic 0: privacy posture + store listing (with GUARDRAILS v1.0),
> Red Carbon story cross-reference.

## Deliverables checklist
- [ ] Name decision (working title "The Enmeshment" — confirm or replace)
- [x] Archetype set locked: **11 types** (2026-06-12) — signal pattern + deep
      layer per type in archetypes.txt; voice samples drafted in Epic 2.
      Routability of adjacent pairs to be pressure-tested in Epic 2.
- [ ] **STORY-TEST.md (NON-CANON sandbox — GATES Name + Output spec + voice):**
      weave the whole scenario together *specifically* — timeline, AI trajectory,
      the intake agent, phases, the Nobody/Someone invariant, the privacy flex —
      and stress it for contradictions. Going specific IS the coherence test (a
      thin spine hides them). Tentative + driftable; **not authoritative.**
- [ ] **LORE.md (canon spine):** promote what survives the brainstorming into the
      authoritative reference downstream work cites. Full prose + lore-codex.txt
      condense = Epic 2; but the load-bearing scenario decisions Name/Output/voice
      depend on get ratified here as they lock.
- [ ] Elicitation *spec* (Plan-level decisions only — the full playbook is an
      Epic 2 knowledge file; MECHANICS §IV already did the design thinking): lock
      the **anchor questions** (fixed backbone, incl. politeness meme), the
      **confidence-threshold stop rule**, and (with GUARDRAILS) the **never-ask
      boundaries**. Signal->archetype mapping lives in the classification-logic
      deliverable below.
- [ ] Classification logic: signal -> archetype mapping rules, tie-breaks
      (must resolve from free-form answers, not fixed options)
- [ ] Output spec: dossier wording, footnote disclaimer final text,
      share-card format
- [ ] **Content architecture (E1->E2 bridge):** lock what goes where before Epic 2
      writes — (a) the instructions.md **section skeleton** (persona / interview
      rules / classification trigger / guardrails block / output handoff) and (b)
      the **knowledge-file split** (what's its own file vs in-instructions) —
      against the 20-file limit and the 8,000-char instructions ceiling (guardrails
      >= 1,800 reserved). Sanity-check it all plausibly fits; precise per-section
      char counts happen while writing in Epic 2.
- [ ] GUARDRAILS.md v1.0: open questions resolved (incl. hard topic-boundaries
      for an improvising interviewer — what it must never ask)
- [ ] Licence split confirmed (MIT code / CC BY-SA lore)
- [ ] Release checklist + version tagging convention (ARCHITECTURE.md)
- [ ] Decision log maintained (see DECISIONS.md — started in Epic 0)

## Decisions to make (carry-ins)
- Interview/elicitation-technique research top-up (small): seed the playbook —
  oblique/projective/cognitive-interview techniques; KUBARK (WORLD §III) as the
  in-world reference. May need a short Epic-0-style research pass.
- One GPT or two? Faction second axis in v1?
- GitHub Pages scope for launch (likely: README + lore only)
