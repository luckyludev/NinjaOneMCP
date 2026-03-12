# OAuth Connector Setup (Scaffold)

This is the starter runbook for ChatGPT/Claude/Copilot MCP connector onboarding.

## MCP URL
- `https://ninjaonemcp.example.com/mcp`

## OAuth discovery endpoints
- `/.well-known/oauth-protected-resource`
- `/.well-known/oauth-authorization-server`

## Current implementation status
Implemented now:
- `/oauth/register`
- `/oauth/authorize`
- `/oauth/callback`
- `/oauth/token`
- protected `/mcp` endpoint (auth enforced)

Note: `/mcp` is currently a protected placeholder returning a structured MCP error until NinjaOne tool transport wiring is completed in the next step.
