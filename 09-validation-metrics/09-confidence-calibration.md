# Confidence Calibration Guide

**Document ID**: QGIA-KL-VM-09-CALIBRATION  
**Classification**: UNCLASSIFIED  
**Version**: 1.0  
**Last Updated**: 2026-03-13  
**Authority**: QGIA Validation Metrics Team Lead

## Purpose

Systematic methodology for quantifying, calibrating, and tracking probabilistic confidence in QGIA analytical products. This guide governs how analysts assign numerical confidence to forecasts, how those assignments are scored against outcomes, and how calibration performance is measured, reported, and improved over time. All Tier I and Tier II assessments are subject to mandatory calibration protocols defined herein.

A well-calibrated analyst is one whose stated 70% confidence events resolve as outcomes approximately 70% of the time. Calibration failure — systematic overconfidence, underconfidence, or domain-specific bias — degrades decision-maker trust and distorts QSFE probabilistic models. This document provides the operational tools to detect and correct calibration failures before they propagate.

---

## 1. THE FOUR CONFIDENCE COMPONENTS

### 1.1 Component Architecture

QGIA confidence scores are **composite values** (0.00–1.00) derived from four independently assessed sub-components. Each component reflects a distinct source of epistemic uncertainty. Analysts score each component separately before computing the composite.

| Component | Code | Domain | Weight |
|-----------|------|--------|--------|
| Data Quality | DQ | Completeness, recency, coverage of underlying data | 0.30 |
| Source Reliability | SR | Track record, independence, access of sources | 0.25 |
| Methodological Rigor | MR | Quality of analytical method applied | 0.25 |
| Temporal Stability | TS | How much the assessed condition changes over time | 0.20 |

### 1.2 Component Scoring Rubrics

**Data Quality (DQ)** — Score 0.00–1.00

| Score | Descriptor | Operational Meaning |
|-------|-----------|---------------------|
| 0.90–1.00 | Comprehensive | Multiple independent, current datasets; minimal gaps; full temporal coverage |
| 0.75–0.89 | Adequate | Primary datasets present; minor gaps in coverage or recency |
| 0.55–0.74 | Partial | Significant gaps; reliance on proxies or extrapolation |
| 0.30–0.54 | Fragmentary | Single data stream; heavy inference required |
| 0.00–0.29 | Minimal | Near-absence of direct data; analogy-based estimation only |

**Example**: Assessing PLA amphibious assault readiness — GEOINT on vessel concentration complete (GEOINT DQ: 0.88), HUMINT on training doctrine fragmentary (HUMINT DQ: 0.42). Blended DQ score: 0.65.

---

**Source Reliability (SR)** — Score 0.00–1.00

Corresponds to NATO/ADMIRALTY source reliability ratings mapped to the 0.00–1.00 scale:

| ADMIRALTY Rating | SR Score | Meaning |
|-----------------|----------|---------|
| A – Completely reliable | 0.95–1.00 | Consistent track record, verified access, no known deception history |
| B – Usually reliable | 0.75–0.94 | Reliable in most domains; occasional gaps |
| C – Fairly reliable | 0.55–0.74 | Reliable in some instances; inconsistencies recorded |
| D – Not usually reliable | 0.30–0.54 | More unreliable than reliable; significant verification required |
| E – Unreliable | 0.10–0.29 | Consistent inaccuracy or deception detected |
| F – Cannot be judged | 0.05–0.09 | No basis for evaluation; first report |

**Multi-source averaging**: When multiple sources contribute, SR is the weighted average of individual source ratings, weighted by their proportional contribution to the assessment.

---

**Methodological Rigor (MR)** — Score 0.00–1.00

| Score | Descriptor | Methods Applied |
|-------|-----------|-----------------|
| 0.90–1.00 | Maximum rigor | ACH + Red Team + Premortem + Quantitative model + Bayesian updating |
| 0.75–0.89 | High rigor | ACH + at least one contrarian technique + quantitative support |
| 0.55–0.74 | Standard | ACH or equivalent structured technique; single analyst review |
| 0.30–0.54 | Basic | Informal hypothesis testing; no structured technique |
| 0.00–0.29 | Minimal | Expert judgment only; no documented methodology |

**SAT bonus application** (per QGIA-KL-AF-02-02): MR scores receive structured bonus increments when formal SATs are applied and documented. Maximum cumulative bonus: +0.25 over the base MR score, capped at 1.00.

---

**Temporal Stability (TS)** — Score 0.00–1.00

TS reflects how rapidly the assessed phenomenon changes and how current the analysis is relative to that change rate.

| Score | Descriptor | Scenario Type |
|-------|-----------|---------------|
| 0.85–1.00 | Very stable | Structural factors (geography, demographics, treaty frameworks) |
| 0.65–0.84 | Moderately stable | Political alignments, military postures, economic trends |
| 0.40–0.64 | Volatile | Leadership dynamics, tactical situations, negotiations |
| 0.15–0.39 | Highly volatile | Active kinetic operations, diplomatic crises, market shocks |
| 0.00–0.14 | Unstable | Fluid battlefield, breaking intelligence, unresolved events |

**Decay function**: For time-sensitive assessments, TS degrades over time according to domain-specific half-lives (see Section 6.3).

---

### 1.3 Composite Confidence Score Formula

The **Composite Confidence Score (CCS)** is the weighted linear combination of the four components:

```
CCS = (0.30 × DQ) + (0.25 × SR) + (0.25 × MR) + (0.20 × TS)
```

**Worked Example — Russia-Ukraine Escalation Assessment (hypothetical):**

