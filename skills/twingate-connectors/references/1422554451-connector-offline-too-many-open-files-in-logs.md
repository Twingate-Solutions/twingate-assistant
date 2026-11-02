---
source: https://help.twingate.com/articles/1422554451-connector-offline-too-many-open-files-in-logs
type: help
fetched: 2026-11-01
source_version: c6b17c8756a6beed9c3757ee0b4e3e70f4ef5d5f5f06ae8562ec5e465ffe89c1
trust: official
---

# Connector Offline—"too many open files" in Logs

## Summary
When a Twingate Connector's host exceeds the default Linux `ulimit` of 1024 file descriptors, the Connector goes offline. Each Client tunnel consumes 8 file descriptors, capping active clients at ~128 under default settings.

## Key Information
- Default Linux `ulimit` value: **1024** file descriptors
- Each client tunnel uses **8 file descriptors** (8 transports)
- Maximum active clients at default limit: **~128**
- Affects open sockets to Twingate Resources
- Twingate Component: **Connector**

## Symptoms
- Connector fails to send `/heartbeat` metrics
- Connector goes offline with log errors:
```
[ERROR] [connector] Failed to submit analytics events: Unexpected error: error sending request for url 
(https://analytics.twingate.com/v1/track): error trying to connect: dns error: Too many open files (os error 24)
```

## Resolution

### Option 1: Increase ulimit on the Host
Increase the file descriptor limit on the underlying host:
```bash
ulimit -n 2048
```
Scale the value based on expected concurrent client connections (clients × 8 = minimum file descriptors needed).

### Option 2: Add More Connectors
Deploy additional Connectors to distribute load. Twingate load-balances across multiple Connectors, reducing per-Connector connection count.

## Configuration Values
| Parameter | Default | Notes |
|-----------|---------|-------|
| `nofile` (ulimit) | 1024 | Linux default; increase as needed |
| File descriptors per client | 8 | Fixed per tunnel |
| Max clients at default limit | ~128 | Calculated: 1024 ÷ 8 |

## Gotchas
- **AWS ECS Fargate**: You **cannot** modify the `nofile` ulimit parameter on Fargate-hosted tasks. AWS Fargate overrides this value with soft limit **1024** and hard limit **65535** — the hard limit effectively becomes your ceiling, and the soft limit cannot be raised via task definition per [AWS documentation](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html).
- A `ulimit` change via CLI is session-scoped; persist it in `/etc/security/limits.conf` or via systemd `LimitNOFILE` for permanent effect (not documented on this page — verify against your Linux distro's configuration).
- If multiple Connectors are all hitting the limit simultaneously, adding Connectors is preferable to simply raising the limit on each.

## Related Docs
- [AWS ECS Ulimit API Reference](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html)
- Twingate Connector deployment documentation