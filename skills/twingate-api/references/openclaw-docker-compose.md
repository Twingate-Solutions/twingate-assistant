## Securing OpenClaw with Docker Compose + Twingate

How to deploy **OpenClaw** locally / on any Docker host, with optional Twingate Connector for secure remote/team access. Two-mode deployment: local-only (10 min) or remote-accessible (20 min).

### Architecture

**Base (local-only):**
- `openclaw-gateway` container (binds to `localhost:18789` inside container)
- `caddy` container shares the gateway's network namespace, exposes port 80 on `127.0.0.1` (host-local)
- `openclaw-cli` container (CLI for onboarding, runs on demand via `--profile cli`)

**Remote/team access (optional add-on):**
- Add `twingate-connector` container in `network_mode: host`
- Twingate Resource targets the Docker host's IP; users access via Twingate Client

### Key Network Trick

`caddy` uses `network_mode: "service:openclaw-gateway"` -- shares the gateway container's network namespace. Caddy can reach `localhost:18789` inside the gateway container without exposing that port to host or Docker network. **Port 80 is the only port mapped out**, and only to `127.0.0.1`.

### Files Required

- `docker-compose.yml` (defines `openclaw-gateway`, `openclaw-cli`, `caddy`, optionally `twingate-connector`)
- `Caddyfile` (`:80 { reverse_proxy localhost:18789 }`)
- `.env` with secrets:
  ```
  CLAUDE_AI_SESSION_KEY=...   # OR OPENAI_API_KEY=...
  OPENCLAW_GATEWAY_TOKEN=...
  TWINGATE_NETWORK=yourcompany
  TWINGATE_ACCESS_TOKEN=...
  TWINGATE_REFRESH_TOKEN=...
  ```

### Setup Workflow

1. **Prerequisites**: Docker Engine 20.10+, Docker Compose v2 (`docker compose`, not `docker-compose`), 4 GB RAM, AI provider API key
2. **Create dirs**: `mkdir -p ~/openclaw-docker/{config,workspace}`
3. **Onboarding**: `docker compose run --rm openclaw-cli onboard` -> select AI provider, enter API key
4. **Get gateway token**: `docker compose run --rm openclaw-cli dashboard --no-open` -> copy the token, paste into `.env` as `OPENCLAW_GATEWAY_TOKEN`
5. **Start**: `docker compose up -d` -- gateway + caddy run; verify with `docker compose ps`
6. **Access locally**: `http://localhost/?token=<token>`

### Adding Twingate (optional Stage 4)

- Twingate Admin Console: create Remote Network -> Add Connector (Docker) -> generate tokens
- Update `.env` with Twingate values
- Add `twingate-connector` service block to compose file (host network, Connector image)
- `docker compose up -d twingate-connector`
- Create Twingate Resource:
  - Address: Docker host IP (LAN IP for local; `host.docker.internal` for Docker Desktop on macOS/Windows)
  - Protocol: HTTP, Port: 80
  - Assign to a Group
- Install Twingate Client on remote devices; access at `http://<docker-host-ip>/?token=<token>`

### Decision Notes

- **Local-only mode** is sufficient for single-user dev; skip Twingate entirely
- **Remote/team mode** replaces SSH tunneling, ngrok, or VPN -- cleaner for shared homelab/team setups
- The shared-namespace trick keeps the gateway port unreachable except via Caddy -- defense in depth
- Always set the AI provider API key carefully; don't commit `.env`

### Gotchas

- Use `docker compose` (v2) not `docker-compose` -- different syntax in some places
- Linux volume permissions: `chown -R $(id -u):$(id -g) config/ workspace/` if you hit permission errors (macOS/Windows handle automatically)
- Port 80 conflict on host: stop other services or change the port mapping in compose
- Twingate Connector requires `network_mode: host` -- do not change this

### Related Docs

- /docs/openclaw -- Cross-platform OpenClaw deployment overview
- /docs/openclaw-digitalocean -- Cloud equivalent (DigitalOcean Marketplace)
- /docs/deploy-connector-with-docker-compose -- Generic Twingate Connector via compose
- /docs/connector-best-practices, /docs/connector-monitoring
