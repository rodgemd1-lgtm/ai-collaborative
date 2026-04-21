# Workflow: Prism Simulation

## Trigger
Before high-stakes decisions or internal deliberation prep. Activated by: `Pi IAC prism`, "run simulation", "what will Kyle say"

## Goal
Model how IAC leadership will react to a strategic decision and produce an intervention-ranked action plan.

## Steps

### 1. Decision Question Formulation
- State the exact decision this simulation informs
- Example: "Should Kyle propose Package A to the partner group?"
- Example: "What happens if Matthew wasn't pre-briefed?"
- A simulation without a clear decision question is entertainment, not evidence

### 2. Scenario Selection (Research Agent)
Choose from the MiroFish domain:

| Scenario | Use When |
|----------|----------|
| `meeting_reception` | Before any Kyle meeting — 72h deliberation model |
| `strategic_choice` | After a pilot commitment — 12-week trajectory model |

If no scenario matches perfectly, use `meeting_reception` as the base and customize personas.

### 3. Variant Selection
Choose at least 3 variants to compare:

| Variant | When to Use |
|---------|-------------|
| `control` | Baseline — no special moves |
| `matthew_pre_brief` | Matthew will be in the room (highest leverage) |
| `co_ceo_dinner` | You can arrange dinner with Kathleen + Dan |
| `package_a_only` | Decision paralysis risk; simplify the ask |
| `strategos_frame` | You want to position as strategic peer |
| `live_v5_demo` | You have a live demo ready |
| `all_interventions` | Maximum conversion play (resource-intensive) |

### 4. Run the Engine
```bash
cd ~/Desktop/Startup-Intelligence-OS/MiroFish
python run_simulation.py \
  --scenario meeting_reception \
  --variant all_interventions \
  --personas kyle,matthew,kathleen,dan,jeff,rahul \
  --rounds 6
```

### 5. Synthesize Output
For each variant, produce:
- **Champion rates** by leader (Kyle, Matthew, Kathleen, Dan, Jeff, Rahul)
- **Close probability** at 30 days
- **Expected deal size**
- **Objection inventory** (ranked by frequency and severity)
- **Blocking leader** prediction
- **Recommended intervention** (highest ROI move)

### 6. Store & Action
- Save output to `data/simulations/prism-[YYYYMMDD]-[scenario]-[variant].md`
- Surface the recommended intervention in the next agent action
- If simulation fails, DO NOT quote fabricated scores — flag the failure and use heuristic scores from ontology

## Never Rules
- Never run a simulation without a clear decision question
- Never quote simulation scores without running the engine (or flagging heuristics)
- Never use a lightweight model for synthesis — use `kimi-k2.6:cloud` or `claude-sonnet-4.6`
- Never run only one variant; always compare control → intervention
