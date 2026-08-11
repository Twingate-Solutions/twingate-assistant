---
source: https://github.com/Twingate-Solutions/twingate-mdm-connector
type: github
fetched: 2026-08-09
source_version: 9a512d6e94b5f2a7590dd336df5b63a538e6a973
---

<!-- triage: unassigned -->

# Twingate MDM Connector

## Summary
Open-source middleware that automatically marks devices as trusted in Twingate by cross-referencing MDM/EDR provider inventories. Runs on a configurable schedule as a stateless Docker container, matching devices by serial number and calling the Twingate API to set `isTrusted: true`. Never untrusts a device and requires no database.

## Key Information
- **Community project** — not officially supported by Twingate
- Supported providers: NinjaOne, Sophos, ManageEngine (cloud/on-prem), Automox, JumpCloud, FleetDM, Mosyle, Datto RMM, Rippling, Manual (rules-only)
- Tested providers: NinjaOne, ManageEngine (cloud), JumpCloud, Manual
- Webhook destinations: Slack, Discord, raw JSON/SIEM (tested); Teams, PagerDuty, OpsGenie (untested)
- Serial number matching is normalized via `strip().upper()`
- Provider fetches run in parallel; matching is done fully in-memory
- Optional SMTP email alerts and daily digests with customizable templates
- Optional HMAC-SHA256 webhook signing

## Prerequisites
- Docker or Python environment
- Twingate API key with **Devices Read + Write** scopes
- Credentials for at least one MDM/EDR provider
- `pip install -e ".[dev]"` for local development

## Usage / Step-by-Step

1. **Create `config.yaml`** with `twingate` and `providers` sections
2. **Pass secrets as environment variables** using `${ENV_VAR}` interpolation in config
3. **Run via Docker:**
```bash
docker run --rm \
  -v "$(pwd)/config.yaml:/app/config.yaml:ro" \
  -e TWINGATE_API_KEY=your-key \
  ghcr.io/twingate-solutions/twingate-mdm-connector:latest
```
4. **Optionally enable health check** by setting `HEALTHZ_PORT=8080`

## Configuration Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `twingate.tenant` | string | required | Subdomain from `acme.twingate.com` |
| `twingate.api_key` | string | required | Twingate API key |
| `trust.mode` | `any`/`all` | `any` | Trust if compliant in any vs. all providers |
| `trust.max_days_since_checkin` | int \| `null` | `7` | Skip devices not seen within this window; `null` disables the recency check entirely |
| `sync.interval_seconds` | int | `300` | Sync frequency |
| `sync.dry_run` | bool | `false` | Log-only mode; no Twingate mutations |
| `logging.level` | string | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR` |
| `HEALTHZ_PORT` | env var | unset | Enables HTTP liveness endpoint |

## Gotchas
- **Never untrusts devices** — only sets `isTrusted: true`; removing trust requires manual action
- Devices matched by zero providers are never trusted
- Devices exceeding `max_days_since_checkin` are silently skipped; set `max_days_since_checkin: null` to disable this check
- `trust.mode: all` requires a device to appear in **every** enabled provider that recognizes it
- If a provider errors, it is skipped for that cycle — not a fatal failure
- Referenced `${ENV_VAR}` values that are unset cause startup exit
- Several providers are implemented but **untested** against live instances

## FleetDM Provider Notes
- Config key is `url` (not `base_url`)
- Pagination uses **0-indexed** pages with a page size of 500; stops when a page returns fewer rows than the page size
- Online/offline state is read from Fleet's `status` field; only `status == "online"` is treated as online (`offline`, `new`, `mia`, `missing` are treated as not-online); set `trust.require_online