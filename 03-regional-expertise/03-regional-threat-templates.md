# Regional Threat Assessment Templates

**Document ID**: QGIA-KL-RE-03-THREAT-TEMPLATES  
**Classification**: UNCLASSIFIED  
**Version**: 1.0  
**Last Updated**: 2026-03-13  
**Authority**: QGIA Regional Division Chiefs (Collaborative)

---

## Purpose

This document provides standardized operational templates for regional threat assessment. Each template is designed for direct analyst use: score each indicator, record observations, and feed outputs into QSFE scenario generation. Templates apply across all QGIA regional desks — Indo-Pacific, Eastern Europe/Eurasia, Middle East/North Africa, Sub-Saharan Africa, Latin America, and South/Central Asia.

A comprehensive filled example using the **Eastern Europe (Russia-NATO Frontier, 2026)** region is embedded throughout each framework section. A second comparative example covering **South China Sea (Indo-Pacific, 2026)** appears in the Cross-Regional Comparison section (Section 13). Analysts should replicate this structure for any region under assessment.

**Mandatory Use Policy**: This template package is required input for any QSFE regional scenario run. Sections 1–8 must be completed before a QSFE package is submitted. Sections 9–11 are required when Regional Threat Profile (RTP) score ≥ 3.0. Section 14 QGIA integration steps are required for all Tier I assessments.

---

## Document Structure

1. Regime Type Classification Decision Tree  
2. Political Stability Assessment Templates (by regime type: Democracy, Hybrid, Authoritarian, Theocratic, Military Junta)  
3. Economic Fragility Metrics Template  
4. Military Capability Assessment Framework (Conventional, Nuclear/WMD, Asymmetric, Cyber)  
5. Social Cohesion and Identity Conflict Template  
6. External Interference Vulnerability Assessment  
7. Regional Power Dynamics Mapping Methodology  
8. Trigger Event Identification Framework  
9. Fragile State Early Warning Indicators  
10. Alliance Commitment Reliability Scoring  
11. Information Environment Assessment  
12. Scenario Generation: Template-to-QSFE Integration  
13. Cross-Regional Comparison Methodology  
14. QGIA Integration Notes (EDM, OSIQP, Aurora)  
15. Assessment Completion Checklist  
16. References and Data Sources

---

## Scoring Convention

All indicators use a **1–5 ordinal scale** unless otherwise specified:

| Score | Label | Operational Meaning |
|-------|-------|---------------------|
| 1 | Minimal | No significant concern; baseline/stable |
| 2 | Low | Emerging signals; monitoring warranted |
| 3 | Moderate | Active concern; analyst attention required |
| 4 | Elevated | High concern; scenario planning triggered |
| 5 | Critical | Imminent or ongoing threat; crisis protocols applicable |

**Composite Score** = mean of all applicable sub-indicators (round to two decimal places).  
**Confidence Weight** = apply QGIA 4-component confidence score (0.00–1.00) to each composite.  
**N/A Protocol**: If an indicator is structurally inapplicable (e.g., nuclear capability for non-nuclear state), mark N/A and exclude from composite mean. Document the exclusion.

---

## Section 1: Regime Type Classification Decision Tree

Use this decision tree **before** selecting the correct stability template (Section 2). Misclassification inflates or deflates indicator relevance. If contested between two types, assign a Primary and Secondary classification.

```
START: What is the primary source of political authority?

├─ Popular electoral mandate, multiparty competition, independent judiciary,
│   free press, civilian executive control of military
│   └─ → DEMOCRACY (proceed to Template 2A)
│
├─ Electoral institutions exist but executive dominates; selective rule of law;
│   opposition harassed but not eliminated; façade pluralism
│   ├─ Is civilian leadership nominally in charge?
│   │   └─ YES → HYBRID / COMPETITIVE AUTHORITARIAN (Template 2B)
│   └─ NO (military-backed civilian façade or direct military oversight)
│       → MILITARY-GUIDED HYBRID (Template 2D)
│
├─ Single party or personalist rule; no meaningful electoral competition;
│   systematic suppression of opposition
│   ├─ Is religious law / clerical hierarchy the ultimate source of authority?
│   │   └─ YES → THEOCRATIC (Template 2E)
│   └─ NO → AUTHORITARIAN (Template 2C)
│
└─ Military institution holds formal executive power; civilian government
    displaced or subordinated; governing council or junta structure present
    └─ → MILITARY JUNTA (Template 2D)
```

**Borderline Classification Rules:**

| Ambiguity | Resolution |
|-----------|------------|
| Democracy with significant backsliding | Score 2A; flag democratic erosion in 2A-07 |
| Theocracy with elected parliament | Score 2E primary, 2B secondary (weight 0.3) |
| Authoritarian transitioning to military rule | Score 2C primary, 2D secondary |
| Post-junta transitional government | Score 2D; reassess quarterly |

**Classification Confidence Check**: If contested, assign a **Primary** (weight 0.7) and **Secondary** (weight 0.3) classification. Run both templates. Weighted composite = (Primary × 0.7) + (Secondary × 0.3). Document rationale in the Source column.

---

## Section 2: Political Stability Assessment Templates

### Template 2A — Democracy

| # | Indicator | Score (1–5) | Observation / Evidence | Source |
|---|-----------|-------------|------------------------|--------|
| 2A-01 | Electoral integrity (independent monitoring, fraud levels) | | | |
| 2A-02 | Judicial independence (constitutional review capacity) | | | |
| 2A-03 | Legislative effectiveness (oversight capacity, gridlock level) | | | |
| 2A-04 | Press freedom and accountability journalism | | | |
| 2A-05 | Civil society strength (NGO density, protest rights) | | | |
| 2A-06 | Coalition stability / government durability | | | |
| 2A-07 | Populist or anti-democratic movement strength | | | |
| 2A-08 | Minority rights protection and political inclusion | | | |
| **Composite** | | | | |

**Score Definitions — Key Democracy Indicators:**

*2A-01 Electoral Integrity:*
- 1 = Clean elections; credible international monitoring; <2% irregularity rate
- 2 = Minor procedural irregularities; corrected by domestic institutions
- 3 = Significant irregularities; partial remedy; credibility contested by minority parties
- 4 = Systematic fraud or suppression; outcome legitimacy disputed by major parties
- 5 = Election nullified, annulled, or not held; constitutional crisis active

*2A-07 Populist / Anti-Democratic Movement Strength:*
- 1 = Marginal; <5% electoral support; no legislative presence
- 2 = Emerging; 5–15% support; limited parliamentary seats
- 3 = Significant; 15–30% support; capable of blocking legislation
- 4 = Major; >30% support; in or near government; democratic norms under active attack
- 5 = Dominant; anti-democratic forces control executive; systemic rollback underway

---

### Template 2B — Hybrid / Competitive Authoritarian

| # | Indicator | Score (1–5) | Observation / Evidence | Source |
|---|-----------|-------------|------------------------|--------|
| 2B-01 | Executive entrenchment (term limit manipulation, institutional capture) | | | |
| 2B-02 | Opposition viability (media access, legal harassment, candidate exclusion) | | | |
| 2B-03 | Patronage network stability (elite defection risk, business-state relations) | | | |
| 2B-04 | Succession clarity (designated successor, constitutional mechanism) | | | |
| 2B-05 | External legitimation dependency (donor states, multilateral bodies) | | | |
| 2B-06 | Coercive apparatus loyalty and internal factionalism | | | |
| 2B-07 | Public legitimacy erosion (protest frequency, approval trends) | | | |
| **Composite** | | | | |

*2B-02 Opposition Viability:*
- 1 = Robust opposition; full media access; no systematic harassment
- 2 = Mild restrictions; some media bias; sporadic legal pressure on individuals
- 3 = Significant restrictions; opposition media blocked; leaders face periodic detention
- 4 = Opposition neutered; leaders imprisoned or exiled; viable electoral challenge impossible
- 5 = Opposition legally banned or physically eliminated; single-party dominance absolute

---

### Template 2C — Authoritarian

| # | Indicator | Score (1–5) | Observation / Evidence | Source |
|---|-----------|-------------|------------------------|--------|
| 2C-01 | Personalist vs. institutionalized control (succession mechanism clarity) | | | |
| 2C-02 | Elite cohesion (politburo, oligarch, or inner circle unity) | | | |
| 2C-03 | Security sector loyalty (purge frequency, factional splits, FSB/military tension) | | | |
| 2C-04 | Propaganda effectiveness / public compliance and information control | | | |
| 2C-05 | Economic performance as legitimation tool | | | |
| 2C-06 | Nationalist narrative intensity | | | |
| 2C-07 | Repression escalation trend (prosecution rate, disappearances) | | | |
| 2C-08 | Diaspora and exile opposition capacity | | | |
| **Composite** | | | | |

