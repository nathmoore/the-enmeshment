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

Underneath, it's a thought exercise about one potential near-future risk — chosen because
it's specific and unglamorous, not because it's the most likely. Not that AI turns hostile,
but that an over-dependence on AI could produce a quiet **misalignment** between what a
system optimises for and what the institution using it actually intends, and a drift toward
profiling that is cheap, ambient and administratively unremarkable.

We publish the whole method, including the elicitation playbook, because the techniques
are already public, already credible, and already available to anyone who wants them. What
isn't widely distributed is the *experience* of noticing one being used on you. That gap is
the thing a game can actually close.

## Two easy positions, both declined

The project sits between two comfortable readings and takes neither.

**Under-weighting the dependence.** One easy position is that AI in public administration is
mostly hype — vapourware, a procurement cycle, something that will wash out. The adoption
[literature](WORLD-RESEARCH.md) suggests some caution here. Decision-support tooling tends
to get adopted because it is genuinely useful and cheap, and usefulness is a more reliable
adoption mechanism than mandate. Where that happens, reliance can accumulate through a long
series of individually sensible choices rather than one deliberate one. That's a governance
question about review and recourse keeping pace with throughput — not a verdict on the
technology, which in most of these deployments is doing exactly what it says on the tin.

**Over-weighting the catastrophe.** The opposite easy position is the doom register:
superintelligence, hostile takeover, the apocalypse setpiece. It makes for weaker fiction
and, we'd argue, weaker thinking — it points attention at a dramatic discontinuity and away
from the mundane, tractable questions that are actually live now.
[Pillar 4](GAME-DESIGN.md) is *no doom, no utopia* for exactly this reason.

What sits between them is **drift**, which is what the fiction dramatises. In the game's
2038, nobody seizes anything: review windows have quietly shrunk below the time it takes to
read what's being approved, sign-off survives as ceremony, and the system has become
load-bearing before anyone got round to making it accountable. That is a deliberately
pointed version of a real and well-recognised design problem — how meaningful human review
is preserved as volume and automation rise — rendered as fiction. It is not a description
of any existing institution, and it isn't meant as one.

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

A BuzzFeed quiz does not inoculate a society against anything. We're not going to pretend
otherwise, and any framing of this project that implies it should be read as overreach.

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
fast an institution comes to rely on something it never formally adopted. That question is
**structural** — it follows the tooling more than the ideology. An authoritarian system has
fewer brakes on it. A democratic one has procedural friction, institutional review, freedom
of information and the standing possibility of being told no — safeguards that do real work,
and that are worth understanding precisely so they can be maintained as the tooling gets
cheaper. The game is more useful to both if it doesn't hand either an excuse.

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
