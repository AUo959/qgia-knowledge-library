# Iran War 2026 — Actor Cards

**Baseline date:** 2026-04-19T00:00:00Z  
All cards conform to the actor card schema defined in `qgia-knowledge-spine/schemas/actor-card-schema.md`.

Mode identifiers referenced in trigger rules are defined by the Tactical / Modality Set in `qgia-knowledge-spine/frameworks/iran-war-scenario-taxonomy.md`; they are mode-taxonomy references, not standalone rows in this package's probability ledger.

---

## IRGC-QF / IRGC High Command

```json
{
  "actor_id": "IRGC_QF",
  "display_name": "IRGC-Qods Force / IRGC High Command",
  "type": "sub_state_military",
  "decision_mode": ["reactive", "ideological"],
  "utilities": {
    "regime_survival": 5,
    "deterrent_image": 4,
    "regional_influence": 4,
    "ideological_mission": 3,
    "economic_stability": 2
  },
  "risk_appetite": "medium_high",
  "time_horizon": ["medium"],
  "info_inputs": [
    "us_domestic_division",
    "regional_ally_signals",
    "irgc_casualty_index",
    "clerical_backing_signals",
    "battlefield_missile_drone_effectiveness"
  ],
  "hard_constraints": [
    "avoid_first_strike_carrier_kill_unless_regime_survival_at_risk",
    "avoid_irgc_regular_army_fracture",
    "avoid_actions_triggering_russia_china_overt_opposition"
  ],
  "trigger_rules": [
    {
      "condition_id": "US_DOMESTIC_DIVISION_HIGH",
      "if": { "indicator": "us_domestic_division", "operator": ">=", "threshold": 0.7 },
      "then": {
        "scenario_id_scope": "Tactical / Modality Set in qgia-knowledge-spine/frameworks/iran-war-scenario-taxonomy.md",
        "increase_probabilities": { "scenario_ids": ["IRN_MODE_PROXY_ESCALATION_SLOW_BURN"], "delta": 0.05 },
        "decrease_probabilities": { "scenario_ids": ["IRN_MODE_NO_ESCALATION"], "delta": 0.04 }
      }
    },
    {
      "condition_id": "REGIME_SURVIVAL_CRITICAL",
      "if": { "indicator": "IRN_REGIME_H3_REVOLUTIONARY_COLLAPSE", "operator": ">=", "threshold": 0.35 },
      "then": {
        "scenario_id_scope": "Tactical / Modality Set in qgia-knowledge-spine/frameworks/iran-war-scenario-taxonomy.md",
        "increase_probabilities": { "scenario_ids": ["IRN_MODE_HIGH_END_NAVAL_GAMBIT", "IRN_MODE_GULF_INFRASTRUCTURE_STRIKES"], "delta": 0.08 }
      }
    }
  ],
  "notes": "IRGC-QF modeled as primary decision node for proxy activation, missile/drone ops, and unconventional naval actions. Regular IRGC ground forces treated as separate node for escalation modeling.",
  "validation_status": "draft",
  "updated_at": "2026-04-19T00:00:00Z"
}
```

---

## Netanyahu Coalition / Israeli War Cabinet

```json
{
  "actor_id": "ISR_NETANYAHU_COALITION",
  "display_name": "Netanyahu Coalition / Israeli War Cabinet",
  "type": "state_executive",
  "decision_mode": ["reactive", "domestic_constrained", "escalation_tolerant"],
  "utilities": {
    "iran_nuclear_program_destruction": 5,
    "political_survival_netanyahu": 5,
    "idf_deterrence_restoration": 4,
    "us_support_maintenance": 4,
    "civilian_casualty_minimization": 2
  },
  "risk_appetite": "high",
  "time_horizon": ["short", "medium"],
  "info_inputs": [
    "us_force_posture_signals",
    "idf_sortie_sustainability",
    "domestic_coalition_stability",
    "iran_nuke_site_damage_assessment",
    "hezbollah_escalation_level"
  ],
  "hard_constraints": [
    "avoid_actions_causing_US_to_publicly_withdraw_support",
    "avoid_IDF_ground_incursion_Iran_without_US_backing"
  ],
  "trigger_rules": [
    {
      "condition_id": "US_SIGNALS_CEASEFIRE",
      "if": { "indicator": "US_MODE_SIGNAL_CEASEFIRE", "operator": "==", "threshold": 1 },
      "then": {
        "scenario_id_scope": "Tactical / Modality Set in qgia-knowledge-spine/frameworks/iran-war-scenario-taxonomy.md",
        "increase_probabilities": { "scenario_ids": ["ISR_MODE_TACTICAL_PAUSE"], "delta": 0.10 },
        "decrease_probabilities": { "scenario_ids": ["ISR_MODE_DEEP_STRIKES_IRAN"], "delta": 0.06 }
      }
    }
  ],
  "notes": "Netanyahu modeled under TRUMP REACTIVE-AGENT MODEL equivalent: political survival and domestic coalition stability are co-equal drivers with strategic objectives. Treat domestic political pressure as a primary rather than secondary input.",
  "validation_status": "draft",
  "updated_at": "2026-04-19T00:00:00Z"
}
```

---

## US Executive Node

```json
{
  "actor_id": "US_EXECUTIVE_TRUMP",
  "display_name": "US Executive / Trump Administration",
  "type": "state_executive",
  "decision_mode": ["reactive", "impulsive", "pressure_driven"],
  "utilities": {
    "deal_optics": 5,
    "us_casualty_avoidance": 5,
    "oil_price_control": 4,
    "appearing_strong": 4,
    "allied_coordination": 2
  },
  "risk_appetite": "variable",
  "time_horizon": ["short"],
  "info_inputs": [
    "us_economic_indicators",
    "gas_price_index",
    "domestic_approval_rating",
    "fox_news_framing",
    "us_military_casualty_reports"
  ],
  "hard_constraints": [
    "avoid_formal_war_declaration_without_deal_narrative",
    "avoid_actions_that_visibly_crash_us_equity_markets"
  ],
  "trigger_rules": [
    {
      "condition_id": "US_CASUALTY_THRESHOLD",
      "if": { "indicator": "us_military_casualty_reports", "operator": ">=", "threshold": 0.6 },
      "then": {
        "scenario_id_scope": "Tactical / Modality Set in qgia-knowledge-spine/frameworks/iran-war-scenario-taxonomy.md",
        "increase_probabilities": { "scenario_ids": ["US_MODE_SIGNAL_CEASEFIRE"], "delta": 0.12 },
        "decrease_probabilities": { "scenario_ids": ["US_MODE_ESCALATE_RHETORIC"], "delta": 0.08 }
      }
    },
    {
      "condition_id": "GAS_PRICE_SPIKE",
      "if": { "indicator": "gas_price_index", "operator": ">=", "threshold": 0.75 },
      "then": {
        "scenario_id_scope": "Tactical / Modality Set in qgia-knowledge-spine/frameworks/iran-war-scenario-taxonomy.md",
        "increase_probabilities": { "scenario_ids": ["US_MODE_SIGNAL_CEASEFIRE", "US_MODE_NAVAL_CONVOY_THREAT"], "delta": 0.07 }
      }
    }
  ],
  "notes": "Modeled under permanent TRUMP REACTIVE-AGENT MODEL override per QGIA standing directive. Chaos, impulse, and external pressure are primary drivers. Deliberate strategic planning is not the default assumption.",
  "validation_status": "draft",
  "updated_at": "2026-04-19T00:00:00Z"
}
```
