# Browser Use — Cloud API Capability Card

**Platform:** Browser Use Cloud (browser-use.com)  
**Version:** v3 API  
**Current State:** ACTIVE — API key authenticated, sessions created successfully  
**API Base:** `https://api.browser-use.com/api/v3`

## Authentication
```bash
export BROWSER_USE_API_KEY=bu_yqOqXL7AXnTBpo_Wf3fplAxOwu950C-F20HVQ19NczE
```

## What It Does
AI-powered browser automation via cloud API. Send a task in plain English, get structured results back. Supports:
- Live web scraping (JavaScript-rendered pages, auth walls)
- Multi-step workflows (login → navigate → extract)
- Session persistence (cookies, localStorage across tasks)
- Stealth mode (residential proxies in 195+ countries)
- Live preview URL (watch the browser in real time)

## Key Endpoints

### Create Session (run a task)
```bash
curl -X POST https://api.browser-use.com/api/v3/sessions \
  -H "Content-Type: application/json" \
  -H "X-Browser-Use-API-Key: $BROWSER_USE_API_KEY" \
  -d '{
    "task": "Navigate to URL and extract X",
    "model": "claude-sonnet-4.6",
    "max_steps": 25
  }'
```

### Check Session Status
```bash
curl -X GET https://api.browser-use.com/api/v3/sessions/{session_id} \
  -H "X-Browser-Use-API-Key: $BROWSER_USE_API_KEY"
```

### Models Available
- `claude-sonnet-4.6` (recommended, $3.60/M in, $18/M out)
- `claude-opus-4.6` ($6/M in, $30/M out)
- `gpt-5.4-mini` ($0.90/M in, $5.40/M out)

## Use Cases for IAC
1. **Competitor recon** — Scrape competitor careers pages, pricing, recent work
2. **LinkedIn scraping** — Extract profiles with logged-in session (LinkedIn blocks `web_extract`)
3. **IAC website monitoring** — Check iacollaborative.com for updates (case studies, insights, team changes)
4. **Client research** — Navigate client websites to extract org structure, recent news, key hires
5. **Live demo monitoring** — Watch `iac-mid-market-v5.vercel.app` for 404s, broken links, performance

## Known Issues
- **Session status polling:** Sessions show `"stopped"` even when output is ready. May need to check output directly rather than waiting for `"completed"`.
- **Output extraction:** Raw agent output is in the response JSON. Parse it yourself.
- **Quota:** Default max cost $20 per session. Monitor via `totalCostUsd` field.

## Integration Rules
- Always use v3 API (not v2)
- Always include `model` parameter — default is `bu-max`
- Include `max_steps` to control cost and runtime
- For LinkedIn: use session with persistent profile (login once, reuse)
- For auth-required sites: use `profile_id` for persistent browser state

## Python SDK (Alternative)
```python
from browser_use_sdk.v3 import AsyncBrowserUse
client = AsyncBrowserUse()
result = await client.run("Navigate to URL and extract...", model="claude-sonnet-4.6")
print(result.output)
```
