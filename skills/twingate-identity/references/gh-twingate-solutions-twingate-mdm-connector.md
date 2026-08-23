---
source: https://github.com/Twingate-Solutions/twingate-mdm-connector
type: github
fetched: 2026-08-23
source_version: e56c6bef2b78500eed160a792c66f758fef38cde
---

# Twingate MDM Connector

## Summary
Open-source middleware that automatically marks devices as trusted in Twingate by cross-referencing MDM/EDR provider inventories. Runs on a configurable schedule, matches devices by serial number, and calls the Twingate API to set `isTrusted: true` on compliant devices. Stateless Docker container; never untrusts a device.

> Meant as a working example and foundation for teams who want to build device-trust automation of their own. Fork it, adapt it, and make it fit your environment. Not officially supported by Twingate's support team; use the issue tracker for bug reports and questions. Provided under Apache License 2.0 without warranty; use in production is at your own discretion and risk.

---

## Key Information
- **Image:** `ghcr.io/twingate-solutions/twingate-mdm-connector:latest`
- **Supported providers:** NinjaOne, Sophos, ManageEngine (cloud/on-prem), Automox, JumpCloud, FleetDM, Mosyle, Datto RMM, Rippling, Manual (rules-only)
- **Tested providers:** NinjaOne, ManageEngine (cloud), JumpCloud, Manual
- **Webhook destinations:** Slack, Discord, raw JSON/SIEM (tested); Teams, PagerDuty, OpsGenie (untested)
- **Trust modes:** `any` (compliant in at least one provider) or `all` (compliant in every provider that recognizes it)
- **No database required;** all matching is done in-memory per cycle
- **Never sets** `isTrusted: false`

---

## Prerequisites
- Twingate API key with **Devices Read + Write** scopes
- Credentials for at least one MDM/EDR provider
- Docker (or Python environment for development)

---

## Usage / Step-by-Step

1. **Create `config.yaml`** with `twingate` and `providers` keys (minimum required):
   ```yaml
   twingate:
     tenant: acme
     api_key: ${TWINGATE_API_KEY}
   providers:
     - type: ninjaone
       enabled: true
       client_id: ${NINJAONE_CLIENT_ID}
       client_secret: ${NINJAONE_CLIENT_SECRET}
   ```

2. **Run with Docker:**
   ```bash
   docker run --rm \
     -v "$(pwd)/config.yaml:/app/config.yaml:ro" \
     -e TWINGATE_API_KEY=your-key \
     ghcr.io/twingate-solutions/twingate-mdm-connector:latest
   ```

3. **Optional:** Use Docker Compose with `restart: unless-stopped` and health check via `HEALTHZ_PORT`.

---

## Configuration Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `twingate.tenant` | string | — | Subdomain from `<tenant>.twingate.com` |
| `twingate.api_key` | string | — | Twingate API key |
| `trust.mode` | `any`\|`all` | `any` | Trust threshold across providers |
| `trust.max_days_since_checkin` | int\|`null` | `7` | Skip devices not seen within N days; `null` disables |
| `sync.interval_seconds` | int | `300` | Sync frequency |
| `sync.dry_run` | bool | `false` | Log only, no mutations |
| `logging.level` | string | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR` |

**Env vars:**
- `HEALTHZ_PORT` — enables HTTP liveness probe on specified port
- Any config value supports `${ENV_VAR}` interpolation; missing vars cause startup failure

---

## Gotchas
- Serial number matching is normalized to `strip().upper()` — mismatches due to case/whitespace are handled, but malformed serials will silently fail to match
- Provider errors skip that provider for the cycle; they do not abort the run or untrust devices
- `trust.mode: all` requires the device to appear in **every** configured provider —