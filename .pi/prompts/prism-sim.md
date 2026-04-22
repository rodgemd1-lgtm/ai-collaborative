# Prism Simulation Workflow

**When:** Before high-stakes decisions.
**Trigger:** `pi-iac prism`

## Run
```bash
cd ~/Desktop/ai-collaborative
python3 -m iac.simulation --scenario [scenario] --variant [variant]
```

## Scenarios
- `meeting_reception` — Before any IAC meeting
- `strategic_choice` — Package A vs B vs C

## Variants
- `control` — No interventions
- `pre_brief` — Pre-brief Matthew only
- `co_ceo_dinner` — Co-CEO dinner without pre-brief
- `all_interventions` — Both combined

## Stance Scale
| Score | Meaning |
|-------|---------|
| 0.0–0.25 | OPPOSE / KILL |
| 0.25–0.50 | SKEPTICAL / PUNT |
| 0.50–0.75 | NEUTRAL / ENGAGED |
| 0.75–1.00 | CHAMPION / SIGN |

## Key Thresholds
- Matthew stance at hour 0 < 0.50 → pre-brief is MANDATORY
- Kyle no shift at hour 48 → follow-up needs more urgency
- All personas > 0.85 at hour 72 → GO signal

## Output Processing
1. Save to `data/simulations/`
2. Extract top 3 objections
3. Draft pre-emptive responses
4. Update persona tracker in `iac/client.py`
