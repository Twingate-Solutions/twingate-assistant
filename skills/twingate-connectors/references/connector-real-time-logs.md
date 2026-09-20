---
source: https://www.twingate.com/docs/connector-real-time-logs
type: docs
fetched: 2026-09-20
source_version: 8ce741c553d12e2efb0c0ffe1ce0900d91fca4f7ca3fe058256ad98d72fd1290
---

# Connector Real-Time Logs

## Summary
Twingate Connectors support configurable service logging levels and real-time traffic logging output as JSON to stdout. Traffic logs can be ingested by SIEM platforms (CloudWatch, Datadog, Splunk, Loki, etc.) by filtering for lines prefixed with `ANALYTICS`.

## Key Information
- Service logs and traffic logs are mixed in stdout; filter on lines starting with `ANALYTICS` for traffic data
- Traffic logs output single-line JSON (v3 schema) per network connection event
- Two event types: `established_connection` and `closed_connection` (errors omit `closed_connection`)
- `connection.id` links related events for the same connection
- `connection.client_ip` = internet-facing NAT IP; `connection.resource_ip` = private resource IP

## Prerequisites
- Connector installed via Docker, systemd, or Kubernetes Helm Chart
- Access to modify connector config or Docker run command

## Configuration Values

### Environment Variables
| Variable | Values | Default | Purpose |
|---|---|---|---|
| `TWINGATE_LOG_LEVEL` | `3`, `4`, `5`, `7` | `3` | Service log verbosity |
| `TWINGATE_LOG_ANALYTICS` | `v3` | unset | Enable real-time traffic logs |

**Log levels:** 3=ERROR, 4=WARN, 5=INFO, 7=DEBUG (cumulative)

## Step-by-Step: Enable Real-Time Traffic Logs

**Docker:**
```bash
--env TWINGATE_LOG_ANALYTICS="v3"
```

**systemd** — add to `/etc/twingate/connector.conf`:
```
TWINGATE_LOG_ANALYTICS=v3
```

**Read systemd logs:**
```bash
journalctl -u twingate-connector -n 100 -f
```

**Kubernetes Helm Chart:** Set via `env` parameter in values.

## JSON Schema Fields (v3)
```
connection.id          - shared across established/closed events
connection.client_ip   - internet-facing NAT IP of client
connection.resource_ip - private IP of resource
connection.duration    - microseconds
connection.rx / tx     - bytes received/transmitted
connection.protocol    - tcp/udp
connection.tunnel_path - direct or relay
connection.tunnel_proto
resource.address       - as defined in Admin console (DNS name)
resource.applied_rule
device.id              - internal Twingate device ID
user.email / user.id
location               - stringified JSON with geoip data
event_type             - established_connection | closed_connection
timestamp              - Unix milliseconds
```

## SIEM Integration (Vector Example)
```toml
[sources.twingate_connector]
type = "journald"
include_units = ["twingate-connector"]

[transforms.tg_analytics_filter]
type = "filter"
inputs = ["twingate_connector"]
condition = """starts_with!(.message, "ANALYTICS")"""

[transforms.tg_analytics_transform]
type = "remap"
inputs = ["tg_analytics_filter"]
source = """.message = parse_json!(parse_grok!(.message, "ANALYTICS%{SPACE}%{GREEDYDATA:json_event}").json_event)"""
```

## Gotchas
- Log level 7 is very verbose; avoid long-duration use if disk space is limited
- `connection.resource_ip` for DNS-defined resources reflects Connector-resolved IP, not the DNS name
- `device.id` is Twingate-internal and may not match OS-reported device IDs (future schema will standardize)
- `location` field is a stringified JSON string, not a nested object — requires double-parsing

## Related Docs
- Exporting network traffic (historical data)
- How DNS Works with Twingate
- Twingate Helm Chart README