| Component | Raw Score | Weight | Weighted Value |
|-----------|-----------|--------|----------------|
| Data Quality | 0.82 | 0.30 | 0.246 |
| Source Reliability | 0.71 | 0.25 | 0.178 |
| Methodological Rigor | 0.88 | 0.25 | 0.220 |
| Temporal Stability | 0.45 | 0.20 | 0.090 |
| **Composite CCS** | | | **0.734** |

**Interpretation**: CCS of 0.734 → Medium-High confidence. Qualifies for Tier II output. Temporal instability (active conflict dynamics) is the primary confidence constraint.

**CCS Tier Thresholds**:
| CCS Range | Confidence Band | Output Tier Eligibility |
|-----------|----------------|------------------------|
| 0.85–1.00 | High | Tier I (>25% probability scenarios) |
| 0.65–0.84 | Medium-High | Tier I or II depending on probability |
| 0.50–0.64 | Medium | Tier II (10–25% probability scenarios) |
| 0.30–0.49 | Low-Medium | Tier III only |
| 0.00–0.29 | Low | Flagged; not publishable without caveat |

---

## 2. BRIER SCORE: CALCULATION AND INTERPRETATION

### 2.1 Definition

The **Brier Score (BS)** is the primary metric for evaluating probabilistic forecast accuracy. It measures the mean squared difference between forecast probabilities and binary outcomes.

**Formula for a single forecast:**

```
BS = (f - o)²
```

Where:
- `f` = forecast probability (0.00–1.00)
- `o` = outcome (1 = event occurred, 0 = event did not occur)

**For a set of N forecasts:**

```
BS = (1/N) × Σᵢ (fᵢ - oᵢ)²
```

**Brier Score range**: 0.00 (perfect) to 1.00 (maximally wrong). A naive forecaster assigning 0.50 to all events scores BS = 0.25.

### 2.2 Brier Score Benchmarks

| BS Range | Performance Level | Interpretation |
|----------|------------------|----------------|
| 0.00–0.05 | Exceptional | Expert superforecaster tier |
| 0.06–0.10 | Excellent | Consistently well-calibrated; QGIA target |
| 0.11–0.15 | Good | Above-average; acceptable for complex domains |
| 0.16–0.20 | Acceptable | Below target; improvement required |
| 0.21–0.25 | Poor | Near-random; equivalent to uninformed guessing |
| >0.25 | Failing | Worse than random; systematic miscalibration |

**QGIA Standard**: Team Brier Score target ≤ 0.10 across rolling 12-month forecasts. Individual analysts should achieve ≤ 0.13 before qualifying for independent Tier I assessment production.

### 2.3 Worked Examples

**Example A — Well-calibrated forecast:**
- Event: "North Korea conducts nuclear test within 90 days"
- Forecast probability: 0.30
- Outcome: Did not occur (o = 0)
- BS = (0.30 − 0)² = **0.09** ✓ (Good)

**Example B — Overconfident forecast:**
- Event: "Iran nuclear talks collapse by Q3 2026"
- Forecast probability: 0.85
- Outcome: Did not occur (o = 0)
- BS = (0.85 − 0)² = **0.72** ✗ (Failing)

**Example C — Underconfident forecast:**
- Event: "China conducts Taiwan Strait military exercises within 6 months"
- Forecast probability: 0.40
- Outcome: Occurred (o = 1)
- BS = (0.40 − 1)² = **0.36** ✗ (Poor)

**Example D — Calibrated near-certainty:**
- Event: "Russia maintains military presence in occupied Ukrainian territories"
- Forecast probability: 0.95
- Outcome: Occurred (o = 1)
- BS = (0.95 − 1)² = **0.0025** ✓ (Exceptional)

### 2.4 Brier Skill Score (BSS)

The **Brier Skill Score** contextualizes performance against a climatological baseline:

```
BSS = 1 − (BS_analyst / BS_reference)
```

Where `BS_reference` is typically the base rate forecast (always predicting the historical frequency). BSS > 0 indicates the analyst outperforms the baseline; BSS = 1.00 is perfect.

**Example**: Base rate for "major power military confrontation" in any 90-day period: 0.12. Reference forecaster always predicts 0.12. BS_reference = (0.12)² × 0.88 + (0.88)² × 0.12 = 0.0126 + 0.0930 = 0.106. Analyst BS = 0.082. BSS = 1 − (0.082/0.106) = **+0.23** (moderate skill above baseline).

---

## 3. CALIBRATION CURVE GENERATION

### 3.1 Methodology

A **calibration curve** (reliability diagram) plots forecast probability bins against observed outcome frequencies, revealing systematic over- or under-confidence patterns.

**Step-by-step procedure:**

1. **Collect forecast-outcome pairs**: Minimum 50 resolved forecasts for statistically meaningful curve; 200+ for domain-specific curves.

2. **Bin forecasts**: Divide probability range into bins (typically decile bins: 0–10%, 10–20%, ..., 90–100%).

3. **Calculate observed frequency per bin**:
   ```
   Observed_freq(bin) = Count(outcomes = 1 in bin) / Count(forecasts in bin)
   ```

4. **Plot**: X-axis = forecast probability (midpoint of bin); Y-axis = observed frequency.

5. **Perfect calibration reference**: Diagonal line from (0,0) to (1,1).

6. **Calculate calibration error** (Expected Calibration Error, ECE):
   ```
   ECE = Σ (|bin_size| / N) × |forecast_midpoint − observed_freq|
   ```

