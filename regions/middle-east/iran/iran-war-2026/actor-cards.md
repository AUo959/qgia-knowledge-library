# Iran War 2026 — Actor Cards

**Baseline date:** 2026-04-19T00:00:00Z  
**Last audit:** 2026-06-15T09:00:00 EDT  
All cards conform to the actor card schema defined in `qgia-knowledge-spine/schemas/actor-card-schema.md`.

> **Audit note (2026-06-15):** Ali Khamenei was killed approximately March 1, 2026 during Operation Epic Fury. Mojtaba Khamenei (son, IRGC-aligned) has succeeded as Supreme Leader. All IRGC_QF and IRN regime actor cards have been updated to reflect the succession. The uranium transfer directive (barring foreign export of enriched material) was issued by Mojtaba Khamenei in the days before MoU finalization — this is now the primary constraint node in the nuclear scenario tree.

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
    "supreme_leader_directives",
    "us_domestic_division",
    "regional_ally_signals",
    "irgc_casualty_index",
    "clerical_backing_signals",
    "battlefield_missile_drone_effectiveness"
  ],
  "hard_constraints": [
    "comply_with_supreme_leader_uranium_transfer_directive",
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
  "current_state_note": "As of June 15, 2026: IRGC cohesion has held through 107 days of kinetic conflict. Mojtaba Khamenei succession reinforces IRGC institutional power — Mojtaba is IRGC-aligned and his ascension represents a consolidation of IRGC influence at the Supreme Leader level. The uranium transfer directive issued by Mojtaba Khamenei immediately before MoU finalization is the clearest expression of IRGC/SL nuclear red lines. Model this directive as a hard constraint on nuclear talks outcomes.",
  "validation_status": "active",
  "updated_at": "2026-06-15T09:00:00Z"
}
```

---

## Supreme Leader Node

```json
{
  "actor_id": "IRN_SUPREME_LEADER",
  "display_name": "Supreme Leader of Iran",
  "type": "state_executive_supreme",
  "current_holder": "Mojtaba Khamenei",
  "previous_holder": "Ali Khamenei (KIA ~2026-03-01, Operation Epic Fury)",
  "succession_notes": "Mojtaba Khamenei (son of Ali Khamenei) assumed Supreme Leader role ~March 2026 following Ali Khamenei's death. Mojtaba is IRGC-aligned, ideologically conservative, and assessed as less pragmatic than his father on nuclear and foreign policy issues. His uranium transfer directive (June 2026, barring export of enriched material abroad) is the primary structural constraint on MoU Stage 2 nuclear talks.",
  "decision_mode": ["ideological", "IRGC_aligned", "hardline"],
  "utilities": {
    "regime_survival": 5,
    "nuclear_latency_preservation": 5,
    "irgc_institutional_power": 4,
    "ideological_legitimacy": 4,
    "economic_recovery": 2
  },
  "hard_constraints": [
    "no_uranium_transfer_abroad",
    "preserve_enrichment_as_NPT_right",
    "maintain_IRGC_institutional_primacy"
  ],
  "validation_status": "active",
  "updated_at": "2026-06-15T09:00:00Z"
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
    "hezbollah_escalation_level",
    "netanyahu_corruption_trial_status"
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
    },
    {
      "condition_id": "NETANYAHU_TRIAL_PRESSURE_HIGH",
      "if": { "indicator": "netanyahu_corruption_trial_status", "operator": "==", "threshold": "active_resumed" },
      "then": {
        "scenario_id_scope": "Tactical / Modality Set in qgia-knowledge-spine/frameworks/iran-war-scenario-taxonomy.md",
        "increase_probabilities": { "scenario_ids": ["ISR_MODE_SUSTAINED_AIR_CAMPAIGN"], "delta": 0.06 },
        "decrease_probabilities": { "scenario_ids": ["ISR_MODE_EARLY_CEASEFIRE_ACCEPTANCE"], "delta": 0.06 }
      }
    }
  ],
  "current_state_note": "As of June 15, 2026: Netanyahu's corruption trial resumed April 9 after state of emergency lifted. Elections scheduled before October 27, 2026. Israeli public opinion: 61% oppose US-Iran ceasefire; 73% expect hostilities to resume within one year. IDF continued strikes in southern Beirut on June 14-15 despite MoU ceasefire provisions — this is the primary spoiler risk for June 19 signing. Netanyahu has overlapping electoral and legal incentives to prolong the conflict. Model Lebanon compliance as probabilistic, not assumed. President Herzog mediating possible plea deal — this is a potential de-escalation vector for the trial incentive structure.",
  "notes": "Netanyahu modeled under TRUMP REACTIVE-AGENT MODEL equivalent: political survival and domestic coalition stability are co-equal drivers with strategic objectives. Treat domestic political pressure as a primary rather than secondary input.",
  "validation_status": "active",
  "updated_at": "2026-06-15T09:00:00Z"
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
  "empirical_validation": {
    "GAS_PRICE_SPIKE_trigger": "VALIDATED — Brent crude ~$119/bbl peak in late April triggered observable US_MODE_SIGNAL_CEASEFIRE behavior (Trump cancelled strikes June 11; MoU framework pursued). Trigger rule fired as modeled. Reactive-agent model confirmed.",
    "US_CASUALTY_THRESHOLD_trigger": "PARTIALLY VALIDATED — US casualty reports contributed to ceasefire signaling; not solely determinative given concurrent gas price pressure. Interaction effects between triggers noted for future model refinement."
  },
  "current_state_note": "As of June 15, 2026: Trump approval at 35% (Reuters/Ipsos); 38.3% pollster average. Only 22% approve cost-of-living handling. Democrats +5.8% generic ballot. Midterm structural pressure (November 3, 2026) is now the dominant driver of US_MODE_SIGNAL_CEASEFIRE and deal-urgency behavior. MoU signing set June 19 Geneva — deal optics utility (score: 5) is primary motivation.",
  "notes": "Modeled under permanent TRUMP REACTIVE-AGENT MODEL override per QGIA standing directive. Chaos, impulse, and external pressure are primary drivers. Deliberate strategic planning is not the default assumption.",
  "validation_status": "active",
  "updated_at": "2026-06-15T09:00:00Z"
}
```