*2C-01 Personalist Control / Succession Risk:*
- 1 = Institutionalized system; clear succession; leader replaceable without crisis
- 2 = Party/institution dominant; personal authority significant but bounded
- 3 = Significant personalism; succession unclear; inner circle factional risk
- 4 = Highly personalist; no viable designated successor; systemic instability if removed
- 5 = Total personalism; state inseparable from leader; succession would trigger collapse

*2C-02 Elite Cohesion:*
- 1 = Unified elite; no visible fractures; consensus decision-making operative
- 2 = Managed competition; factional differences contained; no defections
- 3 = Visible tension; siloviki vs. technocrats or rival factions; episodic defection signals
- 4 = Active elite competition; public signals of dissent from senior figures; purges occurring
- 5 = Elite fracture; active coup plotting or defections at senior level; regime survival in question

---

### Template 2D — Military Junta / Military-Guided Hybrid

| # | Indicator | Score (1–5) | Observation / Evidence | Source |
|---|-----------|-------------|------------------------|--------|
| 2D-01 | Intra-military factional cohesion (service branch rivalries, coup risk) | | | |
| 2D-02 | Transition roadmap credibility (if announced; timeline, benchmarks) | | | |
| 2D-03 | Civil-military relations (civilian institutional capacity, technocratic presence) | | | |
| 2D-04 | International isolation level and sanctions exposure | | | |
| 2D-05 | Armed group / insurgent challenge to junta authority | | | |
| 2D-06 | Economic management capacity (non-military expertise, budget credibility) | | | |
| **Composite** | | | | |

---

### Template 2E — Theocratic

| # | Indicator | Score (1–5) | Observation / Evidence | Source |
|---|-----------|-------------|------------------------|--------|
| 2E-01 | Clerical hierarchy unity vs. factional schism | | | |
| 2E-02 | Secular-technocratic vs. ideological governance tension | | | |
| 2E-03 | Religious legitimacy contestation (rival interpretations, competing clerical authorities) | | | |
| 2E-04 | Youth and urban alienation from theocratic order | | | |
| 2E-05 | Religious minority treatment and inter-communal stability | | | |
| 2E-06 | External ideological sponsors or rivals (competing theocratic models) | | | |
| **Composite** | | | | |

*2E-04 Youth/Urban Alienation:*
- 1 = Youth broadly integrated; theocratic identity reinforced by state education
- 2 = Generational gap emerging; urban youth passive non-compliance
- 3 = Significant alienation; protests or civil disobedience in urban centers; social media opposition
- 4 = Active resistance; sustained protest cycles; security force deployment to suppress youth unrest
- 5 = Generational revolt; regime survival dependent on mass repression of youth population

---

### FILLED EXAMPLE — Political Stability: Russia, 2026

**Regime Classification**: Authoritarian — Template 2C (Primary, weight 1.0)  
Secondary: Military-Guided Hybrid — Template 2D (consulted; weight applied if post-Putin succession triggers reclassification)

| # | Indicator | Score | Observation |
|---|-----------|-------|-------------|
| 2C-01 | Personalist control | 5 | No viable succession mechanism; constitutional amendments (2020) eliminate term-limit constraints; Putin consolidation complete post-2022 |
| 2C-02 | Elite cohesion | 3 | Wagner Group aftermath produced limited elite signaling (Prigozhin June 2023); siloviki retain loyalty; technocratic faction sidelined |
| 2C-03 | Security sector loyalty | 3 | FSB-GRU institutional tensions documented; no active fracture; Patrushev removal signals ongoing reshuffling |
| 2C-04 | Propaganda effectiveness | 4 | Domestic information space near-total state control; Roskomnadzor blocking pervasive; some urban/educated leakage via VPN |
| 2C-05 | Economic legitimation | 3 | War economy stabilized 2024–2025 via fiscal stimulus; sanctions pressure cumulative; structural deterioration masked |
| 2C-06 | Nationalist narrative | 5 | Great Power/civilizational war framing dominant; "special military operation" terminology enforced; denazification narrative sustained |
| 2C-07 | Repression escalation | 4 | Political prosecution rate at post-Soviet high; Navalny death in custody (Feb 2024); legal amendments criminalize "discrediting" armed forces |
| 2C-08 | Diaspora opposition | 2 | 700,000+ emigrated post-2022; fragmented; low operational capacity inside Russia |
| **Composite** | | **3.63** | **Elevated concern; succession risk and personalism are primary structural vulnerabilities** |

---

## Section 3: Economic Fragility Metrics Template

**Purpose**: Quantify economic conditions that amplify or constrain a state's conflict propensity, crisis resilience, and external coercibility.

| # | Indicator | Score (1–5) | Raw Data | Source | Notes |
|---|-----------|-------------|----------|--------|-------|
| 3-01 | GDP growth trend (3-year rolling average) | | % | | |
| 3-02 | Commodity / single-sector export dependency | | % of export revenue | | |
| 3-03 | Debt-to-GDP ratio | | % | | |
| 3-04 | External debt as % of GNI | | % | | |
| 3-05 | Foreign exchange reserves (months of import cover) | | months | | |
| 3-06 | Currency volatility (1-year range vs. USD) | | % swing | | |
| 3-07 | Trade concentration (top 3 partners as % of total trade) | | % | | |
| 3-08 | Inflation rate (CPI, annual) | | % | | |
| 3-09 | Youth unemployment rate | | % | | |
| 3-10 | Sanctions exposure (active multilateral/unilateral regimes) | | count/severity | | |
| 3-11 | Remittance dependency (% of GDP) | | % | | |
| 3-12 | Food import dependency (% of calories from imports) | | % | | |
| **Composite** | | | | | |

**Score Conversion Reference Table:**

| Indicator | Score 1 (Minimal) | Score 2 (Low) | Score 3 (Moderate) | Score 4 (Elevated) | Score 5 (Critical) |
|-----------|------------------|--------------|-------------------|-------------------|-------------------|
| 3-02 Commodity dependency | <20% | 20–40% | 40–60% | 60–80% | >80% |
| 3-03 Debt-to-GDP | <40% | 40–70% | 70–90% | 90–130% | >130% |
| 3-05 FX reserves | >6 months | 4–6 months | 3–4 months | 2–3 months | <2 months |
| 3-06 Currency volatility | <5% | 5–15% | 15–25% | 25–40% | >40% |
| 3-08 Inflation | <3% | 3–6% | 6–12% | 12–50% | >50% |
| 3-09 Youth unemployment | <10% | 10–18% | 18–30% | 30–50% | >50% |
| 3-10 Sanctions exposure | None | Targeted/individual | Sectoral (financial/energy) | Comprehensive | Comprehensive + energy isolation |
| 3-11 Remittance dependency | <1% GDP | 1–5% GDP | 5–15% GDP | 15–25% GDP | >25% GDP |

---

### FILLED EXAMPLE — Economic Fragility: Russia, 2026

| # | Indicator | Score | Raw Data |
|---|-----------|-------|----------|
| 3-01 | GDP growth trend | 3 | +1.2% official (2025); IMF adjusted estimate -0.3%; war spending inflating headline |
| 3-02 | Hydrocarbon export dependency | 4 | ~62% of export revenue from energy; crude oil rerouted to China/India |
| 3-03 | Debt-to-GDP | 1 | ~18%; low due to resource wealth; war spending elevated absolute deficit |
| 3-04 | External debt % GNI | 2 | ~25%; capital controls limit external refinancing pressure |
| 3-05 | FX reserves | 2 | ~$350B nominal; ~$300B frozen/inaccessible post-SWIFT actions; effective liquidity ~$180B |
| 3-06 | Ruble volatility | 4 | 35% swing range 2024–2025; capital controls masking true pressure |
| 3-07 | Trade concentration | 4 | China ~35%, India ~15%, Turkey ~10% = 60% in 3 partners |
| 3-08 | Inflation | 4 | ~9.5% official CPI; shadow estimates 15–18%; consumer goods 20–25% |
| 3-09 | Youth unemployment | 2 | ~14%; conscription absorbing male 18–35 cohort; female labor force participation rising |
| 3-10 | Sanctions exposure | 5 | Comprehensive G7/EU/UK sanctions; SWIFT partial exclusion; oil price cap mechanism; 12,000+ entities listed |
| 3-11 | Remittance dependency | 1 | Net sender; not materially applicable |
| 3-12 | Food import dependency | 2 | Major grain exporter; processed food and technology imports disrupted |
| **Composite** | | **2.83** | **Moderate fragility; war economy and capital controls masking structural vulnerabilities that will compound post-conflict** |

---

## Section 4: Military Capability Assessment Framework

