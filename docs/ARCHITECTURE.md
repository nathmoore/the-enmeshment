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
│  Shareable paste-prompt (works in ANY AI tool)      │
│  └── src/prompts/profile-prompt.md                  │
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

## 2. The two play modes

| Mode | Flow | Why it exists |
|---|---|---|
| **A. Paste-prompt mode** | GPT gives player a self-profiling prompt → player runs it in their own AI tool(s) → pastes result back → GPT classifies | The meme made playable: "your AI already has a file on you" |
| **B. In-game interview mode** | GPT asks ~6–10 in-fiction questions directly | Zero-friction path for players who don't want to leave the chat |

TODO (Epic 1): decide whether Mode A result + Mode B answers can be combined into one classification.

## 3. Data flow & privacy posture

- No memory, no storage, no accounts. Each session is ephemeral by design.
- The paste-prompt is engineered to elicit **persona-level signals** (Big 5 tendencies, AI-politeness habits, generalist/specialist knowledge, analogue-skills self-assessment, digital footprint *style*) — never identifying data.
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
