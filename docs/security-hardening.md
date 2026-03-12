# Security Hardening Checklist

## Baseline
- Use dedicated service credentials for NinjaOne.
- Store secrets in Key Vault / secret manager (not repo/chat).
- Rotate all secrets on schedule.

## Edge protection
- Add WAF rules for OAuth endpoints.
- Add rate limits:
  - `/oauth/token`
  - `/oauth/register`
  - `/oauth/authorize`
  - `/mcp`

## App-level
- Disable public docs in production (`/docs`, `/openapi.json`, `/redoc`).
- Restrict CORS to required origins.
- Keep structured logs with request IDs.

## Operations
- Maintain incident runbook.
- Validate connector flows after every release.
- Run regular secret rotation + smoke tests.
