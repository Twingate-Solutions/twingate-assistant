---
source: https://github.com/Twingate-Solutions/gatorcast/wiki
type: github
fetched: 2026-11-08
source_version: 221e3bd21145b8519dbc1e5b33b54d558a970a9e
trust: official
---

# Gatorcast Architecture & Operations Reference

## Summary
Gatorcast is a single-container FastAPI service that ingests Twingate Gateway session recordings and kubectl/web audit logs, assembles and stores them, and provides a web UI for search, replay, and detection. It accepts log data via HTTP POST or syslog TCP, writes recordings to disk as `.cast` files, and stores metadata in SQLite. Detection runs live as chunks arrive and again at seal.

## Key Information
- **Single process**: ingestion, assembly, storage, scheduler, and UI all in one FastAPI container
- **State**: SQLite (WAL mode) for metadata; Docker volume for `.cast` files and `.txt.enc` search sidecars
- **Push-only**: Gatorcast exposes endpoints and waits; it never reaches back into the Gateway, Docker, or Kubernetes
- **File-first**: recordings are written plaintext on every append while in progress; encrypted only at seal
- **Two ingest paths**: `POST /ingest` (bearer token auth) and syslog TCP listener (octet-counted or newline-delimited)
- **Gateway version compat**: accepts both preview logger names (`gateway.audit`, `gateway`) and 2.0.0 names (`session_recording`, `audit`, `system`); upgrade Gatorcast before the Gateway
- **Two background jobs**: `idle_finalize` (seals idle recordings, expires stuck-pending connections) and `retention_purge` (runs every 24 h, first run 24 h after start)
- **21 built-in recording detection rules** across `dangerous-command` and `secret-exposure` categories; 6 `kube-api` rules for kubectl requests
- **Findings never store matched text**; only rule id, category, severity, and replay offset

## Prerequisites
- Docker with a named volume for `/data`
- Twingate Gateway emitting JSON logs (Gateway 2.0.0 or the preview fork)
- A log shipper configured to push to Gatorcast (rsyslog `omhttp`, Docker syslog driver, or similar)

## Configuration Values

Nine variables are set in `docker-compose.yml` and take precedence over `.env`; all others go in `.env`.

| Variable | Default | Notes |
|---|---|---|
| `HTTP_PORT` | `8080` | UI + `/ingest` port; update compose port mapping too |
| `SYSLOG_TCP_PORT` | `6514` | `0` disables |
| `DATA_DIR` | `/data` | Volume root |
| `IDLE_TIMEOUT_SECONDS` | `120` | Sets sweep cadence (clamped 5–30 s); not a finalize trigger |
| `SESSION_MAX_IDLE_SECONDS` | `3600` | Idle backstop; must exceed Gateway flush interval |
| `RETENTION_DAYS` | `90` | `0` = keep forever |
| `RETENTION_MAX_GB` | `0` | Size cap on `.cast` files; `0` disables |
| `LOG_LEVEL` | `info` | `debug`, `info`, `warning`, `error` |
| `ENCRYPTION_ENABLED` | `false` | Set in `docker-compose.yml`, not `.env` |
| `INGEST_TOKEN` | `change-me-long-random` | Bearer token for `/ingest`; replace the default |
| `UI_AUTH_USERNAME` | `admin` | Basic auth username |
| `UI_AUTH_PASSWORD` | `change-me` | Basic auth password; replace the default |
| `GATORCAST_MASTER_KEY` | *(unset)* | Required when encryption enabled; `openssl rand -base64 32` |
| `DETECTION_ENABLED` | `true` | Master switch; `false` skips all scans and backfill |
| `BACKFILL_ON_STARTUP` | `true` | Re-index completed recordings missing a sidecar; no-op if detection disabled |
| `SEARCH_PAGE_SIZE` | `50` | Overridable per request (1–200) |
| `KUBECTL_ACTIVITY_GAP_SECONDS` | `900` | Also governs web visit splitting |
| `KUBECTL_ACTIVITY_MAX_SECONDS` | `14400` | Must be ≥ `