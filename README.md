# Pi IA Collaborative — Strategic Engagement Agent

> **Partner Intelligence for AI Collaborative.** A dedicated AI agent system to help Mike Rodgers (RIG) win, deliver, and scale the IA Collaborative strategic partnership.

## Quick Start

```bash
cd ~/Desktop/ai-collaborative
./bin/pi-iac status       # Engagement pipeline
./bin/pi-iac pitch        # Full pitch-prep workflow
./bin/pi-iac prism        # Run Prism decision simulation
./bin/pi-iac jobs         # Check IAC hiring intel
./bin/pi-iac context      # Show master context
```

## Architecture

```
.pi/
├── agents/          # 7 specialist agents (strategy, content, client, web, campaigns, research)
├── capabilities/     # Tool integrations (Browser Use, Composio, Gamma, Apollo, Prism)
├── prompts/
│   └── iac-context.md  # Master context loaded every session
└── workflows.json   # 7 named workflows

iac/
├── client.py        # BD pipeline, stakeholder tracking
└── simulation.py    # Prism simulation runner
```

## Key Intelligence (2026-04-21)

- **IAC hiring 2 AI roles:** Senior GenAI Solutions Strategist + Senior Product Strategist ($140–160K)
- **Matthew's budget approved** for AI talent → pitch = "accelerate your build"
- **Decision window:** 72h post-pitch. Kyle shifts to CHAMPION at hour 48.
- **New wedge:** "For less than your annual AI hiring budget, we ship in 8 weeks."

## Verification

```bash
cd ~/Desktop/ai-collaborative
python3 iac/verify.py
```

Version 1.1.0 — 2026-04-21
