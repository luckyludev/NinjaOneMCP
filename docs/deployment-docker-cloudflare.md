# Deployment: Docker + Cloudflare Tunnel

## Files
- `deploy/http-gateway/docker-compose.yml`
- `deploy/http-gateway/.env.example`

## Steps
1. Copy env template:
   ```bash
   cp deploy/http-gateway/.env.example deploy/http-gateway/.env
   ```
2. Fill secrets and URLs.
3. Start stack:
   ```bash
   cd deploy/http-gateway
   docker compose up -d --build
   ```
4. Verify health:
   ```bash
   curl http://127.0.0.1:8010/health
   ```
5. Verify public discovery endpoints:
   ```bash
   curl https://ninjaonemcp.example.com/.well-known/oauth-protected-resource
   curl https://ninjaonemcp.example.com/.well-known/oauth-authorization-server
   ```

## Cloudflare tunnel routing
Public hostname service should target gateway container/port for your deployment model.