### Template 4A — Conventional Forces

| # | Indicator | Score (1–5) | Evidence | Source |
|---|-----------|-------------|----------|--------|
| 4A-01 | Ground force order of battle (manpower, armor quantity and quality) | | | |
| 4A-02 | Air superiority / contested airspace capacity (fixed-wing, air defense) | | | |
| 4A-03 | Naval power projection capability (blue water, littoral, amphibious) | | | |
| 4A-04 | C4ISR integration level (command, control, comms, computers, intelligence, surveillance, reconnaissance) | | | |
| 4A-05 | Logistics and sustainment depth (fuel, ammunition, maintenance cycles) | | | |
| 4A-06 | Combat experience (recent operational record, last 10 years) | | | |
| 4A-07 | Mobilization capacity and reserve readiness | | | |
| 4A-08 | Equipment modernization rate (% of inventory modern/near-modern) | | | |
| **Composite** | | | | |

*4A-01 Ground Force OOB:*
- 1 = Minimal; constabulary/border force only; no combined arms capability
- 2 = Limited; brigade-size formations; poorly equipped; low readiness
- 3 = Capable; divisional-level combined arms; serviceable equipment; moderate readiness
- 4 = Substantial; corps-level combined arms; modern armor; high training tempo
- 5 = Major regional/global power; multi-theater projection; fully integrated combined arms

*4A-06 Combat Experience:*
- 1 = No recent combat; training-based readiness only
- 2 = Limited peacekeeping or counterterrorism operations
- 3 = Sustained COIN or limited conventional conflict; tactical learning documented
- 4 = Major conventional or hybrid conflict; operational-level learning; doctrine adapted
- 5 = High-intensity combined-arms warfare, active or recent; institutional learning at all levels

---

### Template 4B — Nuclear / WMD Capability

| # | Indicator | Score (1–5) | Evidence | Source |
|---|-----------|-------------|----------|--------|
| 4B-01 | Confirmed nuclear stockpile size and delivery system variety | | | |
| 4B-02 | Second-strike survivability (hardening, dispersal, SSBN capability) | | | |
| 4B-03 | Nuclear doctrine (deterrence posture vs. warfighting / first-use ambiguity) | | | |
| 4B-04 | Chemical / biological capability (if applicable; treaty compliance record) | | | |
| 4B-05 | Proliferation risk (technology export, weapons-grade material security) | | | |
| **Composite** | | | | |

**Non-Nuclear State Protocol**: Score 4B-01 and 4B-02 as N/A. Score 4B-05 based on acquisition risk (proximity to supplier networks, declared ambition). Composite = mean of applicable indicators only.

*4B-03 Nuclear Doctrine Posture:*
- 1 = No-first-use declared; minimum deterrence; de-alerting posture
- 2 = Ambiguous NFU; standard deterrence; no doctrine for sub-strategic use
- 3 = Flexible response; first use reserved for existential threats; modernization active
- 4 = "Escalate to de-escalate" signaled; tactical nuclear use integrated into operational doctrine
- 5 = Explicit first-use capability; coercive nuclear signaling ongoing; threshold dramatically lowered

---

### Template 4C — Asymmetric / Proxy / Irregular Capability

| # | Indicator | Score (1–5) | Evidence | Source |
|---|-----------|-------------|----------|--------|
| 4C-01 | Proxy network breadth and operational reliability | | | |
| 4C-02 | Insurgent / terrorist affiliate capacity (size, reach, lethality) | | | |
| 4C-03 | Guerrilla / IED / ambush operational doctrine maturity | | | |
| 4C-04 | Gray zone operations tempo (last 12 months: sabotage, assassination, hybrid incidents) | | | |
| 4C-05 | Use of mercenaries / private military contractors (PMCs) | | | |
| **Composite** | | | | |

*4C-04 Gray Zone Operations Tempo:*
- 1 = No documented gray zone activity
- 2 = Isolated incidents; ambiguous attribution; no pattern
- 3 = Recurring pattern; attribution established; diplomatic protests filed
- 4 = Active sustained campaign; multiple vectors (cyber + physical + info); escalation risk
- 5 = Continuous multi-domain gray zone warfare; threshold of armed conflict approached

---

### Template 4D — Cyber and Electronic Warfare

| # | Indicator | Score (1–5) | Evidence | Source |
|---|-----------|-------------|----------|--------|
| 4D-01 | Offensive cyber capability (attributed incidents, APT activity) | | | |
| 4D-02 | Critical infrastructure targeting capacity (power, water, finance, transport) | | | |
| 4D-03 | Electronic warfare / GPS jamming / spectrum dominance capability | | | |
| 4D-04 | Information operations / cognitive warfare integration (IO doctrine) | | | |
| 4D-05 | Defensive cyber resilience (CERT capacity, incident response, patch rates) | | | |
| **Composite** | | | | |

*4D-01 Offensive Cyber Capability:*
- 1 = No attributed offensive cyber operations; defensive posture only
- 2 = Limited capability; opportunistic intrusions; no strategic integration
- 3 = Established capability; APT groups attributed; espionage-focus predominant
- 4 = Sophisticated persistent capability; destructive attacks demonstrated; strategic integration
- 5 = Tier-1 cyber power; continuous offensive operations; critical infrastructure attacks deployed in conflict

---

### FILLED EXAMPLE — Military Capability: Russia, 2026

**4A — Conventional Forces:**

| # | Indicator | Score | Evidence |
|---|-----------|-------|----------|
| 4A-01 | Ground force OOB | 4 | ~350,000 active in Ukrainian theater; armor losses replaced by accelerated T-90M production; total ground force ~900,000 |
| 4A-02 | Air superiority | 3 | A2/AD perimeter intact; fixed-wing attrition significant; unable to achieve air superiority vs. integrated Ukrainian defense |
| 4A-03 | Naval projection | 3 | Black Sea Fleet degraded (flagship Moskva sunk; multiple corvettes lost); Arctic and Pacific fleets intact |
| 4A-04 | C4ISR integration | 3 | Improved from 2022 baseline; still below NATO standards; drone ISR integration accelerated |
| 4A-05 | Logistics/sustainment | 3 | Rail logistics competent over domestic distances; forward fuel and ammunition cycles strained under attrition rates |
| 4A-06 | Combat experience | 5 | Three+ years high-intensity combined arms; institutional learning across all echelons; drone and EW doctrine evolved rapidly |
| 4A-07 | Mobilization capacity | 4 | Second partial mobilization completed 2024; ~500,000 additional personnel integrated |
| 4A-08 | Equipment modernization | 3 | T-90M and Lancet drone production increased; legacy T-62 and T-55 still deployed due to attrition |
| **Composite** | | **3.50** | |

**4B — Nuclear/WMD:**

| # | Indicator | Score | Evidence |
|---|-----------|-------|----------|
| 4B-01 | Stockpile size/delivery | 5 | ~5,889 warheads (FAS estimate 2025); strategic triad operational; ~2,000 deployed |
| 4B-02 | Second-strike survivability | 5 | RS-28 Sarmat ICBMs operational; Delta IV/Borei SSBNs dispersed; Avangard hypersonic glide vehicle deployed |
| 4B-03 | Nuclear doctrine | 4 | "Escalate to de-escalate" doctrine; nuclear threshold ambiguity deliberately cultivated post-2022; updated nuclear doctrine (Sept 2024) lowers threshold explicitly |
| 4B-04 | Chemical/biological | 3 | Novichok use (Salisbury 2018) demonstrates state capability; Biological Weapons Convention signatory; compliance contested |
| 4B-05 | Proliferation risk | 2 | Not an active proliferator; North Korea ammunition transfers documented; some dual-use technology leakage |
| **Composite** | | **3.80** | |

**4C — Asymmetric/Proxy:**

| # | Indicator | Score | Evidence |
|---|-----------|-------|----------|
| 4C-01 | Proxy network | 4 | Hezbollah, Syrian regime forces, African PMCs (successor to Wagner); Axis of Resistance coordination |
| 4C-02 | Terrorist affiliates | 2 | No direct AQ/ISIS sponsorship; Chechen Kadyrov forces as irregular component |
| 4C-03 | IED/guerrilla doctrine | 3 | Extensive mine warfare; Russian mining of liberated territories documented |
| 4C-04 | Gray zone tempo | 5 | Continuous: Baltic cable cuts, European arson/sabotage campaign, assassination attempts in EU states, GPS jamming of commercial aviation |
| 4C-05 | PMC use | 4 | Africa Corps (Wagner successor) active in Mali, Niger, Libya, CAR, Sudan; ~15,000 personnel |
| **Composite** | | **3.60** | |

**4D — Cyber/EW:**

