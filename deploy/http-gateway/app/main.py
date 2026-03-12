from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="NinjaOne MCP HTTP Gateway")


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/.well-known/oauth-protected-resource")
async def protected_resource_metadata():
    return JSONResponse(
        content={
            "resource": "https://ninjaonemcp.example.com",
            "authorization_servers": ["https://ninjaonemcp.example.com"],
            "bearer_methods_supported": ["header"],
            "scopes_supported": ["mcp:tools:read", "mcp:tools:execute", "openid", "profile", "email"],
        }
    )


@app.get("/.well-known/oauth-authorization-server")
async def authorization_server_metadata():
    return JSONResponse(
        content={
            "issuer": "https://ninjaonemcp.example.com",
            "authorization_endpoint": "https://ninjaonemcp.example.com/oauth/authorize",
            "token_endpoint": "https://ninjaonemcp.example.com/oauth/token",
            "registration_endpoint": "https://ninjaonemcp.example.com/oauth/register",
            "response_types_supported": ["code"],
            "grant_types_supported": ["authorization_code", "refresh_token"],
            "code_challenge_methods_supported": ["S256"],
        }
    )
