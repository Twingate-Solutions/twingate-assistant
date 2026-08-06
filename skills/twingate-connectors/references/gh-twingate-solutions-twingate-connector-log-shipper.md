---
source: https://github.com/Twingate-Solutions/twingate-connector-log-shipper
type: github
fetched: 2026-08-06
source_version: cfd3a888d6845f5cc99705feaefe5f283aeda17c
---

<!-- triage: unassigned -->

# Twingate Connector Log Shipper

## Summary
A lightweight Python service that captures Twingate connector analytics events from stdout, buffers them into batches, and uploads gzip-compressed NDJSON files to any S3-compatible storage. Runs as a Docker sidecar, host-level Docker watcher, or systemd service. Experimental/community project — no official Twingate support or SLA.

## Key Information
- Filters connector stdout for `ANALYTICS ` prefixed lines; optionally ships stderr too
- Reassembles Docker log lines split at the ~16 KB record boundary
- Outputs gzip-compressed NDJSON; key format: `{prefix}/{YYYY}/{MM}/{DD}/{HH}-{MM}_{uuid8}.ndjson.gz`
- Each record includes `_record_type`: `analytics` (stdout) or `stderr`
- Compatible with AWS S3, MinIO, Cloudflare R2, Backblaze B2, DigitalOcean Spaces
- Host-level Docker mode dynamically discovers/releases connector containers on a configurable interval

## Prerequisites
- Twingate connector must have `TWINGATE_LOG_ANALYTICS=v2` set
- Docker Compose or systemd depending on deployment mode
- S3-compatible bucket with valid credentials
- Python 3.12 + venv (systemd mode only)

## Deployment Modes

**Docker Sidecar** — single connector alongside shipper in same Compose stack:
```bash
docker compose -f docker-compose.sidecar.yml up -d
```

**Docker Host-Level** — one shipper watches all matching containers on the host:
```bash
docker compose -f docker-compose.host.yml up -d
```
Requires `/var/lib/docker/containers` mounted read-only into the container.

**systemd** — connector managed by systemd:
```bash
sudo python3.12 -m venv /opt/twingate-log-shipper/venv
sudo /opt/twingate-log-shipper/venv/bin/pip install -c /tmp/tls-requirements.txt "git+<repo>.git"
sudo systemctl enable --now twingate-log-shipper
```

## Configuration Values (env vars, `TWINGATE_SHIPPER_` prefix)

| Variable | Default | Description |
|---|---|---|
| `MODE` | `auto` | `auto`, `docker`, or `journald` |
| `S3_BUCKET` | *(required)* | Bucket name |
| `S3_ACCESS_KEY_ID` | *(required)* | S3 access key |
| `S3_SECRET_ACCESS_KEY` | *(required)* | S3 secret key |
| `S3_ENDPOINT_URL` | *(none)* | Custom endpoint; omit for AWS S3 |
| `S3_REGION` | `us-east-1` | Bucket region |
| `S3_PREFIX` | `twingate-analytics` | Key prefix within bucket |
| `BATCH_INTERVAL_SECONDS` | `60` | Max seconds between uploads (10–3600) |
| `BATCH_MAX_EVENTS` | `10000` | Events per batch before flush |
| `BATCH_MAX_BYTES` | `10485760` | Uncompressed batch size limit |
| `INCLUDE_STDERR` | `true` | Ship connector stderr alongside analytics |
| `DOCKER_CONTAINER_NAME_FILTER` | `twingate/connector` | Substring matched against container name or image |
| `DOCKER_DISCOVERY_INTERVAL_SECONDS` | `5` | Rescan interval for container discovery (1–300) |
| `UPLOAD_MAX_RETRIES` | `3` | S3 upload retries before discard (0–10) |
| `SHUTDOWN_TIMEOUT_SECONDS` | `30` | Wait time on SIGTERM for in-flight upload |
| `LOG_LEVEL` | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` |
| `JOURNALD_UNIT` | `twingate-connector.service` | systemd unit name (journald mode only) |

Docker Compose files map short names (e.g. `S3