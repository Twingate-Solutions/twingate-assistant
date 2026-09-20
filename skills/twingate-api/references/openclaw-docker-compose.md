---
source: https://www.twingate.com/docs/openclaw-docker-compose
type: docs
fetched: 2026-09-20
source_version: a2f1e8bf01fc7c97ef28e1910cf71412193bd10a5013f4bfa865a09c5277089b
---

# How to Set Up and Secure OpenClaw with Docker Compose

## Summary
Deploys OpenClaw (AI-powered WhatsApp/Telegram assistant) using Docker Compose with Caddy as a reverse proxy. Optionally adds a Twingate Connector for Zero Trust remote access without exposing public ports or using SSH tunnels.

## Key Information
- OpenClaw gateway binds to `localhost:18789` inside the container; Caddy shares its network namespace to expose port 80
- Only port mapped to host: `127.0.0.1:80:80` (localhost only by default)
- Twingate Connector uses `network_mode: host` (required)
- CLI container uses `profiles: [cli]` — only runs when explicitly invoked
- Config persisted in `./config` and `./workspace` bind mounts

## Prerequisites
- Docker Engine 20.10+, Docker Compose v2
- 4GB+ RAM, 10GB+ disk
- Anthropic or OpenAI API key
- Twingate account (remote access only)

## Step-by-Step

**Local deployment (~10 min):**
1. `mkdir -p ~/openclaw-docker/{config,workspace} && cd ~/openclaw-docker`
2. Create `Caddyfile` with `reverse_proxy localhost:18789`
3. Create `docker-compose.yml` (see config below)
4. Create `.env` with API key; leave `OPENCLAW_GATEWAY_TOKEN` blank
5. `docker compose run --rm openclaw-cli onboard`
6. `docker compose run --rm openclaw-cli dashboard --no-open` → copy token
7. Add token to `.env`, then `docker compose up -d`
8. Access at `http://localhost/?token=<token>`

**Remote access via Twingate (~10 min additional):**
1. Add `twingate-connector` service to `docker-compose.yml`
2. Create Twingate account → Admin Console → Remote Networks → Add Remote Network
3. Add Connector → Generate Tokens → copy Access Token + Refresh Token
4. Add to `.env`: `TWINGATE_NETWORK`, `TWINGATE_ACCESS_TOKEN`, `TWINGATE_REFRESH_TOKEN`
5. `docker compose up -d twingate-connector`
6. Admin Console → Resources → Add Resource (address = Docker host IP, port 80, HTTP)
7. Assign access to users/groups
8. Install Twingate Client, connect, browse to `http://<docker-host-ip>/?token=<token>`

## Configuration Values

**`.env` variables:**
| Variable | Description |
|---|---|
| `CLAUDE_AI_SESSION_KEY` | Anthropic API key |
| `OPENAI_API_KEY` | OpenAI API key (alternative) |
| `OPENCLAW_GATEWAY_TOKEN` | Generated via CLI `dashboard --no-open` |
| `TWINGATE_NETWORK` | Network subdomain only (e.g., `yourcompany`) |
| `TWINGATE_ACCESS_TOKEN` | From Twingate Admin Console |
| `TWINGATE_REFRESH_TOKEN` | From Twingate Admin Console |
| `TWINGATE_LOG_LEVEL` | `3` (recommended) |
| `TWINGATE_LOG_ANALYTICS` | `v3` |

**Twingate Connector sysctl:**
```yaml
sysctls:
  net.ipv4.ping_group_range: "0 2147483647"
```

## Gotchas
- **Connector must use `network_mode: host`** — other modes break Twingate Connector operation
- **Caddy and CLI must use `network_mode: "service:openclaw-gateway"`** — required to reach `localhost:18789`; they don't join `openclaw-network`
- **Twingate Resource address** = Docker host IP, **not** `localhost` — the Connector routes through the host network
- Linux volume permission errors require `chown -R $(id -u):$(id -g) config/ workspace/`; macOS/Windows handle automatically
- `TWINGATE_NETWORK` value is just the subdomain prefix, not the full `.twingate.com` domain

## Related