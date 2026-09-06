---
source: https://help.twingate.com/articles/4104282255-connector-offline-status-flapping-offline-online-or-goes-offline-some-time-after-restart
type: help
fetched: 2026-09-06
source_version: 9df691f73b5eecca70b875f5a25c895e7de3eb3a5b3de692b7336d679fe57e54
---

# Connector Offline: Clock Drift / Status Flapping

## Summary
Twingate Connector goes offline, flaps online/offline, or fails with "Invalid token" errors when system clock drifts more than 5 seconds from the Twingate Controller. This can manifest immediately or days after a restart as drift accumulates.

## Key Information
- **Clock drift threshold**: 5 seconds from Twingate Controller
- Affects containers and bare-metal deployments equally
- Container clock issues must be fixed at the **host level**, not inside the container
- Cloud-managed hosts require engaging the cloud provider's support

## Symptoms
- Email alerts for Connector flapping offline/online
- Connector goes offline days after restart or container deployment
- Log errors: `failed to get an access token: Invalid token` / `failed to get SD: Invalid token`
- Debug logs show: `token verification failed: token expired`

## Troubleshooting Steps

1. **Check Time Offset in Admin Console**: Navigate to Connector Details → check "Time Offset" field. If ≥ 5s, clock drift is the cause.

2. **Verify via logs** (requires debug-level logging enabled):
   - Find log line containing `verify_token: {"typ":"DAT"`
   - Extract system timestamp (e.g., `Jun 26 21:39:49`) and `iat` field value (e.g., `1656279597`)
   - Convert `iat` epoch to human-readable time
   - Compare: if difference > 5 seconds → clock drift confirmed

3. **Check for variable drift**: Monitor Time Offset over time to determine if drift is intermittent vs. consistent.

## Configuration Notes
- Enable debug logs per [Twingate Connector Logs](https://help.twingate.com/articles/connector-logs) documentation
- Docker users: ensure `-t` / `--timestamps` flag is set or log lines won't include timestamps

## Resolution

| Scenario | Fix |
|----------|-----|
| Bare-metal / VM | Ensure NTP is synced; install and run `chronyd` alongside `ntpd` |
| Container | Fix clock sync on the **container host** |
| Cloud-managed host | Contact cloud provider support to resolve host clock drift |

## Gotchas
- `ntpd` alone may be insufficient—running `chronyd` in tandem is recommended
- Clock drift can be intermittent (flapping), making it harder to diagnose; monitor Time Offset over time
- Tokens expire based on `iat` (issued-at) time from Controller; if Connector clock is behind, token appears expired before it actually is

## Related Docs
- [Connector Metadata](https://help.twingate.com/articles/connector-metadata)
- [Twingate Connector Logs](https://help.twingate.com/articles/connector-logs)