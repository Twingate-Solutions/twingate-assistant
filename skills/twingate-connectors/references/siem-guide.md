# How to Ingest Connector Logs into a SIEM

## Summary
Twingate Connectors log events in real time via `journald` (systemd). Since journald lacks built-in remote forwarding, several methods exist to send logs to SIEMs: AWS S3, Syslog, Vector, or Datadog agent.

## Key Information
- Logs are written via `journald` on Linux systems running the Connector
- AWS S3 ingestion delivers audit logs, network events, and DNS filtering logs every **5 minutes**
- Real-time connection logs must be explicitly enabled on Connectors before using Syslog, Vector, or Datadog methods

## Prerequisites
- Linux system with systemd/journald
- Real-time connection logs enabled on Connectors (required for Syslog, Vector, Datadog)
- Connector already installed and running

## Methods

### AWS S3 (Recommended - Easiest)
- Twingate sends logs directly to your S3 bucket
- Supports: audit logs, network events, DNS filtering logs
- Forward from S3 to your SIEM

### Syslog
1. Enable real-time connection logs on Connectors
2. Edit `/etc/systemd/journald.conf`
3. Uncomment `#ForwardToSyslog=yes` → `ForwardToSyslog=yes`
4. Edit `/etc/syslog.conf` to forward to central syslog server
5. Restart the Connector

### Vector
1. Enable real-time connection logs on Connectors
2. Install Vector on the Connector host machine
3. Create `vector.toml` with Sources and Transforms (per Twingate docs)
4. Add Sink configuration for your SIEM

**Supported Sinks:** AWS CloudWatch, AWS S3, Datadog, Elasticsearch, GCP Cloud Monitoring, Honeycomb, New Relic, Prometheus, Splunk, and more

### Datadog Agent
1. Enable real-time connection logs on Connectors
2. Install/configure Datadog agent per Datadog's official documentation
3. Enables the Twingate analytics dashboard in Datadog

## Configuration Values
| File | Key Setting |
|------|-------------|
| `/etc/systemd/journald.conf` | `ForwardToSyslog=yes` |
| `/etc/syslog.conf` | Central syslog server destination |
| `vector.toml` | Sources, Transforms, Sinks |

## Gotchas
- Real-time connection logs are **not enabled by default** — must be configured before Syslog/Vector/Datadog methods will capture connection events
- AWS S3 method has a 5-minute delivery delay; not truly real-time
- journald has no native remote forwarding — all methods require an additional agent or service

## Related Docs
- Twingate real-time connection logs (Connector configuration)
- Twingate audit logs documentation
- DNS filtering logs documentation
- Vector configuration documentation (Twingate-specific)
- Datadog official agent documentation