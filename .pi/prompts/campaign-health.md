# Workflow: Campaign Health Check

## Trigger
Checking Instantly/Apollo campaign performance. Activated by: `Pi IAC campaigns`, "check email", "campaign status"

## Goal
Diagnose deliverability, engagement, and list health; produce a prioritized fix list.

## Steps

### 1. Deliverability Audit (Campaigns Agent)
Check for every sending domain:
- SPF record present and valid
- DKIM record present and valid
- DMARC policy present (p=quarantine or p=reject)
- Domain reputation (Google Postmaster, Microsoft SNDS)
- Blacklist check (Spamhaus, Barracuda, etc.)

### 2. Campaign Performance Pull (Campaigns Agent)
From Instantly:
- Total sent, delivered, bounced, opened, clicked, replied, unsubscribed
- Bounce rate (target < 2%)
- Open rate (target > 25%)
- Reply rate (target > 3%)
- Unsubscribe rate (target < 0.5%)
- Failure log (any failure events in last 7 days)

From Apollo:
- List enrichment completeness (target ≥ 80%)
- Lead-to-sequence match rate
- Rate limit hits in last 7 days

### 3. Email Quality Audit (Content + Campaigns Agent)
For each active template:
- Spam score check (Mail-Tester or similar)
- Template A/B test status (minimum 2 variants)
- Unsubscribe link present and functional
- Subject line length (≤ 60 chars)
- Body length (≤ 150 words for cold email)
- Personalization tokens present and populated
- "Consultative" tone (not "Buy our AI")

### 4. List Health Audit (Campaigns Agent)
- Mid-market only: $50M–$500M company size (verified via Apollo)
- Role match: C-suite, VP, Head of, Director-level for strategy/innovation
- Industry alignment: Technology, Healthcare, Financial Services, CPG, Industrial
- No competitors on the list (IDEO, Frog, etc.)
- Recency: leads enriched within 30 days

### 5. Issue Triage

| Severity | Issue | Action | ETA |
|----------|-------|--------|-----|
| P0 | SPF/DKIM/DMARC fail | Fix DNS records immediately | < 24h |
| P0 | > 5% bounce rate | Pause campaign, clean list | < 4h |
| P1 | Open rate < 20% | Refresh subject lines, test 3 variants | < 48h |
| P1 | Reply rate < 2% | Rewrite body copy, add personalization | < 48h |
| P2 | A/B test not running | Launch second variant | < 72h |
| P2 | Enrichment < 80% | Re-enrich via Apollo, batch 100 | < 72h |
| P3 | List quality drift | Re-segment, re-score leads | < 1 week |

### 6. Output
```
campaign-health-[DATE].md
├── Deliverability Summary
├── Performance Metrics
├── Email Quality Audit
├── List Health Audit
├── Issue Triage Table
├── Fix Actions + Owners
└── 7-Day Follow-Up Plan
```

## Known Issues
- **3 Instantly failures since April 10.** Root cause unknown — may be SPF, template, or list quality. This is a P0 investigation.
- **Apollo rate limits** — batch in groups of 100
- **Cold email fatigue** — IAC is a design firm, not SaaS. Outbound must feel consultative.

## Never Rules
- Never launch a sequence without SPF/DKIM/DMARC pass
- Never send without A/B variants
- Never use a list with > 2% bounce rate
- Never mix enterprise leads into the IAC mid-market campaign
