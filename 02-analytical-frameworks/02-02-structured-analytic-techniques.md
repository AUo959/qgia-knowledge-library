# Structured Analytic Techniques (SATs)

**Document ID**: QGIA-KL-AF-02-02  
**Classification**: UNCLASSIFIED  
**Version**: 1.0  
**Last Updated**: 2026-02-16  
**Authority**: QGIA Analytical Methods Division

## Purpose

Systematic techniques to overcome cognitive biases, challenge assumptions, and improve analytical rigor. Mandatory application for all Tier I assessments.

---

## 1. DIAGNOSTIC TECHNIQUES

### 1.1 Key Assumptions Check

**Purpose**: Surface unstated assumptions underlying analysis.

**Method**:
1. List all judgments in assessment
2. Identify assumptions supporting each judgment
3. Challenge: "What if this assumption is wrong?"
4. Rate: Likelihood assumption correct (0-100%)
5. Rate: Impact if wrong (Low/Medium/High)
6. Focus collection on high-impact, low-certainty assumptions

**Example** (Russia-NATO Crisis):
- Assumption: "Putin values regime survival above territorial gains"
- Challenge: What if regime survival requires external victory?
- Likelihood: 70% | Impact if wrong: High
- Action: Increase HUMINT collection on Kremlin decision-making

### 1.2 Quality of Information Check

**Source Reliability Matrix**:

| Rating | Meaning | QGIA Confidence Weight |
|--------|---------|------------------------|
| A | Completely reliable | 1.00 |
| B | Usually reliable | 0.80 |
| C | Fairly reliable | 0.60 |
| D | Not usually reliable | 0.40 |
| E | Unreliable | 0.20 |
| F | Cannot be judged | 0.10 |

**Information Credibility**:
1. Confirmed (multiple independent sources)
2. Probably true (logical, consistent with other info)
3. Possibly true (not confirmed, reasonably plausible)
4. Doubtful (inconsistent with confirmed info)
5. Improbable (contradicts confirmed info)
6. Cannot be judged (no basis for evaluation)

**QGIA Standard**: Tier I assessments require minimum B3 sources.

### 1.3 Indicators and Signposts

**Purpose**: Define observable evidence supporting/refuting hypotheses.

**Method**:
1. State hypotheses clearly
2. List indicators for each hypothesis
3. Specify: What would we observe if hypothesis true?
4. Monitor indicators systematically
5. Update hypothesis probabilities as indicators observed/absent

**Example** (China Taiwan Contingency):

**H1: PLA Amphibious Assault Preparation**
- Indicator 1: PLAAF sortie rate >2x baseline (Observable: SIGINT)
- Indicator 2: PLAN amphibious vessels concentrated (Observable: GEOINT)
- Indicator 3: Reserve mobilization orders (Observable: HUMINT)
- Indicator 4: Blood bank expansion Taiwan-adjacent provinces (Observable: OSINT)

**QGIA Integration**: OSIQP monitors indicators automatically; alerts when thresholds crossed.

---

## 2. CONTRARIAN TECHNIQUES

### 2.1 Devil's Advocacy

**Purpose**: Challenge prevailing view systematically.

**Method**:
1. Assign analyst to argue against consensus
2. Develop strongest possible counter-case
3. Identify evidence supporting alternative
4. Present to team formally
5. Team rebuts or revises assessment

**QGIA Requirement**: All Tier I assessments undergo devil's advocacy review.

**Example** (Iran Nuclear Intent):
- Consensus: Iran pursuing weaponization
- Devil's Advocate: Breakout capability ≠ weaponization intent; could be deterrent posture without actual weapons
- Result: Clarified assessment distinguishes capability from intent

### 2.2 Team A / Team B

**Purpose**: Competitive analysis to surface alternatives.

**Method**:
1. Form two independent teams
2. Same intelligence access
3. Teams develop separate assessments
4. Formal debate
5. Leadership evaluates arguments

**When to Use**: High-stakes assessments with significant uncertainty.

**QGIA Application**: Ukraine conflict escalation scenarios (2023-2024).

### 2.3 Red Team Analysis

**Purpose**: Think like the adversary.

**Method**:
1. Analysts adopt adversary perspective
2. Use adversary strategic culture, decision calculus
3. Identify vulnerabilities in friendly position
4. Predict adversary actions

**Requirements**:
- Cultural expertise (language, history, ideology)
- Strategic culture database access
- Avoid mirror imaging

**QGIA Red Teams**:
- China Red Cell: PLA decision-making simulation
- Russia Red Cell: Kremlin strategic calculus
- Iran Red Cell: IRGC operational planning

---

## 3. HYPOTHESIS GENERATION & TESTING

### 3.1 Analysis of Competing Hypotheses (ACH)

**Method** (Heuer, 1999):

**Step 1**: Brainstorm hypotheses (8-12 typical)
- Include unlikely but possible scenarios
- Ensure mutual exclusivity where feasible

