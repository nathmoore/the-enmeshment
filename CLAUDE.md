# CLAUDE.md — context for AI-assisted dev sessions

## What this is
The Enmeshment: a speculative-fiction profiling game shipped
as a ChatGPT GPT. An elevated BuzzFeed quiz — "what type of resistance would
the AI classify you as?" — wrapped in a near-future scenario about
government decision-making becoming enmeshed with AI.

**Names (locked 2026-06-13, DECISIONS.md):** the game/brand is **"The Enmeshment"**
(used for lore, share-card, result identity). The **GPT store listing title** is
**"The Enmeshment: AI Resistance Profile Quiz"** — brand + keyword tail for
discoverability (store discovery is search + sharing, not sidebar browsing).

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
- src/knowledge/*.txt — GPT knowledge files (lore-codex, archetypes, elicitation-playbook,
  archetype-dossiers — the player-facing voiced dossier prose; also the in-chat VERDICT
  source and, since 2026-07-01, the archetype→dossier-URL map: each block carries its LINK
  line the GPT copies verbatim. The old standalone archetype-links.txt was folded in + retired)
- src/gpt-config.md — the GPT Builder's non-instruction fields: name, store title/description,
  the 4 conversation starters (the cold-start funnel, versioned rather than typed-once)
- site/ — Eleventy public site → GitHub Pages: landing, per-archetype dossier pages
  (`/files/<slug>/`, the GPT's link-out targets), lore, reading room. Runbook: site/README.md

## Working style for sessions
- **Two layers — sort feedback to the right one.** Archetype work splits across two
  homes that share one character engine (Want/Need/Lie + reverse-engineering,
  MECHANICS §IV.D-bis): *"who they are"* — the formed characters + in-world story
  texture (how the AI-state reads each, the threat it poses) — lives in
  **src/knowledge/archetypes.txt**; *"how to tell them apart"* — routing: discriminant
  signatures, confused-pair discriminators — lives in **docs/planning/ELICITATION-SPEC.md
  §8**. They are kept separate so a wrong-feeling result is debuggable: decide whether
  it's *the character definition is off* (fix archetypes.txt) or *the character's right
  but the routing misfired* (fix the spec) — don't blindly edit both. Routing sorts on
  the character, never on the threat (threat is story texture, not a routing driver).
- Update the relevant epic doc's checklist as work completes.
- When editing instructions.md, re-run a character count and update the
  budget line in the comment block.
- Canon is set in 2038 (CANON.md). Keep other player-facing surfaces free of
  *other* hard dates and named real-world actors — unless deliberately decided
  and logged in DECISIONS.md.
- The verdict links out to the site's per-archetype dossier pages: the GPT copies the
  exact URL from the matched archetype's LINK line in src/knowledge/archetype-dossiers.txt
  and never invents one. The `/files/<slug>/` slugs are FROZEN — renaming a
  site/files/*.md breaks its LINK line.
- Public site lives in site/ (Eleventy); internal design docs stay in docs/ and are NOT
  published. Run/deploy steps: site/README.md.
- Sub-CLAUDE.md files: not needed at this repo size; revisit if src/ grows.
