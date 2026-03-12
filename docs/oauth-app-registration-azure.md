# Azure App Registration for NinjaOneMCP

## Create app registration
Create a Web app registration in Entra ID and collect:
- `AZURE_TENANT_ID`
- `AZURE_CLIENT_ID`
- `AZURE_CLIENT_SECRET`

## Redirect URIs (Web)
- `https://ninjaonemcp.example.com/oauth/callback`
- ChatGPT callbacks:
  - `https://chatgpt.com/connector_platform_oauth_redirect`
  - `https://platform.openai.com/apps-manage/oauth`
- Claude callback URI (from Claude UI)
- Copilot callback URI (from Copilot UI)

## Scopes
- `openid`
- `profile`
- `email`

## Env mapping
Set in runtime env:
- `AZURE_TENANT_ID`
- `AZURE_CLIENT_ID`
- `AZURE_CLIENT_SECRET`
- `AZURE_SCOPES=openid profile email`
- Optional `AZURE_AUDIENCE`
