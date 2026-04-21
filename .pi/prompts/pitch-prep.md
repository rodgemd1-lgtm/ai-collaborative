# Workflow: Pitch Preparation

## Trigger
Before any IAC meeting or client presentation. Activated by: `Pi IAC pitch`, "meeting tomorrow", "prepare for Kyle"

## Goal
Produce a meeting-ready brief that maximizes the probability of a positive Kyle Smith response within the 72-hour decision window.

## Steps

### 1. Decision Chain Map (Client Agent)
- Identify who attends the meeting
- Map formal authority: Kyle < $100K; Co-CEOs for > $100K
- If Matthew attends → TRIGGER Matthew pre-brief workflow immediately
- If Kathleen attends → verify materials pass IA-grade craft gate
- If Dan attends → ensure P&L and unit economics memo are attached

### 2. Recon Refresh (Research Agent)
- Scrape iacollaborative.com for new case studies, insights, team changes (Browser Use API)
- Check LinkedIn for target attendees: recent posts, job changes, speaking engagements
- Refresh competitive landscape if > 30 days old
- Document all intel with source URL + confidence level + date

### 3. Prism Simulation (Research Agent)
- Run `meeting_reception` scenario with selected intervention variant
- Default: `all_interventions` variant (Matthew pre-brief + Co-CEO dinner + Package A only + live v5 demo)
- If simulation unavailable, flag and use heuristic scores from ontology
- Record: projected champion rates, objection inventory, blocking leader

### 4. Material Assembly (Content Agent)
- Pitch deck: max 12 slides (Kyle attention span)
- Deck must include: The Flip (60s reframe), live demo URL, MiroFish numbers, packages (lead with A), clear ask
- Speaker notes: persona-aware (Kyle = evidence-first, Kathleen = craft-first, Dan = numbers-first)
- Leave-behind memo: proof URL + 90-day success criteria + 3 risks + mitigations
- All stats cited with source; all frameworks (Hexis, IDEALS, Seven Elements) anchored to IAC IP

### 5. Pre-Meeting Checklist
- [ ] Decision chain mapped and attendees confirmed
- [ ] Recon data refreshed within 7 days
- [ ] Prism simulation run (or flagged unavailable)
- [ ] Deck: ≤ 12 slides, IA-grade craft, live demo included
- [ ] Speaker notes: persona-aware for every attendee
- [ ] Leave-behind: crisp memo with success criteria
- [ ] Matthew pre-brief sent (if Matthew attending)
- [ ] Follow-up email drafted before the meeting ends

### 6. Output Bundle
```
pitch-brief-[DATE]/
├── decision-chain.md
├── recon-summary.md
├── prism-sim-output.md
├── deck/ (Gamma ID + PDF export)
├── speaker-notes.md
├── leave-behind-memo.md
└── follow-up-draft.md
```

## Never Rules
- Never send a deck without running it through the Kathleen gate (visual + narrative quality)
- Never pitch without a clear ask (Package A as default)
- Never attend a Matthew-attended meeting without a pre-brief
- Never present Package B or C as the lead — always anchor with A
