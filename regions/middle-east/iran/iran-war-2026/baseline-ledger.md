# Iran War 2026 — Baseline Probability Ledger

**Baseline date:** 2026-04-19T00:00:00Z  
**Last audit:** 2026-06-15T09:00:00 EDT  
**Forecast context:** Active kinetic conflict; Operation Epic Fury in progress; Strait of Hormuz contested.

> **Audit note (2026-06-15):** MoU finalized June 14; signing ceremony set Geneva June 19. MoU is **unsigned** as of this audit. Israeli Lebanon compliance unconfirmed. Khamenei II uranium authorization pending. No scenario dependent on MoU implementation, nuclear talks, or Israeli compliance has been resolved. Only time-bounded windows that expired before June 15 have been closed.

---

## Strategic War Outcomes (0–180 days)

All entries modeled as independent Beta/Bernoulli events.

| Scenario ID | Scenario Label | Window | P (baseline) | P (current) | ΔP | Confidence | Resolution | Notes |
|---|---|---|---:|---:|---:|---:|---|---|
| `IRN_WAR_CEASEFIRE_0_60D` | Early ceasefire | 0–60d | 0.24 | — | — | 0.68 | **RESOLVED FALSE** | Window expired 2026-04-29 (Day 60). No ceasefire occurred. MoU under negotiation did not meet 0–60d window criterion. Clean temporal resolution independent of June 19 outcome. |
| `IRN_WAR_PROTRACTED_AIR_CAMPAIGN_60_180D` | Protracted air campaign | 60–180d | 0.51 | — | — | 0.74 | **RESOLVED TRUE** | Campaign active through Day 107 (June 15) with no decisive settlement. Confirmed hit. |
| `IRN_WAR_HORMUZ_CLOSURE_GE_60D` | Hormuz closure ≥ 60 days | 0–180d | 0.37 | — | — | 0.72 | **RESOLVED TRUE** | Closure began Feb 28; still active June 15 = 107 days. IEA confirmed "largest supply disruption in history of global oil market." Confirmed hit. |
| `IRN_WAR_CARRIER_COMBAT_LOSS` | Carrier combat loss | 0–180d | 0.11 | 0.07 | −0.04 | 0.63 | **OPEN** | Window expires ~2026-08-26 (Day 180). No carrier loss confirmed as of June 15. Probability revised down given MoU framework reducing kinetic intensity. |
| `IRN_WAR_REGION_WIDE_CONFLICT_GE_6_STATES` | Regional war ≥ 6 states | 0–180d | 0.46 | — | — | 0.76 | **RESOLVED TRUE** | ABC News confirmed 11 countries struck by Day 6 (March 5). Threshold of ≥6 states exceeded by Day 6. Confirmed hit with wide margin. |
| `IRN_WAR_NUCLEAR_DECISION_WITHIN_12M` | Nuclear weaponization decision | 12m | 0.29 | 0.21 | −0.08 | 0.64 | **OPEN** | Window expires 2027-02-28. MoU framework (if signed) reduces near-term incentive; nuclear talks deferred to 60-day follow-on. Khamenei II uranium directive (barring transfer abroad) is active constraint. No weaponization decision confirmed. Probability revised down modestly given MoU pathway. |

---

## Regime Trajectory Set (12 months)

Modeled as mutually exclusive and collectively exhaustive. Use Dirichlet prior Dir(4.0, 2.0, 1.8, 1.2). Rows must sum to 1.00.

| Scenario ID | Scenario Label | Window | P (baseline) | P (current) | ΔP | Confidence | Resolution | Notes |
|---|---|---|---:|---:|---:|---:|---|---|
| `IRN_REGIME_H1_HARDLINE_SURVIVAL` | Hardline survival | 12m | 0.44 | 0.49 | +0.05 | 0.72 | **OPEN** | Window expires ~2027-02-28. Mojtaba Khamenei succession confirmed as new Supreme Leader. IRGC cohesion intact through 107-day campaign. Wartime nationalism observed. MoU negotiated from position of resilience, not collapse. Probability revised upward. |
| `IRN_REGIME_H2_MANAGED_TRANSITION` | Managed internal transition | 12m | 0.22 | 0.24 | +0.02 | 0.67 | **OPEN** | MoU pathway creates a diplomatic opening vector for partial elite rebalancing. Slight upward revision. |
| `IRN_REGIME_H3_REVOLUTIONARY_COLLAPSE` | Revolutionary collapse | 12m | 0.20 | 0.16 | −0.04 | 0.68 | **OPEN** | IRGC cohesion and Khamenei II succession reduce collapse probability. Revised down. |
| `IRN_REGIME_H4_FRAGMENTED_AUTHORITY` | Fragmented authority | 12m | 0.14 | 0.11 | −0.03 | 0.65 | **OPEN** | Same factors as H3. Revised down. |
| **Total** | | | **1.00** | **1.00** | | | | Dirichlet constraint maintained. |

