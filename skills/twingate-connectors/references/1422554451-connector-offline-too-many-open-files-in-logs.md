---
source: https://help.twingate.com/articles/1422554451-connector-offline-too-many-open-files-in-logs
type: help
fetched: 2026-10-04
source_version: c61f9667f7f7311c917b9166c4a977c12395f615d5a3abe37aeb3c7c738a3e5e
trust: official
---

# Connector Offline—"too many open files" in Logs

## Summary
When a Twingate Connector's underlying Linux host hits its `ulimit` file descriptor limit (default 1024), the Connector goes offline. Each connected Client consumes 8 file descriptors, capping support at ~128 active clients with default settings.

## Key Information
- Default Linux `ulimit` value: **1024** file descriptors
- Each Client tunnel uses **8 file descriptors** (8 transports)
- Max active clients at default limit: **~128**
- Limit applies to open sockets to Twingate Resources
- AWS ECS Fargate has special behavior (see Gotchas)

## Symptoms
- Connector stops sending `/heartbeat` metrics
- Connector goes offline with log entries containing:
```
[ERROR] [connector] Failed to submit analytics events: Unexpected error: error sending request for url (https://analytics.twingate.com/v1/track): error trying to connect: dns error: Too many open files (os error 24)
```

## Resolution

### Option 1: Increase ulimit on the Host
Increase the file descriptor limit on the Connector's underlying host:
```bash
ulimit -n 2048
```
- Adjust the target value based on expected concurrent client load
- Formula: `(max_clients × 8) + headroom`

### Option 2: Add More Connectors
- Add additional Connectors to the Remote Network to distribute load
- Twingate load balances across multiple Connectors automatically
- Recommended if all existing Connectors are hitting the limit simultaneously

## Configuration Values
| Parameter | Default | Notes |
|-----------|---------|-------|
| `ulimit -n` (nofile) | 1024 | File descriptors per process |
| File descriptors per client | 8 | Fixed per Twingate architecture |
| Max clients at default | ~128 | Calculate: `floor(1024 / 8)` |

## Gotchas
- **AWS ECS Fargate**: Cannot modify the `nofile` `ulimit` parameter on the underlying host. Fargate enforces:
  - Soft limit: **1024** (cannot override)
  - Hard limit: **65535**
  - See [AWS ECS Ulimit API docs](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html)
- `ulimit -n` changes may not persist across reboots—use `/etc/security/limits.conf` or systemd unit `LimitNOFILE` for permanent changes (not covered in this article)
- Increasing `ulimit` on one Connector doesn't help if multiple Connectors are all saturated

## Related Docs
- [AWS ECS Fargate Ulimit API Reference](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html)
- Twingate Connector deployment documentation