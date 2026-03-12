# Claude Connector Setup (NinjaOneMCP)

## MCP URL
- `https://ninjaonemcp.example.com/mcp`

## OAuth
- Use OAuth login flow in Claude MCP connector setup.
- Ensure Claude callback URI shown by Claude is added to Azure App Registration.

## Required Azure redirect URIs
At minimum:
- `https://ninjaonemcp.example.com/oauth/callback`
- Claude-provided callback URI (copy from Claude setup screen exactly)

## Notes
- Claude may include trailing slash in `resource`; server should normalize.
- If auth succeeds but tools missing, verify `/mcp` transport and server logs for tool list calls.
