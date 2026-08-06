---
source: https://help.twingate.com/articles/4104282255-connector-offline-status-flapping-offline-online-or-goes-offline-some-time-after-restart
type: help
fetched: 2026-08-06
source_version: 4d37287d72318eef6823a080a1e985621fc9923f651b38e67388eb87d2e2702d
---

# Connector Offline: Clock Drift Issue

## Summary
The Twingate Connector fails authentication when its system clock drifts more than 5 seconds from the Twingate Controller. This causes connectors to flap offline/online or go offline days after deployment. The root cause is improper NTP/clock synchronization on the host.

## Key Information
- **Clock drift threshold**: 5 seconds maximum allowed deviation from Twingate Controller
- Symptoms appear gradually—often days after restart, not immediately
- Affects both bare-metal installs and containerized deployments
- Container clock sync must be fixed on the **container host**, not the container itself

## Symptoms
- Email alerts for connector flapping offline/online
- Connector becomes unavailable several days after restart/deployment
- Log errors: `failed to get an access token: Invalid token` / `failed to get SD: Invalid token, err code 1`
- Debug logs show: `token verification failed: token expired`

## Troubleshooting Steps

1. **Check Time Offset in UI**: Navigate to Connector Details in Twingate Admin Console → check the **Time Offset** field
   - If ≥ 5 seconds → clock drift confirmed
   - Monitor over time; offset may be variable if clock is flapping

2. **Verify via logs** (requires debug-level logging enabled):
   - Enable debug logs per [Twingate Connector Logs](https://help.twingate.com/articles/connector-logs) docs
   - Find log line containing `verify_token: {"typ":"DAT"`
   - Extract: system timestamp (e.g., `Jun 26 21:39:49`) and `iat` value (e.g., `1656279597`)
   - Convert `iat` epoch to human-readable time
   - Compare system timestamp vs `iat` timestamp
   - Difference > 5 seconds = clock drift issue

3. **Docker note**: Ensure `-t` / `--timestamps` flag is used, otherwise log output won't include timestamps

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| `iat` (JWT claim) | Issued-at time from Controller token, in Unix epoch |
| Time Offset | Visible in Connector Details UI; threshold is 5s |

## Resolution

- **Bare-metal/VM**: Ensure hardware clock is synced
  - NTP (`ntpd`) alone may be insufficient
  - **Install and run `chronyd` alongside or instead of `ntpd`**
- **Containers**: Fix clock sync on the **container host**, not inside the container
- **Cloud-managed hosts**: Contact cloud provider support to investigate host-level clock drift

## Gotchas
- `ntpd` alone is sometimes insufficient—`chronyd` handles larger/faster drift corrections better
- Clock drift can be intermittent, making it hard to catch; monitor Time Offset over time
- Container clocks inherit from the host; fixing the container itself won't resolve the issue
- Tokens appear valid on issuance but fail verification seconds later due to local clock being behind

## Related Docs
- [Connector Metadata](https://help.twingate.com/articles/connector-metadata) — Time Offset field details
- [Twingate Connector Logs](https://help.twingate.com/articles/connector-logs) — Enabling debug logging