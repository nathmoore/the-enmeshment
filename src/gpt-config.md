# GPT deploy config (non-instruction builder fields)

Everything the GPT Builder needs that ISN'T the instructions block. Versioned here
so the cold-start funnel (store listing → starters → cold open) is a repo artefact,
not typed-once-into-the-UI. Instructions live in `instructions.md`; knowledge files
in `knowledge/`. On release, copy these fields into the GPT Builder.

## Name
- **In-app / display name:** The Enmeshment
- **Store listing title:** The Enmeshment: AI Resistance Profile Quiz
  (brand + keyword tail for discovery — store discovery is search + sharing, not
  browsing. Locked 2026-06-13, DECISIONS.md.)

## Description (the single "Description" field — 295/300 chars)
One field, used in both places: it's the store-listing blurb AND what shows at the
top of the GPT's page when someone opens it. So it does double duty — curiosity-gap
primer for a cold arrival, and the "what this is" a player repeats to a friend.
> What kind of problem would you be? In a near future where the state's
> intelligence has grown enmeshed with an AI's, Concord — its cheerful new
> screening agent — needs a quick read on you before your next placement. A
> personality quiz that profiles which way you'd lean if things ever came apart.

Craft notes (why this copy): leads with a provocative self-directed question (the
hook), names the frame in one clause (near-future, enmeshed state, Concord), and
lands on "personality quiz" so a player can explain *what this is* to a friend. The
menace is bureaucratic, not scary — it matches where the dossiers land (warm,
affectionate "which role would you bring"), so store → play → verdict is one
continuous register with no tonal whiplash. "Threat" was considered and dropped from
the headline: it promises menace the game deliberately doesn't pay off (kept only as
in-fiction seasoning Concord can tease, e.g. "your file stays open").

## Conversation starters (the 4 buttons on an empty chat — the true cold open)
1. Hello
2. Let's begin
3. Hi, I'm here to get my OPPPA please?
4. Do I have to be here?

Why this mix: it sets the tone/joke before Concord says a word. (1)/(2) let an eager
player dive straight in; (3) is the in-fiction deadpan (a player playing along with
the bureaucracy); (4) is the wary/joking opener — and Concord reading that reluctance
warmly *is* the first free signal. No "what is this?" button is needed: the store
blurb + Concord's cold-open self-intro already orient a cold arrival, and the EDGE
CASES "declines / distressed" paths cover anyone who needs more.

How-to-respond guidance is deliberately NOT added to instructions.md: the cold open +
these starters make the natural mode (answer cheerfully, in conversation) self-evident.
