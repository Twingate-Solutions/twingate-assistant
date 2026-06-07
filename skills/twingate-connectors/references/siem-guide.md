# How to Ingest Connector Logs into a SIEM

## Summary
Twingate Connectors log events in real-time via `journald` (systemd). Since journald lacks native remote forwarding, this guide covers four methods to send Connector logs to a SIEM or centralized logging system.

## Key Information
- Logs are written via `journald` on Linux systems running Connectors
- Real-time connection logs must be explicitly enabled on Connectors before configuring any method
- Four supported ingestion paths: AWS S3, Syslog, Vector, Datadog agent

## Prerequisites
- Linux machine hosting a Twingate Connector
- Real-time connection logs enabled on Connectors (required for all methods)
- Root/sudo access to edit system config files

---

## Methods

### 1. AWS S3 (Recommended)
- Twingate natively pushes audit logs, network events, and DNS filtering logs to an S3 bucket every 5 minutes
- Configure S3 → SIEM pipeline separately

### 2. Syslog
**Steps:**
1. Enable real-time connection logs on Connectors
2. Edit `/etc/systemd/journald.conf`
3. Uncomment `#ForwardToSyslog=yes` → `ForwardToSyslog=yes`
4. Edit `/etc/syslog.conf` to forward to central syslog server
5. Restart the Connector

### 3. Vector
**Steps:**
1. Enable real-time connection logs on Connectors
2. Install Vector on the Connector host
3. Create `vector.toml` with Sources and Transforms
4. Add Sink configuration for target SIEM

**Supported Sinks:** AWS CloudWatch, AWS S3, Datadog, Elasticsearch, GCP Cloud Monitoring, Honeycomb, New Relic, Prometheus, Splunk, and more

### 4. Datadog Agent
- Install Datadog agent per Datadog's official documentation
- Enables the Twingate analytics dashboard in Datadog
- Requires real-time connection logs enabled

---

## Configuration Values
| Method | Config File |
|--------|-------------|
| Syslog | `/etc/systemd/journald.conf`, `/etc/syslog.conf` |
| Vector | `vector.toml` (user-defined path) |

**Key config line (Syslog):**
```
ForwardToSyslog=yes
```

---

## Gotchas
- Real-time connection logs must be enabled **before** configuring any forwarding method — this is a separate step not covered in this guide
- AWS S3 push is on a 5-minute interval; not truly real-time
- Syslog config file location may vary (`/etc/syslog.conf` is typical but not universal)
- Vector requires a separate installation and manual Sink configuration per SIEM

## Related Docs
- Twingate Audit Logs
- Network Events
- DNS Filtering Logs
- Real-time Connection Logs (Connector configuration)
- Vector configuration documentation (Twingate-specific)
- Datadog integration / Twingate analytics dashboard