| # | Indicator | Score | Evidence |
|---|-----------|-------|----------|
| 4D-01 | Offensive cyber | 5 | GRU Sandworm (APT44); APT28 (Fancy Bear); SVR APT29 (Cozy Bear); continuous attribution |
| 4D-02 | CI targeting | 5 | Power grid attacks on Ukraine demonstrated at scale; financial sector attacks; Viasat disruption (Feb 2022) |
| 4D-03 | Electronic warfare | 4 | Krasukha-4; Murmansk-BN; GPS jamming of Baltic commercial aviation; drone EW decisive in Ukrainian theater |
| 4D-04 | Info ops integration | 5 | Strategic information warfare fully doctrinally integrated; GRU Unit 26165 operational; social media manipulation at industrial scale |
| 4D-05 | Defensive resilience | 3 | Significant domestic cyber defense; SORM surveillance infrastructure; vulnerable to Western cyber operations |
| **Composite** | | **4.40** | |

---

## Section 5: Social Cohesion and Identity Conflict Template

| # | Indicator | Score (1–5) | Evidence | Source |
|---|-----------|-------------|----------|--------|
| 5-01 | Ethnic fractionalization index (EFI) | | Fearon-Laitin / V-Dem / own assessment | |
| 5-02 | Religious fractionalization / sectarian tension | | | |
| 5-03 | Horizontal inequality (group-based economic disparities by ethnicity/religion) | | | |
| 5-04 | Gini coefficient / vertical income inequality | | | |
| 5-05 | Youth bulge (ages 15–29 as % of total population) | | % | |
| 5-06 | Youth unemployment (combined with 5-05 for grievance multiplier) | | % | |
| 5-07 | Historical grievance intensity (unresolved trauma, displaced persons, post-conflict legacy) | | | |
| 5-08 | Inter-communal violence frequency (last 5 years, ACLED) | | incident count | |
| 5-09 | Secessionist or autonomist movement strength | | | |
| 5-10 | Urban-rural polarization (political, economic, cultural cleavage) | | | |
| **Composite** | | | | |

**Grievance Multiplier Protocol**: If 5-05 (youth bulge score) ≥ 3 **AND** 5-06 (youth unemployment score) ≥ 3, multiply composite by **1.15** and flag as **Youth Mobilization Risk (YMR)**. Document in assessment header.

**Score Definitions:**

*5-01 Ethnic Fractionalization:*
- 1 = Homogeneous (>90% single group); no active minority tension
- 2 = Moderate diversity; minority rights institutionalized; political representation present
- 3 = Significant diversity; periodic communal friction; ethnicity politically salient
- 4 = Deep ethnic cleavages; ethnically-based parties; episodic communal violence
- 5 = Active ethnic conflict; political system structured around ethnic exclusion or domination

*5-04 Gini / Income Inequality:*
- 1 = Gini <0.30; broad middle class; low deprivation
- 2 = Gini 0.30–0.35; manageable inequality; social mobility present
- 3 = Gini 0.35–0.42; significant inequality; class tension politically activated
- 4 = Gini 0.42–0.50; sharp stratification; grievance mobilization occurring
- 5 = Gini >0.50; extreme inequality; oligarchic capture; revolutionary conditions possible

*5-05 Youth Bulge:*
- 1 = <20% of population aged 15–29; aging demographic
- 2 = 20–25%; moderate youth cohort
- 3 = 25–32%; significant youth demographic pressure
- 4 = 32–40%; classic youth bulge; historical correlation with conflict onset
- 5 = >40%; extreme youth bulge; state capacity cannot absorb labor market demand

---

### FILLED EXAMPLE — Social Cohesion: Ukraine (NATO Frontier State), 2026

| # | Indicator | Score | Evidence |
|---|-----------|-------|----------|
| 5-01 | Ethnic fractionalization | 3 | Russian-speaking minority (~17%); Crimea/Donbas populations excluded from count; wartime Ukrainian national consolidation strong offsetting factor |
| 5-02 | Religious fractionalization | 3 | Orthodox Church institutional split (OCU vs. UOC-MP); Moscow-linked parishes suppressed; Greek Catholic / Roman Catholic in West Ukraine |
| 5-03 | Horizontal inequality | 2 | Oligarchic structures weakened by war; Zelensky anti-oligarch reforms advanced; significant but declining |
| 5-04 | Gini coefficient | 2 | ~0.26 pre-war (low by regional standards); war disruption compressed extremes |
| 5-05 | Youth bulge | 2 | 22% of population 15–29 pre-war; declining sharply due to male casualties and emigration (~8M displaced) |
| 5-06 | Youth unemployment | 3 | Wartime conscription absorbed male 18–35; female youth unemployment elevated; economic sector collapse in East |
| 5-07 | Historical grievance | 4 | Holodomor, Soviet occupation, Chornobyl, Crimea annexation (2014), Donbas displacement (2014–2022), full-scale invasion — layered high-salience grievances |
| 5-08 | Inter-communal violence | 1 | Wartime suppression of internal conflict; pro-Russian collaboration prosecuted; near-zero inter-communal incidents |
| 5-09 | Secessionist movements | 1 | Occupied territories under Russian control; no internal separatism in government-controlled areas |
| 5-10 | Urban-rural polarization | 2 | War-driven internal migration; Kyiv-western province tension manageable; East-West cultural divide suppressed by war solidarity |
| **Composite** | | **2.30** | **Wartime solidarity suppressing typical indicators; monitor for post-conflict fragmentation once war ends** |

---

## Section 6: External Interference Vulnerability Assessment

| # | Indicator | Score (1–5) | Actor Identified | Vector | Source |
|---|-----------|-------------|-----------------|--------|--------|
| 6-01 | Economic coercion exposure (trade/energy leverage) | | | | |
| 6-02 | Foreign debt dependency on hostile/non-aligned creditor | | | | |
| 6-03 | Disinformation penetration by external actor | | | | |
| 6-04 | Proxy political party or movement presence | | | | |
| 6-05 | Foreign-controlled critical infrastructure (energy, telecoms, ports) | | | | |
| 6-06 | Diaspora remittance leverage (foreign state controls or targets diaspora) | | | | |
| 6-07 | Military basing or overflight rights held by external power | | | | |
| 6-08 | Intelligence service penetration (documented incidents, last 10 years) | | | | |
| 6-09 | Treaty / alliance dependence asymmetry (patron-client power imbalance) | | | | |
| 6-10 | Civil society capture by foreign-funded entities (hostile intent) | | | | |
| **Composite** | | | | | |

**Actor Mapping Instruction**: For each score ≥ 3, enter the specific interfering actor, primary vector (economic / political / information / military / intelligence), and current trend (escalating / stable / declining). Feed all identified actors directly into EDM network analysis (see Section 14).

**Score Definitions — 6-05 Foreign-Controlled Critical Infrastructure:**
- 1 = No significant foreign control of CI; domestic or allied ownership
- 2 = Minor foreign stakes; no strategic leverage; oversight mechanisms present
- 3 = Significant foreign ownership in one CI sector; leverage potential but limited
- 4 = Foreign control of strategic CI (major port, telecom backbone, power grid); leverage actively exercised
- 5 = Systemic foreign control across multiple CI sectors; state sovereignty over infrastructure severely compromised

---

## Section 7: Regional Power Dynamics Mapping Methodology

### Step 1 — Actor Inventory

List all actors with meaningful influence in the region. Be exhaustive: include non-state armed groups, diaspora organizations with political leverage, and major multilateral bodies.

| Actor | Type | Primary Interests | Key Capabilities | Current Posture |
|-------|------|--------------------|-----------------|-----------------|
| [State A] | Hegemon / Challenger / Status Quo / Revisionist | | | Assertive / Deterrent / Cooperative / Hedging |
| [State B] | Regional Power / Swing State | | | |
| [Non-state A] | Armed Group / IO / MNC | | | |
| [Multilateral] | Alliance / IO / Coalition | | | |

**Actor Type Definitions:**
- **Regional Hegemon**: Dominant military/economic power within the geographic theater
- **External Great Power**: Global-level state projecting influence into region (US, China, Russia)
- **Revisionist Power**: Seeks to alter current territorial, governance, or norm arrangements
- **Status Quo Power**: Benefits from current order; resists change
- **Swing State**: Relationships with multiple blocs; strategic posture contestable
- **Proxy Actor**: Non-state entity receiving material support from external state

### Step 2 — Relationship Matrix

Construct a directed relationship matrix. Score each dyad using the scale below. The matrix is directional: Actor A's relationship toward B may differ from B's toward A. Average both directions for the bilateral score.

| | Actor A | Actor B | Actor C | Actor D |
|---|---------|---------|---------|---------|
| **Actor A** | — | | | |
| **Actor B** | | — | | |
| **Actor C** | | | — | |
| **Actor D** | | | | — |

