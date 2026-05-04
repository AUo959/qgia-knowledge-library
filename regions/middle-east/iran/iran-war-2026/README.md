# Iran War 2026 — Documentation Package

## Scope

This package contains baseline documentation for the Iran War 2026 assessment set within the QGIA Knowledge Library. It bridges reusable QGIA schema from the Knowledge Spine with theater-specific scenario definitions, actor cards, and probability ledgers.

## Package Contents

| File | Contents |
|---|---|
| `README.md` | This document |
| `baseline-ledger.md` | Initial probability estimates for strategic and regime scenarios |
| `actor-cards.md` | Behavioral profiles for IRGC-QF, Netanyahu Coalition, and US Executive |
| `scenario-catalog.md` | Full scenario index with brief descriptions and modeling notes |

## Current Analytical Focus

- Regime survival versus collapse dynamics under wartime pressure
- Strait of Hormuz closure persistence and economic cascade effects
- Carrier vulnerability and naval escalation tails
- Multi-state regional war expansion (≥ 6 states)
- Nuclear weaponization decision incentives inside a wartime survival frame

## Baseline Date

All initial estimates are anchored to: **2026-04-19T00:00:00Z**

## Dependencies

This package depends on the following QGIA Knowledge Spine documents:

- `qgia-knowledge-spine/frameworks/iran-war-scenario-taxonomy.md`
- `qgia-knowledge-spine/schemas/actor-card-schema.md`
- `qgia-knowledge-spine/schemas/probability-ledger-schema.md`
- `qgia-knowledge-spine/methods/iran-regime-dirichlet-template.md`

All `scenario_id` values used in this package must conform to the canonical taxonomy defined in the Spine.

Knowledge-index publication includes this `regions/` package as regional expertise content. The package README is indexed as `theater_readme`; the package ledger, actor cards, and scenario catalog use their matching document domains.

## Confidence Benchmarks

| Level | Range | Meaning |
|---|---|---|
| High | 0.75–1.00 | Multi-source corroboration, stable model agreement |
| Medium | 0.55–0.74 | Moderate source quality, some model divergence |
| Low | 0.00–0.54 | Sparse data, high uncertainty, treat as indicative only |

## Maintenance

- **Update frequency:** Event-driven during active crisis; weekly summary otherwise
- **Forecast horizons:** 0–30d, 1–6mo, 6–12mo
- **Package owner:** QGIA Middle East Analytical Cell
- **Versioning:** Append-only ledger; scenario catalog and actor cards versioned on change
