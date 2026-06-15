# Iran War 2026 — Scenario Catalog

**Baseline date:** 2026-04-19T00:00:00Z
**Last audit:** 2026-06-15T09:31:00 EDT
All `scenario_id` values conform to `qgia-knowledge-spine/frameworks/iran-war-scenario-taxonomy.md`.

> **Audit note (2026-06-15):** Three scenarios resolved since April 19 baseline. Tier structure rebuilt from `baseline-ledger.md` current P-values. Resolved scenarios moved to **Resolved Archive** section. MoU framework (unsigned as of audit; Geneva signing June 19) introduces post-ceasefire scenario set — see Tier I additions below.

---

## Tier I — Active Scenarios (P ≥ 0.25)

Primary drivers in all QGIA deliverables.

| Scenario ID | P (current) | Window | Tier | Delta vs. Baseline |
|---|---:|---|---|---:|
| `IRN_REGIME_H1_HARDLINE_SURVIVAL` | 0.49 | 12m | I | +0.05 |
| `IRN_WAR_NUCLEAR_DECISION_WITHIN_12M` | 0.21 → promoted to monitor | 12m | I→II | −0.08 |
| `IRN_MOU_SIGNING_SUCCESS_JUNE19` | 0.78 | 0–7d | **I (new)** | — |
| `IRN_NUCLEAR_TALKS_STALL_60D` | 0.42 | 0–60d post-MoU | **I (new)** | — |

> **Note:** `IRN_WAR_NUCLEAR_DECISION_WITHIN_12M` revised down to 0.21 — see Tier II below. `IRN_MOU_SIGNING_SUCCESS_JUNE19` added as a Tier I event-bounded scenario given 0.78 ABCP composite.

---

## Tier II — Elevated Risk Scenarios (P 0.10–0.25)

Materially elevated probability; must be included in risk exposure and scenario planning.

| Scenario ID | P (current) | Window | Tier | Delta vs. Baseline |
|---|---:|---|---|---:|
| `IRN_REGIME_H2_MANAGED_TRANSITION` | 0.24 | 12m | II | +0.02 |
| `IRN_REGIME_H3_REVOLUTIONARY_COLLAPSE` | 0.16 | 12m | II | −0.04 |
| `IRN_WAR_NUCLEAR_DECISION_WITHIN_12M` | 0.21 | 12m | II | −0.08 |
| `IRN_REGIME_H4_FRAGMENTED_AUTHORITY` | 0.11 | 12m | II | −0.03 |
| `IRN_WAR_CARRIER_COMBAT_LOSS` | 0.07 | 0–180d | **→ III** | −0.04 |
| `IRN_MOU_SIGNING_DELAYED_INFORMAL_CEASEFIRE` | 0.18 | 0–30d | **II (new)** | — |
| `IRN_NUCLEAR_PRELIMINARY_INSPECTION_AGREEMENT` | 0.28 | 60d post-MoU | **II (new)** | — |
| `IRN_RETURN_TO_HOSTILITIES_30D` | 0.09 | 0–30d post-MoU | **→ III** | — |

---

## Tier III — Low-Probability, High-Consequence (P < 0.10)

Retain for catastrophic tail risk framing; do not anchor planning on these.

| Scenario ID | P (current) | Window | Notes |
|---|---:|---|---|
| `IRN_WAR_CARRIER_COMBAT_LOSS` | 0.07 | 0–180d | Reduced from Tier II given MoU kinetic de-escalation trajectory |
| `IRN_RETURN_TO_HOSTILITIES_30D` | 0.09 | 0–30d post-MoU | Primary spoilers: Israeli Lebanon non-compliance; Khamenei II uranium authorization failure |
| `IRN_US_GROUND_FORCE_COMMITMENT` | 0.03 | 0–180d | Functionally impossible outlier per QGIA standing calibration |

---

## Resolved Archive

Scenarios with expired windows or confirmed outcomes. **Do not use as active tracking inputs.**

| Scenario ID | Baseline P | Outcome | Brier Score | Resolved |
|---|---:|---|---:|---|
| `IRN_WAR_CEASEFIRE_0_60D` | 0.24 | **FALSE** — no ceasefire by Day 60 (2026-04-29) | 0.058 | 2026-06-15 |
| `IRN_WAR_PROTRACTED_AIR_CAMPAIGN_60_180D` | 0.51 | **TRUE** — campaign active through Day 107 (June 15) | 0.240 | 2026-06-15 |
| `IRN_WAR_HORMUZ_CLOSURE_GE_60D` | 0.37 | **TRUE** — 107-day confirmed closure, IEA corroboration | 0.397 | 2026-06-15 |
| `IRN_WAR_REGION_WIDE_CONFLICT_GE_6_STATES` | 0.46 | **TRUE** — 11 states struck by Day 6 (March 5) | 0.292 | 2026-06-15 |

**Mean Brier Score (resolved set):** 0.247 — acceptable calibration with systematic underconfidence on Iranian escalation scenarios. See calibration note in `baseline-ledger.md`.