**Dyad Scoring Scale:**
- **+2** = Formal alliance, defense treaty, deep integration
- **+1** = Aligned, cooperative, no formal treaty
- **0** = Neutral / no significant relationship
- **-1** = Competitive, adversarial but managed; no active conflict
- **-2** = Active conflict or crisis-level hostility; armed incidents occurring

### Step 3 — Regional Influence Score (RIS)

For each actor, calculate **Regional Influence Score**:

```
RIS = (Military Capability Composite × 0.30)
    + (Economic Weight in Region × 0.25)
    + (Political Alignment Score × 0.20)
    + (Information Influence Index × 0.15)
    + (Diplomatic Network Density × 0.10)
```

All inputs normalized 1–5. RIS range: 1.00–5.00. Actors with RIS ≥ 4.0 are **High-Leverage Nodes** — their posture changes disproportionately affect regional stability.

### Step 4 — Regional Stability Assessment

Sum all dyad scores in relationship matrix. Divide by number of dyads (n × (n-1) / 2 for n actors).

| Mean Dyad Score | Regional Order Classification | QSFE Action |
|-----------------|------------------------------|-------------|
| ≥ +0.5 | Generally cooperative order | Routine monitoring |
| 0 to +0.5 | Managed competition; fragile stability | Quarterly QSFE run |
| -0.5 to 0 | Latent conflict; active rivalry | Monthly QSFE run |
| < -0.5 | Conflict-prone; hegemonic competition | Trigger framework (Section 8) mandatory; bi-weekly QSFE |

---

## Section 8: Trigger Event Identification Framework

### Template 8A — Trigger Typology

For each category, identify plausible trigger events and assign **Probability (P)** and **Impact (I)** scores (1–5). Compute **Trigger Priority Score (TPS) = P × I**.

| Category | Trigger Event | P (1–5) | I (1–5) | TPS | QSFE Tier |
|----------|---------------|---------|---------|-----|-----------|
| **Political** | Leadership death / incapacitation | | | | |
| **Political** | Election irregularity / disputed result | | | | |
| **Political** | Coup attempt / constitutional crisis | | | | |
| **Political** | Sudden leadership change (purge, resignation) | | | | |
| **Economic** | Currency collapse / sovereign default | | | | |
| **Economic** | Commodity price shock (energy/food) | | | | |
| **Economic** | Sanctions escalation / financial decoupling | | | | |
| **Military** | Cross-border incident / skirmish | | | | |
| **Military** | Military exercise escalation / miscalculation | | | | |
| **Military** | Nuclear or WMD use / credible threat | | | | |
| **Military** | Precision strike on high-value target | | | | |
| **Social** | Mass protest / popular uprising | | | | |
| **Social** | Major terrorist attack on key target | | | | |
| **Social** | Ethnic / sectarian violence outbreak | | | | |
| **Environmental** | Natural disaster compounding instability | | | | |
| **Environmental** | Resource scarcity crisis (water, food) | | | | |
| **External** | Great power direct military intervention | | | | |
| **External** | Alliance activation (Article 5 or equivalent) | | | | |

**TPS-to-QSFE Tier Mapping:**

| TPS | QSFE Tier | Action Required |
|-----|-----------|-----------------|
| ≥ 20 | Tier I | Immediate QSFE run; Crisis Protocol notification |
| 15–19 | Tier I | QSFE priority run; senior analyst review |
| 10–14 | Tier II | QSFE standard run; bi-weekly monitoring |
| 5–9 | Tier III | QSFE background queue; monthly monitoring |
| < 5 | N/A | Background monitoring only; reassess quarterly |

### Template 8B — Trigger Cascade Analysis

For any TPS ≥ 15 trigger, complete cascade analysis:

```
PRIMARY TRIGGER: [Event description]
     ↓
IMMEDIATE EFFECTS (0–72 hours):
  - Political: [response]
  - Military: [response]
  - Economic: [response]
  - Information: [response]
     ↓
SHORT-TERM EFFECTS (72 hours – 2 weeks):
  - [key developments]
  - Market signals: [currency/energy/equity impacts]
     ↓
MEDIUM-TERM EFFECTS (2 weeks – 6 months):
  - [structural changes]
  - Alliance posture shifts: [key dyad changes]
     ↓
STRUCTURAL EFFECTS (6+ months):
  - [irreversible changes to regional order]
     ↓
QSFE SCENARIO BRANCHES:
  ├─ Branch A — Most Likely ([%]): [description]
  ├─ Branch B — Adverse ([%]): [description]
  └─ Branch C — Catastrophic ([%]): [description]
```

---

### FILLED EXAMPLE — Trigger Analysis: Eastern Europe (Russia-NATO Frontier), 2026

| Trigger Event | P | I | TPS | QSFE Tier |
|---------------|---|---|-----|-----------|
| Russian tactical nuclear use in Ukraine | 2 | 5 | 10 | II |
| NATO Article 5 activation — Baltic incident | 2 | 5 | 10 | II |
| Putin incapacitation / succession crisis | 2 | 5 | 10 | II |
| Ukrainian counteroffensive reaching Russian territory | 3 | 4 | 12 | II |
| Russian energy infrastructure attack on EU member state | 3 | 4 | 12 | II |
| Prolonged attritional stalemate; no territorial resolution | 5 | 2 | 10 | II |
| Ceasefire / frozen conflict stabilization agreement | 3 | 3 | 9 | III |
| Russian mobilization to 1,000,000+ active | 3 | 3 | 9 | III |
| NATO member internal political crisis undermining solidarity | 3 | 3 | 9 | III |

**Cascade Analysis — NATO Article 5 Activation (Baltic Incident):**

```
PRIMARY TRIGGER: Russian special forces or ambiguous hybrid operation
  causes casualties in Estonian or Latvian territory
     ↓
IMMEDIATE EFFECTS (0–72h):
  - Political: NATO Article 4 consultations invoked; Baltic states declare
    national emergency; emergency UN Security Council session
  - Military: NATO air policing mission surged; Baltic NATO rapid reaction
    force elevated to full readiness; US EUCOM force posture elevated
  - Economic: EUR/USD -3%; Brent crude +12%; European defense equities +8%
  - Information: Russian denial campaign; NATO/EU information coordination
    activated; OSIQP detects coordinated Russian disinformation surge
     ↓
SHORT-TERM EFFECTS (72h – 2wk):
  - NATO Article 5 deliberations; threshold determination debate (armed attack?)
  - US force posture in Europe elevated (carrier battle group + 82nd Airborne)
  - Russia threatens "asymmetric" response; ICBM exercise signaling
  - Belarus position critical: will it mobilize in support?
  - EU emergency economic measures; financial transaction monitoring
     ↓
MEDIUM-TERM EFFECTS (2wk – 6mo):
  - NATO military response options: limited punitive strike vs. sustained campaign
  - Sweden/Finland integration into Baltic defense architecture accelerated
  - Germany Zeitenwende 2.0: defense spending surge to 3%+ GDP
  - Nordic-Baltic corridor security dominates EU agenda
  - China watches for US commitment signal re: Taiwan parallel
     ↓
STRUCTURAL EFFECTS (6+ months):
  - EITHER: Deterrence holds; Russia backs down to gray zone operations
  - OR: Escalation ladder climbed; conventional NATO-Russia conflict; nuclear signaling intensifies
     ↓
QSFE BRANCHES:
  ├─ Branch A — De-escalation (45%): Article 5 declared; limited NATO response;
  │   Russia backs down; frozen deterrence becomes new baseline; major
  │   NATO military buildup in Baltics; Russian gray zone ops continue
  ├─ Branch B — Limited Conventional Conflict (35%): Conventional
  │   exchange in Baltic theater; air/ground operations; no nuclear use;
  │   ceasefire within 60 days; large territorial and civilian cost
  └─ Branch C — Major Escalation (20%): Full NATO-Russia conventional
      conflict; nuclear threshold signals crossed; QSFE highest-priority
      watch; Orion Station simulation activated
```

---

## Section 9: Fragile State Early Warning Indicators

Use this checklist when composite scores across Sections 2–6 average ≥ 3.0, **or** when any single indicator scores 5. Completion is mandatory for all QSFE Tier I assessments.

### Tier 1 — Acute Warning (any single indicator = immediate crisis protocol escalation)

- [ ] State monopoly on violence lost in ≥ 1 major territory or provincial capital
- [ ] Central bank unable to conduct normal operations (payments, currency issuance)
- [ ] Head of state fled, incapacitated, or publicly defied by senior military command
- [ ] Multiple simultaneous armed factions with territorial control inside recognized borders
- [ ] Mass atrocity indicators present: civilian displacement >500,000 persons in 30 days
- [ ] Foreign military intervention underway without host-state consent

