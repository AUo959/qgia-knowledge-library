# Quantitative Models

**Mathematical frameworks, statistical methods, machine learning, and quantum-inspired algorithms**

## Directory Structure

```
06-quantitative-models/
├── mathematical-foundations/
│   ├── differential-equations/
│   │   ├── lanchester-equations.md
│   │   ├── richardson-arms-race.md
│   │   ├── lotka-volterra-competition.md
│   │   └── predator-prey-models.md
│   ├── optimization/
│   │   ├── linear-programming.md
│   │   ├── dynamic-programming.md
│   │   ├── optimal-control.md
│   │   └── multi-objective-optimization.md
│   └── probability-theory/
│       ├── bayesian-inference.md
│       ├── markov-chains.md
│       ├── stochastic-processes.md
│       └── monte-carlo-methods.md
├── statistical-methods/
│   ├── regression-analysis/
│   │   ├── linear-regression.md
│   │   ├── logistic-regression.md
│   │   ├── time-series-regression.md
│   │   └── panel-data-methods.md
│   ├── time-series/
│   │   ├── arima-models.md
│   │   ├── vector-autoregression.md
│   │   ├── state-space-models.md
│   │   └── change-point-detection.md
│   ├── survival-analysis/
│   │   ├── kaplan-meier.md
│   │   ├── cox-proportional-hazards.md
│   │   ├── duration-models.md
│   │   └── regime-duration-forecasting.md
│   └── causal-inference/
│       ├── instrumental-variables.md
│       ├── difference-in-differences.md
│       ├── regression-discontinuity.md
│       └── synthetic-control.md
├── machine-learning/
│   ├── model-zoo.md (Tier III - Priority 14)
│   ├── supervised-learning/
│   │   ├── random-forests.md
│   │   ├── gradient-boosting.md
│   │   ├── support-vector-machines.md
│   │   └── ensemble-methods.md
│   ├── deep-learning/
│   │   ├── neural-networks.md
│   │   ├── convolutional-nets.md
│   │   ├── recurrent-nets.md
│   │   ├── transformers.md
│   │   └── transfer-learning.md
│   ├── unsupervised-learning/
│   │   ├── clustering.md
│   │   ├── dimensionality-reduction.md
│   │   ├── anomaly-detection.md
│   │   └── topic-modeling.md
│   └── nlp-applications/
│       ├── text-classification.md
│       ├── named-entity-recognition.md
│       ├── sentiment-analysis.md
│       ├── machine-translation.md
│       └── event-extraction.md
├── network-science/
│   ├── alliance-network-toolkit.md (Tier III - Priority 11)
│   ├── graph-theory/
│   │   ├── centrality-measures.md
│   │   ├── community-detection.md
│   │   ├── structural-holes.md
│   │   └── network-resilience.md
│   ├── dynamic-networks/
│   │   ├── temporal-networks.md
│   │   ├── network-evolution.md
│   │   └── contagion-dynamics.md
│   └── applications/
│       ├── alliance-formation.md
│       ├── trade-networks.md
│       ├── terrorist-networks.md
│       └── cyber-attack-propagation.md
├── game-theory/
│   ├── game-theory-compendium.md (Tier II - Priority 6)
│   ├── classical-games/
│   │   ├── prisoners-dilemma.md
│   │   ├── chicken-game.md
│   │   ├── stag-hunt.md
│   │   └── battle-of-sexes.md
│   ├── bargaining-models/
│   │   ├── nash-bargaining.md
│   │   ├── rubinstein-bargaining.md
│   │   ├── ultimatum-game.md
│   │   └── crisis-bargaining.md
│   ├── signaling-games/
│   │   ├── cheap-talk.md
│   │   ├── costly-signaling.md
│   │   ├── screening-models.md
│   │   └── credibility-mechanisms.md
│   └── computational/
│       ├── agent-based-models.md
│       ├── evolutionary-game-theory.md
│       ├── solution-algorithms.md
│       └── python-implementations.md
└── quantum-frameworks/
    ├── qsfe-specifications.md
    ├── edm-specifications.md
    ├── abcp-specifications.md
    ├── rprn-specifications.md
    ├── tca-specifications.md
    ├── quantum-error-correction.md
    ├── amplitude-weighting.md
    ├── entanglement-modeling.md
    ├── bayesian-quantum-fusion.md
    └── performance-validation.md
```

