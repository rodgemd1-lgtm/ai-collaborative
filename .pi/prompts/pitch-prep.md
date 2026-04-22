# Pitch Preparation Workflow

**When:** Before any IAC meeting or client presentation.
**Trigger:** `pi-iac pitch` or "meeting tomorrow" or "prepare for Kyle"

## Phase 1 — Context Load (5 min)
- [ ] Load `.pi/prompts/iac-context.md`
- [ ] Check `data/clients/` for last meeting notes
- [ ] Confirm who is attending
- [ ] Identify decision weight

## Phase 2 — Prism Simulation (10 min)
- [ ] Run: `python3 -m iac.simulation --scenario meeting_reception --variant all_interventions`
- [ ] Read stance at hour 0, 24, 48, 72
- [ ] Identify #1 objection to pre-empt
- [ ] Confirm: has Matthew been pre-briefed?

## Phase 3 — Materials Check (5 min)
- [ ] Gamma deck reviewed? (`.vault/last-gamma-deck.txt`)
- [ ] Demo site live? (https://iac-mid-market-v5.vercel.app)
- [ ] Printed PDF backup ready
- [ ] Calculator ready for Dan's deal math test

## Phase 4 — Persona-Specific Prep
| Audience | Lead With | Key Ask |
|----------|-----------|---------|
| Kyle | Evidence + live artifact | "Here's what IAC could become" |
| Matthew | Technical depth (74 agents) | "I work WITH your team" |
| Dan | Unit economics + outcomes | 90-day metrics, go/no-go gate |
| Kathleen | Craft + Seven Elements | Category creation language |

## Phase 5 — Follow-Up Draft (BEFORE meeting ends)
Draft T+48h follow-up email now. Kyle shifts to CHAMPION at exactly hour 48.

## Phase 6 — Go/No-Go
- Matthew pre-briefed?
- Package scoped correctly?
- Metrics are 90-day achievable?
- Follow-up drafted?

If ANY is NO → delay the pitch.