**Step 2**: List evidence (all available information)

**Step 3**: Create diagnosticity matrix
- Rows: Evidence items
- Columns: Hypotheses
- Cells: Consistent / Inconsistent / Neutral

**Step 4**: Refine judgments
- Focus on most diagnostic evidence (distinguishes hypotheses)
- Downweight non-diagnostic evidence (consistent with all)

**Step 5**: Reject inconsistent hypotheses

**Step 6**: Report surviving hypotheses with confidence intervals

**QGIA Automation**: ABCP performs ACH at scale; analysts validate.

**Example Matrix** (North Korea Leadership Transition):

| Evidence | H1: Kim Jong Un Stable | H2: Succession Crisis | H3: Military Coup | H4: Controlled Transition |
|----------|------------------------|----------------------|-------------------|---------------------------|
| Purges of generals | Neutral | Consistent | Inconsistent | Neutral |
| Sister elevated | Consistent | Inconsistent | Inconsistent | Consistent |
| Nuclear tests continue | Consistent | Inconsistent | Neutral | Consistent |
| Economic reforms | Consistent | Inconsistent | Inconsistent | Consistent |
| China support maintained | Consistent | Inconsistent | Neutral | Consistent |

**Result**: H2 and H3 rejected; H1 and H4 remain (distinguish via leadership health indicators).

### 3.2 Multiple Hypothesis Generation

**Technique**: Force generation of multiple explanations before analysis.

**Prevents**: Premature closure on single hypothesis.

**Rule**: Minimum 4 hypotheses; include at least one "unlikely but possible."

---

## 4. IMAGINATIVE THINKING

### 4.1 Alternative Futures Analysis

**Purpose**: Map range of plausible outcomes.

**Method**:
1. Identify key drivers (variables shaping future)
2. Assess uncertainty/impact for each driver
3. Select 2 highest-impact, highest-uncertainty drivers
4. Create 2x2 matrix (4 scenarios)
5. Develop narratives for each quadrant
6. Identify indicators distinguishing scenarios
7. Monitor indicators; update probabilities

**Example** (US-China Competition 2026-2030):

**Driver 1**: Taiwan crisis (escalates / status quo)  
**Driver 2**: US domestic cohesion (fractured / united)

| | Taiwan Status Quo | Taiwan Crisis |
|------------------|-------------------|---------------|
| **US United** | Competitive coexistence (45%) | Managed crisis (25%) |
| **US Fractured** | Chinese advantage (20%) | Catastrophic escalation (10%) |

**QGIA Integration**: QSFE models all four paths simultaneously with amplitude weighting.

### 4.2 High-Impact/Low-Probability (HILP) Analysis

**Purpose**: Identify tail risks.

**Criteria**:
- Probability: <10%
- Impact: Strategic warning level

**Examples**:
- Pakistan nuclear command breakdown during India-Pakistan crisis
- North Korea collapse with WMD security failure
- Gulf Cooperation Council rupture

**QGIA Requirement**: Quarterly HILP review; one HILP scenario included in each major assessment.

### 4.3 Brainstorming and Starbursting

**Brainstorming Rules**:
- No criticism during generation phase
- Quantity over quality initially
- Wild ideas encouraged
- Build on others' ideas

**Starbursting**: Generate questions about scenario (Who? What? When? Where? Why? How?)

---

## 5. SCENARIO ANALYSIS

### 5.1 Scenario Development

**Components**:
1. **Driving forces**: Key variables
2. **Critical uncertainties**: High-impact unknowns
3. **Scenario logic**: Causal chains
4. **Indicators**: Observable signposts
5. **Implications**: Policy consequences

**QGIA Scenarios**: Time-phased (0-30d, 1-6mo, 6-12mo).

### 5.2 Cone of Plausibility

**Concept**: Range of outcomes narrows near-term, widens long-term.

**QGIA Confidence Calibration**:
- 0-30 days: 0.85-0.95 confidence
- 1-6 months: 0.70-0.85 confidence
- 6-12 months: 0.50-0.70 confidence

**Decoherence Events**: Trigger scenarios collapse to single path (wars, coups, pandemics).

---

## 6. DECISION SUPPORT TECHNIQUES

### 6.1 Pros-Cons-Faults-Fixes (PCFF)

**Method**:
1. **Pros**: List advantages of option
2. **Cons**: List disadvantages
3. **Faults**: Identify flaws in pros/cons reasoning
4. **Fixes**: Propose mitigations for cons

**Use**: Policy option evaluation.

### 6.2 SWOT Analysis

**Quadrants**:
- **Strengths**: Internal advantages
- **Weaknesses**: Internal limitations
- **Opportunities**: External favorable conditions
- **Threats**: External risks

**QGIA Application**: Allied capability assessments.

---

## 7. CHALLENGE ANALYSIS

### 7.1 What If? Analysis

**Method**: Systematically vary assumptions; observe impact on conclusions.

