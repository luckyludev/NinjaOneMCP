# OAuth Connector Setup (Scaffold)

This is the starter runbook for ChatGPT/Claude/Copilot MCP connector onboarding.

## MCP URL
- `https://ninjaonemcp.example.com/mcp`

## OAuth discovery endpoints
- `/.well-known/oauth-protected-resource`
- `/.well-known/oauth-authorization-server`

## Next implementation step
This scaffold currently provides discovery + health endpoints only.
Next, we will add:
- `/oauth/register`
- `/oauth/authorize`
- `/oauth/callback`
- `/oauth/token`
- protected `/mcp` forwarding to NinjaOne tools.