### 3.2 Interpreting Calibration Curves

**Patterns and their meaning:**

| Curve Shape | Interpretation | Action Required |
|-------------|---------------|-----------------|
| On diagonal | Perfect calibration | Maintain procedures |
| Below diagonal (S-curve) | Overconfidence | Apply dampening protocol (Section 5) |
| Above diagonal (inverted-S) | Underconfidence | Apply extremizing protocol (Section 7) |
| Below for high p, above for low p | Double-sided overconfidence | Full recalibration training |
| Flat line | No discrimination skill | Remedial methodological training |

### 3.3 Domain-Stratified Calibration Curves

QGIA maintains separate calibration curves for each primary domain. Do not aggregate across domains — military forecasts and economic forecasts exhibit different calibration profiles. A well-calibrated military analyst may be systematically overconfident in economic domains.

**Minimum sample thresholds by domain:**

| Domain | Minimum Forecasts for Valid Curve | Recommended |
|--------|----------------------------------|-------------|
| Military conflict onset | 40 | 150 |
| Diplomatic negotiations | 30 | 100 |
| Leadership transitions | 25 | 80 |
| Economic shock/crisis | 35 | 120 |
| Terrorist/insurgent activity | 50 | 200 |
| Election outcomes | 20 (per election cycle) | 60 |

### 3.4 QSFE Integration

Calibration curves feed directly into **QSFE probability adjustment matrices**. When QSFE receives a probability estimate from an analyst, it applies the analyst's historical calibration correction:

```
QSFE_adjusted_p = f⁻¹(analyst_p)
```

Where `f⁻¹` is the inverse of the analyst's empirical calibration function. This correction is transparent to the consumer and documented in the assessment metadata.

---

## 4. INTERVAL ESTIMATION BEST PRACTICES

### 4.1 Confidence Interval Construction

**Credible intervals** in QGIA products follow Bayesian conventions (the interval contains the true value with stated probability, given priors and data), not frequentist confidence intervals.

**Standard intervals**: QGIA reports 50%, 80%, and 95% credible intervals for quantitative estimates. All three must be reported for Tier I assessments.

**Procedure:**

1. State the point estimate (median of posterior distribution)
2. State the 50% CI: "We assess [value] with 50% of our probability mass between [low] and [high]"
3. State the 80% CI for planning purposes
4. State the 95% CI for risk bounding

**Example — Russian force mobilization timeline:**
- Point estimate: 45 days to operational readiness
- 50% CI: [38, 54] days
- 80% CI: [28, 72] days
- 95% CI: [18, 110] days

### 4.2 Common Interval Errors

**Interval too narrow (overconfidence):**
Analysts produce 90% intervals that capture the true value only 60% of the time. Training calibration target: stated 90% intervals should contain the outcome approximately 85–95% of the time.

**Asymmetric intervals without justification:**
When intervals are asymmetric, explicitly state the skew direction and reason (e.g., "right-skewed due to potential for rapid escalation; left tail bounded by logistical constraints").

**Point estimate outside interval:**
Never report a point estimate that falls outside the stated CI. This indicates internal inconsistency.

**Updating intervals without widening during crises:**
During rapidly evolving situations, CIs should widen to reflect increased uncertainty. Analysts commonly fail to update interval width when updating point estimates.

### 4.3 Interval Width Standards

See Section 6 (Domain-Specific Calibration Tables) for recommended minimum interval widths by domain. As a general rule:

- **0–30 day horizon**: 80% CI width ≥ ±15% of point estimate
- **1–6 month horizon**: 80% CI width ≥ ±30% of point estimate
- **6–24 month horizon**: 80% CI width ≥ ±50% of point estimate
- **>24 month horizon**: 80% CI width ≥ ±75% of point estimate

Intervals narrower than these minimums require supervisor sign-off and explicit justification.

---

## 5. OVERCONFIDENCE DETECTION AND MITIGATION

### 5.1 Systematic Detection

**Individual analyst overconfidence flag criteria** (any one triggers review):

- Rolling 20-forecast Brier Score > 0.18
- Stated 80% CI captures outcome fewer than 60% of the time (n ≥ 20)
- Average forecast probability for events that did not occur > 0.55
- Calibration curve is systematically below diagonal by > 0.10 for any bin

**Team-level overconfidence indicators:**

- Team mean BS > 0.15 for 2 consecutive quarters
- Team 90% CIs capture outcomes fewer than 70% of the time
- Consensus drift: Team forecasts become less dispersed during crises (inverse of correct behavior)

### 5.2 Root Causes of Overconfidence

| Cause | Description | Domain Prevalence |
|-------|-------------|-------------------|
| Confirmation bias | Anchoring on confirming evidence | All domains |
| Narrative coherence | Compelling stories feel certain | Geopolitical, leadership |
| Expertise illusion | Domain knowledge inflates certainty | Technical domains |
| Groupthink | Consensus pressure narrows intervals | All team environments |
| Availability heuristic | Vivid recent examples distort base rates | Military, terrorism |
| Outcome bias | Historical retrospection increases perceived predictability | All domains |

### 5.3 Mitigation Protocols

**Protocol A — Probability Dampening:**
When OSIQP flags overconfidence risk, apply the **dampening formula** before publishing:

```
f_adjusted = f_raw × (1 − δ) + 0.50 × δ
```

Where δ is the domain-specific dampening coefficient (default: 0.15; high-volatility domains: 0.25). This shifts probability toward 50% by a controlled amount, reducing the expected squared error from overconfident outliers.

