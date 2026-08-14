---
source: https://www.twingate.com/docs/siem-guide
type: docs
fetched: 2026-08-14
source_version: 7c68fc248217abbd9a335e83713837a76b2b4a8d73f5d17f0de692ef98914d65
---

# How to Ingest Connector Logs into a SIEM

## Summary
Twingate Connectors log events in real time via journald (systemd). Since journald lacks built-in remote forwarding, logs must be routed to SIEMs through one of several methods: AWS S3, syslog forwarding, Vector, or the Datadog agent.

## Key Information
- Logs are written via **journald** (systemd) on Linux hosts
- Four supported ingestion methods: AWS S3, Syslog, Vector, Datadog agent
- AWS S3 path delivers audit logs, network events, and DNS filtering logs on a **5-minute interval**
- Vector supports sinks including: AWS CloudWatch, AWS S3, Datadog, Elasticsearch, GCP Cloud Monitoring, Honeycomb, New Relic, Prometheus, Splunk

## Prerequisites
- Real-time connection logs must be **enabled on Connectors** before configuring any log forwarding method
- Linux host with systemd/journald running the Connector

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
3. Create `vector.toml` with Sources and Transforms per Twingate documentation
4. Add the appropriate Sink block for your target SIEM
5. Run Vector

### Datadog
1. Enable real-time connection logs on Connectors
2. Install and configure Datadog agent per Datadog's official documentation
3. Feeds the Twingate analytics dashboard in Datadog

## Configuration Values
| File | Key Setting |
|------|-------------|
| `/etc/systemd/journald.conf` | `ForwardToSyslog=yes` |
| `/etc/syslog.conf` | Central server forwarding rules |
| `vector.toml` | Sources, Transforms, Sinks |

## Gotchas
- Real-time connection logs must be explicitly enabled—this is a required step for all methods except AWS S3
- journald has **no native remote forwarding**; an intermediary tool is always required
- AWS S3 is the only method where Twingate pushes logs directly; all other methods require agent/config on the Connector host

## Related Docs
- Twingate real-time connection logs (enable on Connectors)
- Twingate audit logs / network events / DNS filtering logs
- Vector documentation (Sources, Transforms, Sinks)
- Datadog agent official documentation
- Twingate Vector configuration guide