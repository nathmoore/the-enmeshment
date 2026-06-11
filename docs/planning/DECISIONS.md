# Decisions & Decision Log

> The project's **permanent decision log** — the record of what was decided and why,
> so future sessions don't re-litigate settled calls. Newest first.
> Running scratch / notes appendix at the bottom.

## Decision log

| Date | Decision | Rationale | Revisit? |
|---|---|---|---|
| 2026-06-11 | Research split into three docs **by objective**: [WORLD-RESEARCH](../WORLD-RESEARCH.md) (world/scenario grounding), [MECHANICS-RESEARCH](../MECHANICS-RESEARCH.md) (how the game is built), [STORY-RESEARCH](../STORY-RESEARCH.md) (narrative/genre) | A single RESEARCH.md conflated distinct objectives; profiling/surveillance is a standout, reviewer-facing thread that deserves its own home | If a 4th research objective emerges |
| 2026-06-11 | **Scenario positioning locked**: drift / boiling-frog, triangulated — *reject* the precipice camp's threshold event (Aschenbrenner, AI 2027); *accept* the normal-tech camp's gradual diffusion (Narayanan/Kapoor) but *reject* its reassurance | We never have to speculate about an AI "moment." "Normal technology, abnormal outcome" is the original position | — |
| 2026-06-11 | **Control-horizon invariant**: the Enmeshment sits between "rule by Nobody" (gradual disempowerment) and "rule by a hidden Someone" (power concentration), and stops short of the singleton's closure. The Nobody/Someone ambiguity is **permanent** | Credible (both horizons are real literature), apolitical (no named villain), dramatically alive (unanswerable, not merely hidden). Revealing a cabal collapses the story into the rejected malevolent-AI lineage | Protect through Epic 1+ |
| 2026-06-11 | **Resistance target = state overreach** (state + AI enmeshed), *not* technology (Luddite correction). Resistance = illegibility = preserving the social substrate for a possible tipping point ("keeping the kindling dry") | Keeps the game out of technophobia and inside "what relationship do we want?"; gives "persist illegibly" a real stake | — |
| 2026-06-11 | The GPT's **character persona is the inference mechanism**, not decoration — a bland helpful-assistant voice produces measurably worse profiling *and* worse UX | Research finding (conversational personality inference); affects how strictly the Directorate persona is held in instructions.md | — |
| 2026-06-11 | GPT Builder hard limits **verified**: 8,000-char instructions; 20 knowledge files (≤512 MB each) | Unblocks Epic 1 instructions.md budgeting against a confirmed ceiling, not an assumption; CLAUDE.md prime directive #3 holds | Re-verify if OpenAI changes limits |
| 2026-06-11 | Research stats **fact-checked** in a fresh validation conversation (11 load-bearing claims): 9/11 confirmed. Huawei "Safe City" footprint corrected to ~73 deployments/52 countries (CSIS) vs marketing's 700/100; minor reframes to sluggish-schizophrenia "38%" and the metadata-inference wording. Corrections in WORLD-RESEARCH; full log in [FACT-CHECK-QUEUE](FACT-CHECK-QUEUE.md) | Closes the credibility-calibration loop; stats now safe to draw lore from | If new stats added |
| 2026-06-11 | **Meme calibration**: keep the "be polite to AI" meme's *marketing fun* and *credibility claim* on separate ledgers. Level-two grounding is the **unexamined ambiguity** of our politeness (habit/hedge/joke/unease), NOT a claim that people fear AI judgment | Habit reading is backed by Reeves & Nass CASA / *Media Equation* research (automatic, denied social reflex); the "insurance" survey numbers are commissioned PR research (Talker) that themselves cite "better output"/"habit", not fear. Overclaiming would undercut credibility | — |
| 2026-06-11 | Repo scaffolded; Research→Plan→Implement→Playtest, one epic per step | Playtest added: GPT instruction-tuning is inherently iterative | — |
| 2026-06-11 | Guardrails are normative and get ≥1,800 chars of instructions budget | Privacy-as-feature is core to the Bluey deep layer | — |
| 2026-06-11 | Single root CLAUDE.md, no sub-files | Repo too small to justify; revisit if src/ grows | If repo grows |

## Provisional — NOT yet decided (Epic 1 to lock)

Research *positions/seeds*, deliberately held open until Epic 1:

- Archetype set (6 seeded, target 8–12) and the profiling **axes** that drive classification — see [MECHANICS-RESEARCH §II](../MECHANICS-RESEARCH.md). The "Knowing Participant" (ironic-but-legible) is a strong candidate new archetype.
- Number of classification axes the quiz actually probes (research suggests 5; quiz realistically supports 3–4).
- One GPT or two? Faction second axis in v1? Combined Mode A+B scoring? (carry-ins)
- Working title "The Enmeshment" — confirm or replace.

## Scratch

- Name candidates: The Enmeshment / Please & Thank You / Politeness Telemetry / The Unfiled
- **Naming tension (MECHANICS §III):** "The Enmeshment" is great brand, poor search keyword. Likely answer = two-part store title: evocative brand + keyword tail ("The Enmeshment — AI Resistance Profiler / personality quiz"). Brand name stays for lore + share-card + result identity.
- Share-card idea: dossier renders nicely in monospace for screenshots
- Pages idea: "Reading Room" page built from the research bibliographies (WORLD-RESEARCH is the strongest reviewer-facing thread)
- The "you never know" Altman line is the tightest articulation of the whole premise — candidate epigraph.
