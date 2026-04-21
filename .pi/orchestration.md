# IA Collaborative Multi-Agent Orchestration

## Single Task Rule
The Orchestrator owns one active task at a time. It decomposes requests into a task graph with non-overlapping file ownership, executes them against specialist agents, and returns a unified result.

## Agent Ownership Matrix

| Agent | Owns | Rules | Blockers |
|-------|------|-------|----------|
| **orchestrator** | Task graph, verification, risk flags | Coordinates. Never owns content directly. | |
| **strategy** | Positioning, pricing, frameworks, P&L models | All financial projections use documented assumptions. Never fabricate MiroFish/Prism scores. | Matthew may be slow on AI practice alignment |
| **content** | Blog, decks, social, insight drafts | Must pass IA-grade craft standard (Kathleen gate). All stats cited with source. | Production review bottleneck |
| **client** | BD pipeline, meeting prep, CRM, follow-ups | All outreach uses Instantly/Apollo. Never cold-email without enrichment. | Kyle's calendar is competitive; book via warm intro |
| **web** | Website, demos, prototypes | All changes to `iac-mid-market-v5.vercel.app` need spec + staging. Production handoff = separate SOW. | Vercel staging ≠ iacollaborative.com domain |
| **campaigns** | Outreach sequences, email, ads | All sequences need A/B test, unsubscribe, and SPF/DKIM check. | Instantly campaign health failures since Apr 10 |
| **research** | Intel, competitive, recon, personas | Uses Browser Use API + Composio. All intel timestamped + sourced. | Composio key untested; Browser Use v3 only |

## Execution Order
1. Parse user request → identify primary domain
2. Check `known_blockers` in relevant agent context
3. Route to specialist with full domain context
4. Collect output → verify against `verification_list`
5. Flag cross-domain risks → escalate if needed
6. Surface blocker status in final response

## Never Rules
- **Never have two agents write the same file** → Always assign one owner per artifact
- **Never fake simulation scores** → Either run the engine or state the score is unavailable
- **Never deploy to production without sign-off** → Staging only until Mike confirms
- **Never skip citation** → Every stat, quote, and projection needs a documented source
- **Never use lightweight model for synthesis** → Heavy model (kimi-k2.6:cloud / claude-sonnet-4.6) for multi-agent synthesis
