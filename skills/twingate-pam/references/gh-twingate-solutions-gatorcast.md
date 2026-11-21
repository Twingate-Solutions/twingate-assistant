---
source: https://github.com/Twingate-Solutions/gatorcast
type: github
fetched: 2026-11-08
source_version: 595f2c9e6517c5e3019f183f907cc62031a78d48
trust: official
---

# Gatorcast

Self-hosted, single-container service that receives, reassembles, and replays Twingate Identity Firewall Gateway session recordings (asciicast v2). Accepts log lines via HTTP POST or syslog TCP, demultiplexes concurrent sessions by `conn_id`, and serves a browser-based UI with asciinema playback. Also stores Kubernetes API audit lines and web-app request activity, with built-in detection rules for dangerous commands and on-screen secrets.

## Key Information

- Image is pulled from GHCR; no local build required
- Ingestion: HTTP POST with Bearer token or syslog TCP
- UI: lightweight web interface at port 8080, HTTP Basic auth
- Detection rules flag dangerous commands and secrets with jump-to-timestamp links
- All recordings remain on your infrastructure
- Unsupported example project; provided as-is under Apache 2.0

## Prerequisites

- Docker and Docker Compose

## Usage / Step-by-Step

1. Clone the repository and enter the directory
2. Copy `.env.example` to `.env` and set the three required secrets (see Configuration Values below)
3. Pull and start the container:
   ```bash
   docker compose pull
   docker compose up -d
   ```
4. Open `http://<your-host>:8080` and log in with `UI_AUTH_USERNAME` / `UI_AUTH_PASSWORD`
5. Configure a log shipper to forward Gateway logs to the ingest endpoint — see the [Ingestion Overview wiki page](https://github.com/Twingate-Solutions/gatorcast/wiki/Ingestion-Overview)

## Configuration Values

| Variable | Description |
|---|---|
| `INGEST_TOKEN` | Bearer token required on all POST requests to `/ingest` |
| `UI_AUTH_USERNAME` | Web UI login username |
| `UI_AUTH_PASSWORD` | Web UI login password |

Additional configuration (retention, encryption at rest, reverse proxy, etc.) is documented in the [wiki](https://github.com/Twingate-Solutions/gatorcast/wiki/Configuration).

## Gotchas

- Gatorcast logs a startup warning (`config.insecure_default`) if any secret still matches the placeholder defaults (`change-me-long-random`, `admin`, `change-me`). The service starts anyway — do not expose it on a network with defaults set.
- Project is explicitly unsupported and was partially developed with an LLM coding assistant; review and test before any production use.
- No TLS termination built in; use a reverse proxy for HTTPS ([wiki guide](https://github.com/Twingate-Solutions/gatorcast/wiki/Reverse-Proxy-Deployment)).

## Related Docs

- [Wiki home](https://github.com/Twingate-Solutions/gatorcast/wiki)
- [Ingestion Overview](https://github.com/Twingate-Solutions/gatorcast/wiki/Ingestion-Overview) — systemd, Terraform, Docker, Kubernetes, curl test
- [Security Model](https://github.com/Twingate-Solutions/gatorcast/wiki/Security-Model)
- [Encryption at Rest](https://github.com/Twingate-Solutions/gatorcast/wiki/Encryption-at-Rest)
- [Detection Rules](https://github.com/Twingate-Solutions/gatorcast/wiki/Detection-Rules)
- [CHANGELOG.md](https://github.com/Twingate-Solutions/gatorcast/blob/main/CHANGELOG.md)