---

## Post-MoU Scenario Descriptions (New)

### `IRN_MOU_SIGNING_SUCCESS_JUNE19`
The 14-point MoU framework is signed at Geneva on or around June 19, 2026. Triggers: 30-day Hormuz implementation clock, $24B frozen asset release process, 60-day follow-on nuclear talks window. Primary spoilers: Israeli Lebanon non-compliance triggering Iranian walk-back; Khamenei II withholding final authorization on uranium language; US Senate pressure (Graham/Cruz faction).

### `IRN_NUCLEAR_TALKS_STALL_60D`
Follow-on nuclear talks (post-MoU) stall within 60 days without preliminary agreement. Most likely path: uranium enrichment transfer language irresolvable given Khamenei II directive barring foreign export. Kazakhstan storage option (IAEA Chief Grossi) remains only viable bridging mechanism. Stall does not automatically return to hostilities — frozen diplomacy track is possible.

### `IRN_NUCLEAR_PRELIMINARY_INSPECTION_AGREEMENT`
Partial breakthrough: IAEA access agreed to at three storage sites referenced in MoU "in principle" language. Does not resolve enrichment transfer dispute but reduces nuclear breakout timeline visibility gap. Probability conditional on MoU signing success.

### `IRN_MOU_SIGNING_DELAYED_INFORMAL_CEASEFIRE`
Geneva ceremony postponed beyond June 19 but informal kinetic pause holds. Most likely trigger: Israeli Lebanon operations continue through signing date, forcing Iranian delegation to pause pending Israeli compliance signal.

### `IRN_RETURN_TO_HOSTILITIES_30D`
Full resumption of kinetic conflict within 30 days of MoU signing. Requires conjunction of: Israeli Lebanon escalation + Khamenei II authorization failure + US domestic political reversal. Low probability but non-zero; primary monitoring indicators are IDF Lebanon sortie tempo and Khamenei II public statements.

---

## Legacy Scenario Descriptions (Unchanged)

### `IRN_REGIME_H1_HARDLINE_SURVIVAL`
The Islamic Republic survives the war period with its hardline political character intact. IRGC dominance is reinforced, succession (Mojtaba Khamenei, confirmed) stabilizes, and repression contains domestic unrest. Wartime nationalism provides a partial legitimacy buffer.

### `IRN_REGIME_H2_MANAGED_TRANSITION`
The regime survives but undergoes controlled internal rebalancing. MoU diplomatic pathway creates a partial transition vector. Probability slightly elevated post-MoU.

### `IRN_REGIME_H3_REVOLUTIONARY_COLLAPSE`
The existing regime structure falls through revolutionary or quasi-revolutionary transition. IRGC cohesion and Mojtaba Khamenei succession reduce near-term probability. Revised down from baseline.

### `IRN_REGIME_H4_FRAGMENTED_AUTHORITY`
No consolidated successor authority emerges within 12 months. Requires deeper organizational collapse than currently observable. Revised down from baseline.

### `IRN_WAR_NUCLEAR_DECISION_WITHIN_12M`
The Islamic Republic's leadership makes a strategic decision to move from nuclear latency to active weaponization. MoU nuclear talks pathway modestly reduces near-term incentive. Khamenei II uranium directive (barring foreign transfer) is an active constraint but simultaneously signals heightened nuclear autonomy logic. Window expires 2027-02-28.

### `IRN_WAR_CARRIER_COMBAT_LOSS`
A US or Allied carrier suffers combat loss or incapacitation. Reduced to Tier III given MoU kinetic de-escalation trajectory. Window expires ~2026-08-26 (Day 180). Probability rises materially if MoU fails and hostilities resume.

---

## Monitoring Indicators

| Indicator | Scenarios Affected | Threshold |
|---|---|---|
| IDF Lebanon sortie tempo post-MoU | `IRN_MOU_SIGNING_SUCCESS_JUNE19`, `IRN_RETURN_TO_HOSTILITIES_30D` | Any confirmed strike post-signing |
| Khamenei II public statement on uranium | `IRN_MOU_SIGNING_SUCCESS_JUNE19`, `IRN_NUCLEAR_TALKS_STALL_60D` | Authorization or rejection signal |
| Kazakhstan storage proposal response | `IRN_NUCLEAR_PRELIMINARY_INSPECTION_AGREEMENT` | IAEA acceptance or Iranian rejection |
| IRGC casualty index rising | H3, H4, IRGC trigger rules | Sustained elevation > 30 days |
| US domestic division index | IRGC trigger rules, ceasefire scenarios | ≥ 0.70 |
| Gas price index | US executive trigger rules | ≥ 0.75 |
| Elite defection signals | H3, H4 | Any observable |
| Hezbollah Lebanon re-activation | `IRN_RETURN_TO_HOSTILITIES_30D` | Confirmed Lebanese Hezbollah strike vs. IDF |
| IAEA site access — confirmed denial | `IRN_WAR_NUCLEAR_DECISION_WITHIN_12M` | Confirmed access denial |
