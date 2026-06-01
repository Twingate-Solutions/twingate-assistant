# How to Ingest Connector Logs into a SIEM

## Summary
Twingate Connectors log events in real time via `journald` (systemd). Several methods exist to forward these logs to a SIEM: AWS S3, Syslog forwarding, Vector agent, or Datadog agent.

## Key Information
- Logs are written via `journald` on Linux systems hosting Connectors
- AWS S3 integration pushes audit logs, network events, and DNS filtering logs every 5 minutes
- Four supported forwarding methods: AWS S3, Syslog, Vector, Datadog

## Prerequisites
- Real-time connection logs must be enabled on Connectors (required for Syslog, Vector, and Datadog methods)
- Linux system with systemd/journald
- Shell access to the Connector host machine

## Step-by-Step

### Syslog
1. Enable real-time connection logs on Connectors
2. Edit `/etc/systemd/journald.conf`
3. Uncomment `#ForwardToSyslog=yes` → `ForwardToSyslog=yes`
4. Edit `/etc/syslog.conf` to forward to central syslog server
5. Restart the Connector

### Vector
1. Enable real-time connection logs on Connectors
2. Install Vector on the Connector host
3. Create `vector.toml` with Sources, Transforms, and Sink configuration
4. Configure the appropriate Sink for your SIEM

### Datadog
1. Enable real-time connection logs on Connectors
2. Install and configure Datadog agent per [Datadog official docs](https://docs.datadoghq.com/)

### AWS S3
- Configure via Twingate admin panel; no host-level setup required

## Configuration Values

| Method | Config File | Key Setting |
|--------|-------------|-------------|
| Syslog | `/etc/systemd/journald.conf` | `ForwardToSyslog=yes` |
| Syslog destination | `/etc/syslog.conf` | Central server address |
| Vector | `vector.toml` | Sources, Transforms, Sinks |

## Vector Supported Sinks
AWS CloudWatch, AWS S3, Datadog, Elasticsearch, GCP Cloud Monitoring, Honeycomb, New Relic, Prometheus, Splunk, and others.

## Gotchas
- Real-time connection logs must be explicitly enabled on each Connector before Syslog/Vector/Datadog will capture meaningful data
- AWS S3 has a 5-minute delivery delay — not suitable for real-time alerting
- `journald` does not natively forward to remote systems; an intermediary (syslog/Vector/Datadog) is required
- Datadog integration also powers the Twingate analytics dashboard

## Related Docs
- [Enable Real-Time Connection Logs](https://www.twingate.com/docs) (Connector settings)
- [Audit Logs](https://www.twingate.com/docs/audit-log)
- [Network Events](https://www.twingate.com/docs/network-events)
- [DNS Filtering Logs](https://www.twingate.com/docs/dns-filtering)
- [Vector Configuration Guide](https://www.twingate.com/docs) (Twingate-specific Vector docs)
- [AWS S3 Log Integration](https://www.twingate.com/docs)