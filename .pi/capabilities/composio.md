# Composio — Integration Platform Capability Card

**Platform:** Composio (composio.dev)  
**Version:** v2 API  
**Current State:** API key present but connection UNTESTED  
**Dashboard:** https://dashboard.composio.dev/rodgemd1_workspace/

## Authentication
```bash
export COMPOSIO_API_KEY=ck_hqV6czgCTX4ouRh897me
```

## What It Does
Composio is an integration platform with 100+ app connectors (Gmail, Calendar, Notion, GitHub, Slack, etc.) accessible via MCP servers. Enables AI agents to take actions across SaaS tools.

## Key Features
- **MCP Server:** Available for Claude, Cursor, Windsurf, and any MCP client
- **Auth Connectors:** OAuth for Google, Notion, Slack, etc.
- **Action Library:** Pre-built actions for common workflows
- **Workflow Builder:** Chain actions across multiple tools

## Use Cases for IAC
1. **Email integration** — Auto-send follow-ups from Gmail after meetings
2. **Calendar integration** — Schedule meetings with IAC leadership
3. **Notion integration** — Push meeting notes, competitive intel to shared workspace
4. **Slack integration** — Alert channels when Prism simulation completes
5. **CRM integration** — Push Apollo leads to HubSpot/Salesforce

## Known Issues
- **Connection untested:** API key is in environment but we haven't verified which actions are enabled.
- **OAuth flows may require human-in-loop** for initial auth setup.
- **Rate limits unknown** — need to test before large-scale use.

## Test Your Connection
```bash
curl -X GET "https://backend.composio.dev/api/v2/actions" \
  -H "x-api-key: $COMPOSIO_API_KEY" \
  -H "Content-Type: application/json"
```

## MCP Server Setup
```bash
# Add to Claude/Cursor MCP config
{
  "mcpServers": {
    "composio": {
      "command": "npx",
      "args": ["-y", "composio@latest"],
      "env": {"COMPOSIO_API_KEY": "ck_hqV6czgCTX4ouRh897me"}
    }
  }
}
```

## Integration Rules
- Test connection before building workflows
- Verify OAuth tokens are valid for target apps
- Use MCP server for coding agents (Claude Code, Cursor), direct API for scripts
- Log all Composio actions for audit trail
