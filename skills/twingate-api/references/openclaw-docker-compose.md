---
source: https://www.twingate.com/docs/openclaw-docker-compose
type: docs
fetched: 2026-08-14
source_version: b8d911b3e23c52e24c612ca1351ba5b9124537f6a66c9eed2f47fdddb607d057
---

# How to Set Up and Secure OpenClaw with Docker Compose

## Summary
Deploy OpenClaw (AI-powered WhatsApp/Telegram assistant) using Docker Compose with Caddy as a reverse proxy. Optionally add a Twingate Connector for Zero Trust remote access without exposing public ports or using SSH tunnels.

## Key Information
- OpenClaw gateway binds to `localhost:18789` inside the container; Caddy shares its network namespace to expose port 80
- Only port 80 (bound to `127.0.0.1`) is mapped to the host
- Twingate Connector uses `network_mode: host` (required)
- CLI container uses `profiles: ["cli"]` — does not auto-start
- Caddy and CLI use `network_mode: "service:openclaw-gateway"` to reach gateway on shared localhost

## Prerequisites
- Docker Engine 20.10+, Docker Compose v2
- 4GB+ RAM, 10GB+ disk
- Anthropic Claude or OpenAI API key
- Twingate account (remote access only)

## Step-by-Step

1. **Prepare environment**: `mkdir -p ~/openclaw-docker/config ~/openclaw-docker/workspace`
2. **Create `Caddyfile`**: `reverse_proxy localhost:18789` on `:80`
3. **Create `docker-compose.yml`** with `openclaw-gateway`, `openclaw-cli`, `caddy` services
4. **Create `.env`** with API keys; leave `OPENCLAW_GATEWAY_TOKEN` blank initially
5. **Run onboarding**: `docker compose run --rm openclaw-cli onboard`
6. **Get token**: `docker compose run --rm openclaw-cli dashboard --no-open`
7. **Update `.env`** with generated token, then `docker compose up -d`
8. **Access locally**: `http://localhost/?token=<your-token>`
9. **(Optional) Add Twingate**: Add connector service, create Remote Network + Resource in Admin Console, configure access policies, install Twingate Client on remote devices

## Configuration Values

### `.env` file
| Variable | Description |
|---|---|
| `CLAUDE_AI_SESSION_KEY` | Anthropic API key |
| `OPENAI_API_KEY` | OpenAI API key (alternative) |
| `OPENCLAW_GATEWAY_TOKEN` | Generated during onboarding |
| `TWINGATE_NETWORK` | Network name only (no `.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | From Admin Console → Connectors |
| `TWINGATE_REFRESH_TOKEN` | From Admin Console → Connectors |
| `TWINGATE_LOG_LEVEL` | `3` |
| `TWINGATE_LOG_ANALYTICS` | `v2` |

### Twingate Resource Config
- **Address**: Docker host IP (use `host.docker.internal` on macOS/Windows Docker Desktop)
- **Protocol**: HTTP, **Port**: `80` (not 18789)

## Gotchas
- Use Docker Compose v2 (`docker compose`), not legacy `docker-compose`
- `TWINGATE_NETWORK` is just the prefix, not the full domain
- Twingate Resource must point to port `80` (Caddy), not `18789` (gateway)
- Volume permission errors are Linux-only; fix with `sudo chown -R $(id -u):$(id -g) config/ workspace/`
- Token stored in `./config/gateway-token` if lost; re-run `dashboard --no-open` to display
- After changing `OPENCLAW_GATEWAY_TOKEN` in `.env`, restart gateway: `docker compose restart openclaw-gateway`

## Related Docs
- [Twingate Connector Deployment Options](https://www.twingate.com/docs)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- OpenClaw Documentation (openclaw.io)