# QGIA DOMESTIC US — APPROVAL & MIDTERM LEDGER
**Week 24 | June 15, 2026 | 141 days to Midterms (Nov 3, 2026)**
**Classification: PROPRIETARY | OSIQP v4.2.1**
**Composite Confidence: 0.84 | Quantum Coherence: 0.82**

> **Testability standard:** Every scenario carries a `falsification_condition` with a specific, observable, dateable outcome criterion. Prediction market signals are secondary/contextual only per QGIA standing directive. ABCP structural models are primary.

---

## I. TRUMP APPROVAL TRAJECTORY

### Current Aggregate (June 14, 2026)

| Aggregator | Approve | Disapprove | Net | Updated |
|---|---:|---:|---:|---|
| Ballotpedia | 40.0% | 58.0% | −18.0 | June 4 |
| CNN | 36.0% | 63.0% | −27.0 | June 4 |
| Decision Desk HQ | 39.5% | 56.9% | −17.4 | June 4 |
| FiftyPlusOne | 37.0% | 59.1% | −22.1 | June 14 |
| RealClearPolitics | 40.3% | 57.1% | −16.8 | June 4 |
| Silver Bulletin | 38.9% | 57.5% | −18.6 | June 4 |
| The Economist/YouGov | 35.0% | 60.0% | −25.0 | June 5–8 |
| NBC News (registered voters) | 42.0% | 57.0% | −15.0 | May–June 7 |
| NBC News (all adults) | 39.0% | 58.0% | −19.0 | May–June 7 |
| **QGIA Composite Average** | **38.5%** | **58.3%** | **−19.8** | **June 14** |

