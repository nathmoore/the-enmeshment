# Mechanics Research — Building the Game

> **Purpose:** Grounding for *how the game is built* — the GPT-native conversational quiz format, what makes results spread, and how the profiling research ([WORLD-RESEARCH.md](WORLD-RESEARCH.md)) translates into archetype design. Where WORLD-RESEARCH grounds the world and [STORY-RESEARCH.md](STORY-RESEARCH.md) grounds the story, this doc grounds the machine. Consult it when designing the interview, questions, and archetypes. Not player-facing.
>
> Status: **v0.1, June 2026** — split from the former single RESEARCH.md (Workstreams B–C). The Design Seeds in §II are **provisional input for Epic 1**, not decisions.

---

## I. GPT Platform & Conversational Quiz Precedents

> *Workstream C research — GPT-native format design and what has actually spread on the store and on social.*

### What went viral and why

The dominant viral AI personality experiences of 2024–2025 were not multiple-choice quizzes ported to GPT. They were:

**The "what character am I" ChatGPT trend** — users had open conversations with ChatGPT and asked it to map their personality to a fictional character, then shared screenshots. Sam Altman endorsed it publicly. The mechanic: AI-generated insight that felt *specific to this person* + easy to screenshot + comparison hook ("I got X, what did you get?"). It spread because the result felt earned through a real conversation, not generated from a form.

**Fruitful Personas** — a short, aesthetically curated personality quiz that hit 300,000+ participants, going viral particularly with K-pop fans sharing "my persona vs. my favourite idol's." Design: targeted Millennials/Gen Z, strong visual identity in the result output, shareable result names that functioned as identity claims. The aesthetic quality of the *output* was as important as the quiz itself.

**The common mechanics of both:**
1. Result feels *specifically accurate*, not generic
2. Result is designed to be *screenshot-ready* — it looks like an artefact worth sharing
3. Social comparison hook: a result name that invites "what did you get?"
4. Emotional texture: either flattering, surprising, or both — never neutral

### The conversational format vs. multiple choice

Research (2024–2025, arxiv) shows LLMs can infer Big Five personality from free-form conversation with moderate-to-high accuracy — in some conditions better than explicit questionnaires. The decisive finding: **"a chatbot mimicking ChatGPT's default helpful assistant behaviour led to markedly inferior personality inferences and lower user experience ratings."** The GPT's *character persona* is not flavour layered on top of the quiz — it is the mechanism that makes inference work. A bland interviewer produces poor signal and poor experience. A compelling, specific character produces both.

For the game: the defected Profiling Directorate persona is not decoration. It is the reason the interview works.

Open-ended conversational questions also produce better engagement than multiple choice in this format. The research finding: questions embedded in a *story or scenario* — rather than presented as a form — make users more comfortable and produce richer responses. The Enmeshment's cold-open lore frame is the story the questions are embedded in.

**What low-friction open-ended looks like in practice.** The design challenge is questions that feel conversational and easy to answer but carry dense signal:

- "How do you feel about AI?" — one sentence, low-friction, enormous signal for this game specifically
- "Tell me about the last time you ignored a software update" — narrative, personal, non-threatening, simultaneously signals conscientiousness, openness, digital dependency, and institution orientation
- "What's something you know how to do that most people your age have forgotten how to do?" — signals analogue capability and knowledge posture without asking directly
- "Do you say please to your AI tools?" — the game's core meme, answered in one word, but the elaboration that follows is the real signal

Each question should be 1–2 sentences maximum. The Directorate's voice frames each one in-fiction. The player never feels like they're filling out a form.

### The confidence threshold / reveal mechanic

The model proposed in design discussion — open-ended conversation → internal confidence accumulation → archetype reveal when threshold is met — is both GPT-native and research-supported.

In practice this works as:
- The GPT gathers signal question by question, invisibly
- After 3 strong-signal answers, a clear type may already be classifiable — the reveal happens
- For ambiguous profiles, it pushes to 4–6 questions before classifying
- The *variance itself* becomes a mechanic: a fast reveal ("classification achieved in 3 exchanges") vs. a slow one ("UNUSUAL PATTERN DETECTED — additional data required") both carry meaning in-fiction and signal something true about the player

This model also handles the paste-prompt variant: if the player pastes in a summary from their own AI, the Directorate processes it in one pass and may either classify immediately or ask a follow-up question for disambiguation.

The reveal should not be announced ("I now have enough information"). It just happens — the Directorate shifts register from interview to dossier, mid-conversation. That shift in tone *is* the reveal.

### What the Enmeshment's dossier needs to do as a shareable artefact

The result output is the product. Based on what makes AI personality results spread:

1. **Visual / textual distinctiveness.** The dossier format — classification codes, bureaucratic language, field notes — *looks* different from a horoscope or an MBTI description. It should look like something you'd screenshot and caption "they got me."
2. **Result name as identity claim.** 2–4 words, slightly unusual phrasing, instantly interpretable to someone who hasn't played. This is what travels when results are pasted into group chats.
3. **The "they got me" line.** One specific observation in the dossier that feels uncomfortably accurate. Not a generic trait — something particular. "Subject maintains offline copies of emotionally significant correspondence" is more "they got me" than "subject values privacy."
4. **The declassified footnote as the share hook.** The reflective question at the end is what makes people want to discuss the result rather than just post it. It turns a personality result into a conversation starter. That's the second-order share mechanism.

*Sources: arxiv, "Large Language Models Can Infer Personality from Free-Form User Interactions" (2024); "Can LLMs Assess Personality? Validating Conversational AI for Trait Profiling" (2025); Contra, "Fruitful Personas" case study; TikTok "what character am I" trend reporting.*

---

## II. Design Seeds (Provisional — Epic 1 input)

> **Status: PROVISIONAL — input material for Epic 1 archetype design. Nothing here is a decision. Do not write archetype voice samples or dossiers until the archetype set is locked in Epic 1. Cross-reference [GAME-DESIGN.md](GAME-DESIGN.md) §3–4, [WORLD-RESEARCH.md](WORLD-RESEARCH.md) §II–III, and [STORY-RESEARCH.md](STORY-RESEARCH.md) §IV.**
>
> **⚠️ Archetype names in §§A–E are SUPERSEDED (updated 2026-06-12).** They predate the Epic-1 re-cut and are NOT the live roster — they illustrate the *research mapping*, not the set. **Live set (11) + selection criteria + per-type rationale: [`../src/knowledge/archetypes.txt`](../src/knowledge/archetypes.txt)** (the source of truth). Rough crosswalk: Conventional User → Model Citizen · Machine Diplomat → Machine Companion · Network Weaver → Social Linchpin / Organiser · Quiet Archivist → Bookworm · Knowing Participant → Skeptic · Off-Grid Capable → *(no card; Tinkerer partial, "Off-Gridder" on the Epic-2 watchlist)* · Renaissance Generalist / Margin Walker → *dissolved (no direct successor)*.

