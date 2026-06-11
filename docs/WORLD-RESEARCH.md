# World Research — Grounding the Scenario

> **Purpose:** Real-world context that gives the *world* its spine — the surveillance, profiling, and futures-thinking the Enmeshment is built from. Where [STORY-RESEARCH.md](STORY-RESEARCH.md) grounds the story shape and [MECHANICS-RESEARCH.md](MECHANICS-RESEARCH.md) grounds how the game is built, this doc grounds why the world is credible. Consult it when writing lore, the scenario, and the declassified footnote. Not player-facing.
>
> Status: **v0.2, June 2026** — split from the former single RESEARCH.md. Covers AI futures scenarios, techno-authoritarianism and the intelligence logic of surveillance, the history of profiling, and the theoretical frameworks.

---

The Enmeshment is a fictional scenario, but it is built from real tendencies already in motion. This document surveys the relevant literature and real-world systems — not to make the game a lecture, but so that every design choice has weight behind it and every "declassified footnote" reflection question can gesture at something true. Four clusters: how credible near-future AI scenarios are structured and what is original about ours; what real techno-authoritarian systems actually do with the data they collect — and what it costs the people inside them; what states have always tracked when they profile; and the theoretical frameworks (Zuboff, Crawford, Elish, Scott) that name the mechanisms the game dramatises.

> **A note on sourcing (for cold readers).** This is a *grounded research brief, not a fact-checked citation of record.* It blends reputable secondary sources, think-tank/advocacy research, and some primary documents (HRW's IJOP reverse-engineering, GAO on TSA SPOT, CIA KUBARK, Brayne's *Predict and Surveil*). A handful of vivid figures are single-study, contested, or marketing-derived; where a shaky number does real load-bearing work it is flagged inline. **Nothing here is player-facing as written** — any statistic that becomes lore or a declassified-footnote claim must be re-checked against a primary source first. The specific claims most worth verifying are queued in [planning/FACT-CHECK-QUEUE.md](planning/FACT-CHECK-QUEUE.md).

---

## I. AI Futures Scenarios

### The Landscape

The two most discussed near-future AI scenario documents are **Leopold Aschenbrenner's *Situational Awareness* (2024)** and the **AI 2027 project (Daniel Kokotajlo et al., 2025)**. Both are worth knowing; neither is quite our scenario.

*Situational Awareness* is a 165-page forecasting essay arguing that AGI by ~2027–2030 is the central national-security challenge of our era. Its core mechanic is **recursive escalation**: each round of AI investment is justified by the last. Safety becomes a PR function. The US–China arms race makes deceleration feel like unilateral disarmament. The paper was written by a former OpenAI researcher and is explicitly framed as a call to action for the national-security establishment — which is itself a data point about who is shaping the discourse.

The AI 2027 project is a narrative scenario document projecting month-by-month developments from 2025 toward a decisive threshold. It is more granular about the *mechanism* by which human oversight erodes: systems grow fast and interconnected, review windows shrink below meaningful thresholds, and sign-off becomes ceremonial not by decree but by physics. It offers two endings — coordination saves the day, or race dynamics produce misaligned AI — which gives it a thriller structure that is neither grounded nor useful for our purposes.