**Protocol B — Forced Alternative Generation:**
Before finalizing any forecast > 0.75, the analyst must document at least two scenarios under which the event does **not** occur, with probability assigned to each. If alternative scenario probabilities sum to less than 0.10, the forecast requires senior review.

**Protocol C — Pre-mortem Calibration Check:**
For forecasts with CCS ≥ 0.80 and probability ≥ 0.80: convene 2-analyst premortem. Explicitly generate failure modes. If either analyst cannot assign residual probability < 0.15, the forecast is re-examined.

**Protocol D — Historical Analogy Anchoring:**
Pull base rate from the QGIA Historical Performance Database for the event class. If analyst probability deviates from base rate by > 0.25, require explicit written justification citing specific intelligence that warrants departure from prior.

### 5.4 Real-World Example — Iran Nuclear Miscalibration (Illustrative)

In a retrospective training case, analysts assigned 0.82 probability to "Iran abandons nuclear negotiations by mid-year." Outcome: negotiations continued (o = 0). BS = 0.67. Post-analysis identified:

- **Cause**: Overweighting SIGINT intercepts of hardliner rhetoric (availability bias)
- **Error**: Failing to weight diplomatic back-channel signals showing continued Iranian interest
- **Correction applied**: Historical base rate for "negotiations survive internal pressure" in Iran context: 0.58. Base-rate anchor would have suggested probability cap at 0.65 absent extraordinary evidence.

---

## 6. DOMAIN-SPECIFIC CALIBRATION TABLES

### 6.1 Calibration Parameters by Domain

**Historical QGIA performance benchmarks** inform recommended calibration settings across primary analytical domains. These parameters are updated quarterly as the forecast resolution database grows.

| Domain | Base BS Target | Recommended CI Width (80%) | Dampening Coefficient | Temporal Half-Life |
|--------|---------------|---------------------------|----------------------|-------------------|
| Military conflict onset | 0.11 | ±35% | 0.20 | 21 days |
| Military operational outcomes | 0.13 | ±40% | 0.22 | 7 days |
| Diplomatic scenario (negotiations) | 0.09 | ±30% | 0.15 | 45 days |
| Leadership change/transition | 0.10 | ±25% | 0.18 | 60 days |
| Economic crisis onset | 0.12 | ±45% | 0.18 | 14 days |
| Terrorist attack (location/timing) | 0.14 | ±50% | 0.25 | 3 days |
| Election outcomes | 0.08 | ±20% | 0.12 | 30 days |
| Sanctions effectiveness | 0.11 | ±40% | 0.15 | 90 days |
| Nuclear/WMD proliferation event | 0.09 | ±30% | 0.20 | 180 days |
| Space/cyber incident | 0.14 | ±45% | 0.22 | 5 days |

### 6.2 Probability Range Guidance by Domain

**Military Conflict Probability Benchmarks** (historical base rates, 1945–present):

| Scenario Class | Base Rate | QGIA 90-day Typical Range | Notes |
|----------------|-----------|--------------------------|-------|
| Active conflict continuation | 0.85–0.95 | 0.80–0.98 | High predictability when kinetics active |
| Escalation to new theater | 0.08–0.15 | 0.05–0.35 | Rare but high-impact |
| Ceasefire holding 90 days | 0.40–0.55 | 0.30–0.65 | Volatile; wide CI required |
| Coup attempt in wartime | 0.06–0.12 | 0.04–0.20 | Regime-type dependent |
| WMD use (conflict active) | 0.03–0.08 | 0.02–0.15 | Escalation-threshold sensitive |
| Foreign intervention onset | 0.10–0.18 | 0.08–0.30 | Alliance treaty and interest driven |

**Diplomatic Scenario Probability Benchmarks:**

| Scenario Class | Base Rate | QGIA 90-day Typical Range | Notes |
|----------------|-----------|--------------------------|-------|
| Negotiations breakthrough | 0.15–0.25 | 0.10–0.40 | Highly context-dependent |
| Agreement collapse | 0.20–0.35 | 0.15–0.50 | Domestic politics major driver |
| Sanctions regime expansion | 0.25–0.40 | 0.20–0.55 | Security Council dynamics key |
| Bilateral summit convened | 0.30–0.45 | 0.25–0.60 | Leader signaling observable |
| Formal alliance formation | 0.05–0.10 | 0.03–0.18 | Rare structural events |
| UN resolution passage | 0.35–0.50 | 0.25–0.65 | Veto dynamics critical |

**Economic Domain Probability Benchmarks:**

| Scenario Class | Base Rate | QGIA 6-month Typical Range | Notes |
|----------------|-----------|---------------------------|-------|
| Sanctions effectiveness (target compliance) | 0.25–0.35 | 0.15–0.50 | Regime type critical variable |
| Currency crisis onset | 0.08–0.15 | 0.05–0.30 | External reserves and political will |
| Debt default | 0.10–0.20 | 0.07–0.35 | IMF intervention probability key |
| Trade war escalation | 0.30–0.45 | 0.20–0.60 | Electoral cycle sensitive |
| Energy market shock | 0.15–0.25 | 0.10–0.40 | Geopolitical trigger probability |

**Technological Domain Probability Benchmarks:**

| Scenario Class | Base Rate | QGIA 12-month Typical Range | Notes |
|----------------|-----------|----------------------------|-------|
| Major cyber attack on critical infrastructure | 0.35–0.50 | 0.25–0.65 | Attack surface expanding |
| AI-enabled disinformation campaign (state) | 0.55–0.70 | 0.45–0.80 | Near-certain in election years |
| Semiconductor supply disruption | 0.20–0.30 | 0.15–0.45 | Taiwan Strait contingency-linked |
| Hypersonic weapon test (major power) | 0.60–0.75 | 0.50–0.85 | Program maturity indicator |
| Space-based asset denial incident | 0.15–0.25 | 0.10–0.40 | Escalation threshold sensitive |

