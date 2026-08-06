---
source: https://help.twingate.com/articles/1422554451-connector-offline-too-many-open-files-in-logs
type: help
fetched: 2026-08-06
source_version: 63b94593c21e9840dabcdb854712c7b49669e7b36d6431586c4e4219ad93a68b
---

# Connector Offline—"too many open files" in Logs

## Summary
When a Twingate Connector's underlying Linux host hits the default `ulimit` of 1024 file descriptors, the Connector goes offline. Each active client tunnel consumes 8 file descriptors, capping default deployments at ~128 simultaneous active clients.

## Key Information
- Default Linux `ulimit` value: **1024** file descriptors
- Each client tunnel uses **8 file descriptors** (transports)
- Maximum active clients at default limit: **128**
- Threshold formula: `(active clients × 8) > ulimit value`

## Symptoms
- Connector stops sending heartbeat metrics
- Connector goes offline
- Log error:
```
[ERROR] [connector] Failed to submit analytics events: Unexpected error: error sending request for url (https://analytics.twingate.com/v1/track): error trying to connect: dns error: Too many open files (os error 24)
```

## Resolution

### Option 1: Increase ulimit on Host
```bash
ulimit -n 2048
```
Adjust the target value based on expected concurrent client load.

### Option 2: Add More Connectors
- Distribute client connections across multiple Connectors
- Provides load balancing to prevent any single Connector from hitting file descriptor limits

## Configuration Values
| Parameter | Default | Notes |
|-----------|---------|-------|
| `ulimit -n` (nofile) | 1024 | Increase on host as needed |
| Recommended minimum | 2048 | Per Twingate guidance |

## Gotchas
- **AWS ECS Fargate**: Cannot modify the `nofile` ulimit parameter on Fargate tasks. Fargate enforces its own defaults:
  - Soft limit: **1024**
  - Hard limit: **65535**
  - No workaround available for Fargate-hosted Connectors via host configuration
- `ulimit -n` set interactively is session-scoped; for persistence, configure via `/etc/security/limits.conf` or systemd unit file (not explicitly mentioned in docs but implied by "modify the allowance")

## Related Docs
- [AWS ECS Ulimit API Reference](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html)
- Twingate Connector deployment documentation