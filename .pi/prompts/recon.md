# Deep Recon Workflow

**When:** Researching IAC, competitors, or clients.
**Trigger:** `pi-iac recon`

## IAC Targets
- iacollaborative.com (homepage, about, services, insights, results)
- iacollaborative.com/careers (open roles)
- LinkedIn (IA Collaborative page, follower count)
- Crunchbase (funding, headcount, growth signals)

## Competitor Targets
- IDEO, Frog Design, McKinsey Design, Accenture Song, BCGDV

## Browser Use API
```python
import urllib.request, json
api_key = "bu_yqOqXL7AXnTBpo_Wf3fplAxOwu950C-F20HVQ19NczE"
req = urllib.request.Request(
    "https://api.browser-use.com/api/v3/sessions",
    data=json.dumps({"task": "...", "model": "claude-sonnet-4.6", "max_steps": 25}).encode(),
    headers={"Content-Type": "application/json", "X-Browser-Use-API-Key": api_key}
)
resp = urllib.request.urlopen(req, timeout=120)
session_id = json.loads(resp.read())["id"]
```

## Output Standards
Every intel artifact needs:
- Source URL + date collected
- Confidence level (HIGH / MED / LOW)
- Source type (web_scrape / reasoning / Apollo / simulation)