### 6.3 Temporal Stability Half-Lives

Confidence scores decay over time as assessed conditions evolve. Apply the following exponential decay to TS scores when analysis is not refreshed:

```
TS(t) = TS(0) × e^(−λt)
```

Where λ = ln(2) / half-life, and t is time elapsed since assessment.

| Domain | Half-Life | Full TS Reset Trigger |
|--------|-----------|----------------------|
| Active kinetic conflict | 7 days | Any major operational development |
| Diplomatic negotiations | 14 days | New negotiating round, leadership statement |
| Political crisis | 10 days | Electoral event, mass protest, arrest |
| Economic assessment | 21 days | New indicators release, policy announcement |
| Long-run structural trend | 90 days | Treaty change, demographic milestone |
| Nuclear posture | 45 days | Nuclear doctrine publication, test |

---

## 7. EXTREMIZING: APPROPRIATE USE CASES AND METHODOLOGY

### 7.1 Concept

**Extremizing** is the deliberate adjustment of probability estimates away from 50% — toward 0 or 1 — when the analyst has genuine discriminating information that distinguishes their forecast from the reference class average. It is the correction for systematic underconfidence.

Extremizing is appropriate when:
- The analyst has non-public, specific, and recent intelligence that materially informs the probability
- The analyst's historical calibration shows a pattern of underconfidence (calibration curve above diagonal)
- Multiple independent signals converge on the same direction with high consistency

Extremizing is **inappropriate** when:
- Narrative coherence or recent vivid events create illusory certainty
- Intelligence gaps exist but are rationalized rather than surfaced
- The extremized probability would require conditions outside historical precedent without novel justification

### 7.2 Extremizing Formula

```
f_extremized = f_raw^k / [f_raw^k + (1 − f_raw)^k]
```

Where k is the extremizing coefficient (k > 1 extremizes; k = 1 leaves probability unchanged; k < 1 dampens).

**Default QGIA extremizing coefficients by context:**

| Analyst Condition | k Value | Effect |
|-------------------|---------|--------|
| No special intelligence; calibration on diagonal | 1.00 | No adjustment |
| Strong HUMINT convergence on direction | 1.30 | Moderate extremizing |
| Multiple high-quality independent streams agree | 1.50 | Significant extremizing |
| Intelligence indicates near-certainty | 1.80 | Strong extremizing |
| Underconfidence pattern confirmed in calibration review | 1.20 | Correction for systematic bias |

**Worked Example — China Taiwan Military Activity:**
- Raw analyst probability (PLA exercises within 60 days): 0.55
- Intelligence: Three independent SIGINT streams show logistics mobilization; HUMINT from Taiwan defense sources confirms exercise planning
- k = 1.50 (multiple high-quality streams)
- f_extremized = 0.55^1.5 / [0.55^1.5 + 0.45^1.5]
  = 0.408 / [0.408 + 0.302]
  = 0.408 / 0.710
  = **0.575**

Note: The extremizing effect here is modest because the raw probability is near 0.50. Extremizing has larger effect for probabilities further from center.

**Example at higher initial probability:**
- Raw probability: 0.75; k = 1.30
- f_extremized = 0.75^1.3 / [0.75^1.3 + 0.25^1.3]
  = 0.694 / [0.694 + 0.185]
  = **0.790**

### 7.3 Governance Requirements

All extremized forecasts must be:
1. Flagged with `[EXTREMIZED]` tag in the assessment
2. Documented with the k value applied and justification
3. Reviewed by a second analyst before publication
4. Tracked separately in calibration scoring to assess whether extremizing improved or degraded accuracy

---

## 8. CALIBRATION CURVE CONSTRUCTION: WORKED CASE

### 8.1 QGIA Analyst Team — Hypothetical 100-Forecast Calibration Audit

**Dataset**: 100 resolved geopolitical forecasts, 12-month horizon, mixed domains.

**Binning results:**

| Forecast Bin | N in Bin | Observed Frequency | Deviation from Perfect |
|-------------|----------|-------------------|------------------------|
| 0–10% | 12 | 0.08 | −0.03 (slight underconf.) |
| 10–20% | 15 | 0.13 | −0.02 (near perfect) |
| 20–30% | 14 | 0.29 | +0.04 (near perfect) |
| 30–40% | 11 | 0.36 | +0.01 (perfect) |
| 40–50% | 9 | 0.44 | −0.01 (perfect) |
| 50–60% | 10 | 0.70 | **+0.15** (overconfident) |
| 60–70% | 9 | 0.78 | **+0.13** (overconfident) |
| 70–80% | 10 | 0.60 | **−0.15** (underconfident) |
| 80–90% | 7 | 0.71 | **−0.14** (underconfident) |
| 90–100% | 3 | 0.67 | **−0.28** (significantly underconfident) |

**Team BS**: 0.127 — Good, but above QGIA team target (0.10).

**Diagnosis**: The team shows good calibration in the 0–50% range but a problematic pattern above 50%: overconfidence in the 50–70% range (events assigned 55–65% are actually happening 70–78% of the time), and underconfidence in the 70–100% range. This is a classic **probability compression** pattern — analysts are reluctant to commit to high probabilities even when evidence warrants it, while treating near-50% events as more certain than they are.

