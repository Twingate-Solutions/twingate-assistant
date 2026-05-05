# How to Ingest Connector Logs into a SIEM

## Summary
Twingate Connectors log all events in real time via journald (systemd). Multiple methods exist to forward these logs to external SIEMs or log aggregation platforms. AWS S3 is the simplest path; syslog, Vector, and Datadog agent are alternatives.

## Key Information
- Logs are written via **journald** (systemd), no built-in remote forwarding
- Four supported ingestion methods: AWS S3, Syslog, Vector, Datadog Agent
- AWS S3 receives audit logs, network events, and DNS filtering logs every **5 minutes**
- Vector supports many sinks: CloudWatch, S3, Datadog, Elasticsearch, GCP, Splunk, New Relic, Honeycomb, Prometheus, and more

## Prerequisites
- Real-time connection logs must be **enabled on Connectors** (required for all methods except AWS S3)
- Linux host with systemd/journald running the Connector

## Step-by-Step by Method

### AWS S3
1. Configure Twingate to send logs to your S3 bucket (via Twingate admin settings)
2. Forward from S3 to your SIEM

### Syslog
1. Enable real-time connection logs on Connectors
2. Edit `/etc/systemd/journald.conf`
3. Uncomment `#ForwardToSyslog=yes` → `ForwardToSyslog=yes`
4. Edit `/etc/syslog.conf` to forward to central syslog server
5. Restart the Connector

### Vector
1. Enable real-time connection logs on Connectors
2. Install Vector on the Connector host
3. Create `vector.toml` with Sources, Transforms, and Sink config
4. Add SIEM-specific Sink configuration

### Datadog Agent
1. Enable real-time connection logs on Connectors
2. Install and configure Datadog agent per Datadog's official docs
3. Supports Twingate analytics dashboard integration

## Configuration Values
| Method | Config File | Key Setting |
|--------|-------------|-------------|
| Syslog | `/etc/systemd/journald.conf` | `ForwardToSyslog=yes` |
| Syslog | `/etc/syslog.conf` | Remote server forwarding rules |
| Vector | `vector.toml` (custom path) | Sources, Transforms, Sinks |

## Gotchas
- journald has **no native remote forwarding** — requires one of the above methods
- AWS S3 delivery is batched at **5-minute intervals**, not real-time
- Real-time connection logs must be explicitly enabled on each Connector before syslog/Vector/Datadog will capture meaningful data

## Related Docs
- Enable real-time connection logs (Connector settings)
- AWS S3 audit log integration
- Network events and DNS filtering logs
- Vector configuration documentation (Twingate-specific)
- Datadog analytics dashboard for Twingate