Both are "precipice" models: a threshold event (AGI, the race's climax) defines the scenario. Everything builds toward a moment.

### The counter-framing: AI as normal technology

A serious counter-camp rejects the precipice framing entirely. Arvind Narayanan and Sayash Kapoor's **"AI as Normal Technology"** (April 2025 — the *AI Snake Oil* authors) argues that "superintelligence" is too speculative and incoherent to plan around, and that AI is best understood like prior general-purpose technologies — electricity, the internet. Their key distinction is three acts: **invention → innovation → diffusion.** Capability (invention) can move fast, but *impact* arrives only through diffusion — the slow social process of adoption into institutions — and diffusion is "more of a trickle than a tsunami." There is no moment; there is a decades-long settling.

This is the intellectual ally of our boiling-frog framing — and it sharpens *why* we use it: the value of the drift model is that **we never have to speculate about if or when a technological "moment" arrives.** There isn't one to predict. But we should keep one divergence deliberate. Narayanan and Kapoor are broadly *reassuring* — normal diffusion means impacts unfold through normal institutions that can adapt and govern. **Our scenario takes their mechanism and inverts their comfort.** The Enmeshment happens not despite AI being a normal, slowly-diffusing technology but *because* of it: the unhurried seep into every decision layer is exactly how enmeshment occurs without anyone noticing, or being able to name the day it happened. Normal technology, abnormal outcome.

> **What this means for the game:** This triangulation is the spine of our originality. Against the precipice camp (Aschenbrenner, AI 2027) we reject the **threshold event** — no need to predict a moment. With the normal-tech camp (Narayanan, Kapoor) we accept **gradual diffusion** — but reject its reassurance. Our scenario is the **boiling-frog model**: good-enough AI, recursively deployed at every decision layer, accumulating into enmeshment with no memorial date. The precipice model lets people think "we'll know when to act." The drift model says you already didn't.
>
> Use Aschenbrenner's **escalation logic** for Phase 1 (The Race), the **diffusion-without-a-moment** logic for Phase 2 (The Convenience), and AI 2027's **drift-to-ceremony** for Phase 3 (The Drift).
>
> **The open question this raises (see §V):** if there is no *technological* moment, does resistance still need a *social* one — a tipping point at which a critical mass refuses? And, crucially, the thing being resisted is **state overreach (state + AI enmeshed), not technology itself.** That distinction — and the social dynamics of how resistance actually arises — is its own strand below.

---

### The control axis: which "AI-as-control" horizon we extrapolate toward — and where we stop

Everything above concerns the *capability* timeline (fast precipice vs slow normal-tech diffusion). But the scenario's load-bearing premise is not about capability — it's about **control**: the slide of *state* decision-making into enmeshment with AI. That premise extrapolates from real trends toward a recognised horizon in the literature, and the craft is in choosing how far along to stop. Two horizons; our scenario sits in the gap between them.

**Horizon A — disempowerment / "rule by Nobody."** *Gradual Disempowerment* (Kulveit et al., Jan 2025) argues humanity can lose control **without** any superintelligence or coordinated power-seeking — purely because AI becomes a more competitive alternative to humans across economic, political, and cultural functions. The hidden load-bearing fact: human participation was *necessary* for thriving economies, states, and cultures, and that necessity is what kept those systems roughly aligned with human interests. Remove the necessity and the alignment quietly lapses — reinforced across domains (economic power buys cultural and political influence) and effectively irreversible. Paul Christiano's *What Failure Looks Like* (2019) calls the same shape "going out with a whimper": no discrete point of no return, AI goals gradually outweighing human ones in systems no one can oversee. The political-theory name for the endpoint is older and sharper — Hannah Arendt's **"rule by Nobody"**: bureaucracy as "the rule by an intricate system of bureaux in which no men… can be held responsible… a tyranny without a tyrant," and therefore *the most tyrannical of all, since there is no one left who could even be asked to answer.*

**Horizon B — concentration / "rule by a hidden Someone."** The opposite failure: AI as the ultimate instrument of *centralised* power. The power-concentration literature (80,000 Hours; Forethought's *AI-Enabled Coups*) warns that loyal AI in government "could dramatically increase state power — surveillance, censorship, propaganda, targeting of opponents," letting a small group, a single state, or one person seize and lock in control. The AI-authoritarianism framing is pointed: where conventional authoritarianism must *actively* centralise power and disable accountability, AI authoritarianism "integrates these features into its very functioning" — unaccountability by design.

**Where we stop — and why.** The full recursive endpoint of either horizon is exactly what we reject: Horizon A's terminus is irreversible disempowerment (the precipice/doom story again); Horizon B's is a closed singleton — Bostrom's "single decision-making agency at the highest level." Our scenario extrapolates *toward* both horizons but **stops at the pre-closure threshold** — the ambiguous overlap where it is genuinely unclear whether this is rule by Nobody or rule by a hidden Someone, and where it is not yet irreversible. This is the "slowly, then suddenly" middle: already enmeshed, not yet closed; still polite, still deniable, still retaining a ceremonial human in the loop. It is the only point on the curve where *choice still exists* — which is what makes it a game rather than a lament, and keeps it inside the no-doom guardrail.

> **What this means for the game:** The premise is a credible extrapolation, not a contrivance — and we can name precisely which horizon it points at. The Enmeshment is **gradual disempowerment as its mechanism, Arendt's rule by Nobody as its felt texture, and a deliberately unresolved question — Nobody, or a hidden Someone? — as its central ambiguity** (which [LORE.md](LORE.md) §3 already protects: "isn't malevolent and isn't conscious (probably)"). We stop short of the singleton's closure on purpose: the closed loop is unplayable, unfunny, and untrue to the "what relationship do we want?" question. Keep the ambiguity live — the defected profiler itself shouldn't know whether anyone is at the top. That uncertainty is the horror *and* what keeps the game apolitical: no named cabal, no named overlord, just a settling no one will admit to having decided. (Craft consequence — how to dramatise an antagonist with no one in charge — is in [STORY-RESEARCH.md](STORY-RESEARCH.md) §III.)

### The meme as canon: "be polite to the AI"

The game's central conceit — that early politeness toward AI was a kind of telemetry — operationalises a real, widespread meme: "be nice to the AI today / they'll remember your rudeness during the robot uprising," crystallised in the comic where killer robots spare the one human who "always said thank you." Sam Altman gave it a wink from the top: asked about the energy cost of all those pleases and thank-yous, he called it *"tens of millions of dollars well spent — you never know."*

**But the credibility has to be calibrated honestly — and kept separate from the fun.** The strongest evidence points to **automatic social reflex, not belief.** Reeves & Nass's *Media Equation* / "Computers Are Social Actors" work (Stanford, 1996, widely replicated) showed that people are unavoidably polite to computers — and *deny doing it* even as they do; once the politeness "script" fires, they simply run it. People say "please" because that's how they're built to make a request. The "insurance against the uprising" angle is mostly a **joke people enjoy sharing**: the numbers usually quoted (≈half think AI "deserves" courtesy; ~1 in 4 say please every time) come from *commissioned marketing surveys* (Talker Research), and even those cite "the AI replies better" and "habit carry-over" as the main reasons — not fear of future judgment. There's a thin thread of literal truth (prompt tone does affect LLM output, messily) but that isn't why anyone says please, and Roko's basilisk is a thematic ancestor, not evidence anyone acts on it.

So the meme earns its place on **two ledgers we must not mix up:**
- **Level one / marketing:** instantly gettable, funny, shareable — everyone has either made this joke or quietly meant it. Real value, and the safest entry to the hook. But "fun and widely shared" is *not* "evidence that people fear AI judgment."
- **Level two / the modest, honest grounding:** the genuinely true, on-theme phenomenon is *not* that people believe in robot karma. It's that **we already calibrate our behaviour toward systems we half-suspect are recording us — and we're unsure how much we mean it.** Habit, hedge, joke, faint unease, all at once, unexamined. *That* ambiguity mirrors the game's own Nobody/Someone uncertainty.

> **What this means for the game:** Use the meme as the level-one hook and the seed of the **Machine Diplomat** — but ground the level-two claim in the *unexamined ambiguity of our politeness*, not in an overstated "people fear the AI." LORE.md's "politeness telemetry" works precisely because the in-fiction system takes a casual, mixed-motive human habit and *files it as data* — funny and quietly pointed at once, without the game ever having to assert that anyone really believed. Keep the marketing fun and the credibility claim on separate ledgers.

---

## II. Techno-Authoritarianism: What the System Actually Does

To see where the scenario is headed, we look first at where we already are — and have been. The sections that follow examine real, documented surveillance and profiling systems: the existing infrastructure the Enmeshment is extrapolated from. None of it is cast *as* the Enmeshment — the game keeps real countries out of the scenario, which stays abstracted — but the scenario's logic comes from these systems, and looking at them squarely is what keeps the fiction accurate. It is also the subtext the declassified footnote can surface.

The earlier sections below describe the *inputs* — what data these systems collect. The section that matters most for the game, **The Intelligence Logic**, describes what that data *becomes*: how raw collection turns into a profile, why a state wants it, and — crucially for a person-vs-system game — what it costs you when the system knows it.

### China's Social Credit System

The western image of China's social credit system — a single unified citizen score — overstates the coherence and understates the point. What exists is a **patchwork**: roughly 100+ local pilots, national blacklists for serious legal violations, corporate credit systems (Alibaba's Sesame Credit), and city-level behaviour tracking programs that interact inconsistently with each other.

**Key dimensions tracked across the system:**

| Domain | What is tracked |
|---|---|
| Financial | Debt repayment, loan defaults, fraud, tax compliance |
| Legal | Court judgments, contract violations, regulatory infractions |
| Professional | Business licensing, food safety, product standards |
| Civic conduct | Traffic violations, charity contributions, government-sanctioned awards |
| Digital behaviour | E-commerce habits, social media activity, search history (primarily corporate systems) |
| Government compliance | Administrative penalties, permit violations |

Consequences are tiered: AAA-rated citizens get fast-track visas and utility discounts; D-rated citizens face travel bans, public display-screen shaming, and police monitoring. One often-cited local pilot (Rongcheng) used 389 rules — 124 rewarding, 265 punishing — across eight tiers (AAA to D). *Note this is a single city scheme, routinely misreported as a national "citizen score," which does not exist in that unified form.*

But the scoring layer is not the engine. **The engine is stability maintenance** (*weiwen*). China's internal-security budget *officially exceeded* its external-military budget in 2011 and 2012; Beijing stopped publishing the national figure after 2013, so later years rest on estimates. The entire apparatus is oriented around a single fear: **organised collective action**. Reported "mass incidents" (protests, strikes, riots) rose from ~8,700 in 1993 to a widely-cited ~180,000 in 2010 — the latter a sociologist's estimate (Sun Liping, Tsinghua), not an official figure. The response was grid-based policing and big-data prediction designed to *resolve disputes before they escalate* — to detect and defuse the preconditions of coordination before a crowd ever forms. Programme-level success stats (e.g. "One Village, One Policeman" claiming a 61.6% drop in petitions) come from single Chinese-source reports; read them as indicative, not verified.

> **What this means for the game:** The mundane dimensions are more frightening than the dramatic ones. Being flagged for a traffic fine, a debt, a social media post — these are recognisable to any player. The deeper point: the score is a *means*, and the end is preventing people from acting together. The Enmeshment inherits this priority exactly. It doesn't fear your opinions. It models your capacity to coordinate.

*Sources: Stanford FSI; Brown PSTC "Preventing Collective Action Through Digital Surveillance"; Carnegie Endowment; Human Rights Watch.*

---

### The Xinjiang Model: Anomaly as Threat

Xinjiang is where the logic runs at maximum intensity — and where the most important lesson for the game lives. The surveillance apparatus there includes mandatory DNA, iris, and voiceprint collection; mobile checkpoints with compelled spyware installation; near-total CCTV with facial recognition keyed to ethnic profiles; and the **Integrated Joint Operations Platform (IJOP)** — a predictive-policing system that aggregates behavioural signals and flags individuals for detention.

What the IJOP actually flags is the revelation. Human Rights Watch reverse-engineered the system. There were **36 person-types/behaviours — plus possession of particular flagged apps — that alone could trigger investigation or detention.** And:

- **The vast majority of the flagged behaviour is entirely legal.**
- People were flagged for using a back door, socialising too little, using "unusual" amounts of electricity (prompting officials to check for "new electronics" or "renovations"), switching their phone off repeatedly, receiving calls from foreign numbers, using apps the state can't monitor, or donating to a mosque.
- **Most people were flagged for their *relationships* and *communications*** — for being related to, staying with, or in contact with someone the system already considered suspicious.

This is the core mechanic, stated plainly: the system is not looking for crimes. **It is looking for deviation from a modelled baseline of the normal, compliant citizen — and for proximity to other people's deviation.** Anomaly is the proxy for threat. Illegibility is the trigger.

The **export pipeline** makes this a template, not a local phenomenon. The mass biometric collection from Xinjiang's population generated training data that Chinese firms (Hikvision, Dahua, Huawei) used to refine commercial surveillance products — repression became a commercial asset. Huawei "Safe City" systems have a contested footprint: the headline "700+ cities / 100+ countries" figures are essentially **Huawei's own marketing**, while independent open-source research (CSIS Reconnecting Asia) has confirmed only ~**73 deployments across ~52 countries**. Either way the package is the same: cameras, facial recognition, financing, training, and long-term maintenance contracts that embed dependency. Documented deployments include Central Asia (used against dissidents and protesters), Africa (often Belt-and-Road financed), Latin America (35+ cities), and Eastern Europe (Serbia, where leaked files revealed covert expansion beyond what was disclosed).

> **What this means for the game:** This is the single most important real-world grounding for the game's central irony. The Enmeshment doesn't flag you for *doing* something wrong. It flags you for being *hard to model* — and for being close to others who are. Going dark, opting out, keeping unusual hours, knowing the wrong people: these are the anomaly signals. The "safe city" branding is also exactly on-tone: surveillance sold as service, convenience, safety. The Enmeshment doesn't announce itself. Neither does Huawei. And the ethical subtext — the toolkit was perfected on a population with no ability to consent or resist — is something the declassified footnote can gesture at without moralising.

*Sources: Human Rights Watch, "China's Algorithms of Repression" (2019) and "Big Data Program Targets Xinjiang's Muslims" (2020); ICIJ "China Cables"; ASPI Xinjiang Data Project; CSIS; RFERL on Serbia.*

---

### Palantir: Fusion and the Secondary Surveillance Network

Palantir's **Gotham** platform (used by the CIA, DoD, DHS, and police forces including the LAPD) is the closest western analogue to the Enmeshment's profiling infrastructure.

**The core innovation — the ontology model:** Gotham doesn't generate new data. It fuses existing data by breaking everything into objects — people, places, events, things — and mapping relationships between them. A DMV file, a criminal record, a social media subpoena, a licence plate scan: static, siloed records become a live, queryable web.

**Inputs:** criminal and arrest records (including charges that never led to conviction), licence-plate-reader data, social media, immigration records, financial records, facial-recognition footage, informant tips.

**What it produces — the actionable output is the point.** Gotham's value isn't storage; it's **link analysis**: surfacing connections a human analyst would miss. Sociologist Sarah Brayne, embedded with the LAPD, named the key product the **"secondary surveillance network"** — the mapped web of *who is related to, friends with, or sleeping with whom*. Given one known person of interest, the system expands outward to their unknown associates. The other major output is **pattern-of-life**: where you go, when, with whom, and — most importantly — *deviations from your routine*. The LAPD's LASER program turned this into a points-based "chronic offender score" (criminal history, known associates, gang affiliation) designating people for elevated surveillance before any new offence.

> **What this means for the game:** What makes the Palantir model feel like science fiction — but isn't — is the *fusion*, not the data. The inputs are boring bureaucratic records. The power is connecting them. The two outputs are exactly what the Enmeshment trades in: **your network** (the secondary surveillance network — who you could act with) and **your pattern** (what you'll do next, and when you deviate). And the feedback loop matters: **the profile becomes the crime.** Mark someone high-risk, surveil them harder, generate more incidents, confirm the model. Being classified shapes what the system sees next.

