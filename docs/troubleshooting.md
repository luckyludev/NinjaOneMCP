# Troubleshooting

## OAuth errors
- Invalid resource: ensure `MCP_RESOURCE_URL` matches connector URL base.
- Callback failure: missing redirect URI in Azure app registration.
- Token exchange failure: verify tenant/client/secret.

## Connector shows no tools
- Ensure MCP URL is `/mcp`.
- Confirm OAuth completed.
- Check gateway logs for `/mcp` calls and response codes.

## 401/403/405 issues
- 401 on `/mcp`: missing/invalid bearer token.
- 405: wrong method/path combination from connector.
- 403/421: host/origin/security middleware mismatch (proxy setup issue).

## Discovery checks
```bash
curl -I https://ninjaonemcp.example.com/.well-known/oauth-protected-resource
curl -I https://ninjaonemcp.example.com/.well-known/oauth-authorization-server
```