*Source: Wikipedia aggregate, NBC News poll (Trump's 80th birthday release June 14), FiftyPlusOne, USA Today, Newsweek.*

**Key sub-group deterioration:**
- Rural Americans: 50% approval (June 3–8 Reuters/Ipsos) vs. 60% at inauguration Feb 2025 — **−10 points**
- Cost-of-living approval: 22% (QGIA prior briefing)
- Iran war management: 53% view Iran military action as a failure (Emerson April 2026)

---

## II. GENERIC BALLOT TRACKING

| Poll / Source | Democrat | Republican | D Lead | Date |
|---|---:|---:|---:|---|
| Marist (Nov 2025) | 55% | 41% | +14 | Nov 2025 |
| WaPo/ABC/Ipsos (Feb 2026) | 47% | 45% | +2 (reg voters) / +10 (certain voters) | Feb 2026 |
| Fox News (Feb 2026) | 52% | 46% | +6 | Feb 2026 |
| Data for Progress (May 2026) | — | — | +8 | May 20, 2026 |
| Emerson College (April 2026) | 50% | 40% | +10 | April 2026 |
| **QGIA Composite Average** | | | **+7.5 to +8.5** | **June 2026** |

*Enthusiasm gap: 79% of registered Democrats "certain to vote" vs. 65% of registered Republicans (WaPo/ABC/Ipsos Feb 2026) — 14-point gap, largest since at least 2016.*

---

## III. CONSTITUTIONAL STRESS INDEX

| Indicator | Value | Date | Source |
|---|---|---|---|
| Voters agreeing US is in constitutional crisis | **73%** | June 9, 2026 | Pell Center / Salve Regina Univ. |
| Democrats agreeing | 95% | June 9, 2026 | Pell Center |
| Independents agreeing | 79% | June 9, 2026 | Pell Center |
| Republicans agreeing | 48% | June 9, 2026 | Pell Center |
| Prior crisis agreement reading (Oct 2025) | 57% | Oct 2025 | States United Democracy Center |
| Change Oct 2025 → June 2026 | **+16 points** | — | QGIA calculation |

**ABCP Note:** The 73% constitutional crisis reading (June 9) represents a historically significant level. The +16 point acceleration in 8 months (57% Oct 2025 → 73% June 2026) is a leading indicator of structural enthusiasm asymmetry in November. Cross-referencing with 2006 and 2018 midterm cycles: both showed approval ratings and "wrong track" indicators at comparable levels and produced 31+ seat Democratic gains.

---

## IV. MIDTERM FORECAST SCENARIOS (Testable)

### House of Representatives

| Scenario ID | Scenario Label | P (baseline) | Confidence | Resolution Date | Falsification Condition |
|---|---|---:|---:|---|---|
| `DOM_HOUSE_DEM_MAJORITY` | Democrats retake House majority | 0.61 | 0.79 | **Nov 3–4, 2026** | **TRUE if:** AP/NBC/Fox call House majority for Democrats on election night or within 7 days. **FALSE if:** Republicans retain ≥ 218 seats per AP final call |
| `DOM_HOUSE_NARROW_DEM` | Democrats win House by ≤ 10 seats | 0.22 | 0.69 | Nov 3–7, 2026 | **TRUE if:** AP final House call shows Democratic majority of 218–227 seats. **FALSE if:** Democratic majority exceeds 228 seats OR Republicans retain majority |
| `DOM_HOUSE_LARGE_DEM_WAVE` | Democrats win ≥ 30 net seats | 0.18 | 0.66 | Nov 3–14, 2026 | **TRUE if:** AP final call shows Democrats net ≥ 30 seats vs. current Republican majority. **FALSE if:** Democratic net gain < 30 seats |
| `DOM_HOUSE_GOP_RETENTION` | Republicans retain House majority | 0.31 | 0.73 | Nov 3–14, 2026 | **TRUE if:** Republicans hold ≥ 218 seats per AP final call. **FALSE if:** Democrats called as majority |

*Note: DOM_HOUSE_DEM_MAJORITY and DOM_HOUSE_GOP_RETENTION are complementary — they sum to ~0.92 (leaving 0.08 for unresolved/special circumstances). DOM_HOUSE_NARROW_DEM and DOM_HOUSE_LARGE_DEM_WAVE are subsets of DOM_HOUSE_DEM_MAJORITY and do not need to sum with it.*

### Senate

| Scenario ID | Scenario Label | P (baseline) | Confidence | Resolution Date | Falsification Condition |
|---|---|---:|---:|---|---|
| `DOM_SENATE_GOP_RETENTION` | Republicans retain Senate | 0.72 | 0.80 | Nov 3–14, 2026 | **TRUE if:** Republicans hold ≥ 51 Senate seats after Nov 3 election per AP final call. **FALSE if:** Democrats + Independents reach ≥ 50 seats with VP tiebreak or ≥ 51 outright |
| `DOM_SENATE_DEM_MAJORITY` | Democrats retake Senate | 0.21 | 0.67 | Nov 3–14, 2026 | **TRUE if:** Democrats + caucusing Independents reach ≥ 50 seats (with VP tiebreak) or ≥ 51 outright per AP final call. **FALSE if:** Republicans hold ≥ 51 seats |
| `DOM_SENATE_50_50_TIE` | 50–50 Senate with VP tiebreak | 0.07 | 0.62 | Nov 3–14, 2026 | **TRUE if:** Final Senate composition is exactly 50–50 and Democratic VP holds tiebreak. **FALSE if:** Either party holds outright majority |

---

## V. APPROVAL TRAJECTORY SCENARIOS (Testable)

| Scenario ID | Scenario Label | Window | P (baseline) | Confidence | Resolution | Falsification Condition |
|---|---|---|---:|---:|---|---|
| `DOM_APPR_IRAN_BOUNCE_GE5PT` | Trump approval rises ≥ 5 points on Iran MoU signing | 0–30d post-Geneva | 0.44 | 0.73 | OPEN | **TRUE if:** QGIA composite average approval rises to ≥ 43.5% within 21 days of confirmed MoU signing at Geneva. **FALSE if:** Composite average remains below 43.0% at Day 21 post-signing |
| `DOM_APPR_NEW_LOW_SUB35` | Trump approval drops below 35% composite | 0–90d | 0.22 | 0.68 | OPEN | **TRUE if:** QGIA composite average falls below 35.0% and holds for ≥ 7 consecutive days. **FALSE if:** Composite average does not breach 35.0% before Sept 15, 2026 |
| `DOM_APPR_MIDTERM_FLOOR_38` | Approval stabilizes 38–42% range through Nov | 6–16 weeks | 0.51 | 0.76 | OPEN | **TRUE if:** QGIA composite average remains in the 38.0–42.0% band from July 1 through Nov 2, 2026 without a sustained (≥ 7-day) breach in either direction. **FALSE if:** Composite falls below 38.0% OR rises above 42.0% for ≥ 7 consecutive days |

---

## VI. CONSTITUTIONAL STRESS SCENARIOS (Testable)

| Scenario ID | Scenario Label | Window | P (baseline) | Confidence | Resolution | Falsification Condition |
|---|---|---|---:|---:|---|---|
| `DOM_CONST_SCOTUS_MAJOR_RULING_VS_EXEC` | SCOTUS issues major ruling against executive action | 0–6m | 0.47 | 0.74 | OPEN | **TRUE if:** SCOTUS issues a ruling (≥ 5-4) that directly strikes down or substantially limits a Trump executive action or order, with public compliance statement from administration required. **FALSE if:** No such ruling before Dec 15, 2026 |
| `DOM_CONST_CONTEMPT_ESCALATION` | Congressional or judicial contempt proceeding escalates to enforcement standoff | 0–6m | 0.31 | 0.69 | OPEN | **TRUE if:** A federal court issues a contempt finding against a named executive branch official that the administration publicly refuses to enforce, confirmed by at least 2 of AP/Reuters/NYT/WaPo. **FALSE if:** No such confirmed refusal-to-enforce incident before Dec 15, 2026 |
| `DOM_CONST_NATL_EMERGENCY_MIDTERM_CONTEXT` | National emergency declaration used with explicit electoral nexus | 0–5m | 0.14 | 0.66 | OPEN | **TRUE if:** President declares national emergency within 60 days of Nov 3 election AND declaration is characterized by ≥ 3 legal scholars in major outlets as having an electoral rationale. **FALSE if:** No such declaration-plus-characterization event before Nov 3, 2026 |

---

## VII. STRUCTURAL MODEL INPUTS

QGIA domestic structural model uses the following fundamentals-based inputs. All values sourced from published polls as of June 14, 2026.

| Input | Current Value | Historical Midterm Benchmark | Signal |
|---|---|---|---|
| Presidential approval (composite) | 38.5% | Sub-45% → net loss for president's party | ⚠️ BEARISH for GOP |
| Generic ballot (D lead) | +7.5 to +8.5 pts | +7 pts → historically ~20–25 seat swing | ⚠️ BEARISH for GOP |
| Enthusiasm gap | Dems +14 pts certainty-to-vote | +10 pts → structural turnout advantage | 🔴 BEARISH for GOP |
| Constitutional crisis perception | 73% | No historical midterm precedent above 60% | 🔴 BEARISH for GOP |
| Rural approval erosion | −10 pts from inauguration | Loss of rural margin typically decisive in competitive districts | ⚠️ BEARISH for GOP |
| Iran war approval | 53% view as failure | Major war mismanagement tracked in 2006 cycle (Iraq) → D+31 seats | ⚠️ BEARISH for GOP |

**ABCP Structural Projection (as of June 15, 2026):** Democratic net gain of **11–18 House seats** — sufficient to flip majority (current Republican majority requires D+9 or more to flip). Senate remains structurally favored GOP given map (more vulnerable Democratic seats up for election).

---

## VIII. UPDATE LOG

| Timestamp | Scenario ID | Old P | New P | ΔP | Trigger |
|---|---|---:|---:|---:|---|
| 2026-06-15T09:45:00Z | (all) | — | (baseline) | — | Initial baseline commit |

*Next mandatory update triggers: G7 Évian outcome (Iran MoU bounce test); any Trump approval movement ≥ 3 points in 14-day window; SCOTUS term end (late June / early July 2026)*

---

## IX. PRIOR STATE REFERENCE

- [QGIA Weekly Rollup W24](../weekly-rollups/QGIA_Weekly_Rollup_2026-W24_June09-15.md)
- [QGIA Global Monitoring Report 2026-06-14](../QGIA_Global_Monitoring_Report_2026-06-14.md)
- Wikipedia: Opinion polling on the second Trump presidency (June 4, 2026 aggregate)
- Pell Center / Salve Regina University constitutional crisis poll (June 9, 2026)
- NBC News poll (June 14, 2026 — second-term low)
- Data for Progress generic ballot (May 20, 2026)
- Emerson College national poll (April 2026)

---

*Generated: June 15, 2026 | OSIQP v4.2.1 | ABCP Active | Senior Analyst TS/SCI*
*Midterm countdown: 141 days*
