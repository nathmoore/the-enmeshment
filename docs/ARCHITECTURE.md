# Architecture

> Status: **COMPLETE (Epic 1, 2026-06-13)** — system shape, knowledge-file split, and hosting locked. Release checklist + per-section char budgets = Epic 2.

## 1. System overview

The Enmeshment is not an app. It's a **prompt-architecture product** with three components:

```
┌─────────────────────────────────────────────────────┐
│  ChatGPT GPT (the product surface)                  │
│  ├── instructions.md  (≤ 8,000 chars — the "engine";│
│  │                     holds the voiced verdict fmt)│
│  └── knowledge files  (the "content cartridge")     │
│       ├── lore-codex.txt                            │
│       ├── archetypes.txt                            │
│       ├── elicitation-playbook.txt                  │
│       └── archetype-dossiers.txt (prose + LINK line)┼──┐
├─────────────────────────────────────────────────────┤  │ exact link
│  GitHub repo (the open kitchen)                     │  │ (copied,
│  ├── docs, lore, guardrails, conversation           │  │  not guessed)
│  └── site/ → GitHub Pages (Eleventy)                │◄─┘
│       ├── /                  landing + CTA          │
│       ├── /files/<slug>/     11 dossier pages       │
│       ├── /scenario/         story background       │
│       └── /reading-room/     research bibliographies│
└─────────────────────────────────────────────────────┘
```

The GPT delivers a paraphrased verdict in chat, then hands the player the **exact URL** of their
archetype's dossier page — copied from the matched archetype's `LINK` line in
`archetype-dossiers.txt`, never constructed (see
[CONTENT-ARCHITECTURE.md](planning/CONTENT-ARCHITECTURE.md) and MECHANICS §I "Platform
capabilities & constraints").

### Design constraint that shapes everything
The GPT instructions field is capped at **8,000 characters**. Therefore:
- **Instructions** hold only: persona, game loop, guardrail enforcement, output format rules, and pointers to knowledge files.
- **Knowledge files** hold all content: lore, archetype definitions, question bank, example outputs.
- **Settled (MECHANICS §I + CONTENT-ARCHITECTURE.md §2–3, 2026-06-13):** load-bearing, exact-wording or fires-every-session content (guardrails, stop rule, persona, **the voiced verdict format + verbatim disclaimer**, output-handoff rule) = instructions; bulk authored content (archetypes, questions, URL map) = knowledge files. *(The in-chat verdict template was folded from a knowledge file into instructions on 2026-06-13 — DECISIONS — for retrieval reliability; it's small and fires every session.)*

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
- Character-count check: tracked via CLAUDE.md prime directive (re-run and update the budget line on each edit to `instructions.md`). Precise per-section counts = Epic 2 authoring.

## 5. The public site (GitHub Pages)

**Locked 2026-06-13** (DECISIONS; [CONTENT-ARCHITECTURE.md](planning/CONTENT-ARCHITECTURE.md) §4):
[Eleventy](https://www.11ty.dev/) static site in [`site/`](../site/), deployed to **GitHub Pages
via the "GitHub Actions" source** — *not* the legacy root/`/docs` mode, so the internal design
`docs/` is never published. The internal `docs/` stays the design layer; `site/` is the curated
public face.

- **Why it exists:** the GPT links each verdict to a per-archetype dossier page here (the
  standardised, shareable "file Concord forwards"). Also hosts the landing page, lore, and the
  research "reading room."
- **Routes:** `/` · `/files/<slug>/` (×11, frozen slugs) · `/scenario/` · `/reading-room/`.
- **One template, 11 data files:** `site/_includes/dossier.njk` + `site/files/<slug>.md`. Per-page
  OG/Twitter meta for share unfurls (the virality engine, MECHANICS §I). No third-party trackers.
- **Deploy:** [`.github/workflows/pages.yml`](../.github/workflows/pages.yml) — **manual-only**
  (`workflow_dispatch`) until Pages is enabled with source "GitHub Actions"; then add the `push`
  trigger (Epic 2/3).
- **Status:** scaffold + stubs only. Page prose, styling, share images, lore/reading-room content
  = Epic 2/3 (see [EPIC-2-IMPLEMENT.md](planning/EPIC-2-IMPLEMENT.md)).
- **URL base:** `nathmoore/the-enmeshment` project page → `https://nathmoore.github.io/the-enmeshment/`
  (`pathPrefix: "/the-enmeshment/"`). Planned upgrade to custom domain **`enmeshed.xyz`** (flip
  `pathPrefix` to `/`; GitHub auto-redirects old links). See CONTENT-ARCHITECTURE §4–5.

## 6. Deferred decisions

- [x] **One GPT (MVP):** single intake-screener experience. No lore-explorer GPT in v1 (2026-06-13, DECISIONS.md).
- [x] **Shareable output format:** locked in [OUTPUT-SPEC.md](planning/OUTPUT-SPEC.md) — share-card (name + one-liner + hook), built for screenshot; no image gen for v1. Execution = Epic 2.
- [ ] Localisation / non-ChatGPT versions (Claude Project, Gem) — confirmed out of scope for MVP; revisit post-launch.
