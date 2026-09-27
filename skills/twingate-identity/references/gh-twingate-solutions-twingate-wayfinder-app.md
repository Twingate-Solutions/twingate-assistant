---
source: https://github.com/Twingate-Solutions/twingate-wayfinder-app
type: github
fetched: 2026-09-27
source_version: e8fa32fb00272bfa09b138195bd97bf1f9e5e163
---

# Twingate Wayfinder

## Summary
Wayfinder is an experimental reference implementation that automatically moves a Twingate user between two locally-managed groups based on physical location (office vs. remote). A PowerShell agent on Windows endpoints collects location signals and POSTs them to a FastAPI service, which adjudicates and calls the Twingate Admin API to switch group membership. Treat as a learning template, not production-ready software.

## Key Information
- **Service:** Single FastAPI Docker container; stateless except for ephemeral in-memory caches (device list, two group memberships)
- **Agent:** PowerShell script (`wayfinder-agent.ps1`) on Windows; holds no secrets, no Twingate IDs
- **Location signals:** `tcp_probe` (authoritative), `public_ip`, `domain_network`, `dns_suffix`, `wifi_ssid`
- **API rate limits respected:** 60 reads/min, 20 writes/min; configurable throttled write queue
- **No application-layer auth:** security relies entirely on network-level Twingate access control
- **Image:** `ghcr.io/twingate-solutions/wayfinder:latest` (GHCR)
- **Request attribution:** every outbound Admin API call carries a structured `User-Agent` built by `build_user_agent()` in `twingate/client.py`, injected in `_execute()` — the single code path all reads and writes pass through

## Prerequisites
- Twingate tenant with Admin API token (write access to group membership)
- Two **locally-managed** (not IdP-synced) Twingate groups created in the Admin Console
- Docker host reachable over Twingate
- Windows endpoints for the agent (PowerShell, scheduled task)

## Usage / Step-by-Step
1. Create two locally-managed groups in Twingate Admin Console; copy both group IDs from the URL
2. Generate an admin-level API token under Settings > API
3. `cp .env.example .env` and populate required variables
4. Restrict port binding to the Twingate interface (see [Network Exposure](#gotchas))
5. `docker compose pull && docker compose up -d`
6. Verify readiness: `curl http://<host>:8000/readyz` → `200 OK`
7. Deploy agent: copy `wayfinder-agent.ps1` and `wayfinder-config.json` to `C:\ProgramData\Wayfinder\`; register scheduled task to run every 5 minutes as the logged-in user

## Configuration Values

| Variable | Required | Default | Description |
|---|---|---|---|
| `WAYFINDER_TWINGATE_TOKEN` | Yes | — | Admin API token. Treat as admin-grade; never commit. |
| `WAYFINDER_TWINGATE_SUBDOMAIN` | Yes | — | The part of your Admin Console URL before `.twingate.com` — `acme` for `acme.twingate.com` (legacy single-label), or `acme.us1` for `acme.us1.twingate.com` (shard-based). Copy from the console URL rather than assuming a single label. |
| `WAYFINDER_OFFICE_GROUP_ID` | Yes | — | Group ID for office routing path |
| `WAYFINDER_AWS_GROUP_ID` | Yes | — | Group ID for remote/AWS routing path |
| `WAYFINDER_OFFICE_IPS` | Yes | — | Comma-separated office egress IPs/CIDRs |
| `WAYFINDER_POLL_INTERVAL_SECONDS` | No | `300` | Cache refresh interval |
| `WAYFINDER_WRITE_RATE_PER_MIN` | No | `18` | Throttled write queue target rate |
| `WAYFINDER_DEBOUNCE_SECONDS` | No | `60` | Min interval between switches per user |
| `WAYFINDER_LIVE_FALLBACK_COOLDOWN_SECONDS` | No | `30` | Global cooldown on the cache-miss live-fallback path. Prevents burst of simultaneous cache misses from overwhelming the read budget. |
| `WAYFINDER_MAX_ROUTE_BODY_BYTES` |