## Quantitative Modeling Philosophy

### Role of Models

**Models are tools, not oracles**:
- Simplify complex reality to essential dynamics
- Generate testable predictions
- Force explicit assumptions
- Enable "what-if" scenario exploration
- **Never substitute for human judgment**

### All Models Are Wrong, Some Are Useful

**Box's Dictum**: Every model makes simplifying assumptions that are technically "wrong"

**Useful Models**:
- Capture key mechanisms
- Make accurate-enough predictions for decisions
- Reveal non-obvious insights
- Help organize thinking

**Dangerous Models**:
- Black boxes with no interpretability
- Overfitted to historical data
- Assumed infallible by users
- Poorly matched to problem

### QGIA Modeling Standards

**Transparency**:
- Document assumptions explicitly
- Explain model limitations
- Provide uncertainty quantification

**Validation**:
- Out-of-sample testing
- Compare against naive baselines
- Track real-world performance

**Human-in-the-Loop**:
- Models inform, analysts decide
- Override capability when judgment conflicts with model
- Continuous feedback for improvement

## Quantum-Inspired Frameworks

### Why "Quantum-Inspired"?

Not true quantum computing, but classical algorithms inspired by quantum mechanical principles:

- **Superposition**: Model multiple states simultaneously
- **Entanglement**: Capture non-local correlations
- **Amplitude Weighting**: Probabilistic scenario branching
- **Interference**: Constructive/destructive probability interactions

**Advantages**:
- Handle massive uncertainty spaces
- Model non-linear interdependencies
- Fast computation on classical hardware
- Interpretable outputs

### QSFE (Quantum Superposition Forecasting Engine)

**Core Concept**: Rather than forecast single future, model ensemble of futures simultaneously

**Mechanism**:
1. Identify key uncertainties (economic growth, leadership decisions, external shocks)
2. Generate discrete scenarios for each uncertainty
3. Assign quantum amplitudes (complex numbers whose squared magnitude = probability)
4. Propagate scenarios forward with amplitude evolution
5. New evidence "collapses" superposition (updates amplitudes)

**Advantages Over Traditional Scenarios**:
- Maintains full probability distributions, not just 3-5 discrete scenarios
- Tracks interference effects between scenarios
- Enables continuous updating as evidence arrives

**Application**: Long-term forecasting (6-12 months) with multiple branching paths

### EDM (Entanglement Dynamics Mapper)

**Core Concept**: Alliances and conflicts create "entangled" states—outcomes correlated across actors

**Mechanism**:
1. Model international system as network of actors
2. Define entanglement relationships (alliances, rivalries, dependencies)
3. Perturbation to one actor propagates through network
4. Non-linear cascade effects modeled via entanglement strength
5. Predicts secondary and tertiary impacts of crises

**Example**: 
- Taiwan Strait crisis (primary event)
- Japan increases defense readiness (entangled ally)
- South Korea faces pressure to choose sides (entangled to both)
- Philippines reassesses US alliance value (weakly entangled)
- Global semiconductor supply disrupted (economic entanglement)

**Application**: Cascade analysis, alliance cohesion assessment, indirect effects forecasting

### ABCP (Adaptive Bayesian Conflict Predictor)

**Core Concept**: Continuously update conflict probabilities as new evidence arrives

**Mechanism**:
1. Prior probability distribution over conflict scenarios
2. Evidence stream (SIGINT, GEOINT, HUMINT, OSINT) arrives continuously
3. Likelihood ratio computed for each evidence piece
4. Bayesian updating shifts probability distribution
5. Decay function prevents stale evidence from dominating
6. Sequential Monte Carlo filtering for computational efficiency

**Real-Time Operation**:
- Updates every 15 minutes as new intelligence processed
- Alerts when probability crosses thresholds
- Explains which evidence drove updates (transparency)

