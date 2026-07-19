# How to Ingest Connector Logs into a SIEM

## Summary
Twingate Connectors log events in real time via journald (systemd). This guide covers four methods to forward those logs to a SIEM: AWS S3, Syslog, Vector, and Datadog agent.

## Key Information
- Connector logs use **journald** (Linux/systemd standard)
- journald has no built-in remote forwarding; requires configuration
- Four supported ingestion methods: AWS S3, Syslog, Vector, Datadog
- AWS S3 method delivers audit logs, network events, and DNS filtering logs every **5 minutes**

## Prerequisites
- Real-time connection logs must be **enabled on Connectors** (required for Syslog, Vector, and Datadog methods)
- Linux machine hosting Twingate Connector
- Shell access to the Connector host

## Methods & Steps

### AWS S3 (Easiest)
Twingate natively pushes logs to an S3 bucket every 5 minutes. Configure in Twingate settings, then route from S3 to your SIEM.

### Syslog
1. Enable real-time connection logs on Connectors
2. Edit `/etc/systemd/journald.conf`
3. Uncomment `#ForwardToSyslog=yes` → `ForwardToSyslog=yes`
4. Save file
5. Edit `/etc/syslog.conf` to forward to central syslog server
6. Restart the Connector

### Vector
1. Enable real-time connection logs on Connectors
2. Install Vector on the Connector host
3. Create `vector.toml` with Sources, Transforms, and Sink config
4. Supported Sinks: AWS CloudWatch, AWS S3, Datadog, Elasticsearch, GCP Cloud Monitoring, Honeycomb, New Relic, Prometheus, Splunk, and more

### Datadog
1. Enable real-time connection logs on Connectors
2. Install and configure Datadog agent per official Datadog documentation
3. Supports Twingate analytics dashboard integration

## Configuration Values
| Method | Config File |
|--------|------------|
| Syslog | `/etc/systemd/journald.conf` |
| Syslog forwarding | `/etc/syslog.conf` |
| Vector | `vector.toml` (custom path) |

**journald key setting:**
```
ForwardToSyslog=yes
```

## Gotchas
- journald forwards to syslog must be explicitly uncommented (disabled by default)
- AWS S3 is batch-based (5-minute intervals), not real-time streaming
- Real-time connection logs must be enabled separately before configuring any agent-based method (Syslog, Vector, Datadog)

## Related Docs
- Twingate real-time connection logs (Connector configuration)
- Twingate audit logs / network events / DNS filtering logs
- Vector documentation (Sources, Transforms, Sinks)
- Datadog official agent documentation
- Twingate analytics dashboard (Datadog integration)