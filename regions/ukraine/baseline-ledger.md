# QGIA Ukraine Theater — Baseline Probability Ledger

**Baseline date:** 2026-06-15T09:45:00 EDT (War Day 1,572)
**Last audit:** 2026-06-15T09:45:00 EDT
**Classification: PROPRIETARY | OSIQP v4.2.1**
**Composite Confidence: 0.87 | Quantum Coherence: 0.85**

> **Testability standard:** Every open scenario carries a `falsification_condition` — a specific, observable event or non-event that would definitively resolve it TRUE or FALSE. Scenarios without falsifiable resolution criteria are not accepted into this ledger.

---

## I. WAR TERMINATION SET (mutually exclusive at 12-month horizon)

Modeled as mutually exclusive and collectively exhaustive. Use Dirichlet prior Dir(2.5, 3.0, 1.5, 1.0, 0.8). Rows must sum to 1.00.

| Scenario ID | Scenario Label | Window | P (baseline) | Confidence | Resolution | Falsification Condition |
|---|---|---|---:|---:|---|---|
| `UKR_WT_H1_KINETIC_CONTINUATION` | Kinetic continuation — no ceasefire | 12m (to June 2027) | 0.44 | 0.85 | OPEN | **FALSE if:** Official ceasefire announced by any recognized mediator and holds ≥ 14 days |
| `UKR_WT_H2_FROZEN_CONFLICT` | Partial/frozen ceasefire | 12m | 0.26 | 0.79 | OPEN | **TRUE if:** Formal ceasefire signed AND front line stabilizes with ≤ 10 sq km movement for ≥ 30 consecutive days. **FALSE if:** Full war termination treaty signed OR kinetic operations resume within 30 days of ceasefire |
| `UKR_WT_H3_UKRAINIAN_STRATEGIC_ADVANCE` | Ukrainian operational breakthrough | 12m | 0.14 | 0.72 | OPEN | **TRUE if:** ISW confirms Ukraine has taken a district-level administrative center (raion capital) in Russian-occupied Donetsk, Luhansk, or Zaporizhia that was not previously held by Ukraine since Feb 2022 |
| `UKR_WT_H4_RUSSIAN_TERRITORIAL_ADVANCE` | Russian operational breakthrough | 12m | 0.11 | 0.74 | OPEN | **TRUE if:** ISW confirms net Russian gain exceeding 500 sq km within any 60-day window after June 15, 2026 |
| `UKR_WT_H5_FULL_WAR_TERMINATION` | Full treaty — war ends | 12m | 0.05 | 0.70 | OPEN | **TRUE if:** Signed peace treaty or equivalent binding agreement ratified/acknowledged by both Ukrainian Rada and Russian government, confirmed by UN or OSCE |
| **Total** | | | **1.00** | | | Dirichlet constraint maintained |

---

## II. RUSSIAN FORCE TRAJECTORY (0–6 month window)

| Scenario ID | Scenario Label | Window | P (baseline) | Confidence | Resolution | Falsification Condition |
|---|---|---|---:|---:|---|---|
| `UKR_RU_CULMINATION_CONFIRMED` | Russian culmination point confirmed | 0–6m | 0.58 | 0.83 | OPEN | **TRUE if:** ISW publishes 3 consecutive monthly assessments showing net Russian territorial loss OR monthly advance rate < 1.0 sq km/day for 3 consecutive months. **FALSE if:** Russian monthly net gain exceeds 100 sq km in any single month before Dec 2026 |
| `UKR_RU_DPRK_FORCE_EXPANSION` | DPRK force contribution expands >15,000 | 6m | 0.31 | 0.74 | OPEN | **TRUE if:** South Korea NIS, US DOD, or NATO officially confirms DPRK troop count in Russia/Ukraine theater exceeds 15,000. **FALSE if:** Official DPRK withdrawal announcement or confirmed drawdown to <5,000 |
| `UKR_RU_MASS_STRIKE_ESCALATION` | Russia executes ≥3 mass strikes (>500 weapons) in 30-day window | 3m | 0.27 | 0.77 | OPEN | **TRUE if:** AP/Reuters/ISW confirm three or more strikes of 500+ combined missiles and drones within any 30-day window June 15–Sept 15, 2026. **FALSE if:** No such window occurs before Sept 15, 2026 |
| `UKR_RU_NATO_ART4_TRIGGER` | Russian escalation triggers NATO Article 4 consultation | 6m | 0.09 | 0.68 | OPEN | **TRUE if:** NATO formally convenes Article 4 consultations and official NATO communiqué cites Russian action as trigger. **FALSE if:** No Article 4 consultation convened before Dec 15, 2026 |

