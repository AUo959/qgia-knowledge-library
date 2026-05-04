# Iran War 2026 — Baseline Probability Ledger

**Baseline date:** 2026-04-19T00:00:00Z  
**Forecast context:** Active kinetic conflict; Operation Epic Fury in progress; Strait of Hormuz contested.

---

## Strategic War Outcomes (0–180 days)

All entries modeled as independent Beta/Bernoulli events.

| Scenario ID | Scenario Label | Window | P | Prev P | ΔP | Confidence | Notes |
|---|---|---|---:|---:|---:|---:|---|
| `IRN_WAR_CEASEFIRE_0_60D` | Early ceasefire | 0–60d | 0.24 | — | — | 0.68 | Plausible but not favored; neither party at capitulation threshold. |
| `IRN_WAR_PROTRACTED_AIR_CAMPAIGN_60_180D` | Protracted air campaign | 60–180d | 0.51 | — | — | 0.74 | Dominant operational track under current force postures. |
| `IRN_WAR_HORMUZ_CLOSURE_GE_60D` | Hormuz closure ≥ 60 days | 0–180d | 0.37 | — | — | 0.72 | Sustained closure driven by attack risk and insurance shock. |
| `IRN_WAR_CARRIER_COMBAT_LOSS` | Carrier combat loss | 0–180d | 0.11 | — | — | 0.63 | Tail event; non-trivial under A2/AD stress and mass ASCM saturation. |
| `IRN_WAR_REGION_WIDE_CONFLICT_GE_6_STATES` | Regional war ≥ 6 states | 0–180d | 0.46 | — | — | 0.76 | Hezbollah, Houthis, Iraqi militia, and Gulf spillover already materially elevated. |
| `IRN_WAR_NUCLEAR_DECISION_WITHIN_12M` | Nuclear weaponization decision | 12m | 0.29 | — | — | 0.64 | Wartime survival pressure increases later weaponization incentives substantially. |

---

## Regime Trajectory Set (12 months)

Modeled as mutually exclusive and collectively exhaustive. Use Dirichlet prior Dir(4.0, 2.0, 1.8, 1.2). Rows must sum to 1.00.

| Scenario ID | Scenario Label | Window | P | Confidence | Notes |
|---|---|---|---:|---:|---|
| `IRN_REGIME_H1_HARDLINE_SURVIVAL` | Hardline survival | 12m | 0.44 | 0.72 | IRGC cohesion intact; wartime nationalism reinforcing regime. |
| `IRN_REGIME_H2_MANAGED_TRANSITION` | Managed internal transition | 12m | 0.22 | 0.67 | Internal adjustment without collapse; partial elite opening. |
| `IRN_REGIME_H3_REVOLUTIONARY_COLLAPSE` | Revolutionary collapse | 12m | 0.20 | 0.68 | Possible under sustained military losses and unrest; not dominant. |
| `IRN_REGIME_H4_FRAGMENTED_AUTHORITY` | Fragmented authority | 12m | 0.14 | 0.65 | Requires deeper institutional breakdown; currently lower-probability. |
| **Total** | | | **1.00** | | |

---

## Composite Confidence Breakdown

Composite confidence uses the QGIA Confidence Calibration Score formula: `CCS = (0.30 × DQ) + (0.25 × SR) + (0.25 × MR) + (0.20 × TS)`.

| Component | Score | Notes |
|---|---:|---|
| Data Quality | 0.71 | Active conflict limits observable ground truth |
| Source Reliability | 0.74 | Multi-source OSINT with moderate SIGINT corroboration |
| Methodological Rigor | 0.82 | Bayesian + Lanchester + ABCP ensemble active |
| Temporal Stability | 0.68 | Highly fluid; 0–30d estimates subject to rapid revision |
| **Composite** | **0.74** | |

---

## Update Log

| Timestamp | Scenario ID | Old P | New P | ΔP | Trigger |
|---|---|---:|---:|---:|---|
| 2026-04-19T00:00:00Z | (all) | — | (baseline) | — | Initial baseline commit |