---

## Composite Confidence Breakdown

Composite confidence uses the QGIA Confidence Calibration Score formula: `CCS = (0.30 × DQ) + (0.25 × SR) + (0.25 × MR) + (0.20 × TS)`.

| Component | Score (baseline) | Score (current) | Notes |
|---|---:|---:|---|
| Data Quality | 0.71 | 0.81 | 107 days of observable record materially improves ground truth |
| Source Reliability | 0.74 | 0.85 | Multi-source OSINT cross-validated across AP, Reuters, Al Jazeera, ISW, IEA |
| Methodological Rigor | 0.82 | 0.84 | ABCP ensemble + retrospective resolution validation active |
| Temporal Stability | 0.68 | 0.74 | MoU framework reduces near-term volatility; nuclear/Lebanon tracks remain fluid |
| **Composite** | **0.74** | **0.81** | |

---

## Brier Score Summary (Resolved Scenarios)

Brier Score formula: BS = (forecast − outcome)²

| Scenario ID | Forecast P | Outcome | Brier Score | Assessment |
|---|---:|---|---:|---|
| `IRN_WAR_CEASEFIRE_0_60D` | 0.24 | 0 (FALSE) | 0.058 | Good calibration — low probability, correctly did not occur |
| `IRN_WAR_PROTRACTED_AIR_CAMPAIGN_60_180D` | 0.51 | 1 (TRUE) | 0.240 | Slightly underconfident — should have been higher given force postures |
| `IRN_WAR_HORMUZ_CLOSURE_GE_60D` | 0.37 | 1 (TRUE) | 0.397 | Underconfident — closure was near-certain given IRGC doctrine and April precedent |
| `IRN_WAR_REGION_WIDE_CONFLICT_GE_6_STATES` | 0.46 | 1 (TRUE) | 0.292 | Underconfident — regional spillover was structurally overdetermined |
| **Mean Brier Score** | | | **0.247** | Acceptable calibration; systematic underconfidence on Iranian escalation scenarios |

> **Calibration note:** The April 19 baseline systematically underweighted Iranian resolve and IRGC escalation capacity. The reactive-agent model applied to Trump correctly predicted ceasefire-signaling behavior; the corresponding Iranian mirror image (IRGC as a high-resolve, high-endurance actor) was underweighted. Recommend upward baseline adjustment for IRGC resolve indicators in future scenario sets.

---

## Update Log

| Timestamp | Scenario ID | Old P | New P | ΔP | Trigger |
|---|---|---:|---:|---:|---|
| 2026-04-19T00:00:00Z | (all) | — | (baseline) | — | Initial baseline commit |
| 2026-06-15T09:00:00Z | `IRN_WAR_CEASEFIRE_0_60D` | 0.24 | RESOLVED FALSE | — | Window expiry (Day 60 = 2026-04-29); no ceasefire occurred |
| 2026-06-15T09:00:00Z | `IRN_WAR_PROTRACTED_AIR_CAMPAIGN_60_180D` | 0.51 | RESOLVED TRUE | — | Campaign confirmed active through Day 107 |
| 2026-06-15T09:00:00Z | `IRN_WAR_HORMUZ_CLOSURE_GE_60D` | 0.37 | RESOLVED TRUE | — | 107-day confirmed closure; IEA corroboration |
| 2026-06-15T09:00:00Z | `IRN_WAR_REGION_WIDE_CONFLICT_GE_6_STATES` | 0.46 | RESOLVED TRUE | — | 11 states struck confirmed by Day 6 |
| 2026-06-15T09:00:00Z | `IRN_WAR_CARRIER_COMBAT_LOSS` | 0.11 | 0.07 | −0.04 | MoU framework reduces kinetic intensity; no carrier loss confirmed |
| 2026-06-15T09:00:00Z | `IRN_WAR_NUCLEAR_DECISION_WITHIN_12M` | 0.29 | 0.21 | −0.08 | MoU nuclear talks pathway active; Khamenei II uranium directive constrains but does not eliminate risk |
| 2026-06-15T09:00:00Z | `IRN_REGIME_H1_HARDLINE_SURVIVAL` | 0.44 | 0.49 | +0.05 | Mojtaba Khamenei succession; IRGC cohesion confirmed through 107-day campaign |
| 2026-06-15T09:00:00Z | `IRN_REGIME_H2_MANAGED_TRANSITION` | 0.22 | 0.24 | +0.02 | MoU diplomatic opening creates partial transition vector |
| 2026-06-15T09:00:00Z | `IRN_REGIME_H3_REVOLUTIONARY_COLLAPSE` | 0.20 | 0.16 | −0.04 | IRGC cohesion and succession stability reduce collapse probability |
| 2026-06-15T09:00:00Z | `IRN_REGIME_H4_FRAGMENTED_AUTHORITY` | 0.14 | 0.11 | −0.03 | Same factors as H3 |
