# How to Set Up and Secure OpenClaw with Docker Compose

## Summary
Deploy OpenClaw (AI-powered WhatsApp/Telegram assistant) using Docker Compose with Caddy as a reverse proxy. Optionally add a Twingate Connector for Zero Trust remote access without exposing public ports or using SSH tunnels.

## Key Information
- OpenClaw gateway binds to `localhost:18789` inside the container; Caddy shares the gateway's network namespace to proxy it on port 80
- Port 80 is the only host-mapped port, bound to `127.0.0.1` by default
- CLI container uses Docker Compose profiles (`cli`) — only runs when explicitly invoked
- Twingate Connector requires `network_mode: host`

## Prerequisites
- Docker Engine 20.10+, Docker Compose v2
- 4GB+ RAM, 10GB+ disk
- Anthropic Claude or OpenAI API key
- Twingate account (remote access only)

## Step-by-Step

1. **Create project structure**: `mkdir -p ~/openclaw-docker/{config,workspace}`
2. **Create `Caddyfile`**: `reverse_proxy localhost:18789` on `:80`
3. **Create `docker-compose.yml`** with `openclaw-gateway`, `caddy`, `openclaw-cli` services
4. **Create `.env`** with API keys (token field left empty initially)
5. **Run onboarding**: `docker compose run --rm openclaw-cli onboard`
6. **Get gateway token**: `docker compose run --rm openclaw-cli dashboard --no-open`
7. **Update `.env`** with generated token
8. **Start services**: `docker compose up -d`
9. **Access locally**: `http://localhost/?token=<your-token>`
10. *(Optional)* Add Twingate Connector service, create Remote Network + Resource in Admin Console, install Twingate Client on remote devices

## Configuration Values

| Variable | Description |
|---|---|
| `CLAUDE_AI_SESSION_KEY` | Anthropic API key |
| `OPENAI_API_KEY` | OpenAI API key |
| `OPENCLAW_GATEWAY_TOKEN` | Generated gateway auth token |
| `TWINGATE_NETWORK` | Network name (without `.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token |
| `TWINGATE_LOG_LEVEL` | Set to `3` |
| `TWINGATE_LOG_ANALYTICS` | Set to `v2` |

**Twingate Resource config**: Address = Docker host IP, Protocol = HTTP, Port = `80`

## Gotchas
- `network_mode: "service:openclaw-gateway"` on Caddy/CLI means they cannot join named networks — the gateway handles all networking
- Linux hosts may need `chown -R $(id -u):$(id -g) config/ workspace/` for volume permissions
- Twingate Resource must point to port `80` (Caddy), **not** `18789` (gateway internal port)
- Token stored in `./config/gateway-token`; regenerate with `docker compose run --rm openclaw-cli dashboard --no-open`
- Always backup before `docker compose pull` updates

## Related Docs
- [Twingate Connector Deployment Options](https://www.twingate.com/docs)
- [OpenClaw Documentation](https://openclaw.io/docs)
- [Docker Compose Networking](https://docs.docker.com/compose/networking/)