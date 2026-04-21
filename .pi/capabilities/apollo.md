# Apollo — Lead Enrichment Capability Card

**Platform:** Apollo.io  
**Current State:** ACTIVE — used for lead enrichment and account intelligence  
**Purpose:** Enrich leads with title, company size, tech stack, recent news before outreach

## What It Does
Apollo provides B2B contact data and account intelligence. Used to:
- Enrich lead lists with verified contact info
- Find decision-makers at target accounts
- Identify tech stack signals ("uses Salesforce") for personalization
- Track job changes and company news as trigger events

## IAC Target Persona (Apollo query)
```
Title: "CEO", "COO", "Chief Innovation Officer", "Head of Strategy", "VP Product"
Company size: 50–5000 employees (mid-market focus: 200–2000)
Industry: Technology, Healthcare, Financial Services, CPG, Industrial
Location: US, UK, Canada, Singapore, India
Tech stack (if known): Salesforce, HubSpot, Slack, AWS
Recent trigger: Funding round (Series A–D), new C-suite hire, IPO preparation
```

## Use Cases for IAC
1. **Lead enrichment** — Before any Instantly sequence, enrich to 80%+ data completeness
2. **Account mapping** — Map IAC's 10 anchor targets (Glossier, YETI, Warby Parker, etc.)
3. **Trigger monitoring** — Alert when funded companies hire a Head of AI or CINO
4. **Competitor intelligence** — Track hiring patterns at IDEO, Frog, McKinsey Design

## Integration Rules
- Batch pulls in groups of 100 to avoid rate limits
- Export enriched lists to `data/leads/` directory
- Tag leads with IAC-relevance score (0–100)
- Cross-reference with Instantly campaign segments
