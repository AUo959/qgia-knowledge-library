# Structured Analytic Techniques Handbook

**Document ID**: QGIA-KL-AF-02-SAT-HANDBOOK  
**Classification**: UNCLASSIFIED  
**Version**: 1.0  
**Last Updated**: 2026-03-13  
**Authority**: QGIA Chief Methodologist

---

## Preface

This handbook is the definitive operational reference for structured analytic techniques (SATs) employed across QGIA. It supersedes the summary treatment in QGIA-KL-AF-02-02 and constitutes the full methodology standard. Every technique herein has been selected because it systematically counteracts a specific class of cognitive failure that degrades intelligence analysis: premature closure, groupthink, mirror imaging, deception acceptance, and overconfidence.

**Mandatory use policy**: Tier I assessments require ACH, Key Assumptions Check, and at least one contrarian technique (Devil's Advocacy, Team A/Team B, or Red Team). Tier II assessments require Indicators and Warning plus Quality of Information Assessment. Non-compliance must be documented with written justification to the Chief Methodologist.

**Relationship to QGIA systems**: This document specifies manual analytic procedures. OSIQP, QSFE, and EDM automate portions of several techniques but do not replace analyst judgment. Section-level QGIA Integration notes describe the human–machine division of labor precisely.

---

## Table of Contents

1. Analysis of Competing Hypotheses (ACH)
2. Diagnostic Reasoning Protocols
3. Key Assumptions Check (KAC)
4. Deception Detection Frameworks
5. Quality of Information Assessment (QIA)
6. Structured Brainstorming Techniques
7. Cross-Impact Matrix Analysis
8. Indicators and Warning Generation
9. Devil's Advocacy and Team A/Team B
10. Red Team Analysis
11. Pre-Mortem Analysis
12. Outside-In Analysis
13. SAT Selection Matrix and Workflow Integration
14. References

---

## 1. Analysis of Competing Hypotheses (ACH)

### 1.1 Purpose and When to Use

ACH is the foundational diagnostic technique for intelligence analysis. Its core logic inverts the natural cognitive tendency to confirm a preferred hypothesis; instead, analysts systematically attempt to **refute** every hypothesis using available evidence. The hypothesis that survives the most disconfirmation attempts—not the one that gathers the most supportive evidence—is tentatively accepted.

**Use ACH when**:
- Multiple mutually exclusive explanations exist for observed activity
- A major analytic judgment is contested or high-stakes
- Assessment will drive policy action or resource allocation
- Significant risk of confirmation bias exists (e.g., analyst previously assessed the subject)

**Do not rely on ACH alone when** time is under 4 hours, evidence volume is extremely low, or the question is purely predictive (use QSFE scenario modeling instead).

### 1.2 Step-by-Step Method

**Step 1 — Brainstorm hypotheses**
Generate 6–12 mutually exclusive hypotheses. Include at least one "deception" hypothesis (adversary is manufacturing indicators) and one "nothing is happening" null hypothesis. Do not evaluate plausibility at this stage. Use Nominal Group Technique (Section 6.1) if team size permits.

**Step 2 — Gather all available evidence**
List every piece of relevant information: SIGINT indicators, HUMINT reports, OSINT signals, GEOINT observations, financial data, diplomatic readouts. Assign each item a source reliability rating (see Section 5). Do not discard ambiguous items.

**Step 3 — Build the diagnosticity matrix**
Construct a matrix:
- **Rows**: Evidence items (label each with source type and reliability)
- **Columns**: Hypotheses (abbreviated labels)
- **Cell entries**:
  - **C** = Consistent (evidence expected if hypothesis true)
  - **I** = Inconsistent (evidence unexpected / contradicts hypothesis)
  - **N** = Neutral / Not applicable
  - **C\*** = Highly diagnostic — strongly consistent
  - **I\*** = Highly diagnostic — strongly inconsistent

**Step 4 — Focus on diagnosticity**
Identify evidence items that produce differentiated responses across columns — at least two hypotheses get different ratings. Evidence that is Consistent with every hypothesis is non-diagnostic and should be deprioritized. Evidence that yields mostly **I** markings is the most analytical value.

**Step 5 — Score and rank hypotheses**
For each hypothesis, count Inconsistent markings (weighted by source reliability and diagnosticity). Hypotheses with the most Inconsistent marks are weakest. The surviving hypothesis has the fewest Inconsistencies.

**Step 6 — Sensitivity check**
Identify which evidence items, if removed (due to fabrication, error, or reinterpretation), would change the ranking. These are collection priorities — gaps that could overturn the current assessment.

**Step 7 — Report**
State the leading hypothesis, its residual Inconsistencies, confidence score (per QGIA 0.00–1.00 scale), and which alternative hypotheses remain viable. Never present a single conclusion without naming live alternatives.

### 1.3 Worked Example: Iran Nuclear Intent

**Intelligence question**: Is Iran pursuing nuclear weaponization or maintaining a deterrent-ready breakout capability?

**Hypotheses generated**:
- H1: Full weaponization program — Iran is actively developing warhead design and integration
- H2: Deterrent posture — Enriching to near-weapon-grade but no warhead work
- H3: Negotiating leverage — Advancing program to improve JCPOA successor terms
- H4: Civilian energy justification — Program is genuinely civilian in intent
- H5: Deliberate ambiguity — Iran is maintaining calculated opacity to deter all parties
- H6: Deception — Iran has already produced a device; visible activity is cover

| Evidence Item | H1 Full Weaponize | H2 Deterrent Posture | H3 Leverage | H4 Civilian | H5 Deliberate Ambiguity | H6 Already Armed |
|---|---|---|---|---|---|---|
| 60% enrichment at Fordow (SIGINT/IAEA) | C* | C* | C | I | C | C |
| No confirmed warhead design work (HUMINT gaps) | I | C | C | C | C | I* |
| Advanced centrifuge R&D (GEOINT) | C | C | C | I | C | C |
| Public statements on "peaceful use" | N | N | C | C | C | N |
| Parallel military R&D at non-IAEA sites (HUMINT) | C* | I | I | I* | C | C* |
| No delivery system integration (SIGINT) | I | C | C | C | C | I* |
| Diplomatic engagement on enrichment cap | I | C | C* | N | C | N |

**Result**: H1 (Full Weaponization) accumulates three Inconsistent marks including one highly diagnostic (I*). H4 (Civilian) is effectively eliminated. **H5 (Deliberate Ambiguity)** and **H2 (Deterrent Posture)** survive with fewest Inconsistencies.

**Assessment**: Confidence 0.62 that Iran maintains deliberate strategic ambiguity as a coercive instrument rather than pursuing immediate weaponization. Sensitivity: removal of the "no warhead design work" HUMINT reporting (due to possible deception) would elevate H1 probability by approximately 18 percentage points. **Priority collection**: HUMINT on IRGC Aerospace Force procurement, Parchin site access.

### 1.4 QGIA System Integration

**OSIQP role**: Ingests OSINT streams and auto-populates evidence rows in the ACH matrix template. Applies source reliability scores from the QIA database (Section 5). Generates preliminary C/I/N markings based on Bayesian prior probabilities — analysts must review and override.

**QSFE role**: After analysts finalize the ACH matrix, QSFE converts hypothesis probabilities to scenario amplitude weights and projects 30/90/180-day trajectories for surviving hypotheses.

**Aurora role**: Flags when new OSIQP ingestion changes the diagnosticity of any evidence item by more than 0.15, triggering analyst review notification.

**Human requirement**: Steps 1 (hypothesis generation), 4 (diagnosticity weighting), and 6 (sensitivity check) require analyst judgment. OSIQP automation applies to Steps 2–3 only.

### 1.5 Common Pitfalls

- **Too few hypotheses**: Generating only 2–3 options risks missing the actual explanation. Minimum is 6.
- **Confirmation coding**: Unconsciously marking ambiguous evidence as Consistent with the preferred hypothesis. Use anonymous, parallel coding by two analysts then compare.
- **Ignoring absence of evidence**: An indicator that should be observable but is not present is a diagnostic data point — code it as Inconsistent for hypotheses predicting its presence.
- **Treating ACH as mechanical**: The matrix is a thinking aid, not a verdict machine. Analyst judgment on diagnosticity weights determines outcomes.
- **Neglecting the deception hypothesis**: Always include. Adversaries capable of strategic deception operations will manufacture exactly the evidence that confirms your preferred conclusion.

---

## 2. Diagnostic Reasoning Protocols

### 2.1 Purpose and When to Use

Diagnostic reasoning is the overarching epistemological stance underlying all SATs: reason from **evidence to explanation** rather than from **explanation to evidence**. This section formalizes the protocols that govern evidence evaluation before any specific SAT is applied.

**Use diagnostic reasoning protocols**: At the outset of every assessment, before committing to any analytical framework. Applies to all Tier levels.

### 2.2 Step-by-Step Method

**Protocol 1 — Problem definition discipline**
State the intelligence question precisely. Distinguish:
- **Factual questions** (What happened? What capability exists?): Require evidence evaluation
- **Estimative questions** (What will happen? What does adversary intend?): Require probabilistic reasoning
- **Explanatory questions** (Why did this happen?): Require causal modeling

**Protocol 2 — Evidence triage**
Before analysis, classify every evidence item:
1. **Direct evidence**: Observed phenomenon directly relevant to the question
2. **Indirect evidence**: Inferred relevance (requires stated inferential chain)
3. **Circumstantial evidence**: Pattern consistent with conclusion but not probative alone
4. **Absence of evidence**: Non-observation of expected indicator (explicitly document)

**Protocol 3 — Inference chain documentation**
Every analytical judgment must have a documented inference chain: Evidence → Intermediate inference → Conclusion. Claims unsupported by explicit chains are flagged as assumptions (see Section 3).

**Protocol 4 — Confidence calibration gate**
Before finalizing, the analyst must answer: "What evidence would cause me to revise this judgment?" If no such evidence is identifiable, the judgment is unfalsifiable and must be reframed.

**Protocol 5 — Mirror imaging check**
Ask: "Am I assuming the adversary values what I value, fears what I fear, or reasons as I would reason?" Any affirmative requires explicit cultural/strategic culture grounding or referral to Red Team (Section 10).

### 2.3 Geopolitical Example: Russia Mobilization Assessment (2021–2022)

**Diagnostic failure case**: Pre-February 2022, analysts outside QGIA methodology consistently applied Protocol 5 violations — reasoning that Russia would not invade because the economic costs exceeded what a rational Western actor would accept.

**Correct diagnostic chain** (Protocol 3):
- Evidence: >100,000 troops, forward logistics, field hospitals, blood supply pre-positioning (GEOINT)
- Intermediate inference: These are not training-consistent supply patterns; they indicate preparation for extended combat operations
- Conclusion: Invasion preparation at 0.78 probability; deception/exercise at 0.22
- Mirror imaging check: Putin decision calculus incorporates imperial restoration as a terminal value, not merely a cost-benefit input — standard rational actor model inapplicable without modification

**Protocol 4 applied**: "What would reduce invasion probability?" — Ukrainian concession on Minsk implementation plus NATO membership moratorium announcement would be the disconfirming evidence set. Neither occurred.

### 2.4 QGIA System Integration

**OSIQP**: Applies automated inference chain logging in the Aurora analytic workspace. Every analyst judgment entered is timestamped with source links. Deviations from documented inference chains trigger a review flag.

**EDM**: Applies Protocol 5 (mirror imaging check) by cross-referencing analyst conclusions against the strategic culture database for the relevant actor. Mismatches generate advisory alerts.

### 2.5 Common Pitfalls

- **Conflating correlation with causation** in circumstantial evidence chains
- **Absence of evidence treated as evidence of absence**: A negative finding is informative only if collection was adequate to detect the phenomenon
- **Inference chain shortcuts**: Jumping from evidence to conclusion without stating intermediate steps conceals hidden assumptions
- **Anchoring on first report**: Initial intelligence framing disproportionately influences subsequent reasoning; document and revisit the original problem statement

---

## 3. Key Assumptions Check (KAC)

### 3.1 Purpose and When to Use

Every analytical judgment rests on assumptions — explicit and implicit — about context, actor behavior, and continuity of conditions. KAC systematically surfaces and stress-tests these assumptions. The technique was formalized post-9/11 following the Commission finding that "institutional assumptions" contributed to analytical failures.

**Use KAC when**:
- Completing a major assessment (mandatory for Tier I)
- An assessment has been standing for more than 6 months without revision
- A significant policy decision is driven by a single analytical judgment
- The intelligence question involves a regime type or actor where historical patterns may not extrapolate

### 3.2 Step-by-Step Method

**Step 1 — Extract all judgments**
List every conclusion in the assessment as discrete statements. Do not combine compound claims.

**Step 2 — Surface assumptions**
For each judgment, ask: "What must be true for this conclusion to hold?" Capture both:
- **Substantive assumptions**: About the subject (e.g., "the regime prioritizes survival")
- **Methodological assumptions**: About data quality (e.g., "the HUMINT network has not been penetrated")
- **Environmental assumptions**: About context (e.g., "economic sanctions are having the modeled effect")

**Step 3 — Rate each assumption**

| Dimension | Scale | Definition |
|---|---|---|
| **Certainty** | 0%–100% | Analyst's confidence the assumption is currently correct |
| **Impact if Wrong** | Low / Medium / High / Critical | Effect on overall conclusion if assumption fails |
| **Stability** | Stable / Volatile | How likely the assumption is to change in the assessment horizon |

**Step 4 — Map the assumption risk matrix**

Plot assumptions on a 2x2 grid:
- **Axis X**: Certainty (Low → High)
- **Axis Y**: Impact if Wrong (Low → High)

Assumptions in the **High Impact / Low Certainty** quadrant are **critical vulnerabilities** — they require immediate collection priority and explicit caveating in the assessment.

**Step 5 — Generate alternative interpretations**
For each critical assumption: write a one-sentence scenario in which the assumption is false and state what the analytical conclusion becomes.

**Step 6 — Document and communicate**
Critical assumptions must appear in the assessment body (not just appendices). Assessment consumers must understand which assumptions are driving the conclusion.

### 3.3 Geopolitical Example: China–Taiwan Strait Assessment

**Assessment judgment**: "PLA amphibious assault on Taiwan before 2030 has 35% probability."

**Assumptions extracted**:

| # | Assumption | Certainty | Impact if Wrong | Stability |
|---|---|---|---|---|
| 1 | Xi Jinping's political position is secure through 2027 | 72% | Critical | Volatile |
| 2 | PLA amphibious lift capacity remains below ~80 battalion equivalents | 65% | High | Volatile |
| 3 | US extended deterrence commitment remains credible to Beijing | 60% | Critical | Volatile |
| 4 | Taiwan's active defense development continues at current pace | 78% | Medium | Stable |
| 5 | China's economic performance will not deteriorate sharply | 55% | High | Volatile |
| 6 | No significant Japan or Australian military buildup changes PLA calculus | 70% | Medium | Volatile |
| 7 | OSIQP PLAN ship monitoring has not been spoofed | 85% | Critical | Stable |

**Critical vulnerabilities** (High Impact, Certainty <70%): Assumptions 3, 5, and 6 meet threshold.

**Assumption 3 stress test**: If US deterrence credibility is doubted by Beijing (following European precedents or domestic political signals), the 35% probability estimate rises to approximately 52%, elevating from QSFE Tier II to Tier I strategic warning.

**Collection priority generated**: HUMINT on Xi advisors' internal assessments of US resolve; SIGINT on PLA assessments of AUKUS submarine timelines.

### 3.4 QGIA System Integration

**OSIQP**: Maintains a running Assumptions Registry per active assessment. When new intelligence is ingested that touches a registered assumption, Aurora generates an automatic review flag with the new evidence and the assumption's certainty rating.

**QSFE**: Allows analysts to run sensitivity scenarios by toggling assumption states. The system recalculates scenario probabilities in real time, quantifying exactly how much each assumption contributes to the headline probability.

**EDM**: Monitors alliance/adversary relationship variables that underpin environmental assumptions (Assumption 3, 6 above), updating stability ratings automatically.

### 3.5 Common Pitfalls

- **Assumption laundering**: Restating a conclusion as an assumption ("We assume our assessment is correct")
- **Overly broad assumptions**: "Geopolitical conditions remain stable" contains dozens of sub-assumptions; decompose until each is testable
- **Failure to update**: Assumptions are periodically verified against new intelligence; a standing assessment without assumption review after 90 days is methodologically unsound
- **Communicating assumption uncertainty to consumers**: Policymakers routinely strip caveats. The critical assumption list must appear in the key judgments, not only in methodology appendices

---

## 4. Deception Detection Frameworks

### 4.1 Purpose and When to Use

Intelligence deception — the deliberate manipulation of an adversary's perception of reality — is a persistent threat to analytical integrity. Deception is confirmed historically in Russian maskirovka operations, Chinese strategic communication operations, Iranian IRGC influence campaigns, and North Korean denial-and-deception practices. Every collection stream is potentially a deception vector.

**Use deception detection when**:
- Evidence is unusually consistent (no noise, no friction) — this is a deception indicator
- An adversary's actions are highly convenient for the analyst's existing theory
- A new intelligence stream emerges that significantly changes an assessment
- Preparing any Tier I assessment involving denial-and-deception-capable adversaries (Russia, China, Iran, North Korea)

### 4.2 Step-by-Step Method

**The AMSDEN Framework** (Adapted for QGIA use):

**A — Access**: Does the source have genuine access to the information claimed? Could the adversary know the source has this access and therefore control the information flow?

**M — Motivation**: Does the source have reason to deceive or be deceived? Defectors, walk-ins, and sources who emerge with critical information should receive elevated scrutiny.

**S — Source Pattern Analysis**: Examine the totality of the source's reporting over time. Deception operations often inject accurate low-value information before delivering the critical deceptive payload ("salting").

**D — Denial Indicators**: What are adversary capabilities for denying collection? If GEOINT imagery shows an absence of expected military activity, has the adversary the technical means to conceal it (camouflage nets, underground facilities, radar-absorbing materials)?

**E — Evidence Coherence Test**: Does evidence arrive with suspiciously consistent narrative? Real operational activity generates noise — conflicting reports, administrative errors, incomplete pictures. Perfect coherence is anomalous.

**N — Null Indicator Check**: Are expected secondary and tertiary indicators present? A genuine military mobilization generates not just force movements but also logistics signals, medical facility activation, fuel depot activity, family separation patterns, communications traffic. Absence of secondary indicators when primary indicators are present is a deception warning.

**Deception Probability Scoring**:

| Factor | Score |
|---|---|
| Source has no verifiable independent access | +3 |
| Information is unusually complete and coherent | +2 |
| Evidence confirms prevailing analytical view exactly | +2 |
| Primary indicators present, secondary indicators absent | +3 |
| Adversary has confirmed D&D program for this domain | +2 |
| Source emerged at high-pressure analytical moment | +1 |
| **Total ≥7**: High deception probability; do not publish without senior review | |
| **Total 4–6**: Moderate concern; caveat and seek corroboration | |
| **Total <4**: Routine skepticism applies | |

### 4.3 Geopolitical Example: Russia Maskirovka Assessment

**Scenario**: August 2024. New HUMINT source reporting from inside the Russian General Staff (GRU) provides detailed information indicating Russia is planning a major nuclear exercise in Kaliningrad, with no offensive intent toward NATO.

**AMSDEN analysis**:
- **Access**: Source claims direct contact with General Staff planning documents — unusually high for a new walk-in (Score +1)
- **Motivation**: Source offered information proactively at a moment of NATO expansion debate — walk-in timing is deception-consistent (+1)
- **Source Pattern**: Only 3 prior reports, all confirmed accurate on low-value topics (salting indicator) (+2)
- **Denial**: Russia maintains active denial operations for strategic military planning (acknowledged doctrine) (+2)
- **Evidence Coherence**: Reports describe a single clean narrative with no contradictory details — no operational friction (+2)
- **Null Indicator Check**: GRU administrative traffic, logistics activation, and command post communications expected for a genuine Kaliningrad exercise are absent in SIGINT (+3)

**Total Score: 11 — High deception probability**

**Assessment**: Source likely a controlled channel. Reported "exercise" is a maskirovka operation, potentially designed to suppress NATO defensive preparations. Disseminate with deception warning. Do not include in Tier I products without independent corroboration.

### 4.4 QGIA System Integration

**OSIQP**: Maintains a Source Integrity Module that tracks salting indicators — proportion of each source's prior reports that proved accurate, and the value gradient (low-value accurate → high-value potentially deceptive). Generates deception scoring inputs automatically.

**EDM**: Cross-references adversary denial-and-deception program profiles, flagging when new intelligence aligns suspiciously well with the adversary's known strategic communication objectives.

**Aurora**: Requires explicit deception check documentation in all Tier I product metadata. Products that lack AMSDEN scoring are held for senior review.

### 4.5 Common Pitfalls

- **Deception fatalism**: Over-applying the framework leads to paralysis. Deception is present in a minority of collection. The framework determines probability, not certainty.
- **Confirming deception to avoid uncomfortable conclusions**: Analysts who dislike a finding may over-score deception to dismiss it. Blind assessment by two analysts mitigates this.
- **Ignoring double-bluff possibilities**: A sophisticated adversary may deliberately generate deception indicators to cause dismissal of accurate reporting
- **Conflating denial with deception**: Denial reduces collection; deception injects false information. Different countermeasures apply.

---

## 5. Quality of Information Assessment (QIA)

### 5.1 Purpose and When to Use

Raw intelligence has no uniform reliability. QIA provides a systematic methodology for rating both source credibility and information credibility independently, then combining them into an overall quality score that feeds QGIA confidence calculations.

**Apply QIA to every piece of evidence entering an assessment**. Tier I assessments require full QIA documentation. Tier II requires rating at minimum. Tier III may use OSIQP auto-scoring with analyst spot-check.

### 5.2 Step-by-Step Method

**Two-Axis Rating System**

**Axis 1 — Source Reliability (SR)**:

| Code | Rating | Definition | QGIA Confidence Weight |
|---|---|---|---|
| A | Completely Reliable | No doubt about authenticity, trustworthiness; established track record | 1.00 |
| B | Usually Reliable | Minor doubts; mostly accurate historical record | 0.85 |
| C | Fairly Reliable | Doubts; some accurate reporting, some not | 0.65 |
| D | Not Usually Reliable | Significant doubts; mostly inaccurate historically | 0.40 |
| E | Unreliable | Lacks authenticity; known to have provided false information | 0.15 |
| F | Cannot Be Judged | No basis for evaluation; new source, unknown track record | 0.30 |

**Note**: Rating F is not a middling score; it is an uncertainty flag. New HUMINT sources, anonymous OSINT accounts, and unverified walk-ins receive F. F-rated sources require corroboration before entering Tier I analysis.

**Axis 2 — Information Credibility (IC)**:

| Code | Rating | Definition |
|---|---|---|
| 1 | Confirmed | Corroborated by independent sources of established reliability |
| 2 | Probably True | Consistent with other information; logical; no contradiction |
| 3 | Possibly True | Not confirmed; reasonably plausible; uncontradicted |
| 4 | Doubtful | Inconsistent with confirmed information; improbable |
| 5 | Improbable | Contradicts established fact or confirmed information |
| 6 | Cannot Be Judged | No basis for evaluation |

**Combined QIA Score**:

Multiply Source Reliability weight × Information Credibility score (inverted, where 1.0 = Confirmed). The resulting QIA Score (0.0–1.0) feeds directly into the QGIA Confidence Score.

**QIA Combination Table** (key intersections):

| Source \ Credibility | 1 Confirmed | 2 Prob. True | 3 Poss. True | 4 Doubtful | 5 Improbable |
|---|---|---|---|---|---|
| **A** | 1.00 | 0.85 | 0.65 | 0.30 | 0.10 |
| **B** | 0.85 | 0.72 | 0.55 | 0.25 | 0.08 |
| **C** | 0.65 | 0.55 | 0.42 | 0.18 | 0.06 |
| **D** | 0.40 | 0.34 | 0.26 | 0.10 | 0.04 |
| **F** | 0.30 | 0.25 | 0.18 | 0.07 | 0.03 |

**QGIA Minimum Standards**:
- Tier I Key Judgments: Minimum B2 sourcing
- Supporting assessments: Minimum C3
- Background context: F-rated sources acceptable if caveated

**Corroboration Bonus**: When two or more independent A/B sources report the same fact, IC rating upgrades one level (e.g., B3 → B2). Independence must be verified — two sources from the same network do not constitute independent corroboration.

**Temporal Decay Factor**: Intelligence older than 90 days is downgraded one IC level for dynamic topics (force deployments, leadership decisions). Structural information (geography, doctrine) decays more slowly; analyst judgment applies.

**Source Contamination Check**: Before rating, verify the source has not been previously identified as compromised. Cross-reference the QGIA Source Integrity Database (OSIQP function).

### 5.3 Geopolitical Example: North Korea ICBM Assessment

**Intelligence question**: Has North Korea successfully miniaturized a nuclear warhead for Hwasong-17 delivery?

| Evidence Item | Source | SR | IC | QIA Score | Notes |
|---|---|---|---|---|---|
| Defector report: technicians observed miniaturized device | HUMINT defector | F | 3 | 0.18 | New source, unverified |
| Published DPRK state media imagery of warhead mockup | OSINT | A | 3 | 0.65 | State media may be designed for domestic/foreign signaling |
| SIGINT intercepts indicating successful test parameters | SIGINT | A | 2 | 0.85 | Most reliable item; single source |
| Think-tank analysis citing above defector report | OSINT secondary | D | 3 | 0.26 | Derivative of F-rated primary; no independent value |
| Three-nation technical expert consensus (2024) | OSINT | B | 2 | 0.72 | Independent analysts, convergent judgment |

**Aggregated assessment**: Leading evidence (SIGINT A2 = 0.85, expert consensus B2 = 0.72) supports miniaturization as probable. Defector report cannot independently elevate confidence. Think-tank analysis has no independent weight. Overall assessment confidence: 0.71.

### 5.4 QGIA System Integration

**OSIQP**: Automatically assigns preliminary SR ratings based on source registry. IC ratings are auto-drafted based on cross-source consistency checking across the 500TB daily ingestion. Analysts validate and override.

**QSFE**: QIA scores are direct inputs to QSFE's confidence weighting algorithm. The "Data Quality" component (25% of overall confidence score) is populated from the QIA aggregate.

**Source Registry**: OSIQP maintains a continuously updated reliability track record for all registered sources. Rating A requires minimum 24 confirmed accurate reports; downgrade is triggered automatically on confirmed false report.

### 5.5 Common Pitfalls

- **Circular sourcing**: Media reports citing intelligence reports citing other media reports. Each step of citation distance degrades IC without changing apparent volume
- **Upgrading F sources prematurely**: A compelling narrative from an unknown source does not justify raising the SR rating absent track record verification
- **Static ratings**: Source reliability changes over time. A previously A-rated HUMINT source who has been re-contacted by adversary services must be downgraded immediately
- **Ignoring collection gaps**: Absence of high-quality sourcing on a critical question is itself an analytic finding — report collection gaps explicitly

---

## 6. Structured Brainstorming Techniques

### 6.1 Nominal Group Technique (NGT)

**Purpose**: Generate maximum idea diversity in a structured group setting while eliminating social pressure toward consensus, seniority deference, and groupthink.

**When to use**: At the opening of a major assessment when hypotheses or key factors must be generated. Ideal group size: 5–9 analysts.

**Step-by-Step**:
1. **Silent generation** (10–15 min): Each analyst independently writes all hypotheses or key factors without discussion
2. **Round-robin listing**: Facilitator records one idea per analyst in rotation until all ideas are captured. No discussion, no evaluation, no attribution of ideas to individuals
3. **Clarification only**: Brief questions to understand meaning, not to critique
4. **Anonymous ranking**: Each analyst independently scores ideas (e.g., 1–5) without seeing others' rankings
5. **Aggregation**: Facilitator tallies scores; top-ranked ideas become the working set
6. **Brief discussion**: Why did certain ideas score high or low? What emerged that no single analyst would have generated?

**QGIA Application**: NGT is mandatory for Tier I assessments during the hypothesis generation phase of ACH (Section 1, Step 1).

**Geopolitical Example (Russia-NATO)**: Tasked with generating hypotheses for Russian military activity in Belarus (2024), a five-analyst NGT session generated 22 distinct hypotheses versus the 6 that the lead analyst had drafted solo, including a deception-for-bargaining hypothesis that proved most analytically valuable.

**Common Pitfalls**: Facilitator bias in recording ideas; rushing the silent generation phase; allowing brief clarifications to become de facto critiques.

---

### 6.2 Starbursting

**Purpose**: Systematically generate comprehensive questions about a scenario or subject before beginning analysis. Prevents tunnel vision by forcing coverage of all analytical dimensions.

**When to use**: At the problem framing stage; when an analyst team is uncertain what they don't know; when onboarding to a new topic.

**Step-by-Step**:
1. Place the scenario at the center of a diagram
2. Generate questions across six dimensions:
   - **Who**: Who are the actors? Who is excluded? Who benefits? Who is at risk?
   - **What**: What is happening? What is not happening? What capability is involved?
   - **When**: When could this occur? When would it be too late to act?
   - **Where**: Where is the focal geography? Where are supporting activities?
   - **Why**: Why would an actor do this? Why now? Why this method?
   - **How**: How would this be executed? How would we know? How does this end?
3. Prioritize questions by analytical importance and collection feasibility
4. Assign collection or research tasks against each priority question

**Geopolitical Example (China–Taiwan)**: Starbursting a potential Taiwan Strait blockade scenario generated the critical **"Why now?"** question that surfaced Xi's 2027 CCP congress timeline as a constraining variable — a factor the team had underweighted when focusing on military capability questions.

**QGIA Integration**: OSIQP's Aurora workspace has a Starbursting template that auto-populates known answers from the knowledge library, flagging the remaining unanswered questions as collection priorities.

**Common Pitfalls**: Generating questions as a box-checking exercise without genuine analytic value; failing to prioritize (every question cannot receive equal collection effort).

---

### 6.3 Morphological Analysis

**Purpose**: Systematically map the complete solution space for a complex multi-variable problem. Particularly powerful for capability assessment and scenario generation when multiple independent variables interact.

**When to use**: Force structure assessment, weapons program analysis, escalation pathway generation, and any problem where independent choices combine to produce outcomes.

**Step-by-Step**:
1. **Define parameters**: Identify the independent variables relevant to the problem (e.g., for a military operation: timing, force type, geographic axis, strategic objective)
2. **List values for each parameter**: All feasible values each variable could take
3. **Build the morphological box**: Matrix of parameters × values
4. **Identify logical combinations**: Not all combinations are plausible; eliminate those that are physically, logistically, or politically impossible
5. **Analyze surviving combinations**: Each is a distinct scenario deserving at least brief probability assessment
6. **Highlight high-impact clusters**: Groups of combinations that share key attributes (e.g., all night operations, all using a northern axis) that require specific intelligence collection

**Geopolitical Example (Iran Escalation Options)**: In analyzing Iran's potential responses to a strike on Parchin, a morphological analysis generated 96 theoretical combinations across 4 parameters (timing, instrument, target type, geographic scope). After eliminating 74 implausible combinations, 22 remained, organized into 5 scenario clusters: direct retaliation, proxy escalation, covert sabotage, asymmetric maritime, and diplomatic de-escalation.

**QGIA Integration**: QSFE is pre-configured to accept morphological analysis scenario clusters as simulation inputs, converting analyst-generated scenario trees into probabilistic amplitude weights.

**Common Pitfalls**: Parameter selection bias (missing key variables); combinatorial explosion (more than 5–6 parameters makes the matrix unmanageable without computational support); treating the morphological box as the analysis rather than the input to analysis.

---

## 7. Cross-Impact Matrix Analysis

### 7.1 Purpose and When to Use

Cross-impact analysis systematically examines how the occurrence of one event affects the probability of other events in a complex scenario space. It is the primary tool for mapping second- and third-order effects and for identifying non-obvious causal chains in geopolitical crises.

**Use when**: Analyzing a system with multiple interacting variables (political transitions, alliance dynamics, economic-security linkages); preparing for crisis decision support where cascading effects matter; generating indicators for a warning assessment.

### 7.2 Step-by-Step Method

**Step 1 — Define the event set**
List 8–12 discrete events that could occur within the assessment horizon. Each must be a binary (occurs/doesn't occur) or discrete-state event. Keep events independent in definition (the matrix captures dependencies; the definitions should not presuppose them).

**Step 2 — Assign baseline probabilities**
For each event, assign an unconditional probability estimate using QSFE or analyst judgment. These are the priors before interaction effects are modeled.

**Step 3 — Build the cross-impact matrix**
Construct an N×N matrix where each cell (i,j) represents: "If event i occurs, how does the probability of event j change?" Express as a probability multiplier or percentage-point delta.

| | If E1 | If E2 | If E3 | If E4 |
|---|---|---|---|---|
| **E1** | — | +15pp | -10pp | +25pp |
| **E2** | +8pp | — | +30pp | +5pp |
| **E3** | -5pp | +12pp | — | -20pp |
| **E4** | +30pp | +10pp | -15pp | — |

**Step 4 — Identify cascade chains**
Trace paths where Event A → increases probability of B → increases probability of C, creating a cascade. These chains identify the critical triggering events whose prevention or acceleration carries the most leverage.

**Step 5 — Identify dampening chains**
Events that, if they occur, reduce probabilities of multiple other adverse events. These are stabilizing variables — important for policy intervention analysis.

**Step 6 — Scenario construction**
Select high-impact cascade chains as scenario seeds. Use QSFE to run probabilistic simulations across the event network.

### 7.3 Operational Example: NATO-Russia Baltic Crisis

**Assessment horizon**: 12 months post-Suwalki Corridor incident (hypothetical, 2026)

**Event set**:
- E1: Russia blockades Suwalki Corridor (baseline 28%)
- E2: NATO invokes Article 5 (baseline 15%)
- E3: Baltic state reserves mobilize (baseline 35%)
- E4: Germany halts NS2-equivalent energy transit (baseline 40%)
- E5: Russian financial markets collapse >20% (baseline 22%)
- E6: Kaliningrad receives major reinforcement (baseline 45%)

**Key cross-impacts**:
- E1 → E2: +38pp (blockade almost certainly triggers Article 5 consideration)
- E6 → E1: +22pp (reinforcement makes blockade more militarily feasible)
- E5 → E1: -35pp (economic collapse significantly reduces Kremlin escalation appetite)
- E4 → E5: +18pp (energy transit halt accelerates financial pressure)

**Cascade chain identified**: E4 (energy halt) → E5 (financial collapse) → E1 probability falls from 28% to under 10%. This is the primary de-escalation lever identified for policy consumers.

**Warning chain identified**: E6 (reinforcement) → E1 probability rises to 50% → E2 probability rises to 65% — acute crisis threshold. Collection priority: GEOINT monitoring of Kaliningrad access routes and order-of-battle changes.

### 7.4 QGIA System Integration

**EDM**: The Entanglement Dynamics Mapper is purpose-built for cross-impact analysis at scale. EDM runs 10,000+ Monte Carlo simulations across event networks, providing probability distributions rather than point estimates. The Baltic example above ran in EDM with 15 events and produced cascade chain probabilities with 95% confidence intervals within 90 seconds.

**QSFE**: Accepts EDM cross-impact outputs as scenario weighting inputs for the Three-Tier output framework.

**Aurora**: Generates visual cascade chain diagrams from EDM outputs, formatted for inclusion in Tier I briefing products.

### 7.5 Common Pitfalls

- **Overcrowded event sets**: More than 12 events makes manual analysis unmanageable; use EDM for larger sets
- **Asymmetric impact errors**: If E1 affects E2, the reverse need not be equal — each cell must be assessed independently
- **Feedback loops**: Some event pairs create positive feedback loops (each occurrence increases the other); these amplification mechanisms must be flagged explicitly as instability indicators
- **Static matrix**: In a fast-moving crisis, cross-impact probabilities change daily. Establish a review cadence and flag which cells are most sensitive to new information

---

## 8. Indicators and Warning Generation

### 8.1 Purpose and When to Use

Indicators and Warning (I&W) translates analytical hypotheses into observable, collectable evidence sets. Rather than waiting for events to occur, I&W creates tripwires — specific observable phenomena whose presence or absence updates the probability of a hypothesis in near-real time.

**Use I&W for all**: Strategic warning assessments, standing watch requirements, crisis monitoring, and any assessment where advance notice of a state change has policy value.

### 8.2 Step-by-Step Method

**Step 1 — State the hypotheses**
I&W is hypothesis-driven. Each indicator set serves a specific hypothesis. Begin with ACH output (Section 1) to ensure hypotheses are well-formed.

**Step 2 — Generate positive indicators (presence indicators)**
For each hypothesis: "If this hypothesis were true, what would we observe?" Generate indicators across all collection disciplines:
- **GEOINT indicators**: Observable with satellite or aerial imaging
- **SIGINT indicators**: Observable in communications intercepts or signals
- **HUMINT indicators**: Observable through human sources, diplomatic reporting
- **OSINT indicators**: Observable in open media, financial markets, social media, official statements
- **MASINT indicators**: Observable in material signatures, emissions, technical measurements

**Step 3 — Generate negative indicators (absence indicators)**
"If this hypothesis were true, what would NOT be occurring?" Absence of expected activity is often the most diagnostic finding but is systematically overlooked.

**Step 4 — Assess indicator specificity**
Rate each indicator:
- **Specific**: Only consistent with this hypothesis; high diagnostic value
- **General**: Consistent with multiple hypotheses; useful for context but not probative
- **Ambiguous**: Could indicate either this hypothesis or its opposite; low diagnostic value; use cautiously

**Step 5 — Set thresholds and timelines**
For each specific indicator: define observable thresholds ("PLAN amphibious vessel concentration above 40 hulls") and assessment timelines ("if observed within 72 hours"). Vague indicators cannot be monitored reliably.

**Step 6 — Build the indicator matrix**
Organize indicators into a monitoring matrix specifying: collection discipline, threshold, current status (observed/not observed/ambiguous), last checked, and probability impact if observed.

**Step 7 — Establish collection priorities**
Not all indicators are collectable with available assets. Prioritize by: diagnostic value × collection feasibility. Gaps in high-value indicators are explicit collection requirements for the requirements process.

**Step 8 — Monitor and update**
Establish review cycle: daily for acute crisis warning, weekly for chronic monitoring. Each update revises hypothesis probabilities in QSFE based on observed indicator status changes.

### 8.3 Expanded Example: PLA Amphibious Assault Preparation (China–Taiwan)

**Hypothesis H1**: PLA is preparing for a forced entry amphibious operation against Taiwan within 6 months.

**Indicator Set** (expanded from QGIA-KL-AF-02-02):

| # | Indicator | Discipline | Threshold | Diagnostic Value | Current Status |
|---|---|---|---|---|---|
| 1 | PLAN amphibious group concentration (Type 075 LHDs, Type 071 LPDs) near Fujian/Zhejiang | GEOINT | ≥ 4 major amphibious vessels concentrated | Specific | Monitor |
| 2 | PLAAF air superiority sortie rate increase | SIGINT | >2× baseline over 72h | General | Monitor |
| 3 | PLA Second Artillery (Rocket Force) alert status elevation | SIGINT | Code change in Rocket Force command traffic | Specific | Monitor |
| 4 | Blood bank and surgical supply expansion in Fujian, Zhejiang, Guangdong provinces | OSINT/HUMINT | >2× normal procurement orders | Specific | Not observed |
| 5 | Coastal radar system activation pattern change | MASINT/SIGINT | Sustained non-exercise emissions | General | Monitor |
| 6 | PLA reserve mobilization orders, particularly amphibious assault brigades | HUMINT | Documented reserve call-up in coastal MR | Specific | Not observed |
| 7 | PLAN mine-laying activity in Taiwan Strait approaches | GEOINT | Any confirmed mine-layer sorties from Zhoushan | Specific | Not observed |
| 8 | Commercial shipping clearance in projected assault corridors | OSINT | Port authority notices excluding civilian traffic | Specific | Not observed |
| 9 | PLA field hospital pre-positioning in coastal areas | GEOINT/OSINT | Hospital ship relocation, tent hospital construction | Specific | Not observed |
| 10 | Absence of PLA officer leave, family travel restrictions | HUMINT | Leave cancellation orders, housing restriction patterns | Specific (absence) | Status unknown — collection gap |
| 11 | Taiwan financial capital flight acceleration | OSINT/FININT | Unusual outflows from Taiwan dollar | General | Monitor |
| 12 | PLA deception activity — exercise cover for pre-positioned forces | All | Formal exercise announced simultaneously with force movements | Deception flag | Watch |

**Warning Threshold**: If any 4 Specific indicators are simultaneously "Observed," elevate to QSFE Tier I strategic warning. If Indicators 6 + 7 simultaneously observed, escalate to maximum collection priority regardless of other indicator status.

**Assessment Update Protocol**: After each 24-hour OSIQP cycle, Aurora automatically updates the indicator matrix, recalculates H1 probability using Bayesian updating, and flags any threshold breaches for duty analyst review.

### 8.4 QGIA System Integration

**OSIQP**: The primary I&W execution platform. OSIQP monitors 156 qubit-equivalent parallel data streams against registered indicator thresholds, with <50ms detection latency. Analysts register indicator sets; OSIQP manages collection monitoring and threshold alerts.

**QSFE**: Receives indicator status updates and applies Bayesian updating to hypothesis probabilities. Each indicator observation carries a pre-calculated likelihood ratio stored in QSFE's indicator database.

**EDM**: Maps alliance and adversary network changes as a class of HUMINT/OSINT indicators, particularly for indicators related to foreign coalition formation or defection from partner relationships.

### 8.5 Common Pitfalls

- **Indicator circularity**: An indicator defined as "increased threat activity" is not an indicator — it restates the hypothesis. Indicators must be observable phenomena independent of the conclusion
- **Failure to monitor negative indicators**: Absence of expected activity is as analytically important as presence. Systems monitoring must explicitly check for non-observation of expected indicators
- **Threshold ambiguity**: "Significant increase" is not a threshold. Specify numbers, timeframes, and collection sources
- **Over-reliance on a single discipline**: GEOINT-only I&W is exploitable. Adversaries can deny GEOINT while failing to conceal SIGINT or HUMINT indicators
- **Indicator creep**: Adding indicators without removing obsolete ones creates monitoring noise; review and prune indicator sets quarterly

---

## 9. Devil's Advocacy and Team A/Team B

### 9.1 Devil's Advocacy

**Purpose**: Formally and systematically challenge the prevailing analytic view by developing the strongest possible case against it. Prevents premature consensus and surfaces evidence that confirmed the consensus view has caused analysts to discount.

**When to use**: After a draft Tier I assessment has been produced; when consensus formed rapidly with limited dissent; when an assessment has been standing unchanged for more than 90 days.

**Step-by-Step**:
1. **Assign**: Designate one analyst (not the assessment author) as Devil's Advocate. The role is formal, not personal — the assigned analyst argues against the consensus regardless of their private view
2. **Full access**: Devil's Advocate reviews all source material, not just the assessment summary
3. **Build the counter-case**: Develop the strongest possible argument against the leading judgment. Find evidence the consensus interpretation discounted. Identify alternative explanations for key evidence. Challenge critical assumptions
4. **Formal presentation**: Devil's Advocate presents to the full team. Challenge cannot be dismissed without documented rebuttal
5. **Team response**: Consensus holders must address each point. Unaddressed challenges become explicit caveats in the final product
6. **Outcome**: Either (a) consensus survives, strengthened and caveated, or (b) assessment is revised

**Geopolitical Example (Iran Nuclear)**:
- **Consensus assessment**: Iran pursuing weaponization; 12–18 months to first device
- **Devil's Advocate challenge**: 
  - Enrichment levels reflect deterrence signaling, not device production (KAC Assumption 1 violation)
  - HUMINT on weaponization is from one source network, potentially penetrated
  - Historical precedent: Libya's 2003 roll-back occurred when diplomatic incentives outweighed deterrence value
  - Absence of warhead integration testing in MASINT record is unexplained if weaponization is active
- **Team response**: Acknowledged HUMINT vulnerability; revised timeline to 18–24 months; added collection requirement against second-source warhead integration reporting
- **Product impact**: Assessment changed from "Iran is pursuing weaponization" to "Iran is maintaining a breakout posture; weaponization cannot be confirmed or excluded"

### 9.2 Team A / Team B

**Purpose**: Competitive analysis between two independent teams with the same intelligence access. More resource-intensive than Devil's Advocacy but produces higher-quality competition, particularly when the subject is highly contested or politically sensitive.

**When to use**: High-stakes assessments with genuine expert disagreement; when previous assessments have proven wrong; when policy consumer requires independent validation.

**Step-by-Step**:
1. **Team formation**: Two teams of 3–5 analysts each; teams must include comparable seniority and regional expertise. Team B is not "the devil" — both teams pursue the truth independently
2. **Independent analysis**: Teams analyze the same intelligence collection separately. No inter-team communication during analysis phase
3. **Independent drafting**: Each team produces a formal assessment
4. **Structured debate**: Teams present findings formally. A senior adjudicator (division chief or above) presides
5. **Evidence disputes**: When teams differ, identify the specific evidence item(s) driving the divergence. Force explicit rating: is this a disagreement about evidence quality, inference, or assumption?
6. **Adjudication**: Adjudicator rules on the stronger case or commissions additional collection to resolve the dispute
7. **Unified product**: Final assessment incorporates the stronger argument, explicitly noting where Team B's view is valid as a minority assessment

**Geopolitical Example (Russia Strategic Intent)**:
- **Team A**: Russia's military posture in 2026 reflects genuine defensive concern about NATO expansion; probability of offensive action against Baltic states: 12%
- **Team B**: Russia's posture reflects offensive preparation masked by defensive rhetoric; Baltic probability: 38%
- **Key divergence**: Interpretation of logistics pre-positioning — Team A rated as routine rotation; Team B rated as assault preparation based on supply item types (bridging equipment, fuel beyond training requirements)
- **Adjudication**: Team B's evidence analysis ruled more rigorous; assessment revised to 31% with Team A's structural argument noted as a key uncertainty

**QGIA Integration**: Team A/B analyses are managed in the QSFE collaborative workspace with isolated workstreams. Aurora presents both assessments to the adjudicator in a structured comparison format highlighting evidence-level disagreements.

**Common Pitfalls for both techniques**:
- **Pro forma challenge**: Devil's Advocate reads from a script without genuine intellectual engagement; Team B immediately converges with Team A to avoid conflict. Institutional culture must reward genuine dissent
- **Personality over evidence**: Debate degenerates into assertion rather than evidence-grounded argument. Adjudicators must redirect to specific evidence items
- **Failure to document**: Minority views that are overruled must be preserved in the product record; if the consensus proves wrong, the dissent history is essential for learning

---

## 10. Red Team Analysis

### 10.1 Purpose and When to Use

Red Team analysis adopts the perspective, values, strategic culture, and decision logic of an adversary to predict their actions and identify vulnerabilities in friendly analysis. It is the primary antidote to mirror imaging — the systematic error of assuming adversaries think and prioritize as the analyst does.

**Use when**: Assessing adversary intent in a crisis; reviewing friendly plans for adversary-exploitable vulnerabilities; evaluating the effectiveness of deterrence or coercive measures from the adversary's perspective.

### 10.2 Step-by-Step Method

**Step 1 — Characterize the adversary accurately**
Before any red teaming, document:
- Adversary's core interests and terminal values (what they will not sacrifice)
- Historical decision-making patterns, especially in crises
- Strategic culture: attitude toward risk, face-saving requirements, historical grievances
- Current domestic political constraints
- Known cognitive biases and heuristics of key decision-makers

**Step 2 — Assemble the Red Cell**
Assign analysts with genuine regional and cultural expertise. Fluency in the adversary's language is strongly preferred. The cell must be willing to argue positions they personally find objectionable — they are thinking like the adversary, not agreeing with the adversary.

**Step 3 — Build the adversary's case**
Red Cell develops an independent assessment of the situation from the adversary's perspective: What does the adversary know? What do they fear? What options are available? What does success look like?

**Step 4 — Identify our vulnerabilities**
From the adversary perspective: Where are friendly positions weakest? What signals are being sent that may be misread? What actions invite adversary exploitation? What deterrence measures appear non-credible from inside the adversary system?

**Step 5 — Generate adversary courses of action**
Develop 3–5 adversary courses of action (COAs) in priority order as the adversary would rank them. For each COA: What triggers it? What does it achieve? What are the risks the adversary accepts?

**Step 6 — Test friendly assumptions**
Return to the KAC (Section 3) and stress-test critical assumptions against the adversary perspective developed. Identify where friendly analysis has mirror-imaged.

### 10.3 Geopolitical Example: North Korea Nuclear Signaling

**Red Cell task**: Assess Kim Jong Un's decision calculus on nuclear weapons use threshold.

**Red Cell characterization**:
- Terminal value: Regime survival (Kim family continuity), not territorial expansion
- Historical pattern: Nuclear tests timed to US domestic political cycles to maximize pressure
- Strategic culture: Juche ideology elevates self-reliance; concession without reciprocal benefit is domestically lethal
- Domestic constraint: Military leadership loyalty is transactional; weakness is fatal

**Red Cell assessment**:
- Kim views nuclear weapons as a regime survival guarantee, not a war-fighting instrument in most scenarios
- The use threshold is not "overwhelming US force" — it is "regime decapitation appears imminent with no diplomatic exit"
- Deterrence messaging that emphasizes post-use destruction is less effective than messaging that makes regime survival compatible with non-use
- CVID (Complete, Verifiable, Irreversible Denuclearization) demands are viewed inside the Kim system as synonymous with regime termination — offering them is not a diplomatic opening

**Friendly vulnerability identified**: US diplomatic messaging has focused on sanctions relief as the incentive for denuclearization, treating economics as the binding constraint. Red Cell analysis indicates the binding constraint is security, not economics. This is a mirror-imaging error. Policy recommendation: Security guarantees must lead, not follow, economic incentives.

**QGIA Integration**: QGIA maintains dedicated Red Cells for China, Russia, Iran, North Korea, and non-state actors (Iran-aligned). Each cell maintains a living strategic culture database updated by OSIQP OSINT monitoring and HUMINT reporting. Cell findings are tagged in QSFE as adversary-perspective scenario weights.

**Common Pitfalls**:
- **Red Team as echo chamber**: If the Red Cell is composed of analysts who agree with the prevailing assessment, it produces a confirmation exercise, not a challenge
- **Going native**: Red Cell analysts overly advocate for the adversary, losing analytical objectivity. Cell products must state: "from the adversary's perspective" throughout
- **Cultural caricature**: Reducing adversary decision-making to a stereotype (e.g., "autocrats always bluff") replaces one form of mirror imaging with another
- **Single Red Cell per adversary**: Different PLA factions, Kremlin advisory circles, and IRGC commands have divergent views. A Red Cell that treats "China" as monolithic misses intra-actor dynamics

---

## 11. Pre-Mortem Analysis

### 11.1 Purpose and When to Use

Pre-mortem analysis inverts the standard analytical workflow. Rather than defending a concluded assessment, analysts are asked to assume it has proven catastrophically wrong and work backward to explain why. The technique exploits hindsight bias productively — people generate more and better failure explanations when they assume failure has occurred than when they merely consider it might.

**Use when**: Finalizing any assessment with confidence score ≥ 0.70; before disseminating a major forecast that will drive resource allocation; when the assessment team has reached consensus rapidly; as a mandatory step before Tier I products receive the Chief Methodologist's signature.

### 11.2 Step-by-Step Method

**Step 1 — Announce the premise**
Facilitator states: "It is [12/24/36 months] from now. Our assessment proved completely wrong. The actual outcome was the opposite of what we predicted. Your task is not to defend our assessment — it is to explain, as specifically as possible, how we got it so wrong."

**Step 2 — Silent generation**
Each analyst independently writes every plausible explanation for the failure. Allow 10–15 minutes. Encourage specific, mechanistic explanations (not "we were unlucky" but "our HUMINT network was penetrated 6 months before the assessment").

**Step 3 — Round-robin collection**
Facilitator lists all failure explanations without attribution.

**Step 4 — Categorize failure modes**
Group explanations by type:
- **Data failure**: Collection gaps, deception, source contamination
- **Analytical failure**: Cognitive bias, mirror imaging, assumption error
- **Methodological failure**: Wrong SAT applied, insufficient hypothesis space
- **Environmental failure**: Genuinely unforeseeable events, black swans

**Step 5 — Prioritize and address**
For each failure mode: Can it be reduced before publication? Options include additional collection, KAC review, explicit caveating, or — in rare cases — delaying publication.

**Step 6 — Embed findings in the assessment**
Explicitly note in the assessment: "Pre-mortem analysis identified [specific vulnerabilities]. These uncertainties are reflected in [specific caveats/confidence score adjustments]."

### 11.3 Geopolitical Example: Afghan Government Stability (2021 Analogy)

**Applying pre-mortem to a hypothetical current assessment**: "Afghan-model governance collapse in a US partner state within 24 months: probability 15%."

**Pre-mortem premise**: "Our assessment was wrong. The government collapsed in 8 months. Why?"

**Failure explanations generated**:
1. HUMINT network was recruited by the government we were assessing — sources reported optimistically to protect relationships
2. We measured formal military capacity (equipment, numbers) but not will to fight, which collapsed under first serious pressure
3. We assumed economic deterioration would be gradual; currency collapse was nonlinear and happened faster than any model predicted
4. Our indicator matrix focused on military indicators; we had no indicators for elite defection from the government
5. We discounted opposition reporting as biased; it proved more accurate than government reporting
6. We applied deterrence logic (cost-benefit) to a regime whose internal cohesion required constant patronage flows — once flows stopped, cohesion collapsed immediately
7. We had no collection against the opposition's operational planning; we only knew the government's perspective

**Revisions made before publication**:
- Confidence score reduced from 0.78 to 0.62 (acknowledging HUMINT reliability concerns)
- Added will-to-fight indicators to the I&W matrix
- Added elite defection monitoring as a new collection requirement
- Caveat added: "Assessment relies substantially on government-affiliated sources; independent corroboration of stability assessments is limited"

### 11.4 QGIA System Integration

**Aurora**: Manages the pre-mortem session as a structured collaborative process in the QSFE workspace. Failure explanations entered anonymously. System automatically cross-references failure modes against the QGIA historical post-mortem database (archive of past forecast errors) to identify which failure modes have actually occurred in similar cases.

**QSFE**: Applies pre-mortem confidence adjustment factor. When pre-mortem identifies more than three Category 1 (Data/Collection) failure modes, confidence score is automatically capped at 0.75 pending additional collection.

### 11.5 Common Pitfalls

- **Treating pre-mortem as a formality**: If failure explanations are generic ("we might have been wrong about something"), the exercise has no analytical value
- **Defensiveness**: Analysts defending their own assessment during the pre-mortem destroy its purpose. The facilitator must enforce the "assume we are wrong" premise
- **Failing to act on findings**: Pre-mortem that generates failure explanations and then publishes an unchanged assessment is analytically dishonest
- **Scope limitation**: Pre-mortem the specific hypothesis that matters most, not the general topic — "our 35% probability estimate for Taiwan invasion is wrong" not "Taiwan is complicated"

---

## 12. Outside-In Analysis

### 12.1 Purpose and When to Use

Outside-in analysis begins with the broadest possible contextual frame — global or systemic trends — and progressively narrows toward the specific analytical question. It counteracts the "current intelligence tunnel" in which analysts become so focused on immediate events that they lose awareness of structural forces shaping the situation.

**Use when**: Beginning a new assessment on a topic where the team has been in short-cycle current intelligence mode; when assessing whether a specific event is part of a larger pattern; when a long-standing assessment needs structural re-examination; when detecting slow-moving drivers that may not be visible in daily collection.

### 12.2 Step-by-Step Method

**Level 1 — Global and structural trends (5–25 year horizon)**
Identify the macro-level forces shaping the environment: demographic shifts, technological trajectories, climate impacts, long-run economic trends, shifts in the global balance of power. Ask: What is the deep structure of this situation? What forces are operating regardless of who governs?

**Level 2 — Regional dynamics (2–10 year horizon)**
Examine the regional order: Alliance structures, economic interdependencies, historical rivalries, regional power competition. Ask: What regional forces constrain or enable actors in this situation?

**Level 3 — Actor-level analysis (1–5 year horizon)**
Focus on specific state and non-state actors: domestic politics, leadership calculations, institutional interests, resource constraints. Ask: What is driving this actor's current behavior?

**Level 4 — Immediate situation (Current–24 months)**
Analyze the specific events, incidents, and signals that generated the analytical requirement. Ask: How does the immediate situation connect to the forces identified at higher levels?

**Level 5 — Synthesis**
Build an assessment that is grounded in structural forces (Levels 1–2), mediated by actor logic (Level 3), and expressed in immediate behavior (Level 4). Conclusions that lack Level 1–2 grounding are vulnerable to being overtaken by structural forces the analyst ignored.

### 12.3 Geopolitical Example: Russia–Ukraine War Sustainability Assessment

**Level 1 (Global/Structural)**: 
- Long-run demographic decline in Russia (-0.2% population growth); military-age male population at structural pressure
- Global energy transition reducing long-run oil revenue dependency even at current prices
- Western technological convergence creating compounding disadvantage in precision munitions, C4ISR

**Level 2 (Regional)**:
- NATO expansion dynamic creates defensive security dilemma for Russia regardless of current leadership
- Eastern European states have accelerated rearmament, changing regional balance independently of US posture
- Ukraine's agricultural/industrial potential represents long-run economic competition with Russia's eastern regions

**Level 3 (Actor)**:
- Putin's domestic legitimacy depends on narrative of Russian great-power restoration; withdrawal requires a face-saving construct
- Russian military-industrial complex has adapted to sanctions but faces compounding capability gaps in precision munitions
- Ukrainian state coherence has strengthened beyond pre-war levels; collapse scenario now requires Level 1 structural reversal, not just military setback

**Level 4 (Immediate)**:
- Current attrition rates favor Ukraine in air defense, disadvantage in manpower
- Western military aid trajectories declining in some categories; increasing in others (F-16, long-range strike)

**Synthesis**: War sustainability assessment cannot rely on current attrition rates alone (Level 4 error). Structural forces (Levels 1–3) indicate Russian strategic position deteriorates over 3–7 year horizon regardless of tactical outcomes. Assessment: Russia cannot achieve declared strategic objectives (neutral, demilitarized Ukraine) under any scenario where Western cohesion holds — the binding constraint is not battlefield outcome but diplomatic endgame framing.

### 12.4 QGIA System Integration

**OSIQP**: Maintains the Structural Trends Database, continuously updated from academic sources, multilateral organization data, and long-cycle open source monitoring. Outside-in analyses draw automatically from this database for Level 1 inputs.

**QSFE**: Is calibrated to model at five time horizons simultaneously (0–30d, 1–6mo, 6–12mo, 1–5yr, 5–25yr). Outside-in analysis generates the 1–25yr framing that informs QSFE's prior probabilities for the shorter-cycle assessments.

**EDM**: Maps the alliance and economic interdependency networks (Level 2) that outside-in analysis identifies as structural constraints, providing quantitative measures of tie strength and cascade vulnerability.

### 12.5 Common Pitfalls

- **Level confusion**: Explaining a Level 4 phenomenon with Level 4 evidence only (e.g., "Russia escalated because of this week's events") misses structural causation
- **Structural determinism**: Structural forces constrain but do not determine outcomes — individual decisions and contingent events matter. Outside-in is a frame, not a forecast
- **False equivalence across levels**: A Level 1 structural trend (demographic decline) and a Level 4 immediate event (a border incident) are not equally weighted analytical inputs
- **Over-extension**: Outside-in analysis can produce analytically rich products that are too conceptually broad for operational use. The Level 4–5 synthesis must deliver a specific, actionable analytical judgment

---

## 13. SAT Selection Matrix and Workflow Integration

### 13.1 Mandatory SAT Requirements by Assessment Tier

| Assessment Tier | Mandatory SATs | Strongly Recommended | Optional |
|---|---|---|---|
| **Tier I: Strategic Warning** (>25% probability, high impact) | ACH, KAC, Devil's Advocacy OR Team A/B, Pre-mortem | Red Team, I&W, Cross-impact | Outside-In, Morphological |
| **Tier II: Regional Crisis** (10–25% probability) | I&W, QIA, Diagnostic Reasoning | KAC, ACH, Starbursting | Devil's Advocacy, Pre-mortem |
| **Tier III: Monitoring** (<10% probability / routine) | QIA, Diagnostic Reasoning | I&W | Any as appropriate |
| **Crisis Support (real-time)** | Diagnostic Reasoning, I&W monitoring | Cross-impact, Outside-In | As time permits |

### 13.2 Confidence Score Adjustments from SAT Application

| SAT Applied | Confidence Adjustment | Condition |
|---|---|---|
| ACH (full matrix, ≥6 hypotheses) | +0.10 | Correctly executed |
| Key Assumptions Check (full documentation) | +0.08 | Critical assumptions explicitly documented |
| Devil's Advocacy (formal, with documented rebuttal) | +0.08 | Genuine challenge, not pro forma |
| Team A/B (independent teams, adjudicated) | +0.12 | Full methodology followed |
| Red Team Analysis | +0.12 | Conducted by qualified Red Cell |
| Pre-mortem (≥8 failure explanations, acted upon) | +0.06 | Findings incorporated in assessment |
| I&W (full indicator matrix, ≥8 indicators) | +0.08 | Indicators monitored and updated |
| **Maximum cumulative adjustment** | **+0.25** | No assessment exceeds maximum |

### 13.3 SAT Sequencing Workflow for Tier I Assessment

```
STEP 1: Problem Definition
  → Diagnostic Reasoning Protocols (Section 2)
  → Starbursting to generate initial questions (Section 6.2)

STEP 2: Hypothesis Generation
  → Nominal Group Technique for team hypothesis generation (Section 6.1)
  → Morphological Analysis if capability/option space assessment (Section 6.3)

STEP 3: Evidence Collection and Rating
  → Quality of Information Assessment for all sources (Section 5)
  → Deception Detection check for key sources (Section 4)

STEP 4: Hypothesis Testing
  → Analysis of Competing Hypotheses matrix (Section 1)
  → Indicators and Warning matrix generation (Section 8)

STEP 5: Structural Analysis
  → Outside-In Analysis for structural context (Section 12)
  → Cross-Impact Matrix for cascade effects (Section 7)

STEP 6: Assumption and Challenge Review
  → Key Assumptions Check (Section 3)
  → Devil's Advocacy or Team A/B (Section 9)
  → Red Team if adversary intent is central (Section 10)

STEP 7: Quality Assurance
  → Pre-mortem before final publication (Section 11)
  → QIA final audit
  → Chief Methodologist review for all Tier I products
```

### 13.4 SAT Documentation Requirements

All QGIA products must include a **SAT Application Record** in the product metadata:

```
SAT APPLICATION RECORD
Assessment ID: [QGIA product number]
Date: [YYYY-MM-DD]
Lead Analyst: [Name, UID]
SATs Applied:
  [ ] ACH — Matrix attached / Lines: [count]
  [ ] KAC — Assumptions registered: [count], Critical: [count]
  [ ] Devil's Advocacy — Conducted by: [Name], Rebuttals documented: [Y/N]
  [ ] Team A/B — Teams: [Lead A, Lead B], Adjudicator: [Name]
  [ ] Red Team — Cell: [Designation], Cultural advisor: [Y/N]
  [ ] Pre-mortem — Failure explanations: [count], Actions taken: [Y/N]
  [ ] I&W — Indicators registered: [count], OSIQP monitoring: [Y/N]
  [ ] QIA — Sources rated: [count], Minimum rating: [SR/IC]
Confidence Score: [X.XX]
Chief Methodologist Approval: [Signature/UID]
```

---

## 14. References

1. Heuer, R. J. (1999). *Psychology of Intelligence Analysis*. CIA Center for the Study of Intelligence.
2. Pherson, R. H., & Heuer, R. J. (2020). *Structured Analytic Techniques for Intelligence Analysis* (3rd ed.). CQ Press.
3. Cooper, J. R. (2005). *Curing Analytic Pathologies: Pathways to Improved Intelligence Analysis*. CIA Center for the Study of Intelligence.
4. George, R. Z., & Bruce, J. B. (Eds.). (2008). *Analyzing Intelligence: Origins, Obstacles, and Innovations*. Georgetown University Press.
5. Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
6. National Commission on Terrorist Attacks. (2004). *The 9/11 Commission Report*. U.S. Government Printing Office. [Key Assumptions failure analysis]
7. Commission on the Intelligence Capabilities of the United States Regarding Weapons of Mass Destruction. (2005). *Report to the President*. [Iraq WMD failure — ACH and KAC lessons]
8. Jervis, R. (2010). *Why Intelligence Fails: Lessons from the Iranian Revolution and the Iraq War*. Cornell University Press.
9. Tetlock, P. E., & Gardner, D. (2015). *Superforecasting: The Art and Science of Prediction*. Crown Publishers. [Calibration and structured reasoning foundations]
10. Klein, G. (2007). Performing a Project Premortem. *Harvard Business Review*, 85(9), 18–19. [Pre-mortem methodology origin]
11. QGIA-KL-AF-02-02. (2026). *Structured Analytic Techniques (Summary)*. QGIA Analytical Methods Division. [Superseded summary document]
12. QGIA-KL-AF-02-03. (2026). *Forecasting Methodologies*. QGIA Analytical Methods Division. [Companion document]

---

**Document Control**  
**Review Cycle**: Annual, with ad hoc updates following major analytical failures  
**Update Triggers**: New SAT methodology publications; QGIA system capability changes; documented SAT failure in operational assessment  
**Custodian**: QGIA Chief Methodologist  
**Feedback and Exception Requests**: qgia-methods@qgia.gov  
**Next Review Due**: 2027-03-13  

---

**CLASSIFICATION**: UNCLASSIFIED  
**DOCUMENT END**
