# Content Architecture — the Epic 1 → Epic 2 bridge

Status: **STARTED 2026-06-13** (delivery model + hosting/Eleventy locked; instructions skeleton +
prose stubbed) | Owns the EPIC-1-PLAN "Content architecture (E1→E2 bridge)" deliverable.

> **Purpose.** Lock *what content goes where* before Epic 2 authors it: the instructions.md
> section skeleton, the knowledge-file split (against the 20-file / 8,000-char / ≥1,800-guardrail
> ceilings), and how the verdict is delivered. Grounded in the GPT-runtime findings in
> [MECHANICS-RESEARCH.md §I "Platform capabilities & constraints"](../MECHANICS-RESEARCH.md).
> This doc is a living bridge — the delivery model below is **decided**; the fuller skeleton and
> split fill in as the elicitation + routing spec (ELICITATION-SPEC, incl. §8 routing principles)
> and output spec lock in Epic 1. **Scope split:** this doc owns the **plumbing** (delivery,
> hosting, file split, slugs); the *artefact's design* — what the dossier must do (anatomy, the
> screenshot fold, register, the "they got me" mechanic, footnote/disclaimer, share-card, the
> decline path) — is [OUTPUT-SPEC.md](OUTPUT-SPEC.md).

---

## 1. Dossier delivery model — DECIDED (2026-06-13)