**Corrective action**: Extremizing protocol for events currently forecast at 70–95% (k = 1.20 correction for systematic underconfidence). Calibration training exercise targeting the 50–70% bin to separate genuinely 55% events from effectively 70%+ events.

---

## 9. HISTORICAL PERFORMANCE BENCHMARKING

### 9.1 Baseline Reference Sources

QGIA calibration performance is benchmarked against three reference classes:

1. **QGIA Historical Average**: Rolling 24-month team BS. Stored in the Forecast Performance Tracking System (FPTS).

2. **Intelligence Community Benchmark**: Published IC accuracy studies (U.S. DNI external research; IARPA forecasting tournament results). Reference BS approximately 0.14–0.18 for professional IC analysts without structured calibration.

3. **Superforecaster Benchmark**: Good Judgment Project superforecaster performance. Reference BS approximately 0.07–0.10. This represents the aspirational standard for QGIA senior analysts.

4. **Naive Baseline**: Always predicting domain base rates. Performance varies by domain; typically BS ≈ 0.18–0.22. Any analyst below this level is performing negatively.

### 9.2 Benchmarking Procedure

**Quarterly calibration review cycle:**

1. Extract all forecasts resolved in the quarter from FPTS
2. Calculate individual BS and team BS
3. Stratify by domain, forecast horizon, and CCS tier
4. Compare against three benchmarks above
5. Generate calibration curve per domain per analyst
6. Identify highest-impact improvement opportunities (highest BS forecasts by category)
7. Assign remedial or advanced calibration exercises based on results (see Section 11)

**Reporting format:**

| Analyst | Q BS | Q-4 BS | Trend | vs. IC Benchmark | vs. Superforecaster | Domains Flagged |
|---------|------|--------|-------|-----------------|---------------------|-----------------|
| Target  | ≤0.10 | — | Improving | Superior | Within 0.03 | None |

### 9.3 Domain-Specific Accuracy Comparison

When comparing performance across domains, normalize BS to the **Brier Skill Score (BSS)** rather than raw BS, because base rates differ. An analyst with BS = 0.14 in military conflict (hard domain, base rate ~0.15) outperforms an analyst with BS = 0.12 in election forecasting (easier domain, base rate ~0.40).

**QGIA BSS floor**: All analysts must achieve BSS > 0.15 across their primary domains within 18 months of joining. Failure to meet this standard triggers formal performance review.

### 9.4 Retrospective Major Miss Analysis

For any forecast where final outcome deviated from probability by > 0.40 (e.g., 0.20 probability event occurred; 0.85 probability event did not), a structured post-mortem is mandatory:

1. Reconstruct what intelligence was available at forecast time (not post-hoc information)
2. Identify specific analytical failure(s) from the taxonomy (Section 12)
3. Determine: Was the miss foreseeable given available intelligence? (Analytical failure) or a genuine black swan? (Irreducible uncertainty)
4. Update domain calibration parameters if systematic patterns emerge
5. Archive in FPTS lessons-learned module

---

## 10. INDIVIDUAL ANALYST CALIBRATION TRACKING

### 10.1 Analyst Calibration Profile

Each QGIA analyst maintains a **Calibration Profile** in OSIQP, updated after each resolved forecast. The profile contains:

- **Rolling BS**: Last 50 resolved forecasts (minimum; recalculates continuously)
- **Domain BS breakdown**: Separate scores per primary domain
- **Calibration curve**: Updated quarterly with minimum 30 resolved forecasts per curve
- **CI accuracy rate**: What fraction of stated 80% CIs captured the true value
- **Extremizing flag rate**: How often extremizing was applied and post-hoc accuracy
- **SAT usage correlation**: Does applying SATs improve individual BS?
- **Temporal degradation pattern**: Does accuracy drop more than expected as forecast horizon extends?

### 10.2 Calibration Record Maintenance Procedures

**Forecast registration** (mandatory before publication):
1. Log forecast in FPTS with: probability (0.00–1.00), CCS score, resolution criteria, resolution date window, domain tag
2. OSIQP assigns a Forecast ID and timestamps the entry
3. Analyst acknowledges they cannot modify the probability after FPTS registration

**Resolution logging** (within 5 business days of event resolution):
1. Analyst or team supervisor logs outcome (binary: 1/0)
2. Reviewer confirms resolution criteria were met
3. OSIQP calculates BS contribution and updates Calibration Profile

**Contested resolutions**: If the analyst disputes whether the resolution criterion was met, escalate to the Validation Metrics Team Lead for adjudication. The decision is final and logged.

### 10.3 Calibration Tiers and Certification

| Tier | Qualification | Privileges | Review Frequency |
|------|--------------|------------|-----------------|
| Calibration Trainee | BS ≥ 0.18 or < 30 resolved forecasts | Tier III production only; all forecasts reviewed | Weekly |
| Calibration Qualified | BS 0.11–0.17; ≥ 30 forecasts | Tier I/II with senior review | Monthly |
| Calibration Certified | BS 0.07–0.10; ≥ 100 forecasts | Independent Tier I production | Quarterly |
| Calibration Expert | BS < 0.07; ≥ 200 forecasts; BSS > 0.30 | Calibration reviewer for others; extremizing authority | Biannual |

Analysts who drop below their certification threshold for two consecutive quarters are downgraded one tier and assigned targeted calibration exercises.

### 10.4 Privacy and Incentives

Individual calibration scores are visible to:
- The individual analyst
- Direct supervisor
- Validation Metrics Team Lead
- Division Chief (aggregate only, not individual rankings)

