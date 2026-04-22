# Campaign Health Check Workflow

**When:** Checking Instantly/Apollo campaign performance.
**Trigger:** `pi-iac campaigns`

## Instantly — 3 Failures Since April 10
**Do NOT launch new campaigns until root cause is diagnosed.**

Diagnostic:
1. Check SPF/DKIM/DMARC on sending domain
2. Check template spam scores
3. Audit lead list quality
4. Warm up cold sending domains

**IAC outreach:** Use warm intro channels (Kellogg, Innovation Roundtable, D&AD) — not cold email.

## Apollo Target Accounts
1. Glossier  6. TransUnion
2. YETI  7. Zendesk
3. Warby Parker  8. Morningstar
4. Robinhood  9. Envestnet
5. Coinbase  10. Monday.com

Target: Title CEO/COO/CINO/VP Product | Size 50–5000 employees | Mid-market $50M–$500M

## Enrichment Workflow
1. Pull list via Apollo API
2. Enrich ≥ 80% complete
3. Score by IAC-relevance (0–100)
4. Export to `data/leads/`
5. Push to Instantly (when healthy)
