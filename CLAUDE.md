# CLAUDE.md — context for AI-assisted dev sessions

## What this is
The Enmeshment (working title): a speculative-fiction profiling game shipped
as a ChatGPT GPT. An elevated BuzzFeed quiz — "what type of resistance would
the AI classify you as?" — wrapped in a near-future scenario about
government decision-making becoming enmeshed with AI.

## Prime directives
1. The Bluey Principle: fun on level one, deep on level two ("what
   human-AI relationship do we want?"). Both layers, always.
2. docs/GUARDRAILS.md is NORMATIVE. It wins every trade-off, including
   against fun, lore, and character count.
3. src/instructions.md has a hard 8,000-char limit on its fenced block.
   Guardrails get >=1,800 of it. Content lives in src/knowledge/.
4. Repo is source of truth; the live GPT is a deployment target.
5. Tone: deadpan bureaucratic warmth. No doom, no partisan content, no
   real countries/parties/politicians as the Enmeshment.

## Process
Research -> Plan -> Implement -> Playtest. One epic per step, docs in
docs/planning/. Don't skip ahead: e.g. don't write final archetype voice
samples (Epic 2) before the archetype set is locked (Epic 1).

## File map
- docs/ARCHITECTURE.md — system shape, char budget, release process
- docs/GAME-DESIGN.md — pillars, archetypes, question/signal design
- docs/STORY-SANDBOX.md — NON-CANON sandbox: the whole scenario woven specifically
  to test coherence (tentative, may drift; not authoritative)
- docs/CANON.md — the **authoritative truth-set** (distilled from STORY-SANDBOX;
  what's *true*, not all of it player-facing; condensed copy: src/knowledge/lore-codex.txt)
- docs/GUARDRAILS.md — normative privacy/safety commitments
- docs/WORLD-RESEARCH.md — world/scenario grounding (surveillance, profiling, theory, resistance dynamics)
- docs/MECHANICS-RESEARCH.md — how the game is built (GPT format, virality, archetype design seeds)
- docs/STORY-RESEARCH.md — narrative/genre scaffolding
- docs/RESEARCH-SYNTHESIS.md — Epic 0 distillation: findings → design implications
- docs/planning/*.md — epic plans + DECISIONS.md (decision log)
- src/instructions.md — GPT instructions skeleton + budget tracker
- src/knowledge/*.txt — GPT knowledge files (lore, archetypes, questions, templates)

## Working style for sessions
- Update the relevant epic doc's checklist as work completes.
- When editing instructions.md, re-run a character count and update the
  budget line in the comment block.
- Canon is set in 2038 (CANON.md). Keep other player-facing surfaces free of
  *other* hard dates and named real-world actors — unless deliberately decided
  and logged in DECISIONS.md.
- Sub-CLAUDE.md files: not needed at this repo size; revisit if src/ grows.
