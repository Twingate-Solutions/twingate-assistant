---
source: https://github.com/Twingate-Labs/tg-render
type: github
fetched: 2026-08-06
source_version: 8c63c22583d2d3bc074b9adcdf999000304f64db
---

<!-- triage: unassigned -->

# tg-render

## Summary
Deploys a Twingate connector on render.com as a private network access point. Enables least-privileged access controls to private resources hosted in a render.com environment.

## Key Information
- Provides a one-click deploy button for render.com
- Runs a Twingate connector as a render.com service
- Requires credentials generated from the Twingate admin console

## Prerequisites
- A Twingate account with admin access
- A render.com account
- Twingate connector tokens (access token and refresh token) obtained from the Twingate admin console
- Twingate account URL (e.g., `https://acme.twingate.com`)

## Usage / Step-by-Step
1. Log in to the Twingate admin console and generate connector tokens (access token and refresh token).
2. Note your Twingate account URL.
3. Click the "Deploy to Render" button in the README or navigate to:
   `https://render.com/deploy?repo=https://github.com/Twingate-Labs/tg-render/tree/main`
4. In the render.com deploy flow, enter the required environment values when prompted.
5. Complete the deployment; the connector will register with your Twingate network automatically.

## Configuration Values

| Variable | Description | Example |
|---|---|---|
| Account URL | Your Twingate tenant URL | `https://acme.twingate.com` |
| Access Token | Connector access token from Twingate admin console | — |
| Refresh Token | Connector refresh token from Twingate admin console | — |

These values are entered interactively during the render.com deploy flow, not in a local config file.

## Gotchas
- Tokens must be generated per-connector in the Twingate admin console; they are not reusable across multiple connectors.
- The repo contains minimal documentation; consult Twingate's official connector docs for troubleshooting connector registration issues.
- render.com free-tier services may spin down when idle, which could interrupt connector availability.

## Related Docs
- [Twingate Connector Documentation](https://www.twingate.com/docs/connectors)
- [Twingate Admin Console](https://auth.twingate.com)
- [render.com Deploy Hooks](https://render.com/docs/deploy-hooks)