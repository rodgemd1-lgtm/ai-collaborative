# Prism (MiroFish) — Decision Simulation Capability Card

**Platform:** Prism™ (formerly MiroFish) — RIG's proprietary swarm-intelligence engine  
**Current State:** ACTIVE — 540+ decision simulations run for IAC  
**Location:** `MiroFish/domains/iac/` in SIO

## What It Does
Prism models strategic decisions using 4–8 personas × 6–12 rounds of LLM-driven simulation. It predicts how stakeholders will react to different interventions and produces a recommended action plan.

## Key Metrics from IAC Simulations
- **540 modeled decisions** — Kyle meeting simulation
- **+0.16 Matthew stance lift** — from pre-brief intervention
- **−43% team objections** — reduced via combined intervention
- **72h standard turnaround** — for PDF + dashboard

## How to Run a Simulation
```bash
cd ~/Desktop/Startup-Intelligence-OS/MiroFish
# The simulation engine runs via Python
python run_simulation.py \
  --scenario meeting_reception \
  --variant all_interventions \
  --personas kyle,matthew,kathleen,dan,jeff,rahul \
  --rounds 6
```

## Use Cases for IAC
1. **Pre-meeting prep** — Run simulation before any high-stakes meeting
2. **Intervention testing** — A/B test "send pre-brief" vs. "don't send pre-brief"
3. **Objection inventory** — Surface likely objections before the meeting
4. **Follow-up timing** — Simulation shows optimal follow-up at T+48h

## Simulation Config Files
- `MiroFish/domains/iac/scenarios/meeting_reception.json` — Kyle meeting scenario
- `MiroFish/domains/iac/scenarios/strategic_choice.json` — Package selection scenario
- `MiroFish/domains/iac/ontology.json` — Full persona system + FBSV framework

## Integration Rules
- Every simulation needs a clear decision question (not "what if")
- Always run 3 variants minimum (control + 2 interventions)
- Save outputs to `data/simulations/` with timestamp
- Never quote simulation scores without running the engine
