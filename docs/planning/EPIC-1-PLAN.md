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
- [x] **STORY-SANDBOX.md (NON-CANON sandbox — GATES Name + Output spec + voice):**
      weave the whole scenario together *specifically* — timeline, AI trajectory,
      the intake agent, phases, the Nobody/Someone invariant, the privacy flex —
      and stress it for contradictions. Going specific IS the coherence test (a
      thin spine hides them). Tentative + driftable; **not authoritative.**
      **Full weave done 2026-06-12 (rewritten around a stronger story engine).**
      Set at the **2038 cusp** — the world caught at the hinge as the state/AI line
      finishes vanishing, *young / overconfident / under-mapped / outcome undecided*
      (replaces the earlier static "settled plateau"). Intake agent *Concord* reframed
      as a **pilot** riding the civic **re-allocation (jobs) stream** — "the apparatus
      growing its first eyes." Keystone: "the system profiling you for an event it
      can't see and you aren't planning" (trajectory = role in the unseen cascade;
      containment = actuarial bet on your threshold). Pacing benchmarked against real
      generational upheavals (Industrial Rev / railways / US frontier / Meiji Japan)
      + the AI-theory bracket → mid-2030s. Adds a Save-the-Cat session beat-sheet with
      **mask-slip timing (~75%)**. Now graduated to canon: the 2038 setting + "no
      one's at the top" as working assumption (CANON §1). Promotion candidates in §8;
      open tensions in §9 (privacy-flex-vs-surveillance read is the live design risk).
- [x] **CANON.md (canon spine):** done 2026-06-12 — [CANON.md](../CANON.md) promotes
      the surviving facts as a *truth-set* (canon = what's true, not what's shown):
      2038 setting, Concord-as-intake-pilot, the actuarial verdict, "no one's home"
      as working assumption. Renamed from LORE.md; stale factions + defected-profiler
      frame deleted. Full prose + lore-codex.txt condense = Epic 2.
- [~] Elicitation *spec* (Plan-level decisions only — the full playbook is an
      Epic 2 knowledge file; MECHANICS §IV already did the design thinking):
      STARTED 2026-06-13 → [ELICITATION-SPEC.md](ELICITATION-SPEC.md). Locks the
      **two-floor length model** (story/experience floor drives the reveal, not the
      routing floor; modal **~5 exchanges**, band 3–6; unit = *exchange* = anchor +
      ≤1 follow-up), the **3-anchor backbone** (behavioural / coordination /
      politeness meme), the **stop rule** (min count + ~75% dramatic floor + signal
      sufficiency), and the **technique palette** (bracketing + BEI + complex-
      reflection spine; KUBARK as lineage only). Open tail: the enumerated
      **never-ask boundaries** finalise *with* GUARDRAILS v1.0 (spec states the
      principle). Signal->archetype mapping lives in the classification-logic
      deliverable below.
- [ ] Classification logic: signal -> archetype mapping rules, tie-breaks
      (must resolve from free-form answers, not fixed options)
- [ ] Output spec: dossier wording, footnote disclaimer final text,
      share-card format
      - **Dossier-delivery model + link-out (DECIDED 2026-06-13):** agent paraphrases
        the verdict in-voice, then emits the archetype's **exact dossier-page URL**
        (copied from a new `archetype-links.txt` map, never guessed). Rationale +
        runtime grounding: [CONTENT-ARCHITECTURE.md](CONTENT-ARCHITECTURE.md) §1 and
        [MECHANICS-RESEARCH §I "Platform capabilities & constraints"](../MECHANICS-RESEARCH.md).
- [~] **Content architecture (E1->E2 bridge):** STARTED — see
      [CONTENT-ARCHITECTURE.md](CONTENT-ARCHITECTURE.md) (delivery model locked; skeleton +
      file split stubbed, fill in as elicitation/classification/output specs land). Lock what
      goes where before Epic 2 writes — (a) the instructions.md **section skeleton** (persona /
      interview rules / classification trigger / guardrails block / output handoff) and (b)
      the **knowledge-file split** (what's its own file vs in-instructions; now incl. the new
      `archetype-links.txt` URL map → 5 of 20 files) — against the 20-file limit and the
      8,000-char instructions ceiling (guardrails >= 1,800 reserved). Sanity-check it all
      plausibly fits; precise per-section char counts happen while writing in Epic 2.
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
- GitHub Pages scope for launch (likely: README + lore only) — **now also a candidate host
  for the per-archetype dossier pages** the link-out delivery model points to (one page per
  archetype, slug scheme in [CONTENT-ARCHITECTURE.md](CONTENT-ARCHITECTURE.md) §4). Building the
  pages is a **future workstream (likely Epic 2/3)** and does not block Epic 1.
