---
source: https://help.twingate.com/articles/4104282255-connector-offline-status-flapping-offline-online-or-goes-offline-some-time-after-restart
type: help
fetched: 2026-10-04
source_version: 4c84e4a7c8b4f1186d9491682f0d24a1916eb31b3f1c8b5aa56e0165932f08c4
trust: official
---

# Connector Offline: Status Flapping or Goes Offline After Restart

## Summary
The Twingate Connector requires system clock to be within 5 seconds of the Twingate Controller's clock. Clock drift beyond this threshold causes token verification failures, resulting in the Connector going offline or flapping online/offline. This often surfaces days after a restart as drift accumulates.

## Key Information
- Clock drift tolerance: **±5 seconds** from Twingate Controller
- Root cause: NTP sync absent or insufficient (ntpd alone may not correct drift fast enough)
- Affects bare-metal, VM, and containerized deployments
- Container issues must be resolved on the **container host**, not the container itself

## Symptoms
- Email alerts for Connector flapping offline/online
- Connector goes unavailable days after restart/deployment
- Log errors: `failed to get an access token: Invalid token` / `token verification failed: token expired`

## Troubleshooting Steps

1. **Check Time Offset in Admin Console**
   - Navigate to Connector Details → inspect the **Time Offset** field
   - If ≥ 5 seconds, clock drift is the issue
   - Monitor over time to detect variable/flapping drift

2. **Confirm via logs**
   - Enable debug-level logging per [Twingate Connector Logs docs](https://help.twingate.com)
   - Find a line containing `verify_token: {"typ":"DAT"`
   - Extract the system timestamp (e.g., `Jun 26 21:39:49`) and the `iat` field value (e.g., `1656279597`)
   - Convert `iat` epoch to human-readable time
   - Compare: if difference > 5 seconds, clock drift is confirmed

3. **Example calculation**
   - System timestamp: `Jun 26 21:39:49`
   - `iat` decoded: `Jun 26 21:39:57`
   - Difference: **8 seconds** → drift confirmed

## Resolution

| Environment | Action |
|---|---|
| Bare-metal / VM | Install and run `chronyd` alongside or instead of `ntpd` |
| Container | Fix clock sync on the **container host** |
| Cloud-managed host | Contact cloud provider support to address host clock drift |

## Configuration Values
- No env vars or CLI flags specific to this issue
- Docker log timestamps: use `-t` / `--timestamps` flag to include system timestamps in container logs

## Gotchas
- `ntpd` alone may not correct drift sufficiently—`chronyd` is recommended in tandem
- Container clock is inherited from host; fixing inside the container has no effect
- Time Offset may be variable/intermittent—monitor over time rather than a single check
- Log lines without timestamps make diagnosis difficult; ensure timestamps are enabled in Docker

## Related Docs
- [Connector Metadata](https://help.twingate.com) (Time Offset field details)
- [Twingate Connector Logs](https://help.twingate.com) (enabling debug logging)