# Operational Methods

**Intelligence collection, multi-source fusion, and operational tradecraft**

## Directory Structure

```
05-operational-methods/
├── sigint-procedures/
│   ├── collection-procedures.md (Tier III - Priority 16)
│   ├── collection-architecture.md
│   ├── target-development.md
│   ├── traffic-analysis.md
│   ├── cryptanalysis-integration.md
│   ├── reporting-formats.md
│   └── analyst-collector-coordination.md
├── humint-procedures/
│   ├── source-validation.md (Tier III - Priority 17)
│   ├── credibility-assessment.md
│   ├── network-analysis.md
│   ├── defector-debriefing.md
│   ├── deception-detection.md
│   ├── source-protection.md
│   └── ethical-legal-constraints.md
├── geoint-procedures/
│   ├── exploitation-guide.md (Tier III - Priority 18)
│   ├── imagery-interpretation.md
│   ├── change-detection.md
│   ├── facility-identification.md
│   ├── order-of-battle-estimation.md
│   ├── terrain-analysis.md
│   ├── commercial-imagery-integration.md
│   └── automated-feature-extraction.md
├── osint-procedures/
│   ├── open-source-exploitation.md
│   ├── social-media-analysis.md
│   ├── web-scraping-automation.md
│   ├── satellite-imagery-osint.md
│   ├── academic-literature-mining.md
│   └── osint-verification.md
├── multi-int-fusion/
│   ├── cross-source-integration.md
│   ├── correlation-methods.md
│   ├── anomaly-detection.md
│   ├── conflicting-source-resolution.md
│   └── confidence-aggregation.md
├── collection-management/
│   ├── requirements-definition.md
│   ├── collection-prioritization.md
│   ├── asset-tasking.md
│   ├── gap-identification.md
│   └── feedback-loops.md
└── security-procedures/
    ├── opsec-protocols.md
    ├── counterintelligence-awareness.md
    ├── classification-handling.md
    └── compartmentation-discipline.md
```

## Intelligence Disciplines (INTs)

### SIGINT (Signals Intelligence)

**Capabilities**:
- Communications intelligence (COMINT)
- Electronic intelligence (ELINT)
- Foreign instrumentation signals (FISINT)

**Strengths**:
- High volume, real-time
- Hard to deny or deceive (technical signatures)
- Reveals operational intentions

**Limitations**:
- Encryption challenges
- Massive data volume requires filtering
- Adversary OPSEC reduces access

**QGIA Processing**: 500TB daily SIGINT stream processed through OSIQP sentiment analysis (94.7% accuracy)

### HUMINT (Human Intelligence)

**Capabilities**:
- Recruited sources with access
- Liaison relationships
- Defector debriefings
- Open-source human contact

**Strengths**:
- Access to intentions and decision-making
- Context and nuance
- Insight into leadership psychology

**Limitations**:
- Deception and fabrication risks
- Limited scalability
- Source reliability variability
- Long development timelines

**Critical for**: Leadership intentions, coup plotting, internal regime dynamics

### GEOINT (Geospatial Intelligence)

**Capabilities**:
- Satellite imagery (government and commercial)
- Aerial reconnaissance
- Terrain analysis
- Mapping and charting

**Strengths**:
- Visual confirmation of activities
- Wide area coverage
- Difficult to conceal physical changes
- Trending over time

**Limitations**:
- Weather-dependent (optical)
- Revisit rate constraints
- Camouflage and concealment
- Requires interpretation expertise

**Commercial Revolution**: Planet Labs (daily global coverage), Maxar/DigitalGlobe (sub-meter resolution)

### OSINT (Open-Source Intelligence)

**Capabilities**:
- Media monitoring (traditional and social)
- Academic publications
- Government documents
- Commercial databases
- Gray literature

**Strengths**:
- Legally and ethically unambiguous
- Massive volume available
- Often complements classified sources
- Rapid dissemination possible

**Limitations**:
- Information pollution and noise
- Disinformation and propaganda
- Verification challenges
- Adversary awareness (public domain)

**OSIQP Role**: Automated OSINT processing, sentiment extraction, narrative tracking

### MASINT (Measurement and Signature Intelligence)

**Capabilities**:
- Nuclear detonation detection
- Radar signatures
- Acoustic intelligence
- Chemical/biological signatures

**Strengths**:
- Technical precision
- Difficult to spoof
- Unique detection capabilities

**Limitations**:
- Specialized sensors required
- Limited geographic coverage
- Interpretation complexity

**Critical for**: Nuclear monitoring, missile launch detection, WMD verification

## Multi-INT Fusion

### The Fusion Challenge

Each INT provides partial picture:
- SIGINT: "They're talking about an operation"
- GEOINT: "We see military equipment moving"
- HUMINT: "Source reports leadership approved attack"
- OSINT: "State media shows military exercises"

**Fusion**: Integrate into coherent assessment with confidence levels

### Correlation Methods

**Temporal Correlation**:
- Events coinciding in time suggest connection
- Example: SIGINT spike + GEOINT troop movement + HUMINT alert

**Spatial Correlation**:
- Activities in same geographic area
- Example: Multiple sources reporting activity at specific facility

**Activity Correlation**:
- Different sources describing same underlying event
- Example: SIGINT of order + GEOINT of execution + OSINT of outcome

### Conflicting Source Resolution

When sources disagree:

1. **Assess Source Quality**
   - Which has better access?
   - Historical reliability?
   - Potential bias or deception?

2. **Seek Discriminating Evidence**
   - What evidence would resolve the conflict?
   - Additional collection to adjudicate?

3. **Consider Alternative Explanations**
   - Could both be correct in different ways?
   - Temporal mismatch in observations?
   - Compartmentalization (sources see different parts)?

4. **Express Uncertainty**
   - If unresolvable, report competing interpretations
   - Assign probabilities to alternatives
   - Specify what would increase confidence

### Confidence Aggregation

**Naive Approach** (WRONG): "Three sources say X, so high confidence"

**Correct Approach**:
- Are sources independent? (Non-independence reduces weight)
- Do sources have direct access or secondhand?
- Quality-weight each source
- Bayesian updating with likelihood ratios

**Example**:
- Three HUMINT sources report coup planning
- Source 1: Direct access to plotters (high quality)
- Source 2: Friend of Source 1 (not independent)
- Source 3: Heard rumors (low quality)
- **Effective**: ~1.5 independent sources, not 3

## Collection Management

### Requirements Definition

**Intelligence Requirement Components**:
1. **What**: Specific information needed
2. **Why**: Analytical purpose (how will it be used?)
3. **When**: Time sensitivity
4. **Where**: Geographic or organizational focus
5. **Priority**: Relative importance vs. other requirements

**Example**:
- **What**: Russian force positioning within 50km of Ukraine border
- **Why**: Early warning of invasion preparation
- **When**: Daily updates
- **Where**: Belgorod, Kursk, Bryansk oblasts
- **Priority**: 1 (Critical)

### Collection Prioritization

Resource constraints require triage:

**Priority Factors**:
- Urgency (time-sensitive vs. strategic)
- Policy relevance (consumer needs)
- Intelligence gaps (unique vs. redundant)
- Probability of success (realistic collection expectation)
- Resource cost (opportunity cost)

**Priority Levels**:
- **Priority 1**: Urgent, critical gaps, high-level consumer interest
- **Priority 2**: Important, supports ongoing analysis
- **Priority 3**: Baseline monitoring, fills routine requirements
- **Priority 4**: Nice-to-have, low urgency

### Asset Tasking

Matching requirements to collection assets:

**SIGINT**: Task specific intercept sites or platforms
**GEOINT**: Schedule satellite passes over target areas
**HUMINT**: Task sources with access to target information
**OSINT**: Configure scraping and monitoring for keywords/entities

**Coordination**: Avoid duplication, maximize complementarity

### Gap Identification

**Known Unknowns**:
- Information we know we need but don't have
- Example: "We don't know China's nuclear warhead count"

**Unknown Unknowns**:
- Questions we haven't thought to ask
- Mitigation: Red teaming, assumption challenges, alternative analysis

**Gap Remediation**:
1. Can existing sources address with refocused tasking?
2. Require new collection capabilities?
3. Accept gap and work around with inference/modeling?

## Security and Counterintelligence

### OPSEC (Operations Security)

Protecting own activities from adversary intelligence:

**Principles**:
- **Identification**: What needs protection?
- **Analysis**: What can adversary learn?
- **Assessment**: How vulnerable are we?
- **Countermeasures**: How do we mitigate?
- **Application**: Implement and monitor

**QGIA OPSEC**:
- Compartmentation of sensitive methods
- Cover stories for collection activities
- Deception to mislead adversary about capabilities
- Limiting digital signatures (cyber hygiene)

### Counterintelligence Awareness

Adversary attempts to:
- **Penetrate**: Plant spies within QGIA
- **Recruit**: Flip QGIA personnel
- **Deceive**: Feed false information
- **Disrupt**: Cyber attacks, blackmail, assassination

**Indicators of Compromise**:
- Unexplained wealth or foreign contacts
- Unusual access patterns to classified systems
- Defensive or evasive behavior
- Foreign travel to denied areas

**Countermeasures**:
- Background investigations
- Continuous evaluation
- Insider threat detection systems
- Security culture and reporting

## Integration with QGIA Frameworks

### Operational Methods → Data Pipelines

**Collection → OSIQP Processing → Analyst Tools**

1. **Ingestion**: Multi-INT feeds into 500TB daily pipeline
2. **Processing**: OSIQP sentiment analysis, entity extraction, event coding
3. **Fusion**: Cross-source correlation and confidence weighting
4. **Delivery**: Structured data to QGIA quantum models (QSFE, EDM, ABCP, RPRN, TCA)
5. **Feedback**: Analyst assessments improve ML models

### Quality Control Loop

**Source Reporting → Analyst Validation → Retrospective Assessment**

- Track source reliability over time
- Identify systematic biases or deception
- Refine confidence weightings
- Inform future collection prioritization

## Training and Professional Development

**Basic INT Training (All Analysts)**:
- Understanding capabilities and limitations of each INT
- Source evaluation fundamentals
- Multi-INT correlation basics

**Advanced INT Specialization**:
- Deep dive into specific discipline (SIGINT/HUMINT/GEOINT specialist)
- Technical tradecraft
- Collection management

**Cross-INT Rotations**:
- Analysts rotate through different INT divisions
- Builds appreciation for complementary perspectives
- Enhances fusion capabilities

---

**Last Updated**: 2026-02-16
**Status**: STRUCTURE ESTABLISHED