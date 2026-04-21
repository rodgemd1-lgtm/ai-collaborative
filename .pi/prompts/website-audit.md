# Workflow: Website Audit & Iteration

## Trigger
Reviewing or updating the IAC demo site. Activated by: `Pi IAC website`, "audit site", "fix vercel"

## Goal
Evaluate the health of `iac-mid-market-v5.vercel.app`, surface issues, and propose prioritized improvements.

## Steps

### 1. Health Scan (Web Agent)
Run automated checks:
- Lighthouse score (performance, accessibility, best practices, SEO)
- Page load time (mobile + desktop, sub-3s FCP target)
- Broken links (404 check)
- IDEALS widget loads on product pages
- Contact form routes to monitored inbox
- Analytics events fire correctly
- Semantic personalization logic works for each segment

### 2. Visual Review (Content + Web Agent)
- Screenshot each major page (homepage, product, about, insights, contact)
- Check against IA-grade craft standard:
  - Dark navy + white palette
  - Bold stat callouts
  - No paragraph blocks — bullets + headlines only
  - Strong white space
  - Mobile responsiveness
- Compare to IAC's current site (`iacollaborative.com`) for brand consistency

### 3. Content Audit (Content Agent)
- Is the copy current? (no old pricing, outdated team listings)
- Are stats cited with sources?
- Is the "Insight to Action" language present?
- Does the IDEALS / Seven Elements framework appear correctly?
- Is the "flip" (60-second reframe) present on the homepage?

### 4. Performance Deep Dive (Web Agent)
- Bundle size analysis (Next.js build output)
- Image optimization (WebP, lazy loading)
- Third-party script audit (analytics, fonts, widgets)
- Core Web Vitals: LCP < 2.5s, CLS < 0.1, FID < 100ms
- Sub-3s first contentful paint on 4G

### 5. Issue Prioritization
Rank findings by impact × effort:

| Priority | Issues | Owner |
|----------|--------|-------|
| P0 | Broken links, 404s, form failures | Web |
| P1 | Performance below 3s, Core Web Vitals fail | Web |
| P2 | Craft quality below IA-grade | Content + Web |
| P3 | Content stale, stats uncited | Content |
| P4 | A/B test candidates (CTA, copy) | Strategy + Web |

### 6. Output
```
website-audit-[DATE].md
├── Health Score Summary
├── Lighthouse Scores (per page)
├── Broken Links List
├── Performance Bottlenecks
├── Content Issues
├── Visual / Craft Issues
├── Prioritized Fix List (P0–P4)
├── A/B Test Recommendations
└── Staging vs Production Notes
```

### 7. Staging vs Production Clarification
- Every audit output must include: "This site is a deployable prototype on `iac-mid-market-v5.vercel.app`. Production handoff to `iacollaborative.com` is a separate SOW item."
- Do not imply the site is "done" until it's on IAC's domain

## Never Rules
- Never fix the site without a spec (spec-driven-development → review → deploy)
- Never deploy to production without Mike sign-off
- Never skip Lighthouse check
- Never audit without the staging ≠ production disclaimer