**Incentive structure**: Calibration Expert status is a prerequisite for promotion to Senior Analyst. Annual calibration excellence awards are given to the top 10% of analysts by BSS improvement. Calibration scores do not directly affect annual performance ratings — the intent is to encourage honest probability reporting rather than strategic score management.

---

## 11. CALIBRATION EXERCISES FOR ANALYST TRAINING

### 11.1 Foundational Exercises (Trainee Level)

**Exercise 1 — Almanac Questions:**
Analysts answer 20 factual questions with probability distributions (e.g., "What is the probability that Russia's GDP is between $1.5T and $2.0T?"). Answers are scored immediately. Purpose: Establish baseline calibration and identify systematic bias direction (over vs. under).

**Exercise 2 — Historical Forecast Reconstruction:**
Given declassified intelligence from a past crisis (Cuban Missile Crisis, 2008 Georgia War, 2011 Arab Spring), analyst makes probability assessments as if in real-time. Outcome known to trainer. Purpose: Practice separating available evidence from post-hoc knowledge; identify anchoring.

**Exercise 3 — Confidence Interval Drills:**
Analyst provides 90% CIs for 10 quantitative historical facts. Success criterion: 8–10 intervals should capture the true value. Most untrained analysts capture 5–7 (systematic overconfidence). Repeat monthly until consistent 8–9 capture rate achieved.

### 11.2 Intermediate Exercises (Qualified Level)

**Exercise 4 — Geopolitical Forecasting Tournament:**
Quarterly internal tournament. Analysts forecast 15 real current events (30-day horizon). Results scored and ranked. Discussion session analyzes top-performing reasoning vs. low-performing reasoning. Purpose: Competitive calibration and peer learning.

**Exercise 5 — Brier Score Decomposition:**
Given a set of 30 forecasts with outcomes, analyst manually computes BS, resolution, and reliability components. Then identifies which forecasts contributed most to BS degradation and what would have been the correct probability. Purpose: Operational fluency with scoring mechanics.

**Exercise 6 — Calibration Curve Interpretation Workshop:**
Analyst receives four anonymized calibration curves (colleagues, real data). Must diagnose the calibration failure mode and prescribe the correct correction protocol from Section 5. Purpose: Build diagnostic pattern recognition.

### 11.3 Advanced Exercises (Certified and Expert Level)

**Exercise 7 — Ensemble Aggregation:**
Given 5 analysts' independent probability estimates on the same event, aggregate using: (a) simple average, (b) extremized average, (c) weighted average by historical BS. Compare aggregation methods against outcomes when resolved. Purpose: Develop skill in ensemble methods used by QSFE.

**Exercise 8 — Temporal Decay Calibration:**
Analyst makes the same forecast at 90 days, 30 days, and 7 days before resolution. Track whether probability update quality matches expected information gain. Analysts who show minimal updating (anchoring on initial estimate) are flagged. Purpose: Ensure forecasts incorporate new information appropriately.

**Exercise 9 — Adversarial Calibration:**
Two analysts receive the same intelligence package and independently produce probabilities. They then attempt to persuade each other without sharing new information — only arguing about weighting. Purpose: Identify which analyst shows more confidence drift under social pressure (a failure mode). The analyst whose final probability is farther from their initial estimate without new evidence has demonstrated social anchoring bias.

---

## 12. COMMON CALIBRATION FAILURE MODES

### 12.1 Failure Mode Taxonomy

| Failure Mode | Description | Detection Indicator | Correction |
|--------------|-------------|--------------------|----|
| **Overconfidence** | Systematic assignment of probabilities closer to 0/1 than warranted | BS > 0.18; calibration curve below diagonal | Dampening protocol (Section 5.3A) |
| **Underconfidence** | Clustering probabilities near 0.50 even with strong evidence | BS > 0.18; calibration curve above diagonal; flat curve | Extremizing protocol (Section 7) |
| **Probability compression** | Good at low/high ends; poor at 50–75% range | Calibration errors concentrated at mid-range bins | Mid-range recalibration training |
| **Domain blindness** | Excellent in one domain, severely miscalibrated in others | Domain-stratified BS shows > 0.08 spread across domains | Domain isolation; restricted scope until recalibrated |
| **Anchoring on CCS** | Treats high CCS as justification for extreme probabilities | Correlation between CCS and probability extremity | CCS/probability independence training |
| **Temporal overreach** | Equivalent confidence at 7-day and 180-day horizon | Flat probability across temporal horizons | Horizon-stratified BS review; TS component scrutiny |
| **Outcome bias** | After resolution, retroactively claims the outcome was obvious | Post-hoc verbal descriptions inconsistent with pre-registration | Strict FPTS registration enforcement |
| **Social anchoring** | Probability shifts significantly when challenged by colleagues without new information | High delta between first draft and published probability | Blind first-registration protocol |

### 12.2 Worked Examples of Failure Modes

**Domain Blindness — Economic Overconfidence:**
A senior military analyst assigned to an economic assessment of Russian ruble stability. Track record BS in military domain: 0.09. First 15 economic forecasts yielded BS: 0.23. The analyst's deep familiarity with military indicators created false confidence in economic pattern recognition. Resolution: Analyst restricted to advisory role on economic assessments; required to complete Economics Domain Calibration Module before independent production.

