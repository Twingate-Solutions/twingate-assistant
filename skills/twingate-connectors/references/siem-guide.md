# How to Ingest Connector Logs into a SIEM

## Summary
Twingate Connectors log events in real-time via `journald` (systemd). This page covers four methods to forward those logs to a SIEM: AWS S3, Syslog, Vector, and Datadog agent.

## Key Information
- Connector logs are written via `journald` on Linux/systemd
- `journald` has no built-in remote forwarding — requires additional tooling
- Real-time connection logs must be enabled on Connectors before using any method
- Four supported ingestion paths: AWS S3, Syslog, Vector, Datadog

## Prerequisites
- Linux host running Twingate Connector
- Real-time connection logs enabled on Connectors (required for all methods)
- Appropriate SIEM/destination access credentials

## Methods

### 1. AWS S3
- Twingate natively sends audit logs, network events, and DNS filtering logs to S3
- Delivery cadence: every 5 minutes
- Forward from S3 to SIEM as secondary step

### 2. Syslog
1. Enable real-time connection logs on Connectors
2. Edit `/etc/systemd/journald.conf`
3. Uncomment `#ForwardToSyslog=yes` → `ForwardToSyslog=yes`
4. Save file
5. Edit `/etc/syslog.conf` to forward to central syslog server
6. Restart the Connector

### 3. Vector
1. Enable real-time connection logs on Connectors
2. Install Vector on the Connector host
3. Create `vector.toml` with Sources and Transforms
4. Add Sink configuration for target SIEM
- Supported Sinks: AWS CloudWatch, AWS S3, Datadog, Elasticsearch, GCP Cloud Monitoring, Honeycomb, New Relic, Prometheus, Splunk, and more

### 4. Datadog (via journald)
1. Enable real-time connection logs on Connectors
2. Install and configure Datadog agent per Datadog's official documentation
- Supports Twingate analytics dashboard integration

## Configuration Values
| Method | File/Config |
|--------|-------------|
| Syslog | `/etc/systemd/journald.conf` |
| Syslog forwarding | `/etc/syslog.conf` |
| Vector | `vector.toml` (custom path) |

**Key journald setting:**
```
ForwardToSyslog=yes
```

## Gotchas
- Real-time connection logs must be explicitly enabled — not on by default
- `journald` forwards to syslog but syslog still needs separate configuration to route to remote server
- Vector must be installed on the same machine as the Connector

## Related Docs
- Twingate real-time connection logs (Connector configuration)
- AWS S3 audit log integration
- Vector configuration documentation (Twingate-specific)
- Datadog agent official documentation
- DNS filtering logs
- Network events logs