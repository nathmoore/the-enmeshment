# Epic 0 — Research
Status: CORE COMPLETE (synthesis ready for review) | Exit gate: research synthesis reviewed; Epic 1 unblocked

## Goal
Ground the scenario in real futures thinking so our nuanced version has
spine, and survey the GPT-building landscape so Epic 1 plans against
reality, not assumption.

## Workstreams & checklist

### A. Futures & scenario research
- [x] Annotated reading list: AI arms-race scenario work (incl. AI 2027-style
      forecasting), "AI as normal technology" counter-framing (Narayanan/Kapoor),
      techno-authoritarianism, surveillance capitalism (Zuboff),
      automation bias & "moral crumple zones", Atlas of AI (Crawford),
      legibility/illegibility (Scott, Seeing Like a State) — see docs/WORLD-RESEARCH.md
- [x] Map each concept to a phase of the CANON.md timeline spine — see WORLD-RESEARCH.md §VI table
- [x] One page: "what makes our pathway different from the standard
      AI-vs-humans story" (the drift thesis; incl. AI-as-normal-technology
      triangulation) — see WORLD-RESEARCH.md §I + §VI
- [x] Social dynamics of resistance: does drift need a social tipping point?
      (preference falsification / Kuran, threshold & tipping-point models,
      Luddite "state overreach not technology" correction) — see WORLD-RESEARCH.md §V
- [x] State-control extrapolation: which "AI-as-control" horizon the premise
      points at — gradual disempowerment (Kulveit), slow takeover (Christiano),
      Arendt's "rule by Nobody," power-concentration / singleton — and why we
      stop short of the recursive endpoint — see WORLD-RESEARCH.md §I + STORY-RESEARCH §III
- [x] Profiling traditions survey (Stasi, KUBARK, KGB, Cambridge Analytica,
      TSA SPOT, CVE) — see WORLD-RESEARCH.md §III
- [x] Personality frameworks + quiz mechanics → provisional archetype axes
      (PROVISIONAL — Epic 1 input only) — see MECHANICS-RESEARCH.md §II
- [x] Meme archaeology: history of "be polite to the AI" — sources, variants — see WORLD-RESEARCH.md §I ("the meme as canon")

### B. Comparable games & quizzes
- [x] 3-5 reference quizzes/games that nail tone (what works, what's cringe) —
      quiz refs in MECHANICS-RESEARCH.md §I (BuzzFeed/Forer, Fruitful Personas,
      "what character am I"); tone refs in GAME-DESIGN.md §5 + STORY-RESEARCH.md §III
- [x] Note shareability mechanics that drive spread — see MECHANICS-RESEARCH.md §I
- [x] GPT Store findability/naming + safety profile of viral self-profiling trends
      (names were prompt-trends not store GPTs; oversharing is our key risk) — see MECHANICS-RESEARCH.md §III

### C. GPT platform research
- [x] GPT-native conversational quiz format — what went viral, open-ended vs
      multiple choice, confidence-threshold reveal mechanic — see MECHANICS-RESEARCH.md §I
- [x] Verify current GPT Builder constraints — confirmed: 8,000-char instructions,
      20 knowledge files (≤512 MB each). Logged in DECISIONS.md
- [ ] Test: how reliably do GPTs follow guardrails in instructions vs
      knowledge files? **→ needs a built GPT; moved to Epic 2 self-test/red-team.**
      Threat model now grounded (MECHANICS-RESEARCH.md §III): assume instructions +
      knowledge are publicly extractable; guardrails must survive roleplay/jailbreak
- [ ] Survey privacy posture options & store listing requirements **→ light;
      can finish in Epic 1 alongside GUARDRAILS v1.0 + store description**

### D. Genre & narrative inheritance
- [x] "Save the Cat" Institutionalized genre: conventions, the three ingredients
      (group / choice / sacrifice), the join–burn–die climax — see docs/STORY-RESEARCH.md §I–II
- [x] Techno-apocalyptic & AI fiction survey: what we inherit vs reject
      (indifferent-optimiser lineage, not the malevolent-AI lineage) — see STORY-RESEARCH.md §III
- [x] Psychology of being inside a resistance: the pull back to conforming,
      seduction of legibility — level-two character work, never surfaced as paranoia — see STORY-RESEARCH.md §IV
- [ ] Cross-reference Red Carbon (redcarbon-game) story research; mine independently
      **→ needs the other repo; carry into Epic 1**
- [ ] Genre/fiction watch-and-read queue worked through — see STORY-RESEARCH.md §VI
      **→ ongoing; can overlap Epic 1, not a blocker**

### E. Synthesis
- [x] RESEARCH-SYNTHESIS.md: findings -> design implications — see docs/RESEARCH-SYNTHESIS.md

## Exit-gate status
Core research **complete** and synthesised; Epic 1 is **unblocked**. The substantive
findings (scenario positioning, intelligence/legibility logic, profiling axes,
conversational format, the meme, control-horizon framing, resistance dynamics) are
done and reviewed across the three research docs + RESEARCH-SYNTHESIS.md.

**Genuinely outstanding (non-blocking), with new homes:**
- Guardrail-reliability testing → **Epic 2** (needs the built GPT)
- Privacy posture + store-listing detail → **Epic 1** (with GUARDRAILS v1.0)
- Red Carbon cross-reference → **Epic 1** carry-in (needs other repo)
- Watch/read queue → ongoing, overlaps Epic 1

## Out of scope
Writing final lore prose, archetype voice samples, or instructions copy.
