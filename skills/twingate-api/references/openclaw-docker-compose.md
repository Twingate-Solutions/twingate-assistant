# How to Set Up and Secure OpenClaw with Docker Compose

## Summary
Deploys OpenClaw (AI-powered WhatsApp/Telegram assistant) using Docker Compose with Caddy as a reverse proxy. Optionally adds a Twingate Connector for Zero Trust remote access without exposing public ports or using SSH tunnels. Local-only setup takes ~10 minutes; remote access adds ~10 minutes.

## Key Information
- OpenClaw gateway binds to `localhost:18789` inside the container—never directly exposed
- Caddy uses `network_mode: service:openclaw-gateway` (shared network namespace) to proxy port 80 → localhost:18789
- Only port mapped to host: `127.0.0.1:80:80`
- Twingate Connector uses `network_mode: host` (required)
- CLI container uses `profiles: ["cli"]`—does not auto-start; invoked manually
- Gateway token auto-generated during onboarding; retrieve anytime via `docker compose run --rm openclaw-cli dashboard --no-open`

## Prerequisites
- Docker Engine 20.10+, Docker Compose v2
- 4GB+ RAM, 10GB+ disk
- API key: Anthropic Claude or OpenAI
- For remote access: Twingate account (free tier available)

## Step-by-Step

1. **Create project directory**: `mkdir -p ~/openclaw-docker/{config,workspace}`
2. **Create `Caddyfile`**: `:80 { reverse_proxy localhost:18789 }`
3. **Create `docker-compose.yml`** with `openclaw-gateway`, `openclaw-cli`, `caddy` services
4. **Create `.env`** with API key; leave `OPENCLAW_GATEWAY_TOKEN` blank initially
5. **Run onboarding**: `docker compose run --rm openclaw-cli onboard`
6. **Get gateway token**: `docker compose run --rm openclaw-cli dashboard --no-open`
7. **Update `.env`** with token, then `docker compose up -d`
8. **Access locally**: `http://localhost/?token=<your-token>`
9. *(Optional)* Add Twingate Connector service, create Remote Network + Resource in Admin Console, update `.env`, `docker compose up -d twingate-connector`

## Configuration Values

| Variable | Description |
|---|---|
| `CLAUDE_AI_SESSION_KEY` | Anthropic API key |
| `OPENAI_API_KEY` | OpenAI API key |
| `OPENCLAW_GATEWAY_TOKEN` | Gateway auth token (from onboarding) |
| `TWINGATE_NETWORK` | Network name only (no `.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Connector access token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token from Admin Console |
| `TWINGATE_LOG_LEVEL` | Set to `3` |
| `TWINGATE_LOG_ANALYTICS` | Set to `v2` |

## Gotchas
- Twingate Resource address must be the Docker host's IP (not `localhost`); use `host.docker.internal` on macOS/Windows Docker Desktop
- Twingate Resource port must be `80` (Caddy), not `18789` (gateway direct)
- Linux volume permission errors: run `sudo chown -R $(id -u):$(id -g) config/ workspace/`
- `TWINGATE_NETWORK` value excludes `.twingate.com` suffix
- Caddy container has no `ports:` mapping—ports are inherited from gateway's network namespace

## Related Docs
- [Twingate Connector Deployment Options](https://www.twingate.com/docs)
- [OpenClaw Documentation](https://openclaw.io/docs)
- [Docker Compose Documentation](https://docs.docker.com/compose/)