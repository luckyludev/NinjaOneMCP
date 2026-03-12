# Copilot Studio Connector Setup (NinjaOneMCP)

## Important compatibility notes
- Copilot supports **Streamable HTTP** transport for MCP.
- SSE transport is not supported in current Copilot guidance.

## MCP URL
- `https://ninjaonemcp.example.com/mcp`

## Prerequisites
- Generative orchestration enabled in Copilot Studio.
- OAuth callback URI from Copilot added to Azure App Registration.

## Quick checklist
1. Add MCP endpoint `/mcp`
2. Configure OAuth
3. Complete login
4. Validate tools are discoverable