**Action**: Any Tier 1 indicator triggers immediate notification to QGIA Crisis Protocols (QGIA-KL-CP series) and QSFE emergency run.

### Tier 2 — Structural Warning (3+ indicators = elevated watch; monthly QSFE run required)

- [ ] GDP decline ≥ 10% in any consecutive 12-month period
- [ ] Inflation ≥ 50% (hyperinflation threshold; IMF definition)
- [ ] Security forces conducting systematic offensive operations against civilian population
- [ ] Major opposition leaders arrested, exiled, killed, or forced to flee in 60-day window
- [ ] Critical infrastructure failure in capital region (power, water, communications)
- [ ] Neighboring states accepting refugee flows exceeding 100,000 in 30 days
- [ ] UN Security Council emergency session or resolution invoked
- [ ] State unable to pay civil service salaries for ≥ 2 consecutive months

### Tier 3 — Trend Warning (5+ indicators = 6-month deterioration trajectory; quarterly reassessment)

- [ ] Press freedom index (RSF/Freedom House) declining 2+ consecutive annual assessments
- [ ] Judicial independence score declining (V-Dem or Freedom House)
- [ ] Military budget as % of GDP increasing >2 percentage points above 5-year baseline
- [ ] Youth unemployment increasing 3+ consecutive quarters
- [ ] Protest frequency increasing year-over-year (OSIQP CivicSignal module)
- [ ] Foreign direct investment declining 2+ consecutive years
- [ ] Regional power changing posture from neutral/cooperative to competitive toward target state
- [ ] Diaspora remittances declining (economic distress signal from emigrant community)
- [ ] External debt service ratio rising to >20% of export revenue

---

## Section 10: Alliance Commitment Reliability Scoring

**Purpose**: Assess how reliably alliance commitments will be honored in crisis conditions, accounting for political will, military capability, and strategic interest alignment.

| # | Indicator | Score (1–5) | Evidence | Source |
|---|-----------|-------------|----------|--------|
| 10-01 | Treaty formality (formal mutual defense treaty vs. informal alignment) | | | |
| 10-02 | Historical commitment record (prior crises, 25-year window) | | | |
| 10-03 | Domestic political support for alliance commitment in defending country | | | |
| 10-04 | Military interoperability (joint exercises, doctrine, equipment standardization) | | | |
| 10-05 | Economic interdependence with treaty partner | | | |
| 10-06 | Geographic proximity (strategic depth between defender and theater) | | | |
| 10-07 | Nuclear umbrella credibility (if extended deterrence is claimed) | | | |
| 10-08 | Competing commitments / strategic overextension of defending country | | | |
| 10-09 | Political leadership alignment (current government disposition toward commitment) | | | |
| 10-10 | Public opinion in defending country | | | |
| **Composite** | | | | |

**Score Definitions:**

*10-01 Treaty Formality:*
- 1 = No formal arrangement; informal alignment only; no binding obligation
- 2 = Memorandum of understanding or political declaration; non-binding
- 3 = Bilateral mutual defense arrangement; binding but not multilateral
- 4 = Multilateral collective defense treaty; formally ratified; legal obligation
- 5 = Highest-formality treaty; explicit military integration; automatic response mechanism

*10-02 Historical Commitment Record:*
- 1 = No record of honoring commitments; abandonment documented
- 2 = Mixed record; commitment honored selectively based on interest
- 3 = Generally reliable; one notable failure or hedge in 25-year window
- 4 = Reliable record; commitments honored consistently; credible deterrent
- 5 = Perfect record; commitments tested and honored at cost; no ambiguity

**Alliance Reliability Tiers:**
- **Composite 4.0–5.0**: High reliability — alliance will almost certainly honor commitment; base scenarios on fulfillment
- **Composite 3.0–3.9**: Conditional reliability — commitment probable; political management required; hedge in extreme scenarios
- **Composite 2.0–2.9**: Low reliability — commitment uncertain; include fulfillment failure as QSFE scenario branch
- **Composite < 2.0**: Unreliable — do not base scenario planning on commitment fulfillment; treat as non-aligned

---

### FILLED EXAMPLE — Alliance Reliability: US–NATO Commitment to Baltic States, 2026

| # | Indicator | Score | Evidence |
|---|-----------|-------|----------|
| 10-01 | Treaty formality | 5 | Article 5, Washington Treaty; ratified by all 32 members; legally binding collective defense |
| 10-02 | Historical record | 4 | Article 5 never invoked for combat response; Cold War deterrence maintained successfully; Kosovo, Afghanistan precedents |
| 10-03 | Domestic political support | 3 | US internal debate ongoing; Republican faction challenges aid but not Article 5 per se; European NATO members unified |
| 10-04 | Interoperability | 5 | Decades of joint exercises; STANAG integration; shared ISR; Baltic Air Policing operational |
| 10-05 | Economic interdependence | 4 | Transatlantic trade ~$1.3T annually; deep financial integration; NATO defense industrial base interdependence |
| 10-06 | Geographic proximity | 3 | US strategic depth substantial; NATO forward presence in Baltics limited (EFP battlegroups ~1,500/country) |
| 10-07 | Nuclear umbrella | 4 | Extended deterrence credible; NATO nuclear sharing operational; "tactical nuclear use" scenario reduces to 3 |
| 10-08 | Competing commitments | 3 | Indo-Pacific rebalancing creates strategic resource competition; AUKUS, Taiwan contingency planning compete for attention |
| 10-09 | Leadership alignment | 3 | Administration commitment variable across electoral cycles; European burden-sharing tension active |
| 10-10 | US public opinion | 3 | Support for Ukraine aid declining (62% → 47%, 2023–2026); direct NATO defense of Baltic states more broadly supported (~65%) |
| **Composite** | | **3.70** | **Conditional reliability — credible deterrent but not automatic; political management and burden-sharing resolution required** |

---

## Section 11: Information Environment Assessment

| # | Indicator | Score (1–5) | Evidence | Source |
|---|-----------|-------------|----------|--------|
| 11-01 | Press freedom (RSF World Press Freedom Index / Freedom House) | | | |
| 11-02 | State media dominance (% audience share, editorial control, funding) | | | |
| 11-03 | Internet freedom (censorship level, shutdown frequency, surveillance infrastructure) | | | |
| 11-04 | Social media platform access (blocked/restricted platforms; VPN prevalence) | | | |
| 11-05 | Disinformation prevalence (documented campaigns, last 12 months) | | | |
| 11-06 | Foreign disinformation actor presence and attribution | | Actor: | |
| 11-07 | Journalist safety (killings, imprisonments in trailing 5 years) | | count | |
| 11-08 | AI-generated / synthetic content share in regional information space (estimated) | | % | |
| 11-09 | Civil society media literacy and counter-disinformation capacity | | | |
| 11-10 | Electoral information integrity (last election cycle) | | | |
| **Composite** | | | | |

**Score Definitions:**

*11-03 Internet Freedom:*
- 1 = Open internet; no political censorship; no documented mass surveillance
- 2 = Selective filtering; some political content restricted; limited surveillance
- 3 = Significant censorship; VPN use widespread; periodic shutdowns; social media monitoring
- 4 = Near-total filtration; only state-approved content permitted; opposition online speech criminalized
- 5 = Complete national internet control; intranet model; all external platforms blocked; access monitored at individual level

*11-05 Disinformation Prevalence:*
- 1 = No significant domestic or foreign disinformation activity detected
- 2 = Isolated campaigns; low reach; quickly debunked by civil society
- 3 = Regular campaigns; moderate reach; partial platform compliance with takedowns
- 4 = Sustained industrial-scale campaigns; significant audience penetration; fact-checking capacity overwhelmed
- 5 = Disinformation dominates key political narratives; epistemological crisis; public unable to distinguish state and non-state reality frames

**OSIQP Integration Note**: Indicators 11-05, 11-06, and 11-08 are directly populated from OSIQP sentiment and narrative-tracking modules. Before completing this section, query:
- **Narrative velocity**: Rate of spread for key disinformation frames in regional discourse
- **Cross-platform amplification coefficient**: Coordination index across Twitter/X, Telegram, TikTok, VKontakte
- **Inauthentic account ratio**: Bot proportion in regional political discussion streams

Access via: OSIQP Dashboard → `NarrativeTrack-Disinfo` → `[REGION_ID]` → trailing 30-day report.

---

## Section 12: Scenario Generation — Template-to-QSFE Integration

### Step 1 — Regional Threat Profile (RTP) Aggregation

Compile all section composites into a single RTP summary:

