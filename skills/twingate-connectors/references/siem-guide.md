# How to Ingest Connector Logs into a SIEM

## Summary
Twingate Connectors log events in real time via `journald` (systemd). Several methods exist to forward these logs to a SIEM: AWS S3, Syslog, Vector, or Datadog agent.

## Key Information
- Logs are written via `journald` on Linux systems
- Real-time connection logs must be explicitly enabled on Connectors before using any method
- AWS S3 ingestion supports audit logs, network events, and DNS filtering logs (5-minute intervals)

## Prerequisites
- Linux system with systemd/journald
- Real-time connection logs enabled on Connectors (required for Syslog, Vector, Datadog methods)

## Methods

### AWS S3
- Twingate natively sends logs to an S3 bucket every 5 minutes
- Log types: audit logs, network events, DNS filtering logs
- Forward from S3 to SIEM as a secondary step

### Syslog
1. Enable real-time connection logs on Connectors
2. Edit `/etc/systemd/journald.conf`
3. Uncomment `#ForwardToSyslog=yes` → `ForwardToSyslog=yes`
4. Edit `/etc/syslog.conf` to forward to central syslog server
5. Restart the Connector

### Vector
1. Enable real-time connection logs on Connectors
2. Install Vector on the Connector host machine
3. Create `vector.toml` with Sources, Transforms, and Sink configuration
4. Supported sinks: AWS CloudWatch, AWS S3, Datadog, Elasticsearch, GCP Cloud Monitoring, Honeycomb, New Relic, Prometheus, Splunk, and more

### Datadog
1. Enable real-time connection logs on Connectors
2. Install and configure Datadog agent per Datadog's official documentation
3. Enables Twingate analytics dashboard in Datadog

## Configuration Values
| Method | File/Config |
|--------|-------------|
| Syslog | `/etc/systemd/journald.conf` |
| Syslog forwarding | `/etc/syslog.conf` |
| Vector config | `vector.toml` (example name) |

## Gotchas
- `journald` has no built-in remote log forwarding — requires one of these additional tools
- Real-time connection logs must be enabled separately before Syslog/Vector/Datadog will capture meaningful data
- AWS S3 method has a minimum 5-minute delay; not real-time

## Related Docs
- Twingate real-time connection logs (Connector configuration)
- Twingate audit logs / network events / DNS filtering logs
- Vector documentation (Sources, Transforms, Sinks)
- Datadog agent official documentation
- Twingate Datadog analytics dashboard setup