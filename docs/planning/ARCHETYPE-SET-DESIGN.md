# Archetype set — design record (maintainer scaffolding)

> **Extracted 2026-09-17 from `src/knowledge/archetypes.txt`** (EPIC-2B Track A1, per the
> CONVERSATION-ARC Appendix A audit). The shipped knowledge file is **agent-facing**: it now
> carries only the framing (THE FRAME / NORTH STAR / PROFILING LENS / SPICE / RULES) and the
> 11 cards. Everything below is the *design process* — how the set was chosen, what was cut,
> what's still open — kept verbatim (original formatting preserved in the fenced blocks) so
> nothing is lost. The pre-split file is in git history (`git log -- src/knowledge/archetypes.txt`).
>
> Also stripped from the shipped cards in the same pass: per-card naming history (listed
> below), pointers to repo docs the GPT doesn't hold (ELICITATION-SPEC, DECISIONS, WORLD-,
> MECHANICS-RESEARCH — replaced with the in-knowledge-file equivalent, `elicitation-playbook.txt
> §7`), and the retired "every archetype is a form of resistance" rule.
>
> **Live sources of truth:** the cards → `src/knowledge/archetypes.txt`; routing →
> [ELICITATION-SPEC §8](ELICITATION-SPEC.md) (repo) / `elicitation-playbook.txt` §6–§7 (shipped);
> decisions → [DECISIONS.md](DECISIONS.md).

## 1. Selection criteria & set-level criteria

```text
SELECTION CRITERIA (in priority order)
--------------------------------------
1. THE TWO-VOICES TEST (first filter). The name must be sayable by BOTH a
   bureaucratic AI filing-clerk AND a mate in the group chat — and the joke is
   the state using your friends' nickname for you as an official file category.
   Fails if only one voice would say it ("Techno Futurist" = only a think-tank;
   "The Planner" = only your friends, and blandly). "Model Citizen" = both. Gold.
2. SHAREABILITY (BuzzFeed mechanics, MECHANICS-RESEARCH §I/§D). Result must feel
   SPECIFICALLY accurate (not Barnum-vague), be screenshot-ready, invite "what
   did YOU get?", and be flattering-with-an-edge. The NAME carries most of the
   work: 2-4 words, claimable identity, brag-with-a-wince, interpretable cold.
3. INTELLIGENCE PRIORITIES (WORLD-RESEARCH §II — the 5 objectives). Each label
   maps to what the state actually tracks, and each peg has a cost-inversion:
     #1 Coordination (master fear)  #2 Predictability  #3 Anomaly/illegibility
     #4 Dependency (leverage)       #5 Function/replaceability (load-bearing)
   Plus the JOIN PULL / pull-to-conform — the comfort the state offers this type
   (Frictionlessness / Recognition / Belonging / Certainty / Status / Provision /
   Pleasure-Wellness / Meaning). Leaning INTO the comfort = favourable; RESISTING
   it = the pressure point the state can press. "Being seen / witnessed" is the
   central pull and the one the player feels while playing.
4. ROUTABILITY (late-stage screen, NOT yet a cutting blade). Can the adaptive
   interview actually tell two types apart in 3-6 answers? Adjacent pairs get
   validated against the elicitation playbook later — they are flagged below,
   not cut now.

SET-LEVEL CRITERIA (the set as a whole, not just each card)
----------------------------------------------------------
A. COVERAGE. The set should span all 5 intelligence objectives (#1-#5). It now
   does. Once all five are covered, more archetypes mostly add ROUTING LOAD, not
   coverage — so the live question becomes routability, not "what's missing."
B. PROTECT THE RESISTER END. The favourable/Join types (#4/#5) are each shareable
   but BLUR as a block ("you, but compliant in a slightly different domain"). The
   illegible/coordination types (#1, #3) are thinner and carry the Tomorrow-When
   fantasy + the dramatic weight. When cutting for discipline, cut from the
   comfortable end first; protect the resister roles.
C. TRAJECTORY SPREAD. The set should offer a satisfying range of break-modes
   (Join / Burn / Die / illegible) — the fantasy is "who'd go which way." Every
   archetype must answer: what is this type's specific MODE of breaking conformity,
   or the specific reason it won't?
D. NO HARD COUNT CEILING, but edit as discipline. Space is ~free (knowledge file,
   not the 8k instructions budget), so don't cut for SPACE. Cut for ROUTABILITY,
   with playtest evidence (Epic 2) — not by guessing now.

```

## 2. Retired rule (removed from RULES, 2026-09-17)

