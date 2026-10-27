---
source: https://github.com/Twingate-Solutions/gatorcast
type: github
fetched: 2026-10-25
source_version: 60b3e643b824de5a2867e8f426466ecd163cc711
trust: official
---

# Gatorcast

Self-hosted, single-container service for reassembling and replaying Twingate Identity Firewall Gateway session recordings. The Gateway emits asciicast v2 fragments, kubectl API audit lines, and web-app request lines via structured JSON logs; Gatorcast receives them by HTTP POST or syslog TCP, demultiplexes by `conn_id`, and serves a web UI for browse/replay. All data stays on your infrastructure.

**Unsupported example project. Review and test before any production use. Apache 2.0 licensed, no warranty.**

---

## Key Information

- Stores SSH/kubectl exec recordings as asciicast v2, kubectl API request metadata, and web-app request metadata
- 21 built-in detection rules (dangerous commands, secret exposure, 6 kubectl API rules); findings include jump-to-timestamp links
- Unified search across all event kinds with CSV export
- Encryption at rest optional (AES-256-GCM); SQLite metadata DB is never encrypted
- Retention by age (`RETENTION_DAYS`) and recording size (`RETENTION_MAX_GB`)
- Schema migrations run automatically on startup; no manual migration steps

---

## Prerequisites

- Docker and Docker Compose
- A Twingate Gateway forwarding structured JSON audit logs

---

## Usage

```bash
git clone https://github.com/Twingate-Solutions/gatorcast.git
cd gatorcast
cp .env.example .env
# Edit .env: set INGEST_TOKEN, UI_AUTH_USERNAME, UI_AUTH_PASSWORD
docker compose pull
docker compose up -d
```

Open `http://<host>:8080`. See [INGESTION_RECIPES.md](https://github.com/Twingate-Solutions/gatorcast/blob/main/INGESTION_RECIPES.md) to forward Gateway logs.

---

## Supported Gateway Versions

Gateway 2.0.0 renamed its loggers. Gatorcast 0.6.0 and later accept both sets of names, so a fleet mixing Gateway versions needs no extra configuration.

| Line | Preview Gateway (before 2.0.0) | Gateway 2.0.0 |
|---|---|---|
| Recording chunk | `gateway.audit` | `session_recording` |
| HTTP request audit (Kubernetes and web app) | `gateway.audit` | `audit` |
| Connection start (`Authenticated connection`) | `gateway` | `system` |

2.0.0 SSH recordings arrive in segments (a chunk about every 256 KB or 5 minutes, then a final `session finished` chunk) and are reassembled the same way as Kubernetes recordings. 2.0.0 SSH audit events and Gateway service/proxy-error lines are dropped.

**Upgrade Gatorcast to 0.6.0 before upgrading any Gateway or gwops to 2.0.0.** A Gatorcast older than 0.6.0 drops every 2.0.0 line and still answers `2xx`; gwops treats any `2xx` as delivered, so those lines are lost with no error on either side.

---

## Configuration Values

Nine variables are set in `docker-compose.yml` and take precedence over `.env`; change them there. All others go in `.env`.

| Variable | Default | Notes |
|---|---|---|
| `HTTP_PORT` | `8080` | UI + `/ingest` port |
| `SYSLOG_TCP_PORT` | `6514` | TCP syslog listener; `0` disables |
| `DATA_DIR` | `/data` | SQLite DB, `.cast` files, search sidecars |
| `IDLE_TIMEOUT_SECONDS` | `120` | Backstop sweep interval |
| `SESSION_MAX_IDLE_SECONDS` | `3600` | Seal recording after this silence; must exceed Gateway flush interval |
| `RETENTION_DAYS` | `90` | Age-based purge; `0` = keep forever |
| `RETENTION_MAX_GB` | `0` | Size cap on recordings; `0` = disabled |
| `LOG_LEVEL` | `info` | `debug`/`info`/`warning`/`error` |
| `ENCRYPTION_ENABLED` | `false` | Set in `docker-compose.yml`, not `.env`