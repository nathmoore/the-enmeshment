# Architecture

> Status: **stub** — to be completed during Epic 1 (Plan)

## 1. System overview

The Enmeshment is not an app. It's a **prompt-architecture product** with three components:

```
┌─────────────────────────────────────────────────────┐
│  ChatGPT GPT (the product surface)                  │
│  ├── instructions.md  (≤ 8,000 chars — the "engine")│
│  └── knowledge files  (the "content cartridge")     │
│       ├── lore-codex.txt                            │
│       ├── archetypes.txt                            │
│       ├── question-bank.txt                         │
│       └── output-templates.txt                      │
├─────────────────────────────────────────────────────┤
│  GitHub repo + Pages (the open kitchen)             │
│  └── docs, lore, guardrails, conversation           │
└─────────────────────────────────────────────────────┘
```

### Design constraint that shapes everything
The GPT instructions field is capped at **8,000 characters**. Therefore:
- **Instructions** hold only: persona, game loop, guardrail enforcement, output format rules, and pointers to knowledge files.
- **Knowledge files** hold all content: lore, archetype definitions, question bank, example outputs.
- TODO (Epic 1): test how reliably the GPT retrieves from knowledge files vs. instructions, and decide what *must* live in instructions (guardrails certainly do).

## 2. The play mode

Single mode: the **adaptive in-game interview**. The agent — a charming intake
screener (see [DECISIONS](planning/DECISIONS.md) 2026-06-11) — improvises ~3–6
oblique, in-fiction questions, diverging on the player's answers, then classifies
at a confidence threshold (DECISIONS 2026-06-12). No questionnaire, no forms.

The former paste-prompt / "Field Kit" mode (run a prompt in your own AI, paste
the result back) was **cut**: it invited data extraction from other tools — the
oversharing risk we most want to avoid (MECHANICS §III). See DECISIONS 2026-06-12.

## 3. Data flow & privacy posture

- No memory, no storage, no accounts. Each session is ephemeral by design.
- The interview elicits only **persona-level signals** (Big 5 tendencies, AI-politeness habits, generalist/specialist knowledge, analogue-skills self-assessment, digital footprint *style*) — never identifying data.
- See [`GUARDRAILS.md`](GUARDRAILS.md) — guardrails are enforced *in the instructions layer*, not just documented.

## 4. Source of truth & sync

The repo is the source of truth. The live GPT is a **deployment target**.

- `src/instructions.md` → manually pasted into GPT Builder on release
- `src/knowledge/*.txt` → uploaded to GPT Builder on release
- TODO (Epic 2): lightweight release checklist + version tag convention (e.g. `gpt-v0.1`)
- TODO: character-count check — keep a counter line at the top of `instructions.md`

## 5. GitHub Pages (later)

- Likely: `/docs` as Pages root or a `site/` folder; decision deferred to post-MVP
- Purpose: lore wiki, design essays, "what relationship do we want with AI?" conversation hub

## 6. Open questions (carry into Epic 1)

- [ ] One GPT or two (game vs. lore-explorer)?
- [ ] How do we make outputs shareable (copy-paste card format? image gen?)
- [ ] Localisation / non-ChatGPT versions (Claude Project, Gem) — out of scope for MVP?
