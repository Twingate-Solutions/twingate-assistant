---
source: https://help.twingate.com/articles/1422554451-connector-offline-too-many-open-files-in-logs
type: help
fetched: 2026-11-08
source_version: 857d6fbdcb04e0fbde36e06f5d4cdefae20a984977ccb0af5b69701b38853380
trust: official
---

# Connector Offline—"too many open files" in Logs

## Summary
When a Twingate Connector's underlying Linux host hits the default `ulimit` of 1024 file descriptors, the Connector goes offline. Each connected client consumes 8 file descriptors, capping default deployments at ~128 active clients.

## Key Information
- Default Linux `ulimit` value: **1024** file descriptors
- Each client tunnel uses **8 file descriptors** (8 transports)
- Max active clients at default limit: **~128**
- File descriptors include open sockets to Twingate Resources

## Symptoms
- Connector fails to send `/heartbeat` metrics
- Connector goes offline with log errors:
```
[ERROR] [connector] Failed to submit analytics events: Unexpected error: error sending request for url (https://analytics.twingate.com/v1/track): error trying to connect: dns error: Too many open files (os error 24)
```

## Resolution

### Option 1: Increase `ulimit` on Host
```bash
ulimit -n 2048
```
Adjust the target value based on expected concurrent client connections.

### Option 2: Add More Connectors
Deploy additional Connectors to distribute load. If multiple existing Connectors are all hitting the limit, scaling out is required alongside increasing `ulimit`.

## Configuration Values
| Parameter | Default | Notes |
|-----------|---------|-------|
| `ulimit -n` (nofile) | 1024 | Increase on host to support more clients |
| Clients per Connector (default) | ~128 max | Based on 8 FDs per client |

## Gotchas
- **AWS ECS Fargate**: You **cannot** modify the `nofile` ulimit parameter on Fargate tasks. AWS Fargate hardcodes soft limit = **1024**, hard limit = **65535**. The hard limit effectively means Fargate tasks are not constrained the same way, but the soft limit applies unless overridden at the task definition level (which Fargate does not permit for `nofile`).
- Changes to `ulimit` via the command above are session-scoped. For persistence, configure via `/etc/security/limits.conf` or the Docker/systemd service unit as appropriate.
- Ensure the new limit accounts for headroom; don't set it exactly at expected peak usage.

## Related Docs
- [AWS ECS Ulimit API Reference](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html)
- Twingate Connector deployment documentation