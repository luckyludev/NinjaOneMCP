# ChatGPT Connector Setup (NinjaOneMCP)

## MCP URL
Use streamable MCP endpoint:
- `https://ninjaonemcp.example.com/mcp`

> Do not use `/sse` for ChatGPT connector setup.

## OAuth settings
- Auth Type: OAuth
- Dynamic registration: enabled (leave client ID/secret blank if using DCR)

## Required Azure redirect URIs
Add these to Azure App Registration (Web):
- `https://ninjaonemcp.example.com/oauth/callback`
- `https://chatgpt.com/connector_platform_oauth_redirect`
- `https://platform.openai.com/apps-manage/oauth`

## Quick test
After connecting, ask:
- "List available tools"
- "Show first 5 NinjaOne devices"

## Common failures
- "No actions available": MCP URL not `/mcp`.
- OAuth loop: missing ChatGPT redirect URI in Azure.
- Invalid resource: mismatch between `MCP_RESOURCE_URL` and connector base URL.
