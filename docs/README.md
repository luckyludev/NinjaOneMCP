# NinjaOneMCP Docs Index

This folder contains deployment, OAuth, connector, troubleshooting, and security guides for the NinjaOneMCP stack.

## Reading Order

1. [deployment-docker-cloudflare.md](./deployment-docker-cloudflare.md)
2. [oauth-app-registration-azure.md](./oauth-app-registration-azure.md)
3. Connector-specific guides:
   - [chatgpt-connector.md](./chatgpt-connector.md)
   - [claude-connector.md](./claude-connector.md)
   - [copilot-connector.md](./copilot-connector.md)
4. [security-hardening.md](./security-hardening.md)
5. [troubleshooting.md](./troubleshooting.md)

---

## Connection Architecture (OAuth + MCP)

```mermaid
flowchart LR
    U1[ChatGPT] -->|OAuth + MCP /mcp| CF[Cloudflare Tunnel / Edge]
    U2[Claude] -->|OAuth + MCP /mcp| CF
    U3[Copilot Studio] -->|OAuth + MCP /mcp| CF

    CF --> GW[NinjaOneMCP HTTP Gateway\n(FastAPI + OAuth Endpoints)]

    GW -->|Authorize / Token Exchange| AZ[Azure App Registration\n(Entra ID)]
    GW -->|Tool Calls| NINJA[NinjaOne RMM API]

    KV[Secrets / Key Vault] -. inject env .-> GW

    subgraph OAuth Discovery
      D1[/.well-known/oauth-protected-resource]
      D2[/.well-known/oauth-authorization-server]
    end

    U1 -. reads .-> D1
    U1 -. reads .-> D2
    U2 -. reads .-> D1
    U2 -. reads .-> D2
    U3 -. reads .-> D1
    U3 -. reads .-> D2
```

### Runtime Notes
- Use `https://<your-domain>/mcp` for connector MCP URL.
- Streamable HTTP transport is the primary compatibility path.
- OAuth callback URI must be registered for each client platform.
- Keep secrets out of git; inject from secret manager.
