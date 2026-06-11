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

> Surveillance, profiling, and theoretical-framework sources live in [WORLD-RESEARCH.md](WORLD-RESEARCH.md)'s bibliography.
