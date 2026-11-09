---
source: https://help.twingate.com/articles/4104282255-connector-offline-status-flapping-offline-online-or-goes-offline-some-time-after-restart
type: help
fetched: 2026-11-08
source_version: 0bef118743f78b56de895055883a09bd606cbbc659d841ad67267ae734ab050b
trust: official
---

# Connector Offline: Status Flapping or Goes Offline After Restart

## Summary
The Twingate Connector goes offline or flaps online/offline when system clock drift exceeds 5 seconds from the Twingate Controller. Token verification fails because issued tokens appear expired from the Connector's perspective. Fix requires ensuring NTP/chrony clock synchronization on the host.

## Key Information
- **Drift threshold:** 5 seconds — any clock offset ≥5s causes token verification failures
- **Failure mode:** Connector may work initially post-restart, then fail after drift accumulates over days
- **Affects:** Both bare-metal/VM deployments and containerized Connectors (fix applied to container host, not container itself)

## Symptoms
- Email alerts for Connector flapping offline/online
- Connector becomes unavailable days after restart/deployment
- Log errors: `failed to get an access token: Invalid token` or `failed to fetch ANT: Invalid token`
- Debug logs show: `token verification failed: token expired`

## Troubleshooting Steps

1. **Check Time Offset in UI:** Navigate to Connector Details → check the **Time Offset** field. If ≥5s, clock drift is the cause.

2. **Confirm via logs** (enable debug logging per [Twingate Connector Logs](https://help.twingate.com/)):
   - Find log line containing `verify_token: {"typ":"DAT"`
   - Extract the system timestamp (e.g., `Jun 26 21:39:49`) and the `iat` (issued-at) field value (e.g., `1656279597`)
   - Convert `iat` from epoch to human-readable (e.g., via `date -d @1656279597`)
   - Compare timestamps — difference >5s confirms clock drift

3. **Monitor variability:** Time Offset may fluctuate; watch over time to confirm it's not a one-time spike.

> **Docker note:** If container logs lack timestamps, add `-t` / `--timestamps` flag to your Docker logging arguments.

## Configuration Values
| Field | Location | Notes |
|---|---|---|
| `Time Offset` | Admin Console → Connector Details | Displays current drift vs. Controller |
| `iat` | Debug log token payload | Epoch timestamp when Controller issued the token |

## Resolution

- **Install and run `chronyd`** alongside or instead of `ntpd` alone — `ntpd` may not correct drift reliably in all environments
- **For containerized Connectors:** Apply clock sync fix on the **container host**, not inside the container
- **For cloud-managed hosts:** Contact the cloud provider's support team to investigate and resolve host-level clock drift

## Gotchas
- `ntpd` alone is insufficient in some environments; `chronyd` is recommended in tandem
- Container deployments inherit the host clock — fixing the container itself has no effect
- Drift can be intermittent/variable, so a single Time Offset check may not capture the problem; monitor over time

## Related Docs
- [Connector Metadata](https://help.twingate.com/) — details on Time Offset field
- [Twingate Connector Logs](https://help.twingate.com/) — enabling debug logging