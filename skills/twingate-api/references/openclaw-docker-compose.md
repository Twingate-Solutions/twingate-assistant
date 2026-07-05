# How to Set Up and Secure OpenClaw with Docker Compose

## Summary
Deploy OpenClaw (AI-powered WhatsApp/Telegram assistant) using Docker Compose with Caddy as a reverse proxy. Optionally add a Twingate Connector for Zero Trust remote access without exposing public ports or using SSH tunnels.

## Key Information
- OpenClaw gateway binds to `localhost:18789` inside the container—never exposed directly
- Caddy uses `network_mode: service:openclaw-gateway` to share the gateway's network namespace and proxy port 80
- Port 80 bound to `127.0.0.1` only (host-local by default)
- Twingate Connector uses `network_mode: host` (required)
- CLI container uses profiles to avoid auto-starting; invoked on-demand

## Prerequisites
- Docker Engine 20.10+, Docker Compose v2
- 4GB+ RAM, 10GB+ disk
- Anthropic or OpenAI API key
- Twingate account (remote access only)

## Step-by-Step

1. **Create project directory**: `mkdir -p ~/openclaw-docker/{config,workspace}`
2. **Create `Caddyfile`**: reverse proxy `localhost:18789` on `:80`
3. **Create `docker-compose.yml`** with three services: `openclaw-gateway`, `openclaw-cli` (profile: cli), `caddy`
4. **Create `.env`** with API keys and empty `OPENCLAW_GATEWAY_TOKEN`
5. **Run onboarding**: `docker compose run --rm openclaw-cli onboard`
6. **Get gateway token**: `docker compose run --rm openclaw-cli dashboard --no-open`
7. **Update `.env`** with generated token
8. **Start services**: `docker compose up -d`
9. **Access locally**: `http://localhost/?token=<your-token>`
10. *(Optional)* Add Twingate Connector service, configure Remote Network/Resource in Admin Console, update `.env`

## Configuration Values

| Variable | Description |
|---|---|
| `CLAUDE_AI_SESSION_KEY` | Anthropic API key |
| `OPENAI_API_KEY` | OpenAI API key |
| `OPENCLAW_GATEWAY_TOKEN` | Auto-generated; retrieve via `dashboard --no-open` |
| `TWINGATE_NETWORK` | Network subdomain (without `.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | From Twingate Admin Console |
| `TWINGATE_REFRESH_TOKEN` | From Twingate Admin Console |
| `TWINGATE_LOG_LEVEL` | `3` (recommended) |

**Twingate Resource config**: Address = Docker host IP, Protocol = HTTP, Port = `80`

## Gotchas
- Twingate Resource port must be `80` (Caddy), NOT `18789` (internal gateway port)
- Linux hosts may need `chown -R $(id -u):$(id -g) config/ workspace/` for volume permissions
- `TWINGATE_NETWORK` is just the subdomain prefix, not the full hostname
- CLI container shares gateway network namespace—depends on gateway being healthy first
- Token must be passed as URL parameter: `?token=<value>`
- Always back up before `docker compose pull` updates

## Related Docs
- [Twingate Connector Deployment Options](https://www.twingate.com/docs)
- [OpenClaw Documentation](https://openclaw.ai/docs)
- [Docker Compose Networking](https://docs.docker.com/compose/networking/)