**Example**:
- Base case: China invades Taiwan 2027 (35% probability)
- What if US AUKUS delayed? Probability increases to 48%
- What if semiconductor sanctions ineffective? Probability increases to 52%

### 7.2 Premortem Analysis

**Method**:
1. Assume forecast failed catastrophically
2. Generate explanations for failure
3. Identify vulnerabilities in current assessment
4. Strengthen analysis to address vulnerabilities

**QGIA Standard**: Premortem for all >0.70 confidence predictions.

---

## 8. QGIA INTEGRATION

### 8.1 SAT Selection Matrix

| Assessment Type | Mandatory SATs | Recommended SATs |
|-----------------|---------------|------------------|
| Tier I Strategic Warning | ACH, Key Assumptions, Devil's Advocacy | Red Team, Premortem |
| Tier II Regional Crisis | Indicators, Alternative Futures | Team A/B, HILP |
| Tier III Monitoring | Quality of Info Check | What If? |

### 8.2 Confidence Calibration

**SAT Application Bonus**:
- ACH applied: +0.10 confidence
- Devil's advocacy: +0.08 confidence
- Red team validation: +0.12 confidence
- Multiple SATs: Cumulative (max +0.25)

### 8.3 OSIQP Automation

**Automated SATs**:
- Quality of Information Check (source reliability scoring)
- Indicators monitoring (threshold alerts)
- ACH matrix generation (ABCP Bayesian updates)

**Human-Required SATs**:
- Devil's advocacy (requires contrarian mindset)
- Red teaming (cultural expertise essential)
- Alternative futures (creative scenario building)

---

## 9. COGNITIVE BIAS MITIGATION

### 9.1 Common Biases in Intelligence

**Confirmation Bias**: 
- Seek evidence supporting beliefs
- Mitigation: ACH forces disconfirming evidence consideration

**Anchoring Bias**: 
- Over-rely on initial information
- Mitigation: Bayesian updating, periodic re-baseline

**Groupthink**: 
- Consensus pressure suppresses dissent
- Mitigation: Devil's advocacy, Team A/B, anonymous input

**Availability Bias**: 
- Overweight recent/vivid events
- Mitigation: Historical base rates, systematic data review

**Mirror Imaging**: 
- Assume adversary thinks like us
- Mitigation: Red team analysis, strategic culture databases

### 9.2 Bias Awareness Training

**QGIA Requirement**: Annual cognitive bias workshop for all analysts.

**Techniques**:
- Case studies of intelligence failures
- Bias self-assessment instruments
- Peer feedback on analytic products

---

## 10. QUALITY CONTROL

### 10.1 Peer Review Process

**Tiers**:
- **Tier I**: Two senior analysts + division chief
- **Tier II**: One senior analyst
- **Tier III**: Automated quality check (OSIQP)

**Review Criteria**:
1. SATs applied appropriately?
2. Assumptions stated explicitly?
3. Alternative hypotheses considered?
4. Confidence calibrated accurately?
5. Sources reliable and corroborated?

### 10.2 Post-Mortem Analysis

**Trigger**: Major forecast error (>0.30 confidence delta from outcome).

**Process**:
1. Reconstruct decision-making process
2. Identify where analysis diverged from reality
3. Assess: Analytical failure vs. unforeseeable event?
4. Update methodologies
5. Disseminate lessons learned

**QGIA Database**: Archive of forecast post-mortems for training.

---

## 11. TRAINING REQUIREMENTS

**Junior Analysts**:
- SAT fundamentals (ACH, Key Assumptions, Indicators)
- Cognitive bias awareness
- Quality of Information Check

**Mid-Level Analysts**:
- Advanced SATs (Devil's Advocacy, Alternative Futures, Red Team)
- SAT selection for problem types
- Facilitating SAT exercises

**Senior Analysts**:
- SAT innovation and adaptation
- Training junior analysts
- Quality control leadership

**Certification**: SAT proficiency exam required for promotion to mid-level.

---

## 12. DOCUMENT MAINTENANCE

**Review Cycle**: Annual  
**Update Triggers**: New SAT development, lessons from intelligence failures  
**Custodian**: QGIA Analytical Methods Division  
**Feedback**: qgia-sat@qgia.gov

---

## REFERENCES

1. Heuer, R. J. (1999). *Psychology of Intelligence Analysis*. CIA.
2. Pherson, R. H., & Heuer, R. J. (2020). *Structured Analytic Techniques for Intelligence Analysis* (3rd ed.). CQ Press.
3. Cooper, J. R. (2005). *Curing Analytic Pathologies*. CIA Center for the Study of Intelligence.
4. George, R. Z., & Bruce, J. B. (Eds.). (2008). *Analyzing Intelligence: Origins, Obstacles, and Innovations*. Georgetown University Press.
5. Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.

**CLASSIFICATION**: UNCLASSIFIED  
**DOCUMENT END**