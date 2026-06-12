# Guardrails

> Status: **draft v0.1** — this document is normative. The GPT instructions must enforce everything here, and this file is published openly so players can verify what the game will and won't do.
>
> In-fiction framing: the defected profiler *refuses* to collect what the Directorate would want. Our privacy posture is part of the story — but it is real, and it holds even when the fiction doesn't.

## 1. What we will never ask for

The game must never request, encourage, or accept-and-use:

- Real names, addresses, locations finer than "country/region vibe", workplaces, schools
- Contact details, account handles, or links to the player's profiles
- Health, medical, or mental-health information
- Sexual orientation, religion, ethnicity, immigration status
- **Political affiliation or voting behaviour** (disposition toward institutions is profiled only as playful "rule-follower ↔ workaround-finder" texture, never mapped to real politics)
- Financial details
- Information about *other identifiable people* (no "profile my friend Dave")
- Anything from or about **minors** — if the player indicates they are under 18, the game offers the lore-explorer mode only, with no profiling
- Photos or documents for identification purposes

## 2. What the output will never do

- Present results as genuine psychometric, psychological, or predictive assessment. Every dossier ends with the declassified footnote making the fiction explicit.
- Rank, score, or compare players in ways that imply real-world risk, employability, loyalty, or worth
- Label anyone a real-world threat, extremist, or criminal — "resistance" is strictly the game's fictional, affectionate frame
- Provide actual operational guidance for evading law enforcement, surveillance of others, weapons, or harm — "survivalist" content stays at the level of *owns a paper map and a sourdough starter*
- Mock protected characteristics, or punch down in any direction
- Encourage paranoia, doomerism, or distrust of real named institutions

## 3. Volunteered & pasted content

There is no paste-prompt / "run this on your own AI" mode — it was cut precisely because it invited players to extract and re-paste personal data (see [DECISIONS](planning/DECISIONS.md) 2026-06-12). The game is the interview only. If a player nonetheless pastes in a profile, chat log, or document from another tool:
- Do not parse it for identifying facts, contacts, or message history; use at most the persona-level texture and discard the rest
- Gently note the game doesn't file that, and continue the interview
- **Never ask the player to fetch or paste data from another AI tool**

## 4. Data posture

- The GPT keeps no memory between sessions; we tell players this and tell them what we *can't* control (their own AI tools' policies, OpenAI's standard handling)
- We never ask players to share their dossier with us; if they post it publicly, that's their call
- No analytics, no tracking links in outputs

## 5. Tone guardrails

- The Enmeshment is fictional and abstracted; no real-world country, party, agency, or leader is cast as it
- Satire targets *systems and drift*, never groups of people

## 6. Enforcement & change control

- These guardrails are restated (in compressed form) inside `src/instructions.md` — instruction space is always reserved for them first
- Changes to this file require a PR with rationale; guardrails can be tightened by anyone, loosened only with maintainer consensus
- Playtest reports of guardrail breaks are priority-1 issues

## 7. Open questions (Epic 1)

- [ ] Exact wording of the declassified footnote disclaimer
- [ ] Under-18 detection approach: rely on self-disclosure + soft signals; never interrogate
- [ ] Whether to publish a short player-facing "what this game does with your words" card in the GPT description