```text
- (Retired: the old "every archetype is a form of resistance" rule — superseded
  by the intake-screener frame; it's predicted trajectory now, not a badge.)
- Names rule, the worked example that was cut from the shipped line: "Avoid 'active
  villain' / saboteur connotations — that's why the Enforcer was cut and why Chaos
  Agent became Wildcard." The RULES line also pointed at "the Off-Gridder watchlist
  note in the parking lot" (§5 below).
```

## 3. Changelogs (2026-06-12 → 2026-06-13)

```text
Changelog 2026-06-12: cut Reformer + Machine Agitator; folded Climber into
Self-Optimiser; added Social Linchpin (rare Priority-Interest tail). 13 -> 11.
Changelog 2026-06-13: added the CHARACTER (Want/Need/Lie) line to each card; relocated the
routing/discriminant scaffolding to ELICITATION-SPEC §8 (layer separation).
Changelog 2026-06-13 (deepening pass): developed each card into a fuller formed character —
added a light GHOST to every CHARACTER line and rewrote each trajectory lean into an explicit
BREAK-MODE (how this type splinters, or why it won't). The paired routing workings were
developed in the same pass into ELICITATION-SPEC §8.3 (per-archetype discriminant signatures)
and §8.4 (confused-pair discriminators) — same engine, two homes; reason the character once,
land it in both. Story-texture / threat reads stay here; the how-to-tell-apart stays in the spec.
Changelog 2026-06-13 (feedback pass): reframed five cards per editing notes — Artist (Want is
the CROWD's recognition, AI is the new mediating layer that "speaks their language"); Self-Optimiser
(body & career woven as ONE drive, two domains/generations, same net effect); Bookworm (broadened
from "reading" to wide independent self-enrichment in any medium; runs INWARD/cerebral); Tinkerer
(broadened from tech-stack to general hands-on making/mending; Ghost = prove individualness, Lie =
apartness is self-sufficient when they still need community; runs OUTWARD/physical — the Bookworm's
twin); Wildcard (the chaos is a self-protective FRONT over a fear of being truly seen — and it's
still MAPPABLE: the slow read lands on "we see you anyway"); Social Linchpin (now the QUIET bridge
across the social graph / high betweenness, vs the Organiser's OVERT mobilising — CANOE as
corroborating colour). Spec §8.3/§8.4 synced in the same pass.
Changelog 2026-06-13 (voice pass): drafted the player-facing voiced prose per archetype —
P1 (personality read) · ASSESSMENT (the trajectory verdict: what they'd bring to a resistance +
one sting) · FIELD NOTES (3 dossier bullets). Authored to the output-templates register and
GUARDRAILS; flattering-with-an-edge, cold-legible, the sting varied across the set so it reads
well as a group-chat compare. EXTRACTED to its own file — src/knowledge/archetype-dossiers.txt —
so the voiced set is maintainable in one place (this doc stays the character/design layer).
```

## 4. Per-card naming history (was in the card titles)

- 3. THE SELF-OPTIMISER  ←  was titled: `3. THE SELF-OPTIMISER   [absorbed The Climber, 2026-06-12]`
- 5. THE SKEPTIC  ←  was titled: `5. THE SKEPTIC   [name SETTLED 2026-06-12: Skeptic over Cynic — the name flatters
                 ("I see through it"), the dossier deflates ("no you don't, and it
                 changes nothing"); the gap is the joke. concept = "Knowing Participant"]`
- 6. THE ARTIST  ←  was titled: `6. THE ARTIST   [simplified from "Auteur"]`
- 7. THE BOOKWORM  ←  was titled: `7. THE BOOKWORM   [simplified from "Autodidact"]`
- 8. THE TINKERER  ←  was titled: `8. THE TINKERER   [renamed from "Saboteur Technician" — Luddite-correction safe]`
- 9. THE ORGANISER  ←  was titled: `9. THE ORGANISER   [renamed from "The Planner" — dual-coded on purpose]`
- 10. THE WILDCARD  ←  was titled: `10. THE WILDCARD   [renamed from "Chaos Agent" 2026-06-12 — "Agent" implied
                    intent/villainy (the Enforcer trap); "Wildcard" keeps the
                    illegibility, drops the menace, more group-chat-native]`
- 11. SOCIAL LINCHPIN  ←  was titled: `11. SOCIAL LINCHPIN   [restored from parking lot, 2026-06-12]`

## 5. Open questions, parking lot, and the MOVED note