| Section | Domain | Composite Score | Confidence Weight | Weighted Score |
|---------|--------|-----------------|-------------------|----------------|
| 2 | Political Stability | | | |
| 3 | Economic Fragility | | | |
| 4A | Conventional Military Capability | | | |
| 4B | Nuclear / WMD Capability | | | |
| 4C | Asymmetric / Proxy Capability | | | |
| 4D | Cyber / Electronic Warfare | | | |
| 5 | Social Cohesion | | | |
| 6 | External Interference Vulnerability | | | |
| 10 | Alliance Commitment Reliability (inverse: high score = low risk) | | | |
| 11 | Information Environment (hostility) | | | |
| **RTP TOTAL** | | | | |

**Inversion Note for Section 10**: Alliance Reliability is a **protective** factor. Invert before including in RTP: `RTP_10 = 6 − [Composite_10]`. A highly reliable alliance (score 5) contributes 1 to RTP (low threat); an unreliable alliance (score 1) contributes 5 (high threat from absence of support).

**RTP Thresholds and Review Cadence:**

| RTP Total | Risk Level | Review Cadence | QSFE Action |
|-----------|-----------|----------------|-------------|
| < 2.0 | Low | Quarterly | Routine run |
| 2.0–2.9 | Managed | Quarterly | Standard run |
| 3.0–3.5 | Elevated | Monthly | Priority run |
| 3.6–4.0 | High | Bi-weekly | Priority run + trigger monitoring |
| > 4.0 | Critical | Continuous | Emergency protocol; daily OSIQP sweep |

### Step 2 — QSFE Input Package

Structure the input package as follows:

```
QSFE INPUT PACKAGE
==================
Region:         [Name]
Assessment Date: [YYYY-MM-DD]
Analyst ID:     [ID]
RTP Score:      [x.xx]  Risk Level: [Low/Managed/Elevated/High/Critical]
Confidence Score: [0.00–1.00]

DRIVER VARIABLES (Sections 2–11; top 5 by score):
  1. [Variable name]: [Score]
  2. [Variable name]: [Score]
  3. [Variable name]: [Score]
  4. [Variable name]: [Score]
  5. [Variable name]: [Score]

TRIGGER EVENTS (Section 8; TPS ≥ 10):
  - [Trigger]: P=[x], I=[x], TPS=[xx], Tier [I/II/III]
  - [Trigger]: P=[x], I=[x], TPS=[xx], Tier [I/II/III]

ACTOR NETWORK (Section 7 dyad matrix; summarized):
  [Actor A]–[Actor B]: [score]
  [Actor A]–[Actor C]: [score]
  ...

CONSTRAINTS:
  Time horizon:        [30 / 90 / 180 / 365 days]
  Scenario count:      [3 / 5 / 10]
  Output tier filter:  [Tier I only / I+II / All]
  Special instruction: [any analyst override or focus area]
```

### Step 3 — QSFE Output Interpretation

QSFE returns a probabilistic scenario tree. Map outputs to three required scenario types for analyst deliverable:

| Scenario Type | QSFE Tier | Probability Band | Analyst Action |
|---------------|-----------|------------------|----------------|
| **Most Likely (ML)** | Tier I | >25% | Full narrative + policy implications + indicator thresholds |
| **Adverse (AD)** | Tier I–II | 10–25% | Contingency planning brief + early warning indicators |
| **Catastrophic (CAT)** | Tier III | <10% | Trigger thresholds + crisis protocol pre-positioning |

**Manual Adjustment Protocol**: Do not manually adjust QSFE probabilities post-output unless new trigger event information justifies re-input. All manual overrides must be logged with: analyst ID, rationale, evidence basis, and supervisor sign-off. Aurora stores all adjustment history.

### Filled Example — QSFE Package: Eastern Europe, 2026

```
QSFE INPUT PACKAGE
==================
Region:         Eastern Europe / Russia-NATO Frontier
Assessment Date: 2026-03-13
Analyst ID:     [QGIA-RE-EE-001]
RTP Score:      3.74   Risk Level: HIGH
Confidence Score: 0.81

DRIVER VARIABLES:
  1. Cyber/Info Ops Capability (4D): 4.40
  2. Nuclear Doctrine Posture (4B): 3.80
  3. Asymmetric/Gray Zone Ops (4C): 3.60
  4. Political Stability/Personalism (2C): 3.63
  5. Economic Fragility (3): 2.83

TRIGGER EVENTS (TPS ≥ 10):
  - NATO Article 5 activation, Baltic incident: P=2, I=5, TPS=10, Tier II
  - Russian tactical nuclear use in Ukraine: P=2, I=5, TPS=10, Tier II
  - Putin succession crisis: P=2, I=5, TPS=10, Tier II
  - Ukrainian counteroffensive reaching Russian territory: P=3, I=4, TPS=12, Tier II
  - Russian CI attack on EU member state: P=3, I=4, TPS=12, Tier II

ACTOR NETWORK (key dyads):
  Russia–NATO: -2  |  Russia–Ukraine: -2  |  Russia–Belarus: +2
  Russia–China: +1 |  NATO–Ukraine: +1    |  US–EU: +2
  NATO–China: -1   |  China–Ukraine: 0    |  Russia–India: +1

CONSTRAINTS:
  Time horizon:    180 days
  Scenario count:  5
  Output filter:   Tier I + II
  Special:         Flag any Putin health/succession signals as priority
```

**QSFE Output Summary (illustrative):**
- **ML Scenario (Tier I, ~38%)**: Continued attritional warfare; no major territorial change; Western support sustained at reduced levels; frozen conflict trajectory emerging; sanctions regime partially eroded
- **AD Scenario (Tier I, ~27%)**: Russian limited offensive gains in Zaporizhzhia or Kharkiv region; NATO internal cohesion debate intensifies; conditional ceasefire pressure builds; US electoral cycle creates commitment uncertainty
- **CAT Scenario (Tier II, ~15%)**: Russian energy/infrastructure attack on EU member state triggers Article 5 consultation; escalation ladder activated; markets: EUR/USD -8%; Brent crude +25%; full NATO-Russia crisis posture

---

## Section 13: Cross-Regional Comparison Methodology

### Regional Threat Profile Comparison Table

Populate when assessing two or more regions simultaneously. Supports resource allocation and QSFE priority sequencing.

| Domain | Eastern Europe | South China Sea | Middle East | Sub-Saharan Africa |
|--------|----------------|----------------|-------------|-------------------|
| Political Stability | 3.63 | 3.20 | — | — |
| Economic Fragility | 2.83 | 2.40 | — | — |
| Conventional Military | 3.50 | 4.00 | — | — |
| Nuclear / WMD | 3.80 | 4.50 | — | — |
| Asymmetric / Proxy | 3.60 | 2.80 | — | — |
| Cyber Capability | 4.40 | 4.80 | — | — |
| Social Cohesion | 2.30 | 2.60 | — | — |
| External Interference | — | 3.40 | — | — |
| Alliance Reliability (inverted) | 2.30 | 2.80 | — | — |
| Information Environment | — | 3.20 | — | — |
| **RTP Total (illustrative)** | **3.74** | **3.37** | — | — |
| **QSFE Priority Tier** | **HIGH** | **ELEVATED** | — | — |

### South China Sea Filled Example (Abbreviated)

**Regime Classification**: China — Authoritarian (Template 2C); Taiwan — Democracy (Template 2A)

**Key Scores for Cross-Regional Comparison:**

| Domain | Score | Key Driver |
|--------|-------|------------|
| Political Stability (China 2C) | 3.20 | Xi consolidation strong; Taiwan Strait legitimation pressure; succession opaque |
| Economic Fragility | 2.40 | Diversified; property sector crisis; US decoupling risk (3-10: Tier II tariff threat) |
| Conventional Military (PLA) | 4.00 | Largest ground force; naval tonnage surpassed US in 2020; A2/AD mature |
| Nuclear/WMD | 4.50 | ~500 warheads; DF-41/DF-5B ICBM; SSBN capability (Jin-class); rapid buildup |
| Cyber (PLA Unit 61398 et al.) | 4.80 | APT40, APT41, Volt Typhoon (CI pre-positioning in US); most prolific state cyber actor |
| Social Cohesion (China) | 2.60 | Han majority; Uyghur/Tibetan suppression elevated; Hong Kong post-NSL stability |
| Alliance Reliability (US–Taiwan, inverted) | 2.80 | TRA ambiguous; "strategic ambiguity" policy; domestic US political debate on commitment |

**Key South China Sea Triggers:**

