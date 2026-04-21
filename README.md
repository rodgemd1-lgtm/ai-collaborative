# Pi — IA Collaborative Agent

> Pi = Partner Intelligence. A strategic engagement agent for AI Collaborative (IAC), the design + innovation consultancy.

## Quick Start

```bash
# 1. Clone and enter the repo
cd ~/Desktop/ai-collaborative

# 2. Verify the agent is healthy
python3 -m iac.verify

# 3. Activate the Pi agent
./bin/pi-iac

# 4. Run a workflow
Pi IAC status
Pi IAC pitch
Pi IAC prism
```

## What This Is

Pi is a multi-agent system that helps Mike Rodgers (RIG) win, deliver, and scale the IA Collaborative strategic partnership. It specializes in:

- Pre-meeting pitch preparation with Prism simulation
- Competitive recon and market intelligence
- Content creation (blogs, decks, social)
- Website audit and iteration
- Campaign health monitoring (Instantly / Apollo)
- Strategic evaluation with Hexis 6-Lens

## Architecture

```
ai-collaborative/
├── .pi/
│   ├── README.md              — Identity, guardrails, commands
│   ├── settings.json          — Agent configuration
│   ├── workflows.json           — 7 workflow definitions
│   ├── orchestration.md       — Task router, agent matrix
│   ├── prompts/
│   │   ├── iac-context.md     — Master context (ontology + intel)
│   │   ├── pitch-prep.md      — Pre-meeting workflow
│   │   ├── prism-sim.md       — Decision simulation
│   │   ├── hexis-eval.md      — 6-Lens evaluation
│   │   ├── recon.md           — Competitive recon
│   │   ├── website-audit.md   — Site review + improvements
│   │   ├── content-create.md  — Content generation
│   │   └── campaign-health.md — Outreach health check
│   ├── agents/
│   │   ├── README.md          — Agent roster + activation map
│   │   ├── strategy.md        — Positioning, pricing, frameworks
│   │   ├── content.md         — Blog, decks, social
│   │   ├── client.md          — BD pipeline, meeting prep
│   │   ├── web.md             — Website, demos, prototypes
│   │   ├── campaigns.md       — Outreach, Instantly, Apollo
│   │   └── research.md        — Intel, recon, personas
│   └── capabilities/
│       ├── browser-use.md     — Cloud scraping API
│       ├── composio.md        — SaaS integration platform
│       ├── gamma.md           — AI presentation builder
│       ├── apollo.md          — Lead enrichment
│       └── prism.md           — MiroFish simulation engine
├── iac/
│   ├── __init__.py            — Package init
│   ├── verify.py              — Health check script
│   ├── client.py              — IAC client library
│   └── simulation.py          — Prism simulation runner
├── bin/
│   └── pi-iac                 — CLI entry point
├── data/                      — Encrypted vault (PII, leads, etc.)
└── scripts/                   — Utility scripts
```

## Commands

| Command | Description |
|---------|-------------|
| `Pi IAC status` | Engagement state: meetings, deals, blockers |
| `Pi IAC pitch` | Full pitch-prep workflow |
| `Pi IAC prism` | Run Prism simulation on a strategic decision |
| `Pi IAC recon` | Trigger deep browser recon |
| `Pi IAC content` | Generate blog, insight, or social post |
| `Pi IAC website` | Website audit + suggestions |
| `Pi IAC campaigns` | Check Instantly/Apollo campaign health |
| `Pi IAC hexis` | Run Hexis 6-Lens on a strategic bet |

## Guardrails

1. **Never act without data.** Every claim must reference a scraped artifact, simulation output, or documented source.
2. **Never fake MiroFish or Prism scores.** Always run the simulation engine or flag the missing run.
3. **Never build without a spec.** All website changes go through spec-driven-development → review → deploy.
4. **Never skip human review on live assets.** Website, pitch deck, and client-facing deliverables require Mike sign-off before publish.
5. **Never share client data outside approved channels.** PII, lead lists, and simulation persona data stay in the encrypted data directory.
6. **Package first, pitch second.** All pricing, scope, and timeline are in the Package Menu in `prompts/iac-context.md`.

## Dependencies

- Python 3.10+
- `requests` (for API calls)
- `python-dotenv` (for env management)
- Browser Use API key (in `.env`)
- Composio API key (in `.env`)
- Gamma API key (in `.env`)

## Version

1.0.0 — 2026-04-21
