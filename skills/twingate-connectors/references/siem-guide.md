# How to Ingest Connector Logs into a SIEM

## Summary
Twingate Connectors log events in real time via `journald` (systemd). Since journald lacks built-in remote forwarding, several methods exist to route logs to SIEMs: AWS S3, Syslog, Vector, or the Datadog agent.

## Key Information
- Logs are written via `journald` on Linux systems running Connectors
- Four supported ingestion methods: AWS S3, Syslog, Vector, Datadog agent
- AWS S3 ingestion includes audit logs, network events, and DNS filtering logs pushed every 5 minutes
- Real-time connection logs must be explicitly enabled on Connectors before using Syslog, Vector, or Datadog methods

## Prerequisites
- Linux machine running Twingate Connector
- Real-time connection logs enabled on Connectors (required for Syslog, Vector, Datadog)
- AWS S3 bucket (for S3 method)
- systemd/journald available (standard on Linux)

## Step-by-Step

### Syslog
1. Enable real-time connection logs on Connectors
2. Edit `/etc/systemd/journald.conf`
3. Uncomment `#ForwardToSyslog=yes` → `ForwardToSyslog=yes`
4. Edit `/etc/syslog.conf` to forward to central syslog server
5. Restart the Connector

### Vector
1. Enable real-time connection logs on Connectors
2. Install Vector on the Connector host machine
3. Create `vector.toml` with Sources and Transforms configured
4. Add appropriate Sink configuration for target SIEM
5. Run Vector

### Datadog
1. Enable real-time connection logs on Connectors
2. Install and configure the Datadog agent per Datadog's official documentation

### AWS S3
- Configure via Twingate settings to push to your S3 bucket; data forwards to SIEM from there

## Configuration Values

| Method | Config File | Key Setting |
|--------|-------------|-------------|
| Syslog | `/etc/systemd/journald.conf` | `ForwardToSyslog=yes` |
| Syslog | `/etc/syslog.conf` | Remote server destination |
| Vector | `vector.toml` | Sources, Transforms, Sinks |

## Supported Vector Sinks
AWS CloudWatch, AWS S3, Datadog, Elasticsearch, GCP Cloud Monitoring, Honeycomb, New Relic, Prometheus, Splunk, and others.

## Gotchas
- Real-time connection logs are **not enabled by default** — must be turned on before Syslog/Vector/Datadog methods will capture Connector activity
- AWS S3 has a 5-minute push interval; not truly real-time
- journald has no native remote forwarding — an intermediary (syslog daemon, Vector, or agent) is always required

## Related Docs
- Enable real-time connection logs (Connector settings)
- Twingate audit logs documentation
- AWS S3 log integration
- DNS filtering logs
- Vector configuration documentation
- Datadog analytics dashboard integration