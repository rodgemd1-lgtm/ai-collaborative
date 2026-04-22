# Website Audit & Iteration Workflow

**When:** Reviewing or updating the IAC demo site.
**Trigger:** `pi-iac website`

## Audit Checklist
- [ ] Lighthouse score 90+ mobile
- [ ] FCP < 2s
- [ ] No 404 links
- [ ] Mobile responsive
- [ ] All product pages live
- [ ] Framework pages live
- [ ] Contact form routes correctly
- [ ] IDEALS widget functional
- [ ] Clear CTAs on every page
- [ ] Package pricing clearly stated
- [ ] Analytics events firing
- [ ] SEO meta tags complete

## Iteration Protocol
1. **Audit** → top 3 issues
2. **Spec** → write in `spec.md`
3. **Build** → staging
4. **Review** → Mike approves
5. **Deploy** → Vercel production

**This is staging.** `iac-mid-market-v5.vercel.app` ≠ `iacollaborative.com`. Production handoff = separate SOW.