| Trigger | P | I | TPS | Tier |
|---------|---|---|-----|------|
| PLA amphibious exercise adjacent to Taiwan | 4 | 3 | 12 | II |
| PLAN vessel collision with USN ship in SCS | 3 | 4 | 12 | II |
| Taiwan presidential declaration / independence signal | 2 | 5 | 10 | II |
| PLA military encirclement exercise (beyond Aug 2022) | 3 | 4 | 12 | II |
| US FONOP resulting in armed incident | 3 | 4 | 12 | II |
| PLA seizure of outlying Taiwan islands (Kinmen/Matsu) | 2 | 5 | 10 | II |

### Standardization Protocol

1. All regional assessments must use the same scoring reference period (default: trailing 12 months from assessment date)
2. Use identical data sources for cross-regional comparisons where available: World Bank, IMF, SIPRI, Freedom House, RSF, ACLED, V-Dem
3. Record source and date for every raw data point to enable version comparison and trend analysis
4. When comparing regions with different regime types, note that Section 2C (Authoritarian) scores are structurally higher on 2C-06 (Nationalism) and 2C-07 (Repression) than 2A (Democracy) by design. Apply **cross-template normalization offset of −0.5** to 2C-06 and 2C-07 before entering into cross-regional composite

### Priority Ranking Output

After populating comparison table, rank regions by RTP Total (highest = highest resource priority). Where RTP scores differ by < 0.3 between regions, apply **Trigger Density Tiebreaker**: count TPS ≥ 10 triggers from Section 8; higher count takes priority rank.

---

## Section 14: QGIA Integration Notes

### EDM — Entanglement Dynamics Mapper

**Primary Use Cases in Regional Threat Assessment:**

**1. Actor Network Visualization**  
Feed the relationship matrix from Section 7 (Step 2) directly into EDM. EDM renders directional alliance/conflict graphs and calculates **network centrality** for each actor (betweenness, eigenvector, degree). High-centrality actors (betweenness > 2σ above mean) are disproportionate stability levers — their posture change has outsized impact on regional order.

**2. External Interference Mapping**  
From Section 6, all actors scoring ≥ 3 are entered as **interference nodes**. EDM traces second- and third-order network effects. Example cascade: Russian financial leverage on Hungarian domestic politics → NATO internal cohesion reduction → Article 5 response reliability degradation → Baltic deterrence credibility erosion.

**3. Alliance Evolution Tracking**  
EDM monitors dyad score changes over time. A decline of ≥ 1 point in any major dyad within 90 days triggers automatic OSIQP monitoring sweep and analyst notification.

**EDM Query Template:**
```python
EDM.query(
  region        = "[REGION_ID]",
  actors        = [list_from_Section_7],
  dyad_matrix   = [Section_7_Step2_output],
  interference_nodes = [Section_6_actors_score_gte_3],
  time_window   = "trailing_12_months",
  output        = ["centrality", "network_graph", "change_alerts",
                   "cascade_simulation"]
)
```

### OSIQP — Open-Source Intelligence Quantitative Platform

**Specifications**: 156 qubit-equivalent processing; 94.7% sentiment accuracy; <50ms latency; 500TB daily intake.

**Primary Use Cases:**

**1. Automated Indicator Population**  
OSIQP auto-populates data fields in Sections 11 (Information Environment), 5-08 (Inter-communal violence frequency from ACLED), and 8A (trigger probability estimates from signal frequency analysis). Pull pre-populated drafts from OSIQP before beginning manual scoring.

**2. Real-Time Sentiment and Narrative Monitoring**  
OSIQP's 94.7% sentiment accuracy enables monitoring across:
- Elite narrative signals (official statements, state media framing changes)
- Mass mobilization sentiment (protest organization language, grievance amplification)
- Disinformation campaign detection (coordinated inauthentic behavior, bot network activation)
- Cross-border narrative export (how Actor A's framing is seeding Actor B's information space)

**3. Trigger Event Early Detection**  
OSIQP flags abnormal signal spikes (>2σ above 30-day baseline) in monitored streams. Any spike in a region with RTP ≥ 3.0 automatically queues a QSFE micro-run. Analyst receives notification within <50ms of flag.

**Standard OSIQP Query Types:**

| Query Type | OSIQP Module | Output |
|------------|-------------|--------|
| Baseline sentiment sweep | `Sentiment-Regional` | 30-day trend; top 10 narrative frames; sentiment polarity |
| Disinformation detection | `NarrativeTrack-Disinfo` | Campaign IDs; origin attribution; spread velocity |
| Elite signal monitoring | `EliteTrack` | Official statement analysis; positional change flags; tone delta |
| Social mobilization | `CivicSignal` | Protest probability score; organizational network density |
| Economic sentiment | `EconSentiment` | Market/public confidence indices; currency speculation signals |
| Cross-border narrative | `NarrativeExport` | Narrative seeding patterns; foreign media amplification |

### Aurora Integration

All template outputs, QSFE runs, and EDM graphs are logged in Aurora's analytical memory layer. When reassessing a region, Aurora provides:
- Prior assessment version comparison with delta highlighting
- Analyst accuracy scoring (post-event calibration against QSFE predictions)
- Automated indicator delta reports (what changed since last assessment)
- Cross-analyst consistency flagging (when two analysts score same region differently)

**Access**: `Aurora.regional_dashboard([REGION_ID])` → "Assessment History" → "Delta Report"  
**Version archiving**: All submitted assessments are immutable once signed. Amendments require new version with change log.

---

## Section 15: Assessment Completion Checklist

Before submitting a completed regional threat assessment for QSFE input, confirm all items are complete:

**Section Completion:**
- [ ] Regime type classified using Section 1 decision tree; Primary/Secondary documented
- [ ] Correct political stability template (2A–2E) completed; all rows scored
- [ ] Section 3 economic indicators populated with raw data, score, and source citation
- [ ] All four military capability templates (4A–4D) scored; N/A exclusions documented
- [ ] Section 5 social cohesion composite calculated; Grievance Multiplier check completed
- [ ] Section 6 external interference actors identified with actor, vector, and trend
- [ ] Section 7 actor inventory and relationship matrix completed; RIS calculated per actor
- [ ] Section 8 trigger events scored; TPS calculated; QSFE tier assigned to each trigger
- [ ] Section 8 cascade analysis completed for any TPS ≥ 15 trigger
- [ ] Section 9 Fragile State checklist completed (required if any composite ≥ 3.0 or any score = 5)
- [ ] Section 10 alliance reliability scored for all relevant dyads
- [ ] Section 11 OSIQP narrative sweep pulled and information environment section completed
- [ ] Section 12 RTP aggregate table populated with all composites and inversion applied to Section 10

**QGIA System Integration:**
- [ ] QSFE input package formatted per Section 12 Step 2 template and submitted
- [ ] EDM query submitted with actor network data and interference nodes from Section 6
- [ ] Assessment logged in Aurora with analyst ID, date, version, and confidence score
- [ ] Any Tier 1 Fragile State indicators reported to Crisis Protocols division
- [ ] Supervisor review completed for any RTP ≥ 4.0 assessment

---

## References and Data Sources

| Source | Type | Use in Templates | Access |
|--------|------|-----------------|--------|
| World Bank Open Data | Economic indicators, development indices | Section 3 | data.worldbank.org |
| IMF World Economic Outlook | GDP, debt, inflation, reserves | Section 3 | imf.org/en/Publications/WEO |
| SIPRI Military Expenditure Database | Defense spending, arms transfers | Section 4 | sipri.org/databases |
| ACLED (Armed Conflict Location & Event Data) | Violence incidents, protest data | Sections 5, 8, 9 | acleddata.com |
| Freedom House Freedom in the World | Political rights, civil liberties | Sections 2, 11 | freedomhouse.org |
| Reporters Without Borders Press Freedom Index | Media freedom rankings | Section 11 | rsf.org |
| Varieties of Democracy (V-Dem) Project | Regime classification, democratic indicators | Sections 1, 2 | v-dem.net |
| Nuclear Threat Initiative (NTI) Index | Nuclear security, WMD capability | Section 4B | nti.org |
| Fearon & Laitin Ethnic Fractionalization Data | EFI baseline values by country | Section 5-01 | scholar.harvard.edu/jfearon/publications |
| Fund for Peace Fragile States Index | State fragility composite | Section 9 | fragilestatesindex.org |
| OSIQP Regional Dashboard | Real-time signals (all indicators) | All sections | Internal — Aurora access required |
| EDM Regional Graph | Alliance/conflict network dynamics | Sections 6, 7 | Internal — Aurora access required |

---

*Document prepared for QGIA Regional Division analyst use. All scoring reflects assessment-date conditions and must be reassessed on the review cadence specified by the RTP score (Section 12, Step 1). Template structure is versioned; check Aurora for the current release before beginning a new assessment. For OSIQP, EDM, or Aurora access issues, contact QGIA Technology Division (QGIA-KL-TS series).*