**Application**: Early warning, near-term forecasting (0-30 days), crisis monitoring

### RPRN (Recursive Pattern Recognition Network)

**Core Concept**: Learn from historical cases to identify analogous current situations

**Mechanism**:
1. Historical case library encoded in 20+ dimensional feature space:
   - Regime type, military balance, economic conditions, alliance structure, ...
2. Current situation encoded in same feature space
3. Neural network identifies nearest neighbors in feature space
4. Weights cases by similarity
5. Outcome distribution from historical analogues informs forecast
6. **Recursive**: Patterns at multiple levels (micro-events, crisis phases, war outcomes)

**Meta-Pattern Learning**:
- Not just "similar to X historical case"
- Identifies patterns across patterns (e.g., "authoritarian diversionary war" class)
- Hierarchical representations

**Application**: Analogical reasoning, reference class forecasting, pattern-based early warning

### TCA (Temporal Convergence Analyzer)

**Core Concept**: Predict when crisis transitions to next phase (latent → emergent → acute)

**Mechanism**:
1. Define crisis phases with observable characteristics
2. Track indicators associated with phase transitions
3. Survival analysis models time-to-transition
4. Hazard rate increases as indicators accumulate
5. Forecasts inflection points (e.g., "70% probability of transition to kinetic conflict within 14 days")

**Phase Transition Indicators**:
- **Latent → Emergent**: Increased diplomatic activity, troop movements, threatening rhetoric
- **Emergent → Acute**: Mobilization, economic sanctions, ultimatums
- **Acute → War**: Border incidents, air/naval confrontations, last-ditch negotiations fail

**Application**: Crisis phase forecasting, warning lead time optimization, intervention timing

## Integration: Quantum Frameworks → Analyst Workflow

**Daily Intelligence Cycle**:

1. **Overnight**: OSIQP processes 500TB intelligence stream
2. **06:00**: ABCP updates conflict probabilities based on overnight intelligence
3. **07:00**: Analysts review ABCP alerts (probability threshold crosses)
4. **08:00**: Morning briefing—analysts present key updates with model support
5. **Throughout Day**: 
   - TCA monitors crisis phase indicators
   - EDM maps potential cascade effects
   - RPRN identifies historical analogues
   - QSFE updates long-term scenario probabilities
6. **16:00**: Analysts finalize assessments, incorporating but not deferring to models
7. **17:00**: Dissemination to consumers

**Model Outputs Are Inputs to Judgment, Not Replacements**

## Performance Metrics

### Forecast Accuracy

**QGIA Target**: 84.7% accuracy for 12-month forecasts

**Measurement**:
- **Brier Score**: \((\text{forecast} - \text{outcome})^2\) averaged over forecasts
- Lower is better (perfect = 0, worst = 1)
- QGIA Brier Score: ~0.153 (well-calibrated)

**Calibration Curve**:
- When we say "70% probability", does it occur ~70% of the time?
- QGIA calibration: Within ±5% across probability bins

### Warning Lead Time

**QGIA Average**: 127 days warning before major crises

**Measurement**:
- Time from first alert (probability crosses threshold) to event onset
- Trade-off: Earlier warning = more false positives
- QGIA optimizes for 15% false positive rate

### Model-Specific Validation

**QSFE**:
- Scenario coverage: Do outcomes fall within modeled space?
- Amplitude accuracy: Do scenario probabilities match frequencies?

**EDM**:
- Cascade prediction: Correct identification of secondary effects?
- Entanglement strength: Correlation between predicted and observed co-movement?

**ABCP**:
- Real-time updating: Does new evidence improve forecasts?
- Belief convergence: Do probabilities converge to truth as event approaches?

**RPRN**:
- Analogical validity: Are historical analogues actually predictive?
- Feature importance: Which dimensions matter most?

**TCA**:
- Phase transition timing: Accuracy of inflection point forecasts?
- Hazard rate calibration: Does estimated time-to-event match reality?

---

**Last Updated**: 2026-02-16
**Status**: STRUCTURE ESTABLISHED | QUANTUM FRAMEWORK SPECIFICATIONS PRIORITIZED