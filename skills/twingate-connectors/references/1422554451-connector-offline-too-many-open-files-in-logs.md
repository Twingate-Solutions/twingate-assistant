---
source: https://help.twingate.com/articles/1422554451-connector-offline-too-many-open-files-in-logs
type: help
fetched: 2026-09-06
source_version: e5f228d18be376196af1b5a1bb53b7dda1c99c5c072d1da6cb3d650da37ff6a7
---

# Connector Offline—"Too Many Open Files" in Logs

## Summary
When a Twingate Connector's underlying Linux host hits the default `ulimit` of 1024 file descriptors, the Connector goes offline. Each connected client consumes 8 file descriptors, limiting the default configuration to ~128 active clients.

## Key Information
- Default Linux `ulimit` value: **1024** file descriptors
- Each client tunnel consumes **8 file descriptors** (8 transports)
- Maximum active clients at default limit: **~128**
- Limit is reached when: `(users connected) × (resources accessed)` exceeds ulimit

## Symptoms
- Connector fails to send `/heartbeat` metrics
- Connector goes offline with log errors:
  ```
  [ERROR] [connector] Failed to submit analytics events: Unexpected error: error sending request for url (https://analytics.twingate.com/v1/track): error trying to connect: dns error: Too many open files (os error 24)
  ```

## Resolution

### Option 1: Increase ulimit on Host
```bash
ulimit -n 2048
```
Adjust the target value based on expected concurrent users and resource connections.

### Option 2: Add More Connectors
Deploy additional Connectors to distribute load via load balancing. This is the preferred long-term solution if multiple Connectors are hitting the limit simultaneously.

## Configuration Values
| Parameter | Default | Notes |
|-----------|---------|-------|
| `ulimit -n` (nofile) | 1024 | Soft limit on Linux hosts |
| Recommended minimum | 2048 | Adjust based on user load |

## Gotchas
- **AWS ECS Fargate**: Cannot modify the `nofile` ulimit parameter on Fargate tasks. AWS Fargate hardcodes defaults:
  - Soft limit: **1024**
  - Hard limit: **65535**
  - Fargate tasks are unaffected by host-level ulimit changes per [AWS ECS API docs](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html)
- Changes made with `ulimit -n` may not persist across reboots—use `/etc/security/limits.conf` or systemd unit overrides for permanent changes (not explicitly documented here, but implied)

## Related Docs
- [AWS ECS Ulimit API Reference](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html)
- Twingate Connector deployment documentation