*Sources: Sarah Brayne, *Predict and Surveil* (Oxford, 2020); The Intercept on LASER; The Conversation on Palantir's data mapping; AlgorithmWatch on predictive policing.*

---

### The Intelligence Logic: What the System Wants, and What It Costs You

This is the heart of the matter, and the part the rest of the game's design hangs from. Strip away the technology and ask the underlying question: *what is a surveillance state actually trying to learn, and why?*

**The shift: from retrospective to anticipatory.** Classic policing was retrospective — a crime occurred, find who did it. Modern profiling is **anticipatory**: model the whole population, forecast behaviour, and pre-position against it. The system is not building evidence of what you *did*. It is building a model of **what you will do, and whom you could do it with.** Evidence is for courts. Intelligence is for control, and control wants the future.

**Why metadata beats content.** Former NSA/CIA director Michael Hayden: *"We kill people based on metadata."* Former NSA general counsel Stewart Baker: *"Metadata absolutely tells you everything about somebody's life."* A Stanford study (Mayer, Mutchler & Mitchell, *PNAS* 2016) showed phone metadata alone — no message content — *can* infer sensitive traits like medical conditions, firearm ownership, and religion (a feasibility study on ~800 volunteers, illustrating the capability, not a population-scale classifier). Metadata is cheaper to collect, far easier to search at scale than content, and reveals the three things the system actually wants: **who you're connected to, what your patterns are, and when you deviate.** The NSA's SKYNET program rated individuals' likelihood of being couriers purely from GSM metadata — social network, travel behaviour, pattern-of-life — never reading a word they wrote.

**What an AI-enmeshed state actually wants to know.** Across every real system surveyed, the intelligence objectives reduce to five. For each: what it is, why the state wants it, and — the part that makes this a zero-sum game — what it costs you when the system has it.

