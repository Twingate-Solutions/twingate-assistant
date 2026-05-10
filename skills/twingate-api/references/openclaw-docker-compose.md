# How to Set Up and Secure OpenClaw with Docker Compose

## Summary
Deploys OpenClaw (AI-powered WhatsApp/Telegram assistant) using Docker Compose with Caddy as a reverse proxy for local access. Optionally adds a Twingate Connector for Zero Trust remote access without exposing public ports or using SSH tunnels.

## Key Information
- OpenClaw gateway binds to `localhost:18789` inside the container; Caddy shares the gateway's network namespace to proxy it on port 80
- Port 80 is the only host-mapped port, bound to `127.0.0.1` by default
- Twingate Connector runs in host network mode (required)
- CLI container uses Docker Compose profiles (`cli`) so it doesn't auto-start

## Prerequisites
- Docker Engine 20.10+, Docker Compose v2
- 4GB+ RAM, 10GB+ disk
- API key: Anthropic Claude or OpenAI
- Twingate account (remote access only)

## Step-by-Step

**Local Deployment (~10 min)**
1. Create project dir: `mkdir -p ~/openclaw-docker/{config,workspace}`
2. Create `Caddyfile` with `reverse_proxy localhost:18789`
3. Create `docker-compose.yml` (see config values below)
4. Run onboarding: `docker compose run --rm openclaw-cli onboard`
5. Get token: `docker compose run --rm openclaw-cli dashboard --no-open`
6. Update `.env` with token, then: `docker compose up -d`
7. Access: `http://localhost/?token=<your-token>`

**Remote Access via Twingate (~10 min additional)**
1. Add `twingate-connector` service to `docker-compose.yml`
2. Create Twingate account → Admin Console → Remote Networks → Add Remote Network
3. Add Connector → Generate Tokens → copy Access/Refresh tokens
4. Update `.env` with Twingate credentials
5. `docker compose up -d twingate-connector`
6. Create Resource in Admin Console: address = Docker host IP, port 80, protocol HTTP
7. Assign access to users/groups
8. Install Twingate Client on remote device and connect

## Configuration Values

**`.env` file:**
```
CLAUDE_AI_SESSION_KEY=your-key        # OR
OPENAI_API_KEY=your-key
OPENCLAW_GATEWAY_TOKEN=abc123...      # Generated during onboarding
TWINGATE_NETWORK=yourcompany          # Without .twingate.com suffix
TWINGATE_ACCESS_TOKEN=...
TWINGATE_REFRESH_TOKEN=...
```

**Twingate Connector environment vars:**
```
TWINGATE_LOG_LEVEL=3
TWINGATE_LOG_ANALYTICS=v2
```
**Connector sysctls:** `net.ipv4.ping_group_range: "0 2147483647"`

**Key service settings:**
- Gateway port: `"127.0.0.1:80:80"`
- CLI: `network_mode: "service:openclaw-gateway"`, `profiles: ["cli"]`
- Caddy: `network_mode: "service:openclaw-gateway"`
- Connector: `network_mode: host`

## Gotchas
- `OPENCLAW_GATEWAY_TOKEN` must be set in `.env` before starting gateway; retrieve it via `dashboard --no-open` after onboarding
- Twingate Resource address must be host IP (not `localhost`), port `80` not `18789`
- Linux hosts may need `chown -R $(id -u):$(id -g) config/ workspace/` for volume permissions
- `docker-compose` (v1) not supported; requires `docker compose` (v2)
- When Docker Desktop on macOS/Windows, use `host.docker.internal` as Resource address

## Related Docs
- [Twingate Connector Deployment Options](https://www.twingate.com/docs)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- OpenClaw Documentation (openclaw.ai)