**Social Anchoring — Iran Nuclear Consensus:**
Team assessment of Iran nuclear talks: initial independent probabilities ranged 0.35–0.65 (genuine uncertainty). After group discussion, all probabilities converged to 0.72 (no new information introduced). Outcome: talks continued (o = 0). BS for consensus estimate: 0.52 vs. mean of independent estimates BS: 0.17. Resolution: Blind registration of first-draft probabilities is now required before any team discussion on Tier I assessments.

**Temporal Overreach — North Korea:**
Analyst maintained the same 0.35 probability for "DPRK ballistic missile test within any rolling 90-day window" regardless of: post-summit diplomatic periods (should have dropped to ~0.15) or post-failed-negotiation periods (should have risen to ~0.55). Flat probability across contexts indicates failure to incorporate temporal and contextual updating. BS was marginally adequate, but **skill score** was negative — the analyst added no value over the naive base-rate forecast.

---

## 13. QGIA SYSTEM INTEGRATION

### 13.1 OSIQP Confidence Scoring Pipeline

**OSIQP** (Open-Source Intelligence Quantitative Platform) automates the initial computation of Data Quality and Source Reliability sub-components, which are then presented to analysts for review and override.

**Automated DQ calculation**: OSIQP evaluates data coverage metrics — number of independent sources, temporal recency, linguistic/geographic diversity of coverage — and produces a DQ pre-score. Analysts review and may adjust ±0.15 with documented justification.

**Automated SR calculation**: Each source in OSIQP has a dynamic reliability score updated by post-hoc accuracy assessments. When an analyst draws on source collections, OSIQP computes the weighted SR pre-score. Analyst can apply override, which triggers a review flag.

**MR and TS**: These components remain analyst-assigned, as they require knowledge of the analytical process (MR) and domain-specific judgment about volatility (TS).

**OSIQP output to analyst**: Pre-populated confidence component scorecard presented in the analysis workspace. Expected completion time: 3 minutes for review and finalization.

### 13.2 QSFE Calibration Data Usage

**QSFE** (Quantum Strategic Forecasting Engine) ingests analyst probability estimates as inputs to multi-scenario modeling. QSFE does not use raw analyst probabilities directly — it applies two corrections:

1. **Calibration correction**: The analyst's historical calibration function (from their OSIQP Calibration Profile) is used to correct their estimate before ensemble aggregation. A known-overconfident analyst's 0.80 estimate might be corrected to 0.68 before entering QSFE.

2. **Ensemble weighting**: Analysts are weighted by their rolling BS in the relevant domain. Calibration Expert analysts receive up to 2× weight relative to Calibration Trainee analysts in the QSFE ensemble.

**Feedback loop**: QSFE scenario amplitude outputs are compared against individual analyst probability estimates quarterly. Analysts whose estimates systematically diverge from ensemble outcomes receive targeted calibration review.

### 13.3 Aurora Orchestration

**Aurora** monitors the aggregate calibration state of the analyst workforce in real-time. When Aurora detects:

- Team mean BS exceeding 0.18 for a rolling 20-forecast window → automatic alert to Validation Metrics Team Lead
- Individual analyst BS exceeding 0.20 for 10 consecutive forecasts → analyst flagged for immediate calibration review
- Domain-wide calibration shift (e.g., all analysts suddenly over/underconfident in a domain) → Aurora initiates domain recalibration review, hypothesis that new domain dynamics require updated base rates

Aurora also applies domain-level calibration corrections to QSFE inputs when a systematic shift is detected but not yet diagnosed, preventing cascading miscalibration from propagating into strategic products.

---

## 14. DOCUMENT MAINTENANCE

**Review Cycle**: Quarterly — calibration benchmarks updated as FPTS database grows  
**Update Triggers**: Significant shifts in team BS (>0.05 change), new academic literature on forecasting, QSFE algorithm updates  
**Custodian**: QGIA Validation Metrics Team Lead  
**Feedback**: qgia-calibration@qgia.gov  
**Next Scheduled Review**: 2026-06-13

---

## REFERENCES

1. Brier, G. W. (1950). "Verification of Forecasts Expressed in Terms of Probability." *Monthly Weather Review*, 78(1), 1–3.
2. Tetlock, P. E., & Gardner, D. (2015). *Superforecasting: The Art and Science of Prediction*. Crown.
3. Murphy, A. H. (1973). "A New Vector Partition of the Probability Score." *Journal of Applied Meteorology*, 12(4), 595–600.
4. Lichtenstein, S., Fischhoff, B., & Phillips, L. D. (1982). "Calibration of Probabilities: The State of the Art to 1980." In D. Kahneman, P. Slovic, & A. Tversky (Eds.), *Judgment Under Uncertainty: Heuristics and Biases*. Cambridge University Press.
5. Mandel, D. R., & Barnes, A. (2014). "Accuracy of Forecasts in Strategic Intelligence." *Proceedings of the National Academy of Sciences*, 111(30), 10984–10989.
6. Satopää, V. A., et al. (2014). "Combining Multiple Probability Predictions Using a Simple Logit Model." *International Journal of Forecasting*, 30(2), 344–356.
7. IARPA (2022). *Good Judgment Project: Forecasting Methodology Reference*. Intelligence Advanced Research Projects Activity.
8. Heuer, R. J. (1999). *Psychology of Intelligence Analysis*. CIA Center for the Study of Intelligence.
9. QGIA Internal (2025). *Forecast Performance Tracking System Technical Specification v2.1*. QGIA Validation Metrics Division.
10. Kent, S. (1964). "Words of Estimative Probability." *Studies in Intelligence*, 8(4), 49–65.

---

**CLASSIFICATION**: UNCLASSIFIED  
**DOCUMENT END**