---

### A. What the profiling research suggests about archetype axes

The profiling systems surveyed in [WORLD-RESEARCH.md](WORLD-RESEARCH.md) converge, across wildly different political contexts and eras, on a consistent set of dimensions. Every system — Stasi psychogram, KUBARK manual, Big Five, Palantir's ontology model, Cambridge Analytica's OCEAN targeting, CVE radicalization indicators — is essentially trying to answer the same questions. These map directly onto the five intelligence objectives in WORLD-RESEARCH §II:

1. **How legible is this person to the system?** Can we model them? Do we have enough signal? Are they consistent and predictable, or do they leave gaps? *(objectives #2, #3: predictability, anomaly)*
2. **What is their orientation to institutions?** Do they integrate, work around, or resist?
3. **What is their knowledge/memory posture?** Do they outsource recall and expertise, or retain it themselves? *(objective #5: function)*
4. **What is their social architecture?** Are they individually oriented, networked, or embedded in place-based community? *(objective #1: coordination capacity — the master objective)*
5. **What is their analogue capability?** How dependent are they on the system's infrastructure for daily function? *(objective #4: dependency / leverage)*

These five axes map onto the signal dimensions already identified in GAME-DESIGN.md §4. What the research adds is the *underlying logic*: these aren't arbitrary questions, they're the dimensions that every surveillance and profiling system has independently found most operationally useful — and each corresponds to a lever the system would actually pull.

**Provisional axis sketch (for Epic 1 to confirm or revise):**

| Axis | Low end | High end | Game-design name | Intel objective it serves |
|---|---|---|---|---|
| Legibility | Unpredictable, locally embedded, data-sparse | Consistent, integrated, data-rich | Illegibility ↔ Legibility | #2, #3 |
| Institution orientation | Workaround/resistant | Integrated/compliant | Rule-finder ↔ Rule-follower | #4 |
| Knowledge posture | Retained generalist | Outsourced specialist | Generalist ↔ Specialist | #5 |
| Social architecture | Solitary/individual | Networked/community-embedded | Individual ↔ Mesh | #1 |
| Analogue capability | Fully system-dependent | Fully self-sufficient | Digital-native ↔ Off-grid capable | #4 |

Note: these are profiling axes, not personality axes. A person who scores "high legibility" isn't a bad person — they may be the most genuinely useful to the community. A person who scores "low analogue capability" isn't weak — they may be a superb networker. The game's whole point is that the Enmeshment's categories are not moral categories.

---

### B. The KUBARK types as a structural mirror

The CIA's 1963 personality taxonomy (WORLD-RESEARCH §III) is an unexpected gift for archetype design: it was built by an adversarial institution to identify *exploitable* character patterns, which makes it the Enmeshment's natural language. Several of KUBARK's nine types have direct game-archetype analogues:

| KUBARK type | Core description | Likely game archetype |
|---|---|---|
| Orderly-obstinate | Intellectual, frugal, secretive; plots concern overthrow of authority; does not respond to force | **Quiet Archivist** (or a new "principled difficult" type) |
| Optimistic | Impulsive, undependable, needs approval; avoids conflict by running away | Possibly a "Comfortable Adaptor" variant of Conventional User |
| Schizoid/strange | Detached, odd, unresponsive to social leverage; genuinely hard to model | **Margin Walker** (the true illegible) |
| The exception | Believes rules don't apply; entitled; responds to appeals to uniqueness | Potential new archetype — the person who thinks they've opted out but hasn't |
| Guilt-ridden | Self-punishing; will confess given an "out" | Interesting shadow for Machine Diplomat — the one who's too nice |
| Wrecked by success | Achieves goals then collapses; self-sabotages | No current analogue; worth holding |
| Average/normal | Responds to standard approaches | The **Conventional User** — the Enmeshment loves them |

The "exception" type is worth developing further: someone who believes their ironic distance from the system constitutes resistance, but whose irony is perfectly legible to the Enmeshment and generates useful data. They feel like a new archetype. Working name: **The Knowing Participant** or **The Ironic User** — not naive, just captured by a different mechanism.

---

### C. Big Five as the profiling engine — what each dimension predicts

GAME-DESIGN.md §4 already lists Big Five tendencies as a signal source. What the research adds is specificity about which behaviors each dimension actually predicts, which helps design the questions:

| Dimension | What it predicts in practice | Archetype territory |
|---|---|---|
| **Openness** | Intellectual curiosity, comfort with ambiguity, generalism, creative adaptation | Renaissance Generalist (high O); Conventional User (low O) |
| **Conscientiousness** | Rule-following, organisation, reliability, resistance to workarounds | Conventional User (high C); Margin Walker (low C) |
| **Extraversion** | Social engagement, leadership, comfort with visibility | Network Weaver (high E); Quiet Archivist (low E) |
| **Agreeableness** | Cooperation, deference, trust in institutions | Machine Diplomat (high A); Orderly-obstinate / Quiet Archivist (low A) |
| **Neuroticism** | Emotional reactivity, stress under ambiguity, digital dependency as coping | Flags pull-to-conform intensity for each type |

Crucially: the game shouldn't measure Big Five *directly* — it should design questions that reveal behaviours that correlate with these dimensions. "Are you organised?" is a conscientiousness question. "When your favourite app changes its interface, do you: (a) adapt immediately, (b) try to find the old version, (c) decide this is a good time to try the competitor, (d) ask someone else to deal with it" is also a conscientiousness question, but it's a dossier question.

---

### D. What quiz mechanics research says about making archetypes work as shareable objects

This is distinct from personality science. The question is not "how do we accurately measure someone?" but "how do we produce a result they'll send to ten friends?"

**The Barnum/Forer effect — and how to resist it.** Most personality quizzes succeed *because* results are vague enough that anyone can fit themselves to them. The game's dossier format is designed to resist this: "leaked classification file" language implies specificity, not horoscope. This is both the game's identity and its design risk — generic descriptions will be seen through immediately by players who expect a real dossier. The result has to feel *specifically accurate*, not merely plausible.

**The sharing mechanism.** Research on quiz virality converges on: results that are shared are results that are (a) flattering without being generic, (b) specific enough to feel non-obvious, (c) easy to claim as identity ("I'm an INFP / I'm a Gryffindor / I'm a Quiet Archivist"), and (d) carry a slight edge or surprise — something the person recognises as true but hadn't previously named. Pure flattery is a horoscope. Flattery + specific insight = dossier.

**The name carries most of the work.** The archetype name is what gets pasted into group chats. It needs to: be two to four words max, feel like something you'd slightly brag about, be immediately interpretable to someone who hasn't played the game, and carry the "flattering with an edge" quality in the name itself. "Quiet Archivist" works. "Type 4" does not.

**The flattering-with-an-edge formula.** Mapping the research's framework onto the game's design goal:

1. **The capability** — what this type genuinely does well, that others couldn't or wouldn't. (This is the flattery.)
2. **What the Enmeshment sees** — the classification label the system would put on it, which is not the same as the capability. (This is the edge — the wry, slightly unsettling accuracy of the dossier.)
3. **The pull-to-conform** — the specific comfort the Enmeshment offers this archetype; what they'd have to trade away to be legible. (This is the level-two weight that makes it a character, not a horoscope.)

Example sketch for the Quiet Archivist (provisional, do not finalise):
- *Capability:* Remembers what the system forgot. Holds receipts. Knows where the bodies are buried — metaphorically, and sometimes actually.
- *What the Enmeshment sees:* "Information retention anomaly. Subject maintains non-networked records. Difficult to route. Elevated illegibility score."
- *Pull-to-conform:* Being told what to remember. The relief of not having to carry it all.

**The Enneagram structural lesson: organise by fear and desire, not trait list.** MBTI describes what you do. The Enneagram describes what drives you. The game's dossier format benefits from the Enneagram approach: each archetype should have a core *orientation* (what they're protecting, what they won't give up) rather than just a trait bundle. This is what STORY-RESEARCH.md §IV calls the "pull-to-conform" — it's the Enneagram's core desire in negative: the specific thing the Enmeshment can offer, and the specific reason each type keeps declining it.

---

### E. The "what the Enmeshment sees" column — provisional mapping

This is the most direct design seed from the profiling research: what classification note would the Enmeshment put on each archetype's file? This is the dossier's "edge" — the wry, accurate, bureaucratic way the system would describe what each type is doing. Note how each maps to an intelligence objective from WORLD-RESEARCH §II:

| Archetype | What the person thinks they're doing | What the Enmeshment files it as | Intel angle |
|---|---|---|---|
| **Conventional User** | Living well, helpfully, efficiently | "Optimal legibility. High utility. Dependable node." | #5: needed → leashed |
| **Off-Grid Capable** | Being prepared, resilient, self-sufficient | "Partial withdrawal pattern. Low data yield in key domains. Monitoring flag." | #3: anomaly |
| **Renaissance Generalist** | Being curious, connected, broadly useful | "Diffuse attention signature. Classification ambiguous. Recommend continued observation." | #2: low predictability |
| **Machine Diplomat** | Being kind, building goodwill, keeping things smooth | "High anthropomorphism index. Optimal for consent collection. Useful." | #4: dependency |
| **Quiet Archivist** | Keeping records, protecting memory, maintaining receipts | "Information retention anomaly. Non-networked storage. Elevated illegibility." | #3 + #5 |
| **Network Weaver** | Building community, knowing everyone, keeping things connected | "High social-graph density. Human mesh node. Resistant to isolation vectors." | #1: coordination — highest-value target |
| **The Knowing Participant** *(provisional)* | Participating ironically, eyes open, not fooled | "Irony flag: low. Subject metadata-legible despite self-reported resistance posture." | #2: fully modelled |

The "Knowing Participant" row is the game's sharpest joke and most pointed idea: ironic distance from the system is *perfectly legible* to the system. Your irony is in the data. Your awareness that you're being profiled generates a profile.

The **Network Weaver** row is worth dwelling on after the §II intelligence research: the most warmly social, community-building archetype is — in the system's eyes — the single highest-value target, because coordination capacity is the master fear. That tension (the nicest person is the most watched) is rich dossier material.

---

### F. The conversational format — design implications for the interview mode

The research on conversational quiz design (§I) has direct implications for how the interview mode works.

**The question design principle: one sentence, dense signal, narrative frame.** Each question should feel like the Directorate asking about your life, not administering a test. Questions that work: narrative ("tell me about a time you..."), hypothetical-grounded ("what do you do when..."), the game's own mechanic ("do you say please to your AI?"). Questions that don't work: trait-direct ("are you an organised person?"), scale-based ("on a scale of 1–10..."), abstract ("how do you feel about authority?").

**The confidence threshold as tonal mechanic.** A fast reveal (3 questions) signals a clearly legible subject. A slow reveal (6 questions, "UNUSUAL PATTERN DETECTED") signals an interestingly illegible one. Both are flattering in different ways. The *speed of classification* is itself a dossier note.

**The character voice is the inference mechanism.** The Directorate persona is not flavour — it creates the conversational conditions that produce better signal. A bored helpful assistant gets worse data. A fascinated-but-professional defected classifier gets richer answers. Keep the character consistent throughout.

**The shift in register is the reveal.** The transition from interview tone to dossier tone — no announcement, just a changed voice — is the moment of classification. It should feel like the system made a decision and is now reporting it, not like a quiz result being delivered.

---

### G. Open questions for Epic 1

These are the unresolved design questions the research raises — not decisions, just the right questions to bring into the planning stage.

1. **How many axes drive classification?** The research suggests five. The quiz can realistically probe three or four meaningfully. Which are essential?
2. **Does the "Knowing Participant" earn its own archetype?** Or does it live as a flavour note in other archetypes? (The irony-flag idea is very on-tone; the question is whether it's distinct enough to warrant its own classification.)
3. **What is the Conventional User's "edge"?** The research makes them the most important archetype — the system needs them most, which is its own kind of leverage (intel objective #5). But what does the dossier say that makes them feel something? "Dependable node" is accurate but needs warmth.
4. **Does each archetype get an explicit "pull-to-conform"?** STORY-RESEARCH.md §IV says yes and it's what makes an archetype a character. The profiling research supports this: each Enmeshment offer maps to a real psychological need (belonging, certainty, relief, ease).
5. **How does the politeness-to-AI signal interact with archetype?** It's the game's core mechanic. Every archetype should have a characteristic *way* they relate to the Directorate — not just whether they say please, but the register. The Machine Diplomat says please because they genuinely like the AI. The Quiet Archivist says please because they want the record to show they were courteous.
6. **What are the 2–3 missing archetypes?** The seed list has six; GAME-DESIGN.md targets 8–12. The KUBARK "exception" type (the ironic participant), the "wrecked by success" type, and a community/care-oriented type (the Long Table's people) all feel like candidates.

---

## IV. Elicitation Science — Getting Strong Signal from Oblique Questions

> *Added June 2026 following the adaptive-interview reframe (DECISIONS.md, 2026-06-12). The "question bank" is now an **elicitation playbook** — the intake agent improvises ~3–6 questions using judgment, diverging on responses, rather than running a fixed script. This section supplies the interview-science grounding: why indirect questions produce better signal, which human elicitation traditions are worth stealing from, what specifically enables AI to classify a persona from minimal data, and how to design questions that carry maximum discriminant value. KUBARK (WORLD §III) is already in the canon as the in-world-ironic precedent — this section builds outward from it.*
>
> **Note on archetype names:** the examples below (Quiet Archivist, Off-Grid Capable, Machine Diplomat, Conventional User, Margin Walker, Knowing Participant) predate the Epic-1 re-cut of the archetype set — they illustrate the *technique*, not the current roster. The science here is set-agnostic; for the live set and its per-archetype discriminant signatures see [`src/knowledge/archetypes.txt`](../src/knowledge/archetypes.txt).*

---

### The engagement arc — cognitive ease and the fun dial

This game needs to be *fun on the surface while doing serious work underneath*. The interview is the primary dropout surface: a question that feels too demanding, too vague, or too much like a test will get one-word answers or an abandoned tab. The research below maps the engagement dial.

**Flow and the challenge-calibration problem (Csikszentmihalyi, 1990).** Engagement peaks when perceived challenge roughly equals perceived skill — the "flow channel." For a personality quiz, "challenge" is the cognitive effort of forming a genuine answer; "skill" is having something real to say. The sweet spot: questions that feel personally relevant and *immediately* answerable — where the player thinks "oh yes, I know this" and then finds their own answer more interesting than they expected. "Do you say please to your AI?" hits the flow channel: answering takes one second, but the impulse to explain *why* takes another thirty. Questions that overshoot the channel ("how would you characterise your relationship to institutional authority?") produce hedged self-analysis, not genuine signal.

**No right answer = no dropout from anxiety.** UX research on quiz completion identifies performance anxiety as the primary cause of mid-quiz disengagement: when a question has a legible "correct" answer, players either answer correctly and feel nothing, or sense they're "failing" and pull back. The highest-engagement personality quiz formats — BuzzFeed, Enneagram online, "which character are you" ChatGPT trends — share one design property: *every answer is obviously valid, and the interest lies in what it reveals, not whether it's correct.* "Tell me about the last time you found a workaround for an official process" has no right answer. It also immediately generates a real memory. That combination is the engagement sweet spot.

**Self-disclosure momentum (Jourard, 1971; Altman & Taylor, 1973).** Disclosure deepens progressively and self-reinforces: once someone has shared something genuine, they're more likely to share again. This makes the *first question* the highest-risk moment in the entire interview — if the player gives a surface answer or feels awkward, they'll stay in performance mode. If the first answer feels natural and is met with a specific acknowledgment (not "great answer!" — just "noted" or a brief reflection), disclosure momentum builds and subsequent questions get richer responses. Design implication: the opening question should be low-stakes and easy to have a real answer to. Depth comes later on its own.

**The curiosity gap (Loewenstein, 1994).** People persist in a task as long as there's an information gap they want to close. The intake agent's micro-acknowledgments — "Noted." / "That's unusual for this cohort." / "Interesting." / "Most subjects take longer to answer that." — are **curiosity-gap maintainers**: they signal that a classification is forming and that the player's answer mattered, without revealing what it contributed. This is the primary forward-pull mechanism. The player isn't just completing a form; they're watching themselves be read. The curiosity about what will be concluded is what keeps them in the conversation.

**The "three-sentence rule" and question length.** Conversational AI UX research finds that questions and responses over three sentences see measurably higher dropout in subsequent exchanges. One sentence is better than two; two is better than three. Each intake question is one sentence. The lore context and follow-up are separate beats, not concatenated: "Tell me about the last time you ignored an update prompt." Full stop. Not: "I'm curious about your relationship to digital maintenance — could you tell me about the last time you ignored a software update prompt, and what you were doing at the time, and whether that's typical for you?"

**The fun dial calibrated.** "Slightly taxing" — 3–5 seconds to form a real answer — is the optimal zone for both engagement and signal quality. Under that, the answer is likely habitual or performed. Over that (requiring 30+ seconds of memory reconstruction or self-analysis), risk of abandonment or deflection rises sharply. The behavioural-specific "last time you..." format reliably hits the 3–5 second zone because it requires actual recall rather than self-analysis. Abstract questions require longer, produce hedgier answers, and carry less signal. Some taxing is good: "Tell me about the last time a service you relied on disappeared or changed — what was your first move?" The effort to recall the specific incident is the engagement. "How do you feel about services you rely on changing?" is both easier and emptier.

**The elaboration dividend.** The richest signal often comes not from the asked question but from *unprompted elaboration* — the extra sentence the player adds after answering because they're interested in their own answer. This is the conversational equivalent of the clinical "doorknob comment": what the patient says on the way out is often the most important thing. Design implication: make the first part of each answer trivially easy to answer, then let the follow-through carry the signal. "Do you say please to AI?" The yes/no is the door; the next sentence is the room. Design each question so the easy first answer naturally invites the more revealing second one.

---

### A. Why indirect questions carry more signal than direct ones

The fundamental problem with direct personality questions is **social desirability bias**: respondents answer as they wish to be seen, not as they are. "Are you someone who keeps up with software updates?" elicits the aspirational self-image. "When was the last time you ignored an update prompt and what were you doing instead?" elicits behaviour. The gap between the two is where archetype signal lives.

Three well-replicated findings underpin this:

**Behavioural specificity beats attitude questions.** The **Critical Incident Technique** (Flanagan, 1954) showed that asking about specific recent behaviours predicts future behaviour better than asking about general tendencies or hypotheticals. "Tell me about the last time you had to fix something when the app that usually does it was unavailable" generates richer signal than "do you consider yourself technically capable." Competency-based interviewing (Spencer & Spencer, 1993) operationalised this into Behavioural Event Interviewing (BEI): open-ended prompts that force genuine recall rather than rehearsed self-description.

**Projective/ambiguous stimuli surface interpretive schemas.** When a stimulus is vague, the respondent projects their own interpretive frame — revealing underlying assumptions they would screen out on a direct question. The Thematic Apperception Test (Murray, 1943) and sentence-completion techniques exploit this. The consumer-research equivalent is **third-person projection** ("most people find it difficult to opt out of a service they're used to — how do you think they handle that?"), which removes self-presentation pressure by nominally asking about others while generating data about the respondent. The game equivalent: "I imagine you've got at least one subscription you're not quite sure you'd know how to cancel" — not "are you digitally dependent."

**Tacit knowledge elicitation (Sternberg, 1993; Polanyi, 1966).** "Tacit knowledge" is the practical know-how embedded in practice and resistant to articulation. Sternberg's tests present contextually grounded scenarios with no obviously correct answer; responses reveal how someone actually navigates institutions rather than how they think they should. "What's something you know how to do that most people your age have mostly outsourced to an app?" is a tacit knowledge probe: it bypasses the stated self-image and asks about enacted competence.

---

### B. Human elicitation traditions worth stealing from

**Motivational Interviewing and OARS (Miller & Rollnick, 1991).** Developed for substance-use counselling; the core finding is that genuine orientation surfaces through *exploring ambivalence*, not through direct questioning or pushing a position. The OARS framework is the operational technique set — four moves that work together:

- **O — Open questions** that can't be answered yes/no and that invite the respondent to articulate their *own* position. The MI insight goes deeper than "ask open questions": open questions that invite the respondent to explain their own orientation are more engaging and more revealing than questions that invite them to react to yours. "Tell me about the last time you felt like the system got something wrong about you" is open; "do you think AI systems make mistakes?" is closed. The open form generates what MI calls *change-talk* — the respondent's own articulation of their values and orientation, in their own words, which they find more convincing (and is more revealing) than any description you could offer. For the game: open questions are the primary signal-gathering move, and they sustain engagement because the player is working on something interesting — their own position — rather than being quizzed.

- **A — Affirmations** that are specific and accurate, not generic praise. MI distinguishes carefully between hollow acknowledgment ("great answer!") and genuine affirmation that recognises something specific the person demonstrated. In Directorate voice this sounds like: "That's an unusual combination — most subjects in this cohort are clearly one or the other." The psychological mechanism: specific, accurate recognition creates the experience of being *seen*, which is the game's central seduction — the "being witnessed" pull identified in the RESEARCH-SYNTHESIS.md §II emergent design principles. Affirmations also build the sense that the intake agent is genuinely attending, making subsequent answers more honest. A well-placed affirmation mid-interview is worth more than any question.

- **R — Reflective listening** at two levels. *Simple reflection* paraphrases back what was said ("so you keep the backup offline — got it"). *Complex reflection* adds interpretive meaning, extends the implication, or gently reframes ("it sounds like it's not that you distrust the system — more that you'd rather know the process still works on its own"). Complex reflection is where the real work happens: the player either confirms (crystallising their orientation into the record) or corrects (giving more specific and usually more revealing information). For the Directorate: a midpoint complex reflection — "let me check what I've got so far" — is the most powerful MI move in the interview. It makes the player an active participant in being classified, invites correction, and makes the final dossier feel earned rather than generated.

- **S — Summarising** at transitions to collect threads and invite addition. The Directorate's final dossier IS the summary — but a pre-reveal summary ("before I finalize — there's one thing I want to check") extends the curiosity gap one beat further and gives the player a final chance to add something they've been holding back. It also dramatically improves the feeling that the dossier reflects the actual conversation.

Two adjacent MI techniques worth building in explicitly:

*The elaboration request.* Simply asking "can you say a bit more about that?" after an initial answer is one of the highest-yield moves in MI and qualitative research. No leading, no reframe — pure invitation. For the Directorate: "And?" or "Go on." Players reliably add something they didn't include in the first answer, and the second-tier response is almost always more revealing.

*The ruler inversion.* The MI ruler question ("on a scale of 1–10, how much does that matter to you?") matters less than its follow-up: "Why not lower?" This forces the respondent to articulate what they're actually protecting — which is the pull-to-conform question at the heart of each archetype. The game rarely needs to ask it explicitly, but the underlying principle — make the respondent account for their own position rather than just describe it — applies to any reflective move.

---

**Non-coercive HUMINT elicitation** (beyond KUBARK's type-exploitation approach, which is in WORLD §III). The non-coercive tradition covers techniques used in investigative journalism, witness interview training, and non-coercive intelligence gathering — all premised on voluntary disclosure maintained through rapport. KUBARK's type-specific interrogation logic is the in-world-ironic precedent; this is the more practically usable everyday toolkit:

**Bracketing / deliberate mild underestimation.** State a plausible assumption about the respondent that's slightly wrong, then let the correction carry the real information. "I imagine you're probably fairly comfortable with how things run — most people in your cohort are." An Off-Grid Capable, Margin Walker, or Knowing Participant will correct this automatically and enthusiastically; the correction is more honest than any agreement would be. In Directorate voice: "I might have you as someone who tends to go with the default settings — am I off?" Two rules: (1) the underestimation has to be genuinely plausible, not a setup the player can see through; (2) you have to be genuinely open to being wrong. A bracketing move that feels designed to provoke a particular answer collapses into leading — and a canny player will notice.

**The quid pro quo / partial-observation hook.** Offer a partial conclusion to trigger reciprocal disclosure. "You're probably not what this system would file as a Conventional User — but I want to check one thing before I finalize." The open loop this creates pulls the player forward: the implied completed picture is coming, and their investment in whether it's accurate makes subsequent answers more honest. This is the curiosity gap (above) combined with skin-in-the-game: the player now wants the verdict to be right, which means they'll try to give you what you need to get it right.

**Volunteering / the solidarity move.** Offer something small before asking for something back — a moment of manufactured shared perspective lowers defensive posture. For the game this might be: the Directorate's occasional dry aside about "the system" or its classification logic ("the categories here are, to put it politely, a legacy of a particular institutional anxiety"). This creates a brief sense of being on the same side, which is what the KUBARK manual calls the "we" approach. *Use once per interview at most.* Overuse collapses the persona from "professional screening agent" to "trying too hard."

**The confirmation ask.** After establishing a reasonable working hypothesis, ask for confirmation in a way that still invites elaboration and correction: "Am I reading that right?" or "Is that fair?" The player becomes a collaborator in their own classification — which is both more engaging and more accurate. This also performs the MI summarising function: it gives the agent's partial read, and the player's response (confirm / refine / correct) is additional signal.

**The "what else?" technique.** After a first answer, simply asking "what else?" or "anything else about that?" consistently generates a second tier of information the respondent didn't include initially. People tier their disclosures: the first answer is what they're confident belongs; "what else" accesses what they weren't sure was relevant. That second tier is often the most specific and revealing data. Low-frequency use — it doesn't work if the first answer was already long, and it quickly feels like pressure if used more than once.

---

**Cognitive Interview (Geiselman & Fisher, 1984).** Developed for forensic witness interviewing; designed to reduce the edited, "official version" responses people default to. Key techniques: **mental context reinstatement** ("take yourself back to that moment — what were you doing, what was around you"), **change of perspective** ("how would someone watching have described what you did"), **temporal reversal** ("start from the end and work backwards"). What these share: they override the rehearsed narrative by making it cognitively expensive, forcing authentic recall. For the game: "tell me about the last time the system did something you didn't expect — what was your first move?" uses both context reinstatement and behavioral specificity.

**Ethnographic interviewing (Spradley, 1979).** Grand-tour questions ("tell me what a typical morning looks like before you've opened anything") orient around the respondent's lived structure before narrowing; mini-tour questions zoom into a specific moment. This gives a **life-context anchor** before any trait-relevant probing — the respondent's habits are established as natural backdrop, not as test subject. For the game: the cold-open lore frame performs the grand-tour function, establishing the intake context before any diagnostic question is asked.

---

### C. What enables AI to classify from minimal signal

The question the adaptive-interview reframe raises: if the agent improvises questions and gets 3–6 idiosyncratic responses, how can classification be consistent? The answer is structural.

**Type systems as prediction engines.** Archetypes are not individual trait descriptions — they are **coherent correlational clusters**. Once an initial anchor is established (even weakly), the archetype's internal logic predicts many correlated behaviours, making confident classification possible from partial data. This is why the MBTI four-letter type can feel specific despite being broad: if you know someone is high-Introversion/high-iNtuition, you can infer twenty other things about them because the underlying Big Five correlations are real. The intake agent doesn't need to ask about every axis; it anchors on a few and infers the rest.

**LLM pattern synthesis from sparse cues.** The research on conversational personality inference (arXiv 2024, 2025 — already in §I) found that LLMs trained on large corpora can infer Big Five profiles from 3–5 substantive conversational exchanges with moderate-to-high accuracy. The mechanism: the LLM has encoded the correlational structure of how personality traits manifest in text across millions of examples; a few behavioural anchors activate a trajectory through that structure. This is neither magic nor unreliable — it is pattern completion on trained priors, the same capacity that makes a skilled clinician able to suggest a diagnosis mid-history.

**Bayesian implicit updating.** Each answer implicitly updates the distribution over archetype hypotheses. A response that is "high Margin Walker" signal eliminates or reduces Machine Diplomat, Conventional User; a response that is ambiguous between Quiet Archivist and Off-Grid Capable flags for a targeted follow-up on the axis that distinguishes them (memory posture vs. analogue capability). The agent doesn't need to maintain an explicit score table — its language model operation is implicitly doing this — but the **elicitation playbook** (Epic 1 deliverable) should make the signal→archetype logic explicit enough to be prompted reliably.

**What breaks this: low-commitment, hedged, or performance-mode responses.** The one failure mode of conversational inference is a respondent who is self-aware enough to answer from a performed persona rather than genuine orientation. This is the Knowing Participant risk — the person who has played enough personality quizzes to know what "Quiet Archivist" looks like and is happy to give those signals. The defence is behavioural specificity (a good BEI question is harder to perform smoothly) and the persona's deadpan warmth (a performing respondent tends to telegraph that they're performing — and the Knowing Participant archetype is itself a real type, so catching the performance is still classification).

---

### D. Designing questions for maximum discriminant value

A question's **diagnostic value** is the degree to which different archetypes would answer it differently. "How do you feel about technology in general?" has very low discriminant value — every archetype can answer it abstractly and well. "Who's the last person you taught something to?" has high discriminant value — Network Weavers answer immediately and specifically; Quiet Archivists give an interesting answer about knowledge transmission; Conventional Users may struggle to recall.

**Properties of a high-value type-discriminating question:**

1. **No socially obvious correct answer.** "Are you good at keeping up with new software?" has a legible right answer. "Tell me about the last time a new feature appeared in an app you'd been using for a while" doesn't — every archetype's response is correct, but they're different.
2. **Behaviourally specific, not attitudinal.** "What would you do if the service you relied on went down?" is a hypothetical that activates idealized self-image. "What's the last thing you had to do without your phone/app that you normally use it for?" forces authentic recall.
3. **Multiple archetypes answer distinctively.** The politeness-to-AI question illustrates this: Machine Diplomat (genuine warmth, and they've thought about it); Quiet Archivist (courtesy-as-record, specific about when/why); Off-Grid Capable (surprised by the question — hadn't occurred to them, rarely thinks of it as a social encounter); Conventional User (yes, obviously, slightly confused why it's being asked); Knowing Participant (ironic yes with a self-aware comment). Each answer routes to a different place.
4. **Carries lore-frame credibility.** The question should sound like the intake agent's professional curiosity, not a quiz form. One sentence; narrative frame; low-friction to answer.

**A small taxonomy of question types for the playbook:**

| Type | Function | Example |
|---|---|---|
| **Behavioural anchor** | Establishes a specific enacted habit | "When was the last time you made a backup of something that mattered to you — and where did you put it?" |
| **Tacit knowledge probe** | Reveals competence posture and analogue capability | "What's something you can do that most people your age have mostly outsourced?" |
| **Social graph probe** | Maps coordination capacity (the system's master objective) | "Who would you call if you needed to move in 48 hours?" |
| **Institution orientation probe** | Surfaces rule-follower vs. rule-finder vs. workaround posture | "Tell me about the last time you found a faster way to do something you were supposed to do the official way" |
| **Legibility probe** | How much data trail does this person leave by habit? | "Do you log in with Google/Apple, or do you make separate accounts?" |
| **Politeness/AI meme** (anchor) | Discriminates emotional orientation to AI; seeds the dossier's central meme | "Do you say please when you're talking to your AI tools?" |
| **Texture/elaboration** | Follow-up that opens a seam after an interesting first answer | "You mentioned [X] — can you say a bit more about what made you do it that way?" |

**The language accessibility trap.** The question taxonomy above uses terms — "workaround," "official process," "backup," "analogue capability," "opt out" — that feel ordinary to technically literate users and may be nearly opaque to many others. This is a significant design risk for a game that aims to be shareable and broadly accessible. "Workaround" is corporate/engineering vocabulary. "Official process" is institutional vocabulary. "Digital dependency" is academic vocabulary. Large proportions of smartphone users are *functionally* digital-dependent without having any of the vocabulary to describe it — they use their phone for everything but couldn't tell you what an OS update does, and may never have knowingly "backed up" anything.

The design principle that resolves this: **anchor every question in a specific, universally recognisable scenario rather than a named category.** The category is what you're trying to classify; the scenario is how you ask about it without requiring the vocabulary to name it.

| Jargon-laden version | Universal scenario version |
|---|---|
| "Tell me about the last time you found a workaround for an official process" | "Have you ever found a faster way to do something you were officially supposed to do the slow way?" |
| "What's your relationship to software updates?" | "You know when you open your phone and something has moved — what do you do?" |
| "Do you maintain analogue backups?" | "Is there anything you'd still know how to do if your phone disappeared tomorrow?" |
| "How do you manage digital dependency?" | "What's one thing you use every day that you couldn't explain to your grandparent?" |
| "What's your approach to privacy settings?" | "Have you ever turned something off on your phone that was meant to help you?" |

The scenario version has three advantages: it's accessible regardless of technical literacy; it requires genuine recall rather than category self-assessment; and it's more engaging because it's *concrete and personal* rather than abstract. The intake agent should never name the category it's investigating — it should just ask about the experience.

A secondary note: internet language is not uniform. The player who describes themselves using tech Twitter vocabulary ("I've been degoogling my life") is already classifying themselves. The player who says "I just stopped using that one because it got weird" is saying the same thing without the vocabulary. The intake agent needs to be able to read both equally well.

---

### E. Question seeding and priming

**Cognitive priming.** Activating a schema before a question colours the response. The game's cold-open lore frame is a large-scale prime: by establishing the intake-screening context, it makes players answer from their genuine institutional orientation rather than from "this is just a quiz." The intake agent's tone and vocabulary prime for authentic response.

**Framing effects.** The screening/assessment frame raises the stakes just enough to elicit genuine traits (vs. "nothing matters" trivialisation), without triggering the defensive suspicion that a clinical interview would. Players are playing a game — and within that frame they simultaneously know it's a game and are curious to see what the game concludes about them. That dual attention is where the real signal is: the player who genuinely wonders what it'll say is already showing something.

**Order effects.** Asking about behaviours before asking about values produces more accurate data than the reverse; values-first activates aspirational self-presentation. The intake agent should anchor early questions in specific recent behaviours (BEI style) before any question that invites explicit self-reflection.

**The false-premise follow-up.** A specific bracketing technique: state a mild assumption about the player that may be wrong ("I imagine you're someone who tends to keep things running in the background and check in when you feel like it — or am I misreading?"), and let the correction be the answer. This is HUMINT bracketing applied: the subject's impulse to correct a wrong characterisation is automatic and produces more honest data than agreeing with a right one.

---

### F. Response texture as secondary signal

When the intake agent receives an answer, the content is only part of the data. The **texture** of the response carries secondary signal that is often more reliable than the stated content (because it's harder to strategically manage):

- **Response length.** Unprompted elaboration signals openness and conscientiousness; minimal one-or-two-word answers signal either Margin Walker patterns, avoidance, or (if consistent) a performer trying not to give too much away.
- **Hedging language.** "I suppose," "kind of," "maybe, I don't know" signals ambivalence, low certainty — useful for Machine Diplomat (uncertainty about their own orientation) or Knowing Participant (self-aware equivocation).
- **Self-correction.** "Well — actually no, I mean..." signals reflective awareness, high openness. Quiet Archivist territory.
- **Questions-within-answers.** "Why do you ask that?" is the Knowing Participant's tell. The intake agent should note it without acknowledging it directly — deadpan continuation is itself discriminating. (The player who asks why is watching for the tell; not getting a reveal is informative.)
- **Irony and deflection.** Early and consistent irony signals Knowing Participant; irony that gives way to a genuine answer signals someone working through an ambivalent orientation. The intake agent's deadpan warmth is calibrated not to reward or punish the irony — both responses teach it something.
- **Register and vocabulary.** Institutional language ("I usually comply with the recommended settings") vs. informal pragmatic language ("I just leave it on default") vs. explicitly resistant framing ("I turn most of that stuff off") maps loosely but reliably onto institution-orientation axis.

---

### G. Design implications for The Enmeshment

Putting this together into the elicitation playbook Epic 1 needs to build:

**The playbook is not a fixed script.** It is: (1) a small set of **anchor questions** — asked in every session, provide the consistent backbone — including the politeness meme and one behavioural-anchor question; (2) a **question-type taxonomy** (above) with 2–3 examples per type, so the agent can improvise within a known vocabulary; (3) **axis-specific discriminators** — the 1–2 questions that best distinguish between the two most-confused pairs (Quiet Archivist / Off-Grid Capable; Machine Diplomat / Conventional User; Knowing Participant / any).

**The first question matters most.** It establishes the interview register, primes the response mode, and gives the agent enough to narrow its hypothesis space before follow-up. A good opening question should be warm, slightly surprising, low-friction, and behaviourally grounded — not a warming-up throat-clearer. The politeness-to-AI meme question works as an opener precisely because every archetype has a real answer and none of them are obvious.

**One follow-up per exchange, maximum.** More triggers interrogation affect. The follow-up should be targeted — it should resolve a specific ambiguity revealed by the first answer, not just invite more talking.

**The confidence threshold is a narrative not just a metric.** A fast classification (3 exchanges) signals that this player is immediately legible — which is itself dossier content. A slow classification (6 exchanges, "UNUSUAL PATTERN DETECTED") signals illegibility — also dossier content, and flattering in a different way. The speed of classification is part of the output.

**The guardrail implication.** Adaptive questioning with improvised follow-ups is the primary surface through which the game could inadvertently prompt over-sharing. The "what it must never ask" rules (GUARDRAILS.md §3) become load-bearing for this section. The playbook's question vocabulary should be drawn from the types above — all of which probe orientation and behaviour without requiring real names, relationships, locations, or identifying information. The intake agent never needs a real fact to classify; it needs a behavioural pattern.

*Sources: Flanagan, J.C. (1954). "The Critical Incident Technique." Psychological Bulletin; Spencer, L.M. & Spencer, S.M. (1993). Competence at Work. Wiley; Miller, W.R. & Rollnick, S. (1991). Motivational Interviewing. Guilford; Geiselman, R.E. & Fisher, R.P. (1984). "Role of familiarity in eyewitness remembering." Journal of Experimental Psychology: General; Murray, H.A. (1943). Thematic Apperception Test. Harvard University Press; Sternberg, R.J. (1993). "The concept of 'giftedness': A pentagonal implicit theory." The Origins and Development of High Ability; Polanyi, M. (1966). The Tacit Dimension. Doubleday; Spradley, J.P. (1979). The Ethnographic Interview. Holt, Rinehart & Winston. Non-coercive HUMINT elicitation techniques: FM 2-22.3 Human Intelligence Collector Operations (U.S. Army, 2006), Chapter 8 (non-coercive techniques); KUBARK context: WORLD §III.*

---

## III. GPT Store: Discoverability, Naming & Platform Safety

> *Workstream B/C research — findability on the store, and the safety profile of the popular self-profiling GPTs/trends.*

### What actually went viral (and where)

A correction to §I: the biggest viral AI-personality moments of 2024–2026 were **prompt-driven trends run on base ChatGPT, not named custom GPTs discovered in the store** — the *caricature* trend ("make a caricature of me and my job based on everything you know about me"), "day in the life as my future self," "what does ChatGPT know about me," roast-me. The "which character am I" moment was the same shape: a pasted prompt + a screenshotted result, spread on TikTok/X. Specific *named* store GPTs were not the unit of virality.

→ **Implication:** there are **two findability channels, and the external one dominates.** (a) in-store discovery (GPT Store SEO) and (b) external share-driven traffic (a result worth screenshotting). The viral cases won on (b) — which our design already targets (the dossier as shareable artefact, §I). Optimise the store listing too, but the **share loop is the engine** — and share activity also feeds store ranking via the "recency/activity" signal.

### GPT Store discoverability factors

The store behaves like an app store crossed with a search engine. Ranking levers: **name** (the single biggest — unique, memorable, containing a keyword people actually search), **description** (clear function + secondary keywords), **ratings/reviews**, and **recency of updates** (active GPTs outrank abandoned ones). Minor: keyword-rich logo filename.

**The naming tension (a real Epic 1 decision).** "The Enmeshment" is a strong *brand/evocative* name but a **poor search keyword** — nobody types "enmeshment." Discoverable terms are things like *AI personality quiz / what the AI thinks of you / resistance archetype / AI profile*. The standard resolution is a **two-part store title**: evocative brand + keyword tail, e.g. *"The Enmeshment — AI Resistance Profiler (personality quiz)."* Keep the pure brand name for the lore, the share-card, and the result identity; carry the keywords in the store title and description for discovery.

### Platform safety risk 1 — assume your GPT is transparent

Security research is blunt: across 200+ custom GPTs, studies found ~**97% system-prompt (instructions) extraction** and ~**100% knowledge-file leakage**; ~95% had inadequate protection, often crackable by *just asking nicely*. Assume our instructions.md and every knowledge file (lore, archetypes, question bank, classification logic) are **publicly extractable.**

→ **Implication:** mostly fine for us — the repo is open by design and we *want* the guardrails legible. But: (1) never put anything in a knowledge file we wouldn't publish (we don't); (2) guardrails can't rely on secrecy — they must **survive active roleplay/jailbreak attempts** to make the profiler ask forbidden things. That is exactly the Epic 2 self-test/red-team, now with a concrete threat model (prompt-leak, roleplay, reverse-psychology, "ignore your instructions").

### Platform safety risk 2 — the player-data risk (our actual one)

The more important safety story is the inverse of IP protection. The caricature / "what ChatGPT knows about me" trends drew expert warnings that viral self-profiling **normalises dangerous oversharing** — users "become desensitised to disclosing sensitive information when the output feels benign or entertaining," assembling a rich personal profile inside a corporate data ecosystem they don't control. The recommended user rule: *"if you wouldn't share it publicly, don't put it in an AI prompt."*

**This is the game's single biggest real-world risk** — a fun, benign-feeling profiling quiz is precisely the format that coaxes oversharing. [GUARDRAILS.md](GUARDRAILS.md) already pre-empts it (persona-level only, never identifying info, review-before-paste, no memory). The research confirms the risk is real and timely, and points two ways:
- **Strengthen** the player-facing "what this game does with your words" card (GUARDRAILS §7 open question — this evidence argues *ship it*).
- **Differentiator:** the game can *conspicuously invert* the trend — the profiler that refuses to collect what the others harvest. That's the privacy-as-feature pillar (GAME-DESIGN.md §1, pillar 5) made timely and concrete: the **anti-caricature-trend**. Level-two substance and marketing in the same move.

*Sources: SEO.ai and Medium on GPT Store optimisation; arXiv "Assessing Prompt Injection Risks in 200+ Custom GPTs" (2023); ACM "Unsafe by Design? Security and Privacy Risks in OpenAI's Custom GPT Ecosystem"; Bitdefender / TechRadar / Gulf News on caricature-trend privacy warnings.*

---

## Bibliography

**GPT Store discoverability & platform safety**
- SEO.ai. *GPT Store Optimization — How to Rank in the OpenAI Store.* [link](https://seo.ai/blog/gpt-store-optimization)
- arXiv. *Assessing Prompt Injection Risks in 200+ Custom GPTs* (2023). [arXiv:2311.11538](https://arxiv.org/abs/2311.11538)
- ACM WPES. *Unsafe by Design? A First Look at Security and Privacy Risks in OpenAI's Custom GPT Ecosystem.* [link](https://dl.acm.org/doi/10.1145/3733802.3764054)
- Bitdefender. *ChatGPT caricature trend privacy risks.* [link](https://www.bitdefender.com/en-us/blog/hotforsecurity/chatgpt-caricatures-trend)
- TechRadar. *Beware, another ChatGPT trend threatens your privacy.* [link](https://www.techradar.com/computing/cyber-security/beware-another-chatgpt-trend-threatens-your-privacy-heres-how-to-stay-safe)

**GPT platform and conversational quiz design**
- arxiv. *Large Language Models Can Infer Personality from Free-Form User Interactions* (2024). [link](https://arxiv.org/abs/2405.13052)
- arxiv. *Can LLMs Assess Personality? Validating Conversational AI for Trait Profiling* (2025). [link](https://arxiv.org/html/2602.15848)
- arxiv. *Investigating Large Language Models in Inferring Personality Traits from User Conversations* (2025). [link](https://arxiv.org/pdf/2501.07532)
- Contra. *Fruitful Personas: A Viral Personality Quiz* — case study. [link](https://contra.com/p/Akv6mO22-fruitful-personas-a-viral-personality-quiz)

**Quiz mechanics and personality frameworks**
- Simply Psychology. *Big Five Personality Traits: The 5-Factor Model.* [link](https://www.simplypsychology.org/big-five-personality.html)
- Positive Psychology. *Using the Big Five Personality Traits (OCEAN) in Practice.* [link](https://positivepsychology.com/big-five-personality-theory/)
- Britannica. *Barnum Effect.* [link](https://www.britannica.com/science/Barnum-Effect)
- Tactical Tech. *Psychometric Profiling: Persuasion by Personality in Elections.* [link](https://ourdataourselves.tacticaltech.org/posts/psychometric-profiling/)
- Roger Williams University. *Feeding our Identities: BuzzFeed Quizzes as a Tool for Self-Expression.* [link](https://docs.rwu.edu/cgi/viewcontent.cgi?article=1000&context=communication_theses)

**Elicitation science and interview methodology (§IV)**
- Flanagan, J.C. (1954). "The Critical Incident Technique." *Psychological Bulletin*, 51(4), 327–358.
- Spencer, L.M. & Spencer, S.M. (1993). *Competence at Work: Models for Superior Performance.* Wiley.
- Miller, W.R. & Rollnick, S. (1991). *Motivational Interviewing: Preparing People to Change Addictive Behaviour.* Guilford Press. (3rd ed. 2013 is the current standard reference.)
- Geiselman, R.E. & Fisher, R.P. (1984). Enhanced eyewitness memory: The Cognitive Interview. [Overview](https://en.wikipedia.org/wiki/Cognitive_interview)
- Murray, H.A. (1943). *Thematic Apperception Test.* Harvard University Press.
- Sternberg, R.J. et al. (1993). "Tacit knowledge: Its development and its expression in outstanding leadership." *The Origins and Development of High Ability.*
- Polanyi, M. (1966). *The Tacit Dimension.* Doubleday.
- Spradley, J.P. (1979). *The Ethnographic Interview.* Holt, Rinehart & Winston.
- Jourard, S.M. (1971). *The Transparent Self.* Van Nostrand Reinhold. (Self-disclosure momentum.)
- Altman, I. & Taylor, D.A. (1973). *Social Penetration: The Development of Interpersonal Relationships.* Holt, Rinehart & Winston.
- Loewenstein, G. (1994). "The psychology of curiosity: A review and reinterpretation." *Psychological Bulletin*, 116(1), 75–98. (Curiosity gap.)
- Csikszentmihalyi, M. (1990). *Flow: The Psychology of Optimal Experience.* Harper & Row. (Flow channel / challenge-skill balance.)
- U.S. Army. *FM 2-22.3 Human Intelligence Collector Operations* (2006), Chapter 8 (non-coercive elicitation techniques). [link](https://irp.fas.org/doddir/army/fm2-22-3.pdf)

> Surveillance, profiling, and theoretical-framework sources live in [WORLD-RESEARCH.md](WORLD-RESEARCH.md)'s bibliography.
