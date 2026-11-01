---
source: https://help.twingate.com/articles/4104282255-connector-offline-status-flapping-offline-online-or-goes-offline-some-time-after-restart
type: help
fetched: 2026-11-01
source_version: 27486fb7d56f059b414ba8c6963d242bbcd9d207331716e920f9df4d48e69df6
trust: official
---

# Connector Offline: Status Flapping or Goes Offline After Restart

## Summary
The Twingate Connector will go offline or flap if its system clock drifts more than 5 seconds from the Twingate Controller. This causes token verification failures (`Invalid token` / `token expired` errors) even when tokens are freshly issued. The fix is ensuring proper NTP/chrony clock synchronization on the host.

## Key Information
- **Drift threshold:** 5 seconds from Twingate Controller clock
- **Root cause:** System clock on Connector host is not staying synchronized
- **Affects:** Bare-metal, VM, and containerized Connector deployments
- **Container note:** Clock sync must be fixed on the **container host**, not inside the container

## Symptoms
- Email alerts for Connector flapping online/offline
- Connector goes offline days after restart (clock drifts gradually)
- Log errors at non-debug level:
  ```
  controller_t::operator(): failed to get an access token: Invalid token
  controller_t::operator(): failed to get SD: Invalid token, err code 1
  ```
- Log errors at debug level: `token verification failed: token expired`

## Troubleshooting Steps

1. **Check Time Offset in UI:** Admin Console → Connector Details → inspect **Time Offset** field. If ≥ 5s, clock drift is the cause.

2. **Enable debug logging** per [Twingate Connector Logs](https://help.twingate.com/articles/connector-logs) docs.

3. **Find the drift in logs:**
   - Locate a log line containing `verify_token: {"typ":"DAT"`
   - Extract the system timestamp (e.g., `Jun 26 21:39:49`) and the `iat` field value (e.g., `1656279597`)
   - Convert `iat` from Unix epoch to human-readable time
   - Compare: if difference > 5 seconds → clock drift confirmed

4. **Docker note:** Ensure container logging includes timestamps via `-t` / `--timestamps` flag, otherwise system timestamps will be absent from logs.

## Configuration Values
| Item | Value |
|------|-------|
| Max allowed clock drift | 5 seconds |
| Token field to inspect | `iat` (issued-at, Unix epoch) |

## Resolution

- **Install and run `chronyd`** alongside or instead of `ntpd` alone. Using only `ntpd` is insufficient in some environments.
- **For containerized Connectors:** Fix clock sync on the **container host** (not the container itself).
- **Cloud-managed hosts:** Contact the cloud provider's support to investigate host-level clock drift.

## Gotchas
- Clock drift can be intermittent/variable — monitor the **Time Offset** field over time, not just at a single point.
- `ntpd` alone may not correct significant drift; `chronyd` handles drift more aggressively.
- Container deployments inherit the host clock; no in-container fix is possible.

## Related Docs
- [Connector Metadata](https://help.twingate.com/articles/connector-metadata)
- [Twingate Connector Logs](https://help.twingate.com/articles/connector-logs)