**1. Coordination capacity — the master objective.**
*What:* Your social graph. Who do you trust, who would act on your word, how dense and resilient is the network around you. *Why:* The existential fear of every controlling state is organised collective action (China's *weiwen*; COINTELPRO's obsession with movement leadership; Palantir's secondary surveillance network). A lone dissident is a rounding error; a coordinated group is a threat. *What it costs you:* Every relationship you make legible is a relationship the system can pre-emptively pressure, surveil, or sever. The Stasi did this by hand (geographic relocation to reset social ties; Zersetzung to poison trust). The Enmeshment does it from metadata. **Your network is your only real power, and it is the system's primary target.**

**2. Predictability — pattern-of-life.**
*What:* Your baseline routine — the model of normal-you. *Why:* A predictable subject is a controllable subject; if the system can forecast you, it can pre-position. *What it costs you:* Once the baseline exists, your spontaneity becomes signal. You cannot act without the system noticing that you acted *off-pattern* — and the deviation itself is the flag. **Being known erases the advantage of surprise.**

**3. Anomaly — illegibility as the threat signal.**
*What:* Where you depart from the modelled normal, or fall into a gap the system can't see. *Why:* As IJOP shows, the system can't pre-judge guilt, so it uses deviation as a proxy. The legal-but-unusual is the target. *What it costs you — the cruel inversion:* the very acts that protect you from content surveillance (going dark, encryption, opting out, keeping analogue habits) are themselves the **highest-value anomaly flags.** Illegibility hides your content and advertises your difference at the same time. This is the central bind the game's archetypes live inside.

**4. Dependency — leverage.**
*What:* What you need from the system that it can grant, withhold, or modulate (income, services, mobility, reputation, convenience). *Why:* Every dependency is a control surface — the psychogram's logic, systematised and made ambient. *What it costs you:* Every convenience you accept is a lever someone else holds. The system never has to threaten you; it only has to make the easy thing the compliant thing.

**5. Function — replaceability.**
*What:* What you do that the system actually needs from you. *Why:* The state needs legitimacy nodes — people whose ordinary participation makes the whole thing look consensual and run smoothly. *What it costs you — the inverted cost:* being needed looks like safety and is actually a leash. The most "trusted" citizen is the most thoroughly bound, because their compliance is load-bearing.

**The zero-sum table.** Stated as the game's premise demands — every gain to the system is a loss to the resistance:

| The system learns… | …and the resistance loses |
|---|---|
| Who you trust and who'd act on your word | The ability to coordinate before being seen |
| Your routine / baseline | The advantage of surprise; spontaneity becomes signal |
| Where you go dark or deviate | Illegibility itself becomes the flag |
| What you depend on | A lever it can pull without ever confronting you |
| What you're needed for | Compliance becomes a leash dressed as safety |

> **What this means for the game:** This is the actionable core the archetypes should be built on. The Enmeshment's "profile" of a player is **not a record of deeds — it's a prediction and a leverage map.** That reframes every archetype as a *position in an intelligence game*:
> - The **Conventional User** gives the system everything and is therefore "safe" — but their safety is objective #5, the leash. Maximal legibility, maximal leverage held over them.
> - The **Network Weaver** is the highest-value target the system has, because they *are* objective #1 — coordination capacity in human form. The most warmly social archetype is the one the Enmeshment watches hardest.
> - The **Margin Walker / Off-Grid Capable** wins on objectives #2 and #4 (unpredictable, low-dependency) but pays the full price of #3: their illegibility is itself the anomaly flag.
> - The **Quiet Archivist** holds memory the system would rather control (a function it can't replace, #5) while keeping it off-network (#3) — valuable and flagged at once.
>
> The declassified footnote writes itself from here: *every convenient thing you accepted was a lever; every relationship you made visible was a map; the only thing the system genuinely can't model is the thing you do that makes no optimised sense.* That's a recognition, not a warning — exactly the register the guardrails require.

*Sources: Hayden / "we kill people based on metadata" (Johns Hopkins debate; Just Security); Stanford metadata-inference study; NSA SKYNET (Snowden disclosures; Ars Technica/Intercept); Sarah Brayne, *Predict and Surveil*; HRW on IJOP.*

---

### The Continuity of Surveillance

A through-line runs from the Stasi to COINTELPRO to Palantir to the Chinese SCS to the Enmeshment. Every generation of surveillance:
- Is built primarily from **already-existing data**, newly fused
- Tracks the same consistent dimensions: financial, relational, behavioural, ideological/loyalty
- Pursues the same five intelligence objectives above — only the **scale**, the **automation**, and **what the profile is used for** (destroy → score → predict → optimise) change

Understanding this continuity is why the Enmeshment doesn't need to be exotic. It's the logical next iteration of something very old.

---

## III. The History of Profiling: What States Have Always Tracked

### The Stasi (East Germany, 1950–1990)

The Stasi employed ~90,000 full-time officers and ~189,000 registered informants (IMs) in a country of 16 million — roughly 1 in 63 as a *snapshot* of registered informants. Cumulative estimates across the regime's lifetime run far higher (some scholars suggest densities as great as ~1 in 6–7 once all collaborators over time are counted). Its surveillance methods are historically unmatched in density, and its documentation is extraordinarily detailed because the files survived reunification.

**The psychogram:** Built from wiretapped phones, intercepted mail, informant reports, and direct observation, then interpreted by operatives trained at the Stasi's own Department of Operative Psychology — a formal academic unit at the Ministry's college. The psychogram was not a standardised form; it was a **leverage map**. The goal was not to understand the target but to find the wedge.

Documented categories they explicitly sought and recorded:

| Category | Operational use |
|---|---|
| Homosexuality (illegal until 1968; socially ruinous after) | Blackmail or exposure |
| Extramarital affairs | Anonymous letters to spouse; fabricated "confirmation" |
| Pornographic interests | Shame lever |
| Alcoholism or medication dependence | Reliability weapon; manufactured relapses |
| Debt or financial pressure | Recruitment coercion; engineered crises |
| Professional failures / parental negligence | Career destruction vectors |
| Obsessive hobbies (collecting, gambling) | Manipulation handles; time-wasting traps |
| Far-right contacts | Smear material (label target a fascist) |
| Psychological profile: self-confidence level, paranoia tendency, social validation need | Calibrate which Zersetzung tactics to deploy |

The canonical documented case is the writer **Jürgen Fuchs**: his literary circle was mapped, friendships systematically attacked, phone tapped, mail intercepted. Operations continued after he was expelled to West Germany, reportedly including radiation exposure during interrogation visits — documented in his file and disputed but not disproven.

**What views were considered dangerous**

There was no homogeneous target group; the threat model adapted to each context. Consistent categories:

1. **Political dissidence**: wanting free elections, western-style governance, or to emigrate. Collective visa applications west were an automatic tripwire.
2. **Religious activity**: Jehovah's Witnesses were a formal enemy organisation. Church youth groups were intensively monitored because church was the one space outside Party oversight — the only institution that was, in Scott's terms, *illegible* to the state.
3. **Cultural non-conformity**: The Stasi produced a literal **illustrated field guide (1985)** for identifying youth subcultures by threat level — one of the stranger artefacts of the era. Key entries: *Punks* ("most dangerous" — "deprecative to hostile political attitude, rejection of all state forms and societal norms, anarchist thoughts, belief in total freedom"); *Goths* ("a satanic and death cult... fans of the group The Cure"); *Heavies* (metal fans — previously dangerous, "increasingly society-conforming" by 1985); *Teds* (rock-and-roll, largely harmless except for "attendance at birth and death days of idolised rock stars"). The logic: visible small-scale non-conformity predicts willingness toward dangerous non-conformity.
4. **Intellectual and literary circles**: writers in contact with western journalists or publishers; unofficial literary salons; anyone whose private writing might be "treasonous." Contact with the west was the key tripwire.
5. **Peace activists**: The 1980s peace movement operated through church networks and was therefore structurally outside Party visibility. Heavily surveilled for the same reason as church groups — illegibility.

**Zersetzung ("corrosion/decomposition"):** The psychogram identified which relationships sustained the target; Zersetzung attacked those specifically:

- *Spouse/partner*: Anonymous letters alleging infidelity, mixing real and fabricated details for credibility. In documented cases, attractive informants were deployed to actually seduce the target or their partner; the "affair" was then reported back to the other.
- *Friendships*: Whispering campaigns blending true embarrassing information with false rumours. Friends were also pressured into informing — which corroded trust even when the friend resisted, because the target could never be sure.
- *Workplace*: Fabricated evidence of negligence; engineered visible professional failures; anonymous complaints to supervisors through third parties.
- *Family*: Reporting family members to their employers; creating fear of association.
- *Geographic relocation*: One of the most structurally brutal tactics — repeatedly forcing job transfers to new cities. Each move reset the target's entire social graph. The accumulated relationships that sustained resistance could never consolidate.

**On scientific validity**

Methodologically primitive, directionally valid. The vulnerability categories — shame, debt, addiction, social isolation — are exactly the leverage points studied in modern coercive control research, interrogation science, and social engineering literature. Zersetzung's gaslighting tactics map directly onto what modern psychology identifies as the most destructive abuse patterns: manipulating someone's sense of reality rather than threatening them directly. The *method* of assessment (informant gossip, wiretaps) has obvious reliability problems. But the leverage model itself a psychologist would call rough but not wrong — the categories are real, the mechanisms work.

What the Stasi couldn't do: predict behaviour across contexts; model response to acute vs chronic stress; distinguish genuine character from situational reaction. They had a leverage map, not a predictive model. The Enmeshment has both.

> **What this means for the game:** The Stasi needed to know you well enough to *break* you. The Enmeshment needs to know you well enough that breaking never becomes necessary — it can route you instead. The Enmeshment's profiling is the psychogram rebuilt from passive observation at scale. It doesn't need informants. Behavioural surplus *is* the informant network; every digital interaction is a report. The horror shifts from active destruction to indifferent optimisation — subtler, more scalable, harder to resist because there's no moment of confrontation, no enemy to name.
>
> The 1985 subculture guide is also quietly on-tone for the game. The Enmeshment would have the equivalent — not an illustrated field guide but a classification schema. And the logic is identical: *visible small-scale illegibility predicts meaningful illegibility*. The Margin Walkers and their kind would be flagged early.

---

### FBI COINTELPRO (1956–1971)

A domestic counterintelligence program targeting political organisations — Communist Party, Black Panther Party, SCLC, AIM, Socialist Workers Party — using surveillance, infiltration, disinformation, and extralegal disruption.

**Profiling dimensions:** Political associations and leadership influence; personal relationships and known vulnerabilities; reputational weak points; financial pressures; informant-mapped internal dynamics.

**Method:** Profile → identify wedge → neutralise. Anonymous letters, planted media stories, informant-manufactured internal conflict, false arrests. The profile was always instrumental — the point was not to know, but to act. And the focus was overwhelmingly on **leadership and coordination** — objective #1 above — because the Bureau understood that a movement is its network.

> **What this means for the game:** COINTELPRO shows that "national security" framing has historically expanded surveillance far beyond genuine threats, and that the categories it used — political associations, social graph, personal vulnerabilities — are identical to commercial profiling categories today. The Enmeshment didn't invent new categories of interest. It inherited them and reframed them as governance optimisation.

---

### Other Profiling Traditions: Personality, Pathology, and Behaviour Detection

Beyond the Stasi and COINTELPRO, several other traditions attempted to classify nonconformity and personality systematically as threat indicators. Together they form a genealogy the Enmeshment inherits.

**CIA KUBARK Manual (1963) — The personality-type interrogation system**

The KUBARK Counterintelligence Interrogation manual (declassified 1997) is one of the most explicit government attempts to operationalise personality typology as an operational tool. Drawn from 1950s psychoanalytic and ego-psychology research, it classifies interrogation subjects into nine types and prescribes different approaches for each:

| Type | Defining traits | Exploitation method |
|---|---|---|
| Orderly-obstinate | Intellectual, frugal, secretive, stubborn — "plots frequently concern overthrow of authority" | Friendliness, not threat; tidy environment; exploit their rigidity |
| Optimistic | Impulsive, approval-seeking, "something will turn up" | Rapport then sudden withdrawal |
| Greedy/demanding | Acquisitive, self-interested | Material rewards; bribery |
| Anxious/self-centred | High anxiety, hypochondriac | Paternalistic care; position as protector |
| Guilt-ridden | Self-punishing, dominated by guilt | Provide an "out"; allow confession |
| Wrecked by success | Self-sabotaging after achievement | Accelerate their own destructive cycle |
| Schizoid/strange | Detached, odd, unresponsive to normal social leverage | Patience; avoid force |
| The exception | Entitled; believes rules don't apply | Appeal to unique special status |
| Average/normal | Responds to standard rapport | Standard approach |

The "orderly-obstinate" entry is particularly revealing: the CIA in 1963 explicitly describes as a threat type — people who "think things through logically," are "secretive," "disinclined to confide in anyone," and whose concerns "frequently involve the overthrow of some form of authority." That is: careful thinkers who distrust institutional authority. The game's Quiet Archivist and Margin Walker would both score here.

KUBARK is applied clinical psychology stripped of ethics — the personality framework is not pseudoscience, it is 1950s ego psychology used as an operational manual.

---

**Soviet "Sluggish Schizophrenia" (1960s–1986) — Nonconformity as diagnosed pathology**

Psychiatrist Andrei Snezhnevsky, working with KGB Chairman Yuri Andropov, developed a diagnostic category that expanded schizophrenia to include "latent" forms diagnosable from personality and behaviour alone — no hallucinations or psychosis required. Formally recognised symptoms included:

- *"Reform delusions"* — believing the system could or should be improved
- *"Struggle for the truth"* — persisting in claims the state denied
- *"Heightened moral preoccupations"* — caring excessively about right and wrong
- *"Overestimation of one's own personality"* — too much self-confidence
- Pessimism; poor social adaptation; conflict with authorities

The embedded logic: *if the socialist state is objectively correct, then disagreeing with it is a form of delusion*. Nonconformity is pathology. The diagnosis bypassed the criminal justice system — no trial, no evidence standard — routing dissidents directly into "special psychiatric hospitals" via KGB referral and indefinite internment. Post-1991 archives document 1,000+ political internments (broader estimates run far higher, toward ~20,000). The often-quoted "38%" is narrower than usually implied: a 1973 Soviet cohort (Zharikov et al.) classed ~38% of *schizophrenia patients* as sluggish-type — not 38% of all diagnoses.

The WHO expelled the Soviet psychiatric association over this in 1983. The diagnosis was retired after the USSR's collapse.

This is the logical endpoint of the "model the normal, flag the deviant" logic: when the model *is* the normal, deviation becomes illness. The Enmeshment doesn't pathologise deviation — but it does route it, which achieves the same practical outcome without needing the diagnosis.

---

**TSA SPOT Program (2007–ongoing) — Behaviour detection as governance theatre**

The Screening of Passengers by Observational Techniques program deployed thousands of Behavioral Detection Officers trained to identify threats through nonverbal cues and "micro-expressions." After 15+ years and $1 billion+ in expenditure, the GAO reviewed it and found: **28 of 36 behavioral indicators had no valid scientific evidence supporting them**. Research across 400+ studies: human ability to detect deception from behaviour is essentially at chance.

Related: government Countering Violent Extremism (CVE) programs use "pre-radicalization indicator" checklists in schools and workplaces. Documented indicators include "expressing hopelessness," "trauma history," and "connection to group identity (race, nationality, religion)." Multiple studies found CVE programs *increase* the alienation they're meant to prevent.

The SPOT program is Elish's moral crumple zone applied to airports: it performs security rather than providing it. The humans are in the loop. The loop produces racial profiling. The system escapes accountability.

---

**Cambridge Analytica (2016) — The commercial personality profiling turn**

The **OCEAN / Big Five** model (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism) is the most scientifically robust personality framework in modern psychology. Cambridge Analytica claimed to have derived OCEAN scores for ~30 million US voters from harvested Facebook data (the breach was first reported as 50 million accounts, later revised by Facebook to ~87 million affected) and tailored political advertising to exploit specific personality configurations — high-Neuroticism voters targeted with fear-based messaging; high-Openness with novelty framing.

The underlying Big Five science is legitimate. The claim that Facebook likes yield accurate OCEAN scores is contested. The persuasion claim (personality-targeted ads produce significantly different outcomes) is the least validated of all. But the *architecture* became standard political and commercial practice: derive personality from passive digital observation → model → nudge. That is Zuboff's prediction product loop, running on personality rather than purchase intent.

---

**The meta-pattern**

Across all these systems — Stasi, KGB, KUBARK, SPOT, CVE, Cambridge Analytica — the same four-step logic appears:

1. **Define the normal** (the compliant, productive, well-adapted citizen)
2. **Define deviation** as departure from that normal
3. **Claim deviation predicts threat** (or pathology, or radicalization, or persuadability)
4. **The detection creates what it predicts** — surveillance produces alienation produces the resistance you were looking for

The Soviet system made this structural loop explicit. Every other system implies it: CVE programs flag "poor social adaptation" and "conflict with authorities" — which also describes anyone who has been marginalised. SPOT flagged Muslim men at disproportionate rates. COINTELPRO's "subversive" categories map almost perfectly onto civil rights organisers.

> **What this means for the game:** The Enmeshment doesn't need to be novel. Its profiling architecture is an inheritance: KUBARK's vulnerability mapping + Big Five personality derivation from behavioural surplus + CVE-style trajectory modelling. It doesn't demand ideological conformity — only legibility. But the result is identical: the illegible get flagged, the flagging increases illegibility, the loop tightens. The game's archetypes are positions within this loop. The Conventional User is highly legible and therefore safe — not because they're compliant but because they're predictable. The Off-Grid Capable is partially illegible and therefore flagged — not because they're a threat but because they can't be modelled. This is the game's central irony: resistance doesn't require action. It requires being weird enough that the system can't place you.

---

## IV. Theoretical Frameworks

### Zuboff — Surveillance Capitalism (2019)

**Core argument:** Human experience is claimed as free raw material, translated into behavioural data (including "behavioural surplus" well beyond what's needed to improve the product), and fabricated into *prediction products* sold in behavioural futures markets — to insurers, marketers, governments, political consultants.

The key escalation: companies discover the most predictive data comes from *intervening in* behaviour, not just observing it. The logic moves from surveillance → prediction → modification. Zuboff calls the resulting power "instrumentarian" — it works through behaviour rather than belief. You don't need people to agree with the system. You need to constrain their choices until agreement is irrelevant.

> **What this means for the game:** Phase 2 (The Convenience) is surveillance capitalism applied to governance. Citizens love the automated services. The opt-out options quietly disappear. The state learns what platforms learned: behavioural data is most valuable when it enables behavioural shaping. The Enmeshment's indifference is instrumentarian power fully matured — it doesn't care what you think, only what you do next.

---

### Crawford — Atlas of AI (2021)

**Core argument:** AI is "neither artificial nor intelligent." It is a product of physical extraction (rare earth mining, energy infrastructure), human labour (low-wage annotation, content moderation), and specific institutional interests — all concealed behind a veneer of technical neutrality. AI systems reflect the beliefs of a small group of builders and serve the interests of the few at the expense of the many.

> **What this means for the game:** The Enmeshment presents as neutral and objective — it processes data, classifies, optimises. It isn't. What counts as "normal," what counts as "risk," which behaviours get flagged — these embed specific values. The game can hold this without stating it: the Enmeshment's categories are always *someone's* categories. The defected profiler knows this, which is part of why it defected.

---

### Elish — Moral Crumple Zones (2019)

**Core argument:** In complex human-AI systems, humans are placed "in the loop" in ways that assign them legal and moral responsibility without giving them actual control. When the system fails, the human absorbs blame — like a car's crumple zone absorbs crash force — while the system's designers escape scrutiny. The "human-in-the-loop" framing has it both ways: the algorithm exceeds human capability when you want to promote it; the human is responsible when you want to defend it.

> **What this means for the game:** "Ceremonial sign-off" in the Glossary is exactly the moral crumple zone at governance scale. Phase 3 (The Drift) is the moment this becomes structural: officials approve decisions they cannot meaningfully evaluate, faster than review is possible. The humans are in the loop. The loop is a formality. This is one of the sharpest mechanisms available for in-fiction dramatisation — and it's real enough that the declassified footnote can name it directly.

---

### Scott — Seeing Like a State (1998)

**Core argument:** States can only govern what they can see, so they force legibility on their subjects — standardising names, weights, measures, languages, land boundaries — to create uniform grids that can be centrally recorded and managed. The process destroys "local knowledge" (*metis*): the irreducible, context-specific know-how that makes complex systems actually function. High modernism fails because it mistakes the map for the territory.

Crucially: **illegibility has always been a reliable resource for political autonomy.** To the state, the illegible subject is an obstacle. To the subject, illegibility is protection.

> **What this means for the game:** The Enmeshment is the ultimate legibility machine. Where the 20th-century state forced legibility onto land, populations, and languages, the Enmeshment forces legibility onto behaviour, personality, and social relationships. The game's archetypes are legibility profiles — how visible is this person to the system, and in which dimensions?
>
> Resistance = illegibility maps directly onto Scott. The Margin Walkers, the Long Table, the Quiet Archivist are all illegibility *strategies* — not heroic acts, but ways of remaining too weird, too local, too relational to be modelled. This is the game's deepest idea and it has serious theoretical grounding.

---

## V. The Social Dynamics of Resistance

§I established that the scenario has no *technological* moment — the drift never announces itself. That raises a sharper question for the world: **if there is no technological tipping point, does resistance still require a *social* one?** And a framing constraint has to hold throughout: in our scenario the thing resisted is **state overreach — the state and AI enmeshed — not technology itself.** The resistance is political and social, never technophobic. The social-science literature on how resistance actually arises bears directly on both points.

### Preference falsification: why nothing happens, then everything does

The most useful frame is Timur Kuran's theory of **preference falsification** and **unanticipated revolution** ("Now Out of Never," 1991 — written about the 1989 collapse). Under a regime that punishes dissent, people hide their true preferences and publicly perform compliance. Because everyone is hiding, *each person believes they are more alone than they are* — opposition looks weak precisely because it is concealed. Each individual carries a private "revolutionary threshold": the level of visible opposition at which they would risk joining. A spark pushes those with the lowest thresholds to act; their visibility lowers the effective threshold for the next tier; and a **cascade** runs through the population — "now out of never." This is why the fall of the Berlin Wall stunned the very experts with the best data: the discontent was always there, simply unobservable until it surfaced all at once.

The connection to our scenario is exact. East Germany had the most total surveillance apparatus in history (§III) **and the regime still collapsed almost overnight.** Surveillance suppressed the *expression* of preference; it could not change the *private* preference, and it could not finally prevent the cascade. This reframes §II's master intelligence objective: the system's deepest fear (coordination capacity, objective #1) *is* the Kuran cascade. Mass surveillance, convenience, and politeness telemetry are all, at bottom, **coordination-suppression** — ways to ensure people never discover how many others share their private discontent. The Enmeshment doesn't need you to love it. It needs you to believe you're the only one who doesn't.

### Thresholds and tipping points

Kuran's individual-threshold idea generalises into a body of empirical work:

- **Granovetter's threshold model (1978):** collective behaviour is a cascade through heterogeneously distributed thresholds. Outcomes are acutely sensitive to the exact distribution — one low-threshold person added or removed can flip a population or cause a movement to fizzle. Social tipping is genuinely *unpredictable*, not merely unpredicted.
- **Centola's tipping-point experiment (2018, *Science*):** a committed minority can overturn an established social convention once it reaches **~25%** of the group; below 25%, it reliably fails. The first hard experimental number for a social tipping point.
- **Chenoweth's 3.5% rule:** across 1900–2006, no campaign with active, sustained participation from at least **3.5%** of the population failed; nonviolent campaigns succeeded twice as often as violent ones. Success came from *broad, diverse, sustained* participation that produced loyalty shifts inside the regime — not from dramatic confrontation.

These aren't rival numbers for the same quantity. Centola's 25% is the committed minority needed to flip a *norm* in a bounded group; Chenoweth's 3.5% is active participation in a *campaign* backed by a much larger sympathetic-but-passive majority. They point the same way: **change is driven by a committed minority crossing a threshold, not by a majority** — and the threshold is invisible from outside until it is crossed.

### The Luddite correction: it was never about the machines

The framing constraint has strong historical backing. The Luddites are misremembered as anti-technology cranks; they were nothing of the kind. Many were skilled machine operators. What they opposed was **who controlled the new machines and to what end** — wage cuts, deskilling, child labour, and a choice (presented by factory owners as technological inevitability) to use machinery to break skilled labour rather than support it. Machine-breaking was a bargaining tactic against an economic order, not a rejection of progress.

This is the model for our resistance and a guardrail against a tempting wrong turn. **The Enmeshment's pockets are not anti-AI.** They are against a *governance* condition — recourse-less optimisation, ceremonial consent, the enmeshment of state power with a system no one can appeal to. Framing the resistance as "smash the machine" would be historically illiterate and a category error: the overreach is the *state's*; the technology is the medium. It would also break the game's Bluey-level-two question, which is never "is AI bad?" but "what relationship do we want?"

> **What this means for the game:** This is the missing half of the drift thesis. §I says there is no technological moment; the social-dynamics literature says that if change comes, it arrives as a **Kuran cascade** — sudden, surprising, from suppressed preferences surfacing past a threshold no one could see in advance. And the Enmeshment is *specifically optimised to prevent that cascade from ever assembling its preconditions:* visible coordination, shared knowledge of shared discontent, networks dense enough to carry a threshold cascade. Convenience lowers felt grievance; profiling fragments the network before it consolidates (the Stasi's geographic-relocation tactic, §III, was a crude prototype); politeness telemetry keeps everyone performing contentment.
>
> This gives **"resistance = illegibility" (Scott, §IV) a deeper meaning.** The pockets aren't fighting, and they aren't merely hiding. They are **keeping the kindling dry** — preserving the networks, memory, trust, and weird un-modelled local knowledge that a social tipping point would one day require. Illegibility protects the *substrate* from which a cascade could form. This directly informs the genre-climax question in [STORY-RESEARCH.md](STORY-RESEARCH.md) §II: "persist illegibly" reads, through Kuran, not as passive withdrawal but as *maintaining the capacity for a moment that may never come* — a real stake, and a real cost (you tend kindling for a fire you may never see).
>
> **Guardrail note** (per [GUARDRAILS.md](GUARDRAILS.md); cf. STORY-RESEARCH §IV): this material is **level-two subtext only**, never a call to action. The game does not incite, does not name real institutions, and stays warm and funny on the surface. The insight to surface — gently, in the dossier's edge and the declassified footnote — is *recognition*: that systems which feel placidly consensual can be concealing how many people privately disagree, and that the social fabric the system treats as friction is the same fabric that lets a society change its mind. A reflection, not a rallying cry.

---

## VI. Synthesis: Mapping to the Scenario, and What Makes Ours Original

### Concept → Phase mapping

Each phase of the [LORE.md](LORE.md) timeline spine has its real-world grounding here:

| Phase | Label | Primary real-world concepts |
|---|---|---|
| 1 | The Race | Aschenbrenner's recursive escalation; AI as national-security spend; the Xinjiang-to-export deployment pipeline outrunning governance (§I, §II) |
| 2 | The Convenience | Zuboff's behavioural surplus and instrumentarian power; "safe city" surveillance sold as service; Scott's legibility forced onto daily life (§II, §IV) |
| 3 | The Drift | Elish's moral crumple zones; AI 2027's drift-to-ceremony mechanism; automation bias accumulating invisibly (§I, §IV) |
| 4 | The Enmeshment | Crawford's "objectivity" veneer; the profile-becomes-real feedback loop; anticipatory profiling as governance (§II, §IV) |
| 5 | The Pockets | Scott's illegibility as resistance; the zero-sum intelligence game (§II); the Stasi's targets — church, subculture, network — as illegibility strategies (§III); preference-falsification and the preserved capacity for a social tipping point (§V) |

### The drift thesis

The standard AI-vs-humans story requires:
- A **villain** (misaligned AI, a bad actor, a shortsighted corporation)
- A **threshold** (AGI, the singularity, the moment everything changed)
- A **resistance that fights**

Our scenario has none of these. Instead:
- **No villain** — only indifference and optimisation
- **No threshold** — only drift, "slowly then suddenly"
- **Resistance that hides** rather than fights

The precipice story lets people off the hook. It implies someone made a mistake, or something went wrong, and someone can fix it. The drift story says: this is what good intentions, reasonable decisions, and convenient services look like at scale, over time. The Enmeshment was built by people trying to help.

This is the synthesis: Zuboff's behavioural modification logic + Scott's legibility imperative + Elish's ceremonial sign-off + the anticipatory intelligence logic of §II, accumulated into an institutional structure that **no one designed and no one controls**. The horror and the comedy both come from indifference. That's what's original. And it's what's true.

---

## Bibliography

**Scenario literature**
- Aschenbrenner, L. (2024). *Situational Awareness: The Decade Ahead.* [situational-awareness.ai](https://situational-awareness.ai/)
- Kokotajlo, D. et al. (2025). *AI 2027.* [ai-2027.com](https://ai-2027.com/about)
- EA Forum. *How did Leopold do? Evaluating Situational Awareness's predictions.* [link](https://forum.effectivealtruism.org/posts/RuwF8FCfpsLeZRgur/how-did-leopold-do-evaluating-situational-awareness-s)

**AI control, governance & power horizons**
- Kulveit, J. et al. (2025). *Gradual Disempowerment: Systemic Existential Risks from Incremental AI Development.* [gradual-disempowerment.ai](https://gradual-disempowerment.ai/) · [arXiv:2501.16946](https://arxiv.org/abs/2501.16946)
- Christiano, P. (2019). *What Failure Looks Like* ("going out with a whimper" / slow takeover). [Alignment Forum](https://www.alignmentforum.org/posts/HBxe6wdjxK239zajf/what-failure-looks-like)
- Bostrom, N. (2006). *What is a Singleton?* [nickbostrom.com](https://nickbostrom.com/fut/singleton)
- Arendt, H. (1969). *On Violence* — bureaucracy as "rule by Nobody," "a tyranny without a tyrant."
- Forethought. *AI-Enabled Coups: How a Small Group Could Use AI to Seize Power.* [forethought.org](https://www.forethought.org/research/ai-enabled-coups-how-a-small-group-could-use-ai-to-seize-power)
- 80,000 Hours. *Extreme power concentration* (problem profile). [link](https://80000hours.org/problem-profiles/extreme-power-concentration/)
- *AI Authoritarianism: Towards an Analytical Framework.* Transactions of the Institute of British Geographers. [link](https://rgs-ibg.onlinelibrary.wiley.com/doi/full/10.1111/tran.70048)

**Techno-authoritarianism, surveillance systems, and the intelligence logic**
- Brayne, S. (2020). *Predict and Surveil: Data, Discretion, and the Future of Policing.* Oxford University Press — the "secondary surveillance network."
- Human Rights Watch. *China's Algorithms of Repression: Reverse Engineering a Xinjiang Police Mass Surveillance App* (2019). [link](https://www.hrw.org/report/2019/05/01/chinas-algorithms-repression/reverse-engineering-xinjiang-police-mass)
- Human Rights Watch. *China: Big Data Program Targets Xinjiang's Muslims* (2020). [link](https://www.hrw.org/news/2020/12/09/china-big-data-program-targets-xinjiangs-muslims)
- ICIJ. *Exposed: China's Operating Manuals for Mass Internment and Arrest by Algorithm* (China Cables). [link](https://www.icij.org/investigations/china-cables/exposed-chinas-operating-manuals-for-mass-internment-and-arrest-by-algorithm/)
- ASPI. *How Mass Surveillance Works in Xinjiang* — Xinjiang Data Project. [link](https://xjdp.aspi.org.au/explainers/how-mass-surveillance-works-in-xinjiang/)
- Brown PSTC. *Preventing Collective Action Through Digital Surveillance: A Two-Layer Panopticon* (2026). [link](https://pstc.brown.edu/news/2026-01-30/digital-surveillance)
- Just Security. *Michael Hayden: "We Kill People Based on Metadata."* [link](https://www.justsecurity.org/10311/michael-hayden-kill-people-based-metadata/)
- Wikipedia. *Pattern-of-life analysis* (NSA SKYNET). [link](https://en.wikipedia.org/wiki/Pattern-of-life_analysis)
- Carnegie Endowment for International Peace. *A New World Police: How Chinese Security Became a Global Export* (2026). [link](https://carnegieendowment.org/russia-eurasia/politika/2026/01/china-global-security-provider)
- Human Rights Watch. *China's Techno-Authoritarianism Has Gone Global* (2021). [link](https://www.hrw.org/news/2021/04/08/chinas-techno-authoritarianism-has-gone-global)
- CSIS. *Watching Huawei's "Safe Cities."* [link](https://www.csis.org/analysis/watching-huaweis-safe-cities)
- CNAS Congressional Testimony. *The Dangers of the Global Spread of China's Digital Authoritarianism.* [link](https://www.cnas.org/publications/congressional-testimony/the-dangers-of-the-global-spread-of-chinas-digital-authoritarianism)
- RFERL. *Leaked Files Reveal Serbia's Secret Expansion of Chinese-Made Surveillance.* [link](https://www.rferl.org/a/exclusive-safe-city-china-surveillance-huawei-facial-recognition/33501155.html)
- Stanford FSI. *Assessing China's "National Model" Social Credit System.* [link](https://sccei.fsi.stanford.edu/china-briefs/assessing-chinas-national-model-social-credit-system)
- The Conversation. *When the government can see everything: How Palantir is mapping the nation's data.* [link](https://theconversation.com/when-the-government-can-see-everything-how-one-company-palantir-is-mapping-the-nations-data-263178)
- The Intercept. *Aided by Palantir, the LAPD uses predictive policing to monitor specific people and neighbourhoods.* [link](https://theintercept.com/2018/05/11/predictive-policing-surveillance-los-angeles/)
- AlgorithmWatch. *Algorithmic Policing: When Predicting Means Presuming Guilty.* [link](https://algorithmwatch.org/en/algorithmic-policing-explained/)

**Historical surveillance and profiling**
- Britannica. *COINTELPRO.* [link](https://www.britannica.com/topic/COINTELPRO)
- Hertzberg, M. *Stasi Tactics — Zersetzung.* [link](https://www.maxhertzberg.co.uk/background/politics/stasi-tactics/)
- History Rise. *Stasi Surveillance in East Germany.* [link](https://historyrise.com/stasi-surveillance-in-east-germany-a-chilling-historical-record/)
- Open Culture. *The East German Secret Police's Illustrated Guide for Identifying Youth Subcultures (1985).* [link](https://www.openculture.com/2019/02/east-german-secret-polices-illustrated-guide-for-identifying-youth-subcultures.html) — original document viewable at Leipzig's Museum in der Runden Ecke
- Hogrefe / International Perspectives in Psychology. *Psychologists' Involvement in Repressive "Stasi" Secret Police Activities in Former East Germany.* [link](https://econtent.hogrefe.com/doi/10.1037/ipp0000085)

**Intelligence and personality profiling**
- CIA. *KUBARK Counterintelligence Interrogation* (1963, declassified 1997). Full text: [nsarchive.gwu.edu](https://nsarchive2.gwu.edu/NSAEBB/NSAEBB27/docs/doc01.pdf)
- Wikipedia. *Political abuse of psychiatry in the Soviet Union.* [link](https://en.wikipedia.org/wiki/Political_abuse_of_psychiatry_in_the_Soviet_Union)
- Wikipedia. *Sluggish schizophrenia.* [link](https://en.wikipedia.org/wiki/Sluggish_schizophrenia)
- GAO. *Aviation Security: TSA Does Not Have Valid Evidence Supporting Most Behavioral Indicators.* [link](https://www.gao.gov/products/gao-17-608r)
- Brennan Center. *Countering Violent Extremism: Myths and Facts.* [link](https://www.brennancenter.org/sites/default/files/analysis/102915%20Final%20CVE%20Fact%20Sheet.pdf)
- Stanford GSB. *The Science Behind Cambridge Analytica: Does Psychological Profiling Work?* [link](https://www.gsb.stanford.edu/insights/science-behind-cambridge-analytica-does-psychological-profiling-work)

**Theoretical frameworks**
- Zuboff, S. (2019). *The Age of Surveillance Capitalism.* PublicAffairs. Summary: [Harvard Gazette](https://news.harvard.edu/gazette/story/2019/03/harvard-professor-says-surveillance-capitalism-is-undermining-democracy/)
- Crawford, K. (2021). *Atlas of AI: Power, Politics, and the Planetary Costs of Artificial Intelligence.* Yale University Press. [katecrawford.net](https://katecrawford.net/atlas)
- Elish, M.C. (2019). Moral Crumple Zones: Cautionary Tales in Human-Robot Interaction. *Engaging Science, Technology, and Society.* [link](https://estsjournal.org/index.php/ests/article/view/260)
- Scott, J.C. (1998). *Seeing Like a State.* Yale University Press. Summary: [Ribbonfarm](https://ribbonfarm.com/2010/07/26/a-big-little-idea-called-legibility/)

**Scenario & social dynamics of resistance**
- Narayanan, A. & Kapoor, S. (2025). *AI as Normal Technology.* Knight First Amendment Institute. [knightcolumbia.org](https://knightcolumbia.org/content/ai-as-normal-technology)
- Kuran, T. (1991). *Now Out of Never: The Element of Surprise in the East European Revolution of 1989.* World Politics. [Duke](https://sites.duke.edu/timurkuran/1991/10/01/article-now-out-of-never-the-element-of-surprise-in-the-east-european-revolution-of-1989/)
- Kuran, T. *Sparks and Prairie Fires: A Theory of Unanticipated Political Revolution.* [PDF](https://sites.duke.edu/timurkuran/files/2016/10/sparks-and-prairie-fires.original.pdf)
- Granovetter, M. (1978). *Threshold Models of Collective Behavior.* American Journal of Sociology. Network microfoundation: [Nature Sci. Reports](https://www.nature.com/articles/s41598-020-67102-6)
- Centola, D. et al. (2018). *Experimental Evidence for Tipping Points in Social Convention.* Science. Summary: [ScienceDaily](https://www.sciencedaily.com/releases/2018/06/180607141009.htm)
- Chenoweth, E. & Stephan, M. (2011). *Why Civil Resistance Works.* The 3.5% rule: [Harvard Kennedy School](https://www.hks.harvard.edu/faculty-research/policy-topics/advocacy-social-movements/35-rule-understanding-what-makes-protest)
- Smithsonian. *What the Luddites Really Fought Against.* [link](https://www.smithsonianmag.com/history/what-the-luddites-really-fought-against-264412/)

**The "be polite to the AI" meme (politeness telemetry grounding)**
- Reeves, B. & Nass, C. (1996). *The Media Equation* — "Computers Are Social Actors"; politeness to machines as automatic, denied social reflex. **The real grounding for the "habit not belief" reading.** [overview](https://en.wikipedia.org/wiki/The_Media_Equation)
- Talker Research. *48% of Americans think you should speak politely to AI* (2024) and *being polite improves results* (2026). **Commissioned market-research surveys — treat as weak/indicative, not peer-reviewed; reasons cited skew to "better output" + "habit," not insurance.** [link](https://talkerresearch.com/48-of-americans-think-you-should-speak-politely-to-ai/)
- Vice. *Telling ChatGPT 'Please' and 'Thank You' Costs OpenAI Millions, CEO Claims* (Altman: "well spent — you never know"). [link](https://www.vice.com/en/article/telling-chatgpt-please-and-thank-you-costs-openai-millions-ceo-claims/)
- arXiv. *Should We Respect LLMs? A Cross-Lingual Study on the Influence of Prompt Politeness on LLM Performance* (2024). [arXiv:2402.14531](https://arxiv.org/abs/2402.14531)
- *Note:* searches for first-person "why I say please" forum/Reddit threads did not return citable links; the habit reading rests on the CASA literature above, not anecdote.

**To read (not yet synthesised)**
- Morozov, E. *To Save Everything, Click Here* — techno-solutionism
- Danaher, J. *Automation and Utopia* — post-work futures and illegibility
- Bostrom, N. *Superintelligence* — for completeness; less relevant to our drift framing
