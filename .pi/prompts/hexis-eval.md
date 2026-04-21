# Workflow: Hexis 6-Lens Evaluation

## Trigger
Evaluating a new strategic bet or venture. Activated by: `Pi IAC hexis`, "run Hexis", "6-lens analysis"

## Goal
Apply the Strategos 6-Lens framework to evaluate a strategic opportunity and produce a board-defensible assessment.

## Steps

### 1. State the Strategic Bet
- What is being evaluated? (e.g., "Should we build an AI practice partner?", "Should IAC enter mid-market?")
- What is the decision horizon? (e.g., 12-month pilot, 3-year platform build)
- What is the resource commitment? (budget, time, reputation)

### 2. Run the 6 Lenses (Strategy Agent)
For each lens, produce a score (1–10) and a one-paragraph analysis:

| Lens | Question | Pass Threshold |
|------|----------|----------------|
| **Desirability** | Does the market want this? Is there a 25X opportunity? | Score ≥ 7 |
| **Feasibility** | Can we build it with our team + partners? | Score ≥ 6 |
| **Viability** | Will it be profitable within the decision horizon? | Score ≥ 6 |
| **Sustainability** | Will the advantage endure? Moat? | Score ≥ 5 |
| **Resilience** | What if the core assumption is wrong? Downside plan? | Score ≥ 5 |
| **Alignment** | Does it fit IAC's brand, mission, and existing capabilities? | Score ≥ 7 |

### 3. Composite Score & Verdict
- Weighted average (custom weights by bet type)
- Default weights: Desirability 0.20, Feasibility 0.20, Viability 0.20, Sustainability 0.15, Resilience 0.10, Alignment 0.15
- Verdict thresholds:
  - **GO** — Composite ≥ 7.0, no lens below 5
  - **CONDITIONAL** — Composite 6.0–6.9, or one lens below 5 with mitigation plan
  - **NO-GO** — Composite < 6.0, or more than one lens below 5

### 4. IAC-Specific Framing
- Map each lens to IAC's known frameworks (IDEALS, Seven Elements, Collaborative Intelligence Stack)
- Reference IAC's specific risk posture: Kathleen = craft, Dan = deal math, Matthew = ownership
- Surface which leader(s) will challenge which lens

### 5. Sensitivity Analysis
- What if the IAC partnership fails to close in 30 days? (Desirability drops if IAC isn't anchor)
- What if Accenture Song launches a mid-market AI offering in Q3? (Sustainability drops)
- What if hiring delays push IAC's internal AI team to month 12? (Feasibility for Mike rises)

### 6. Output
```
hexis-eval-[BET]-[DATE].md
├── Strategic Bet Statement
├── 6-Lens Scoring Matrix
├── Composite Score + Verdict
├── IAC-Specific Framing
├── Sensitivity Analysis
├── Leader Challenge Map
└── Recommended Next Action
```

## Never Rules
- Never score a lens without a written one-paragraph justification
- Never present a verdict without sensitivity analysis
- Never skip the "Alignment" lens for IAC — it's the most frequently challenged by Kathleen
