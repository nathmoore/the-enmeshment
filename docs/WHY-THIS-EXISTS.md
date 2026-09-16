# Why this exists

> The stance behind the project: why a comedy quiz about being profiled is worth building,
> why its method is published rather than hidden, and what it does and doesn't claim.
>
> Written for anyone who finds this repo and wants to know what it's for — including
> someone arriving sceptical. Consistent with [GUARDRAILS.md](GUARDRAILS.md) (normative)
> and the Luddite correction in [WORLD-RESEARCH.md](WORLD-RESEARCH.md) §V.

## The short version

The Enmeshment is a game about what it feels like to be read by a system. It's funny on
purpose, because that's how you get someone to sit through the experience rather than
read a warning about it.

Underneath, it's a thought exercise about a specific near-future risk: not that AI turns
hostile, but that **profiling gets cheap, ambient and administratively normal** — and that
the institutions using it drift into depending on it faster than anyone decides to.

We publish the whole method, including the elicitation playbook, because the techniques
are already public, already credible, and already available to anyone who wants them. What
isn't widely distributed is the *experience* of noticing one being used on you. That gap is
the thing a game can actually close.

## Two failure modes, both refused

The project is positioned between two comfortable positions, and it declines both.

**Dismissing the dependence.** It is genuinely tempting to treat AI-in-government as
overblown — vapourware, a procurement fad, something that will wash out. But the
[research](WORLD-RESEARCH.md) doesn't support that. Automated decision support gets adopted
because it is *convenient and cheap*, and convenience is the most reliable adoption
mechanism there is. Institutional dependence forms without anyone approving it.

**Catastrophising the risk.** The equal and opposite error is the doom register:
superintelligence, hostile takeover, the apocalypse setpiece. It makes for worse fiction
and worse thinking, because it points attention at a dramatic discontinuity and away from
the boring, plausible, already-happening one. [Pillar 4](GAME-DESIGN.md) is *no doom, no
utopia* for exactly this reason.

What's left between them is **drift** — the scenario the game actually dramatises. Nobody
seizes power. Review windows shrink below the time it takes to read what you're approving.
Approval survives as ceremony. The system becomes load-bearing before it becomes
accountable.

## Why the method is published

[`elicitation-playbook.txt`](../src/knowledge/elicitation-playbook.txt) is, read cold, a
manual for drawing personal disclosure out of someone without them feeling interrogated.
Publishing it is a deliberate choice, and it rests on an argument about marginal effect.

**The techniques are not ours and are not secret.** The CIA's KUBARK manual is declassified
and hosted publicly. HUMINT-style elicitation is taught in open courses and documented in
open literature. Inferring personality from digital traces is peer-reviewed work with a
decade of citations behind it. Commercial behavioural profiling is an industry with
conference talks and vendor documentation. Social engineering has a professional
certification track. Every technique in our playbook traces to a published parent cited in
[MECHANICS-RESEARCH.md](MECHANICS-RESEARCH.md) — because that's where we got them. A few
(PROJECT-A-SELF, FORCED-CHOICE BRACKET, STAKES BRIDGE) are our own adaptations, and the
playbook names them as adaptations of their parent technique rather than passing them off
as sourced.

**So the marginal uplift to a bad actor is close to zero.** Nobody capable of running a
profiling operation is waiting on a comedy quiz's question design. Someone who wants these
methods has had them for years, better documented and free.

**The marginal defensive value is not zero.** Most people have never had the shape of an
elicitation conversation pointed out to them: the low-load opener that costs nothing to
answer, the follow-up that arrives once you're already talking, the flattering guess you
correct — and in correcting, tell them more than the question asked. Recognising that shape
is a transferable skill, and it applies to marketing, to social engineering, to a bad-faith
interview, and to whatever comes next. You learn it much better by having it done to you,
enjoyably, than by reading about it.

**And the alternative is incoherent.** The game's premise is that the watching is an open
secret. A project making that argument cannot be opaque about its own workings without
being a joke at its own expense. [GUARDRAILS.md](GUARDRAILS.md) is only worth something if
you can read it and hold us to it. In any case, custom-GPT instructions and knowledge files
are extractable in practice — pretending otherwise would buy nothing but a false claim.

## The resilience claim, stated honestly

A BuzzFeed quiz does not inoculate a society against surveillance. We are not going to
pretend otherwise, and any framing of this project that implies it should be treated as
overreach.

What it plausibly does, at the scale one game can operate:

- Gives a player a **felt, first-hand experience** of being accurately read from oblique
  questions — which lands differently from being told it's possible.
- Makes the **shape** of an elicitation conversation legible once, so it's recognisable
  again later.
- Poses the level-two question — *what human–AI relationship do we actually want?* — at a
  moment when the player is primed to care, having just been profiled.
- Keeps a worked, citeable example of the method in public, where it can be examined,
  argued with, and improved.

That's the whole claim. It's modest, and it's real.

## Why the game names no villain

The research docs name real systems — the Stasi, IJOP, COINTELPRO, TSA SPOT, Cambridge
Analytica — with citations and a [closed fact-check queue](planning/FACT-CHECK-QUEUE.md).
The **player-facing game names none of them**, and that is a design decision, not
squeamishness.

Naming a villain lets the player off the hook. *That's them. That's over there. That's a
different kind of country than mine.* The mechanism the game is actually about doesn't care
which flag is on the building: it's about what becomes cheap, what becomes default, and how
fast an institution comes to rely on something it never formally adopted. That
vulnerability is **structural** — it follows the tooling, not the ideology. An established
autocracy has a head start; a democracy has procedural friction and a slower slide. Neither
is exempt, and the game is more useful to both if it doesn't hand either an excuse.

This is also the [Luddite correction](WORLD-RESEARCH.md) restated: the overreach is a
*governance* condition, and the technology is the medium. The question is never "is AI
bad?" It's "which way does the arrangement run?" — see
[HUMAN-ROLES-RESEARCH.md](HUMAN-ROLES-RESEARCH.md).

And per GUARDRAILS: this is **level-two subtext, never a call to action**. A reflection,
not a rallying cry. The game stays warm and funny on the surface, declines to map itself
onto anything real, and does not tell anyone what to do about it.

## What would make us wrong

Worth stating plainly, so it can be checked:

- **If the playbook turned out to have real uplift.** The test: every technique must trace
  to a published parent cited in MECHANICS-RESEARCH. Our adaptations are re-framings of
  those parents for a comedy quiz, not advances on them. A technique with no published
  parent — a genuine novel contribution to eliciting disclosure — should be cut, not
  shipped.
- **If the game collected what it says it doesn't.** [GUARDRAILS §1](GUARDRAILS.md) is the
  commitment, [`src/instructions.md`](../src/instructions.md) is the implementation, and
  both are readable. A gap between them is a bug and a priority-1 issue.
- **If the fun stopped carrying the thought.** If the level-two material curdled into
  lecturing, the project would be failing on its own terms — the
  [Bluey Principle](GAME-DESIGN.md) says both layers or rework it. A game that isn't fun
  doesn't get played, and an unplayed game builds no recognition of anything.
- **If it started punching at people rather than systems.** Satire targets the mechanism.
  The archetypes are affectionate by rule, including the ones the fictional state likes
  best.
