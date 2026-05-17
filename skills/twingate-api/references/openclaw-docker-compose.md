# How to Set Up and Secure OpenClaw with Docker Compose

## Summary
Deploys OpenClaw (AI-powered WhatsApp/Telegram assistant) using Docker Compose with Caddy as a reverse proxy for local access. Optionally adds a Twingate Connector for Zero Trust remote access without exposing public ports or using SSH tunnels.

## Key Information
- OpenClaw gateway binds to `localhost:18789` inside the container; Caddy shares its network namespace to proxy it on port 80
- Port 80 is the only host-mapped port, bound to `127.0.0.1` by default
- CLI container uses Docker Compose profiles (`cli`) so it only runs when explicitly invoked
- Twingate Connector runs in `network_mode: host` (required)
- Two Docker images used: `ghcr.io/openclaw/openclaw:latest` and `twingate/connector:latest`

## Prerequisites
- Docker Engine 20.10+, Docker Compose v2
- 4GB+ RAM, 10GB+ disk
- Anthropic Claude API key (`CLAUDE_AI_SESSION_KEY`) or OpenAI key (`OPENAI_API_KEY`)
- Twingate account (only for remote access step)

## Step-by-Step

1. **Create project directory**: `mkdir -p ~/openclaw-docker/{config,workspace}`
2. **Create `Caddyfile`**: Single `reverse_proxy localhost:18789` block on `:80`
3. **Create `docker-compose.yml`**: Services: `openclaw-gateway`, `openclaw-cli` (profile: cli), `caddy`, optionally `twingate-connector`
4. **Create `.env`**: Set API key and leave `OPENCLAW_GATEWAY_TOKEN` blank initially
5. **Run onboarding**: `docker compose run --rm openclaw-cli onboard`
6. **Get gateway token**: `docker compose run --rm openclaw-cli dashboard --no-open`
7. **Update `.env`** with generated token, then `docker compose up -d`
8. **(Optional) Add Twingate**: Create Remote Network → generate Connector tokens → add service to compose → create Resource pointing to Docker host IP on port 80

## Configuration Values

| Variable | Description |
|---|---|
| `CLAUDE_AI_SESSION_KEY` | Anthropic API key |
| `OPENAI_API_KEY` | OpenAI API key (alternative) |
| `OPENCLAW_GATEWAY_TOKEN` | Generated during onboarding |
| `TWINGATE_NETWORK` | Network name without `.twingate.com` |
| `TWINGATE_ACCESS_TOKEN` | From Twingate Admin Console |
| `TWINGATE_REFRESH_TOKEN` | From Twingate Admin Console |
| `TWINGATE_LOG_LEVEL` | Set to `3` |
| `TWINGATE_LOG_ANALYTICS` | Set to `v2` |

## Gotchas
- Twingate Resource address must be the Docker **host** IP, not container IP — use `192.168.x.x` (local), private IP (VPS), or `host.docker.internal` (Docker Desktop Mac/Windows)
- Resource port must be `80` (Caddy), **not** `18789` (gateway internal port)
- Linux may require `chown -R $(id -u):$(id -g) config/ workspace/` to fix volume permission errors
- `TWINGATE_NETWORK` value is only the subdomain portion (e.g., `yourcompany`, not `yourcompany.twingate.com`)
- Gateway token is stored in `./config/gateway-token` if lost

## Related Docs
- [Twingate Connector Deployment Options](https://www.twingate.com/docs)
- [OpenClaw Documentation](https://openclaw.io/docs)
- [Docker Compose Documentation](https://docs.docker.com/compose/)