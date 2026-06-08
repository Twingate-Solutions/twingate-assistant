# How to Set Up and Secure OpenClaw with Docker Compose

## Summary
Deploys OpenClaw (AI-powered WhatsApp/Telegram assistant) using Docker Compose with Caddy as a reverse proxy. Optionally adds a Twingate Connector for Zero Trust remote access without exposing public ports or using SSH tunnels.

## Key Information
- OpenClaw gateway binds to `localhost:18789` inside the container; Caddy shares the gateway's network namespace to proxy it on port 80
- Port 80 is the only host-mapped port, bound to `127.0.0.1` only
- CLI container uses `profiles: [cli]` — only runs when explicitly invoked
- Twingate Connector requires `network_mode: host`
- Two deployment modes: local-only (Steps 1–3) or with remote access (+ Step 4)

## Prerequisites
- Docker Engine 20.10+, Docker Compose v2
- 4GB+ RAM, 10GB+ disk
- Anthropic Claude or OpenAI API key
- Twingate account (remote access only)

## Step-by-Step

1. **Create project structure**: `mkdir -p ~/openclaw-docker/{config,workspace}`
2. **Create `Caddyfile`**: `reverse_proxy localhost:18789` on `:80`
3. **Create `docker-compose.yml`** with `openclaw-gateway`, `openclaw-cli` (cli profile), `caddy` services
4. **Create `.env`** with API key and placeholder for gateway token
5. **Run onboarding**: `docker compose run --rm openclaw-cli onboard`
6. **Get gateway token**: `docker compose run --rm openclaw-cli dashboard --no-open`
7. **Update `.env`** with `OPENCLAW_GATEWAY_TOKEN=<token>`
8. **Start services**: `docker compose up -d`
9. **Access locally**: `http://localhost/?token=<your-token>`
10. *(Optional)* Add Twingate Connector service, create Remote Network + Resource in Admin Console, update `.env`, `docker compose up -d twingate-connector`

## Configuration Values

| Variable | Description |
|---|---|
| `CLAUDE_AI_SESSION_KEY` | Anthropic API key |
| `OPENAI_API_KEY` | OpenAI API key (alternative) |
| `OPENCLAW_GATEWAY_TOKEN` | Generated during onboarding |
| `TWINGATE_NETWORK` | Network subdomain only (e.g., `yourcompany`) |
| `TWINGATE_ACCESS_TOKEN` | From Twingate Admin Console → Connectors |
| `TWINGATE_REFRESH_TOKEN` | From Twingate Admin Console → Connectors |
| `TWINGATE_LOG_LEVEL` | Set to `3` |
| `TWINGATE_LOG_ANALYTICS` | Set to `v2` |

**Twingate Resource config**: Address = Docker host IP, Protocol = HTTP, Port = `80`

## Gotchas
- `network_mode: "service:openclaw-gateway"` on Caddy/CLI means they cannot join `openclaw-network`; only the gateway joins that network
- Resource address must be the **host IP** (not `localhost`) — Connector runs on host network and routes to Caddy on port 80
- Linux volume permission errors: run `sudo chown -R $(id -u):$(id -g) config/ workspace/`
- Gateway token is also stored in `./config/gateway-token` if lost
- Docker Desktop on macOS/Windows: use `host.docker.internal` as Resource address

## Related Docs
- [Twingate Connector Deployment Options](https://www.twingate.com/docs)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- OpenClaw Documentation (linked in page)