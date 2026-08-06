---
source: https://github.com/Twingate-Solutions/gatorcast
type: github
fetched: 2026-08-06
source_version: 1cbe50f5ccaba9c572ac4714eb0d90bfe11d4aa7
---

<!-- triage: unassigned -->

# Gatorcast

## Summary
Self-hosted single-container service that receives Twingate Identity Firewall Gateway session recordings (asciicast v2 fragments), reassembles them by `conn_id`, and serves a web UI for browsing and replaying sessions. Includes live detection rules for dangerous commands and secret exposure, with jump-to-timestamp links. All data remains on your infrastructure.

**Status:** Example/reference project. No support or warranty. Apache 2.0, AS IS.

---

## Key Information
- Ingests via HTTP POST (`/ingest`) or syslog TCP; outputs a browse/replay UI
- Groups recordings by target system (`resource_address`); sessions are playable while still in progress
- Built-in detection: dangerous-command and secret-exposure rules run on every append and at seal
- Fully offline — all frontend assets (asciinema-player, htmx, Alpine.js) are vendored locally
- Single SQLite database + `.cast` files stored in a named Docker volume

---

## Prerequisites
- Docker and Docker Compose
- Twingate Gateway emitting structured JSON audit logs with `asciicast` fields

---

## Usage

```bash
# 1. Clone repo
git clone https://github.com/Twingate-Solutions/gatorcast && cd gatorcast

# 2. Configure secrets
cp .env.example .env
# Edit .env: set INGEST_TOKEN, UI_AUTH_USERNAME, UI_AUTH_PASSWORD

# 3. Start
docker compose pull
docker compose up -d

# 4. Open UI
# http://<host>:8080  (HTTP Basic auth)

# Update
docker compose pull && docker compose up -d
```

---

## Configuration Values (Environment Variables)

| Variable | Default | Notes |
|---|---|---|
| `HTTP_PORT` | `8080` | UI + `/ingest` endpoint |
| `SYSLOG_TCP_PORT` | `6514` | `0` disables |
| `DATA_DIR` | `/data` | SQLite + `.cast` storage root |
| `IDLE_TIMEOUT_SECONDS` | `120` | Sweep cadence |
| `SESSION_MAX_IDLE_SECONDS` | `3600` | Idle backstop seal; must exceed Gateway flush interval |
| `RETENTION_DAYS` | `90` | `0` = keep forever |
| `RETENTION_MAX_GB` | `0` | `0` = no size cap |
| `LOG_LEVEL` | `info` | `debug`/`info`/`warning`/`error` |
| `INGEST_TOKEN` | *(required)* | Bearer token for `/ingest` |
| `UI_AUTH_USERNAME` | `admin` | HTTP Basic username |
| `UI_AUTH_PASSWORD` | *(required)* | HTTP Basic password |
| `ENCRYPTION_ENABLED` | `false` | AES-256-GCM at rest |
| `GATORCAST_MASTER_KEY` | *(unset)* | Required if encryption enabled; base64 32-byte key |
| `DETECTION_ENABLED` | `true` | Live detection on every append |
| `BACKFILL_ON_STARTUP` | `true` | Index/detect existing recordings missing search sidecars |
| `SEARCH_PAGE_SIZE` | `50` | Results per page |
| `SEARCH_REGEX_MAX_CANDIDATES` | `2000` | Max sidecars scanned per content search |

---

## Gotchas
- Service starts with placeholder `.env` values but logs a warning — do not expose to a network with defaults
- Only processes lines where `logger == "gateway.audit"` AND `asciicast` field is non-null; API-audit lines are dropped by design
- **journald `LineMax` (default 48 KB)** truncates large asciicast chunks → recordings never assemble; raise to `4M` or use file-tail transport for TUI-heavy sessions
- UDP syslog truncates multi-KB lines — always use TCP or HTTP
- Syslog TCP port binds to `127.0.0.1` by default; change to internal interface IP for remote shippers, never `0.0.0.0`
- Reverse proxy `client_max_body_size` should be `64m`