```text
OPEN QUESTIONS / KNOWN TENSIONS (for the next editing round)
============================================================================
- SET SIZE vs ROUTABILITY (the live question). 11 is fine to CARRY now — archetypes
  live in a knowledge file, NOT the 8,000-char instructions budget, so count costs
  almost nothing on space (knowledge: 20 files, <=512 MB each — DECISIONS 2026-06-11).
  The real ceiling is whether the adaptive interview can tell 11 types apart in 3-6
  answers. Treat the set as a locked-for-now SHORTLIST; pressure-test routability in
  Epic 2 (needs the built GPT) and cut the hardest-to-distinguish pairs THEN, with
  evidence, rather than guessing now.
- ADJACENT PAIRS to validate against the elicitation playbook (routability):
  Model Citizen / Power User (separable by customiser-vs-defaults);
  Self-Optimiser body-vs-career (now ONE card — confirm the split isn't needed);
  Organiser / Social Linchpin (overtly-acts vs quietly-bridges-across-the-graph — the
  discriminator doubles as the fun group-chat compare);
  Bookworm / Tinkerer (shared independent-self-enrichment psychology — split inward/
  cerebral vs outward/physical-hands).
  Full discriminators: ELICITATION-SPEC §8.4.
- NAMES SETTLED 2026-06-12: Skeptic (over Cynic, #5); Wildcard (over Chaos Agent, #10).

PARKING LOT (considered, folded or cut — kept for reference)
- Folded UP: Techno Optimist/Futurist/Merger, AI Advocate -> Power User.
- Folded into Enforcer-then-cut: Social Enforcer, Law & Order Advocate, The
  Enforcer (risked an "active villain" read; held back for tone).
- Cut 2026-06-12: The Reformer (lowest texture, weakest two-voices; reform-delusion
  edge preserved as dossier flavour elsewhere). The Machine Agitator (narrow
  friend-type, overlapped the Skeptic; provocation signal routed into Skeptic =
  head / Tinkerer = hands).
- Folded 2026-06-12: The Climber -> Self-Optimiser (same #4 dependency peg).
- Restored 2026-06-12: Social Linchpin (rare Priority-Interest acute tail).
- WATCHLIST (Epic 2 gap, NOT added 2026-06-12): The Off-Gridder / Survivalist
  (analogue, low-dependency, "would be fine if it all went down"). Held OUT
  deliberately: (a) it's a narrow PRESENT-STATE skillset, but the verdict is a
  PREDICTED TRAJECTORY / future horizon — so a skillset card is a category error;
  route the disposition to where it's HEADED instead. (b) Tinkerer / Bookworm /
  Wildcard / Organiser may already BE the future-state of a low-tech-dependency
  person. Re-add only if playtest shows off-grid players with no good home (mis-
  routed into Tinkerer).
- Renamed: The Planner -> Organiser; Saboteur Technician -> Tinkerer;
  Auteur -> Artist; Autodidact -> Bookworm; Ironist -> Skeptic.
- Held/cut: The Hedonist (pacified-by-pleasure; very shareable — re-add candidate),
  The Truth Seeker (Soviet "struggle for the truth"; folds toward Bookworm),
  Social Chameleon (no stable signature — overlaps Wildcard), Techno Pessimist
  (not a taggable friend-type), The Enmeshed Ideal (terminal Power User; riff on
  the title — strong but extreme), The Expressive Poet (-> Artist).

============================================================================
ROUTABILITY & DISCRIMINANT SIGNATURES → MOVED (2026-06-13)
============================================================================
The routing layer — how to TELL THE ARCHETYPES APART (discriminant signatures, the
confused-pair discriminators, response-texture cues, performer risk, the best-fit
routing model) — now lives in ELICITATION-SPEC §8 "Routing principles." It was
relocated to keep THIS file the STORY layer — "who they are" (formed characters; see
the CHARACTER line per card) PLUS the in-world texture: how the AI-state relates to
each type and the kind of THREAT it poses (the Peg / Edge / "PROFILING LENS" material
above). That threat read is evocative story colour, NOT a routing driver — routing
sorts on the character (Want/Need/Lie), per the spec. The spec is the "how to tell
them apart" layer — so a playtest miss is debuggable against one or the other (is the
character wrong, or the routing guidance?). The confused-pair contrasts are still
flagged per-card under each archetype's "Flags:" line (they double as the fun
group-chat compares); their discriminator MECHANICS live in the spec.
  → docs/planning/ELICITATION-SPEC.md §8 (routing principles)
  → docs/MECHANICS-RESEARCH.md §IV.D-bis (the character-construction engine)

```