---

## III. DIPLOMATIC TRACK (0–6 month window)

| Scenario ID | Scenario Label | Window | P (baseline) | Confidence | Resolution | Falsification Condition |
|---|---|---|---:|---:|---|---|
| `UKR_DIP_NATO_ANKARA_SECURITY_GUARANTEE` | NATO Ankara produces binding security guarantee framework | 0–2m (July summit) | 0.32 | 0.74 | OPEN | **TRUE if:** NATO Ankara summit communiqué includes language legally binding member states to Multinational Force–Ukraine or equivalent security architecture, signed by ≥ 20 NATO members. **FALSE if:** Ankara communiqué contains only hortatory language ("support," "stand with") without binding commitment |
| `UKR_DIP_G7_EVIAN_ENHANCED_AID` | G7 Évian delivers enhanced military aid quantum | 0–7d | 0.40 | 0.78 | OPEN | **TRUE if:** G7 Évian joint statement (or individual member commitments) totals ≥ $20B in new military assistance for Ukraine above existing pledges. **FALSE if:** G7 produces no joint Ukraine statement OR total new commitment is < $10B |
| `UKR_DIP_TRUMP_ZELENSKYY_BILATERAL` | Trump–Zelenskyy bilateral at G7 Évian | 0–7d | 0.24 | 0.76 | OPEN | **TRUE if:** White House readout or pool report confirms 1:1 meeting between Trump and Zelenskyy at Évian. **FALSE if:** G7 concludes without confirmed bilateral (senior US official stated no bilateral scheduled as of June 14) |
| `UKR_DIP_DIRECT_TALKS_INITIATED` | Russia–Ukraine direct talks initiated | 6m | 0.12 | 0.67 | OPEN | **TRUE if:** A face-to-face meeting between credentialed Russian and Ukrainian delegations occurs at any neutral venue, confirmed by both governments. **FALSE if:** No such meeting occurs before Dec 15, 2026 |

---

## IV. BILETSKY / 3RD BRIGADE OPERATIONAL WINDOW

| Scenario ID | Scenario Label | Window | P (baseline) | Confidence | Resolution | Falsification Condition |
|---|---|---|---:|---:|---|---|
| `UKR_MIL_BILETSKY_OPERATIONAL_WINDOW` | 3rd Assault Brigade executes major offensive operation in Donetsk | 0–5m (window closes ~Nov 2026) | 0.38 | 0.72 | OPEN | **TRUE if:** ISW or Ukrainian MoD confirms 3rd Assault Brigade offensive resulting in ≥ 20 sq km gain within a 14-day window. **FALSE if:** Window closes Nov 15, 2026 without confirmed major operation OR 3rd Brigade is reassigned from Donetsk axis |

---

## V. COMPOSITE CONFIDENCE BREAKDOWN

| Component | Score | Notes |
|---|---:|---|
| Data Quality | 0.84 | ISW daily assessments + Ukraine MoD + satellite/OSINT cross-validation |
| Source Reliability | 0.87 | ISW, AP, Reuters, BBC, Ukrainian official sources — strong corroboration |
| Methodological Rigor | 0.83 | Lanchester attrition modeling applied; Bayesian update from 1,572 days of observable record |
| Temporal Stability | 0.85 | Front-line positions stable over 30-day rolling window; low near-term volatility |
| **Composite** | **0.85** | |

---

## VI. BRIER SCORE TRACKING (Resolved Scenarios)

*No scenarios resolved yet — baseline established June 15, 2026. First resolution check: G7 Évian outcome (June 17) and NATO Ankara outcome (July 2026).*

| Scenario ID | Forecast P | Outcome | Brier Score | Resolved |
|---|---:|---|---:|---|
| *(pending)* | | | | |

---

## VII. UPDATE LOG

| Timestamp | Scenario ID | Old P | New P | ΔP | Trigger |
|---|---|---:|---:|---:|---|
| 2026-06-15T09:45:00Z | (all) | — | (baseline) | — | Initial baseline commit — War Day 1,572 |

---

## VIII. PRIOR STATE REFERENCE

- [Ukraine Ledger W24](QGIA_Ukraine_Ledger_2026-W24.md)
- [QGIA Weekly Rollup W24](../weekly-rollups/QGIA_Weekly_Rollup_2026-W24_June09-15.md)
- ISW Russian Offensive Campaign Assessment, June 9, 2026

---

*Generated: June 15, 2026 | OSIQP v4.2.1 | ABCP Active | Senior Analyst TS/SCI*
*Next mandatory update triggers: G7 Évian outcome (June 17); NATO Ankara outcome (July 2026)*
