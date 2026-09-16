# site/ — The Enmeshment public site (runbook)

Eleventy ([11ty](https://www.11ty.dev/)) static site → GitHub Pages. This is the personal ops
runbook: every command to run it locally and every GitHub step to ship it. It's committed
deliberately — the repo is the open kitchen, and the ops steps are part of the workings.

**Locked decision + rationale:** [DECISIONS.md](../docs/planning/DECISIONS.md) (2026-06-13),
[CONTENT-ARCHITECTURE.md](../docs/planning/CONTENT-ARCHITECTURE.md) §4, [ARCHITECTURE.md](../docs/ARCHITECTURE.md) §5.

## What this site is for
The GPT gives a paraphrased verdict in chat, then hands the player the **exact URL** of their
archetype's dossier page here — copied from the matched archetype's `LINK` line in
`src/knowledge/archetype-dossiers.txt`, never guessed. These pages are the standardised,
shareable artefact. **The slugs are FROZEN:** renaming a file changes its URL and breaks its LINK.

## Prerequisites
- **Node.js 20+** (`node -v`). Eleventy 3 needs Node 18+.

## Run it locally — the whole loop
```sh
cd site
npm install      # first time only → creates node_modules/ (gitignored)
npm run serve    # live preview at http://localhost:8080, hot reload
npm run build    # one-off build into _site/ (gitignored)
```
Day to day you only need `npm run serve`.

## Structure / routes
| URL | Source | Purpose |
|---|---|---|
| `/` | `index.njk` | Landing — hook + "Play on ChatGPT" CTA |
| `/files/<slug>/` | `files/<slug>.md` | The 11 dossier pages — the GPT's link targets |
| `/scenario/` | `scenario.md` | Story background (player-safe, from CANON.md) |
| `/reading-room/` | `reading-room.md` | Research bibliographies |

- Shared layout: `_includes/base.njk` (OG/Twitter meta + footer).
- Dossier layout (all 11): `_includes/dossier.njk`.
- Collection defaults (layout + `/files/<slug>/` permalink): `files/files.11tydata.json`.
- `README.md` is kept out of the build via `.eleventyignore`.

The 11 frozen slugs: `model-citizen` · `power-user` · `self-optimiser` · `machine-companion` ·
`skeptic` · `artist` · `bookworm` · `tinkerer` · `organiser` · `wildcard` · `social-linchpin`.

## Add or edit a dossier page
1. Edit `files/<slug>.md`. Front matter: `archetype`, `slug`, `status` (file tail), `title`,
   `description` (drives the share-unfurl card), optional `ogImage`.
2. **Never rename a published file** — the filename is the URL (and the `LINK` line in
   `archetype-dossiers.txt`).
3. The body is the voiced dossier prose — authored in **Epic 2** from the `archetypes.txt` voice
   samples. Stubs currently hold a TODO placeholder.

## Ship it to GitHub Pages

**URL base (already set):** repo `nathmoore/the-enmeshment`, served as a **project page** →
`https://nathmoore.github.io/the-enmeshment/`. `pathPrefix` is set to `"/the-enmeshment/"` in
[`.eleventy.js`](.eleventy.js) and the `REPLACE_ORG` repo links are filled in. Internal links use
the `| url` filter, so they stay correct under this prefix.

> **Later, when you buy `enmeshed.xyz`:** add it as the Pages custom domain (Settings → Pages →
> Custom domain), flip `pathPrefix` to `"/"`, rebuild, and re-author the 11 `LINK` lines in
> `archetype-dossiers.txt` (single find/replace on the base). GitHub auto-redirects the old
> `github.io` URLs, so already-shared links survive.

**One-time setup:**
1. Repo **Settings → Pages → Build and deployment → Source: GitHub Actions**.
2. **First deploy (manual):** Actions tab → "Deploy site to GitHub Pages" → **Run workflow**
   (it's `workflow_dispatch`/manual for now). Confirm `https://nathmoore.github.io/the-enmeshment/`
   renders.
3. **Make it automatic:** uncomment the `push:` trigger block at the top of
   [`.github/workflows/pages.yml`](../.github/workflows/pages.yml) (it filters to `site/**`).
4. Confirm the 11 `LINK` lines in `src/knowledge/archetype-dossiers.txt` hold the absolute URLs
   (`https://nathmoore.github.io/the-enmeshment/files/<slug>/`) — already authored.

**Routine commands cheat-sheet:**
```sh
cd site && npm run serve                       # local preview
cd site && npm run build                       # build to _site/
cd site && npm update                          # bump deps
gh workflow run "Deploy site to GitHub Pages"  # manual deploy (after Pages enabled)
gh run watch                                   # follow the latest workflow run
```

## Do I need a linter?
**No formatting linter yet** — premature for a site this size. The two real risks are covered
more cheaply:
- **Template breakage** → caught by `npm run build` (it errors and names the file). That *is* your
  check. (CI build-on-PR is optional; you build locally anyway.)
- **Slug / link drift** between the 11 pages and the `LINK` lines in `archetype-dossiers.txt` → add a
  tiny consistency check: the built `_site/files/*/` dirs must match the 11 `LINK` slugs, and every
  `LINK` URL must resolve. That's the failure mode worth guarding, not code style.

Optional niceties if you ever want them: **Prettier** (formatting — but its Nunjucks support is
imperfect), **actionlint** (workflow YAML). Skip **markdownlint**/**eslint** — not worth the noise here.
