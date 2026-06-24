# How to Ingest Connector Logs into a SIEM

## Summary
Twingate Connectors log events in real-time via journald (systemd). This guide covers four methods to forward those logs to a SIEM: AWS S3, Syslog, Vector, and Datadog agent.

## Key Information
- Connector logs are written via **journald** (standard systemd, Linux only)
- journald has no built-in remote forwarding; requires additional tooling
- Real-time connection logs must be enabled on Connectors before using any method
- AWS S3 ingestion sends audit logs, network events, and DNS filtering logs on a **5-minute interval**

## Prerequisites
- Linux machine hosting Twingate Connector
- Real-time connection logs enabled on Connectors (required for all methods)
- Shell/root access to Connector host

## Methods

### 1. AWS S3 (Recommended)
- Twingate natively pushes logs to an S3 bucket every 5 minutes
- Log types: audit logs, network events, DNS filtering logs
- Route from S3 to your SIEM using standard S3 integration

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
3. Create `vector.toml` with Sources and Transforms (see Vector docs)
4. Add appropriate Sink for your SIEM

**Supported Vector Sinks include:** AWS CloudWatch, AWS S3, Datadog, Elasticsearch, GCP Cloud Monitoring, Honeycomb, New Relic, Prometheus, Splunk

### 4. Datadog Agent
1. Enable real-time connection logs on Connectors
2. Install and configure Datadog agent per Datadog's official documentation
3. Feeds Twingate analytics dashboard in Datadog

## Configuration Values
| Method | Config File | Key Setting |
|--------|-------------|-------------|
| Syslog | `/etc/systemd/journald.conf` | `ForwardToSyslog=yes` |
| Syslog | `/etc/syslog.conf` | Central server forwarding rules |
| Vector | `vector.toml` (custom path) | Sources, Transforms, Sinks |

## Gotchas
- journald forwarding must be explicitly uncommented — it's disabled by default (`#ForwardToSyslog=yes`)
- AWS S3 method is not real-time — logs batch every 5 minutes
- Real-time connection logs are a **prerequisite** for Syslog, Vector, and Datadog methods; skipping this step means no connection data is logged

## Related Docs
- Twingate real-time connection logs (enable on Connectors)
- Twingate Vector configuration documentation
- Twingate audit logs / network events / DNS filtering logs
- Datadog official agent documentation
- AWS S3 audit log integration