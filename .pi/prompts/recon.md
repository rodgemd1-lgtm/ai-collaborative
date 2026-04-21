# Workflow: Deep Recon

## Trigger
Researching IAC, competitors, or clients. Activated by: `Pi IAC recon`, "research competitor", "scrape careers"

## Goal
Produce timestamped, sourced intelligence on IAC or a target entity for strategy, content, or meeting preparation.

## Steps

### 1. Target Definition
- What entity? (IAC, competitor, client, market)
- What questions need answering? (e.g., "What's changed on iacollaborative.com in the last 30 days?")
- What decisions depend on this intel?

### 2. Source Selection (Research Agent)

| Priority | Source | Tool | Notes |
|----------|--------|------|-------|
| 1 | iacollaborative.com | Browser Use API | JS-rendered; check careers, insights, team |
| 2 | LinkedIn profiles | Browser Use (logged-in session) | Requires persistent profile |
| 3 | Competitor sites | Browser Use API | IDEO, Frog, McKinsey Design, Accenture Song |
| 4 | Job boards | Browser Use API | Ashby, LinkedIn Jobs, Indeed |
| 5 | News / press | Web extract | Google News, TechCrunch, design industry pubs |
| 6 | Apollo enrichment | Apollo API | Account intel, tech stack, trigger events |

### 3. Data Collection
- Scrape all relevant pages
- Extract: dates, numbers, names, quotes, URLs
- Tag each artifact with: source URL, confidence (HIGH/MED/LOW), collection date
- Store raw output to `data/recon/[TARGET]-[DATE]/`

### 4. Synthesis
- What changed? (new hires, case studies, pricing, positioning)
- What is the competitive move? (who is entering/exiting what space)
- What are the implications for IAC engagement?
- What questions remain unanswered?

### 5. Intelligence Brief
```
recon-brief-[TARGET]-[DATE].md
├── Executive Summary (3 bullets)
├── Source Inventory (with confidence levels)
├── Key Changes / Findings
├── Competitive Implications
├── IAC Engagement Impact
├── Open Questions
└── Recommended Actions
```

### 6. Update Master Context
If recon changes anything in `prompts/iac-context.md` (e.g., new hire, new pricing, new case study), flag it for update.

## Known Issues
- LinkedIn blocks unauthenticated scraping — use Browser Use with persistent login
- Competitor data decays fast; schedule refresh for key competitors every 30 days
- Browser Use sessions may show "stopped" even when output is ready — check output directly

## Never Rules
- Never claim intel without a documented source URL
- Never assign HIGH confidence to unverified information
- Never use stale data (> 30 days) for competitive comparison without a refresh flag