**The agent paraphrases the verdict in-voice, then hands over an exact link to a hosted archetype
page.** In play: the intake agent's register shifts from interview to dossier, it names and voices
the classification naturally ("ah — you're a *Skeptic*…", in the Directorate's deadpan warmth),
and then supplies the **exact URL** of that archetype's dossier page.

**Why (from the runtime findings):**
- **Verbatim-from-knowledge is unreliable** (models paraphrase; copyright filters can refuse) —
  and a recited file is *worse* play than a voiced verdict anyway. So the spoken verdict is
  **generated within a voiced template** (the `OUTPUT FORMAT` section of
  [instructions.md](../../src/instructions.md) — folded in from the retired `output-templates.txt`,
  2026-06-13), not echoed from a file. (MECHANICS §I, finding 2.)
- **The one thing that must be exact is the link** — and emitting a link is just text, needing
  **no Web Browsing and no Action**. Reliability depends on the agent **copying** the URL from an
  explicit map, never **guessing** a slug. (MECHANICS §I, finding 3.)

**Consequence:** the rich, standardised dossier can live on a hosted page (the "file Concord
forwards"), while the in-chat moment stays warm and generated — best of both. This un-parks the
"result links out to GitHub Pages / repo doc pages per archetype" idea (DECISIONS.md scratch).

---

## 2. Knowledge-file split

Against the verified ceilings (DECISIONS 2026-06-11): **20 files max**, **≤512 MB / 2 M tokens
each**, instructions **≤8,000 chars** with **≥1,800 reserved for guardrails**. Knowledge is
**uploaded** static `.txt` (RAG-indexed) — *not* live-linked to GitHub (MECHANICS §I, finding 4);
the cost is manual re-upload on release, already in the ARCHITECTURE.md process.

> **One artefact chain, no intermediate.** The full thinking lives in the planning docs
> (ELICITATION-SPEC is the elicitation/routing "workings"); each uploaded `src/knowledge/*.txt` is a
> **distilled, promptable cut** of it, authored in Epic 2 (the playbook is *built from* the spec, not
> a copy). The agent never reads the spec — so depth there costs nothing against its token budget.

| File | Role | Status |
|---|---|---|
| `lore-codex.txt` | Condensed canon for the narrator | exists (stub) |
| `archetypes.txt` | The 11 archetypes — **"who they are":** formed characters (Want/Need/Lie), deep layer (routing/discriminant signatures live in the playbook, not here — see ELICITATION-SPEC §8) | exists (live source of truth) |
| `question-bank.txt` → elicitation + **routing** playbook | Anchor questions + question-type taxonomy + the **"how to tell them apart"** layer (discriminant signatures, confused-pair discriminators) — authored from ELICITATION-SPEC §8 | exists (v0 stub) |
| ~~`output-templates.txt`~~ | **Folded into `instructions.md` `OUTPUT FORMAT` and deleted (2026-06-13).** The voiced verdict + footnote + verbatim disclaimer are thin and fire every session, so they live in always-in-context instructions, not RAG (DECISIONS 2026-06-13). | removed |
| **`archetype-links.txt`** *(new)* | **Archetype → exact dossier-page URL lookup map** | exists (authored 2026-06-30) |

File count after adding the map: **4 of 20** (lore-codex, archetypes, question-bank, archetype-links;
output-templates folded into instructions) — comfortable headroom.

`archetype-links.txt` is deliberately its own tiny file (not folded into archetypes.txt) so the
"copy the exact URL, never invent one" rule has a single unambiguous source the instructions can
point at.

---

## 3. instructions.md section skeleton — STUB

Fills in as Epic 1 locks the elicitation/classification/output specs. Sections (mirrors the
budget plan already in [instructions.md](../../src/instructions.md) and EPIC-1-PLAN's content-
architecture deliverable):

1. **Persona & frame** — the intake-screener voice (the inference mechanism, not decoration).
2. **Interview rules** — improvise within a **~5-exchange** session (band 3–6; one *exchange* =
   anchor probe + ≤1 follow-up); 3-anchor backbone; reveal timed by the story/experience floor,
   not routing confidence. Full decisions: [ELICITATION-SPEC.md](ELICITATION-SPEC.md).
3. **Classification trigger / stop rule** — *when* to classify (minimum exchange count + ~75%
   dramatic floor + "enough signal" condition). Load-bearing because the runtime keeps no
   confidence variable (MECHANICS §I, finding 1).
4. **Guardrails block** — ≥1,800 chars; never-ask boundaries for an improvising interviewer.
5. **Output format + handoff** — the `OUTPUT FORMAT` section *is* the voiced verdict template
   (folded in from the retired `output-templates.txt`, 2026-06-13): shift to dossier voice, voice
   the verdict, **then emit the archetype's exact URL from `archetype-links.txt` — never construct
   or guess a link.** (The single most important reliability rule for the delivery model.)

---

## 4. Hosting + URL scheme — DECIDED (2026-06-13)

**The public site is built with [Eleventy](https://www.11ty.dev/) (11ty) and deployed to GitHub
Pages via the "GitHub Actions" Pages source.** Scaffold started at [`site/`](../../site/) (stubs;
content authored in Epic 2). Rationale and the alternatives weighed are in
[DECISIONS.md](DECISIONS.md) (2026-06-13).

**Why Eleventy + Pages (over the legacy options):**
- **Repo is source of truth** — the site lives beside canon, version-controlled, no server,
  free, no third-party trackers (the privacy-respecting profiler practices what it preaches).
- **One template, 11 data files** — each archetype is a markdown file with front matter rendered
  through a single dossier layout (DRY; consistent; stable URLs). Not 11 hand-written pages.
- **"GitHub Actions" Pages source, not "root or `/docs`"** — the legacy modes would publish our
  *internal* design `docs/` as the website. Actions decouples the published site (`site/`) from
  internal docs, keeping the public face curated.
- **Per-page OG/Twitter meta** — the dossier pages are the share artefacts; the unfurl card when
  a link is pasted into a group chat is the virality engine (MECHANICS §I). A homepage anchor
  can't carry per-archetype previews; separate pages can.
- *Rejected:* Read the Docs / MkDocs (look like technical docs — the dossier *is* the product,
  needs design control); Netlify/Cloudflare Pages (fine, but split hosting from the repo home).

**Routes / IA** (don't put it all on the homepage):

| Path | Source | Purpose |
|---|---|---|
| `/` | `site/index.njk` | Landing — hook + "Play on ChatGPT" CTA + nav |
| `/files/<slug>/` | `site/files/<slug>.md` | The 11 dossier pages — **the GPT's link targets** |
| `/scenario/` | `site/scenario.md` | Shared story background (player-safe, from CANON.md) |
| `/reading-room/` | `site/reading-room.md` | Research bibliographies (the parked "Reading Room") |

Story background is **shared on `/scenario/`** (DRY); each dossier carries only a short
archetype-specific framing + a link to `/scenario/` — not the whole backstory on 11 pages. A link to
the repo sits in the global footer.

**Slug scheme (FROZEN once published):** `…/files/<slug>/`, `<slug>` = lowercase-kebab archetype
name. The canonical 11 (these are what `archetype-links.txt` maps to — renaming a `site/files/*.md`
changes its URL and breaks the map):

`model-citizen` · `power-user` · `self-optimiser` · `machine-companion` · `skeptic` · `artist` ·
`bookworm` · `tinkerer` · `organiser` · `wildcard` · `social-linchpin`

**Still a future workstream (Epic 2/3), not blocking Epic 1:** authoring the dossier page prose
(awaits archetypes.txt voice samples), the `/scenario/` + `/reading-room/` content, styling, share-card
images, enabling Pages, and adding the workflow's `push` trigger. What Epic 1 needs is settled:
the slug scheme + the instructions handoff rule (§3). Build/deploy steps live in
[EPIC-2-IMPLEMENT.md](EPIC-2-IMPLEMENT.md); deploy mechanism in [ARCHITECTURE.md](../ARCHITECTURE.md) §5.

---

**URL base (DECIDED 2026-06-13):** repo `nathmoore/the-enmeshment`, served first as a **GitHub
project page** → `https://nathmoore.github.io/the-enmeshment/`, `pathPrefix: "/the-enmeshment/"`.
Custom domain **`enmeshed.xyz`** is the planned upgrade (flip `pathPrefix` to `/`, re-author the
URL map; GitHub auto-redirects old links). Author `archetype-links.txt` (Epic 2) against the
current project-page base: `https://nathmoore.github.io/the-enmeshment/files/<slug>/`.

## 5. Open / not yet locked
- Full instructions.md skeleton wording + per-section char counts (Epic 2, once prose exists).
- ~~Complete signal→archetype mapping placement (its own deliverable in EPIC-1-PLAN).~~
  **RESOLVED 2026-06-13:** folded into [ELICITATION-SPEC.md](ELICITATION-SPEC.md) §8 "Routing
  principles" (reframed off rigid mapping → probabilistic best-fit; one archetype → one dossier).
- *When to buy `enmeshed.xyz`* — defer to just before public launch (no blocker now).
- Per-archetype share-card (OG) images — placeholder `ogImage` field already stubbed per file.
