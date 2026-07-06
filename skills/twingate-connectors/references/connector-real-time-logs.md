# Connector Real-Time Logs

## Summary
Twingate Connectors support configurable service logging levels and real-time traffic logging output as single-line JSON to stdout. Traffic logs can be ingested by SIEM platforms (CloudWatch, Datadog, Splunk, Loki, etc.) by filtering for lines prefixed with `ANALYTICS`.

## Key Information
- Service logs and traffic logs are mixed in stdout; filter on `ANALYTICS` prefix for traffic logs
- Traffic logs output as single-line JSON, one object per connection event
- Two event types: `established_connection` and `closed_connection` (errors omit `closed_connection`)
- `connection.id` links related events for the same network connection
- `connection.client_ip` = internet-facing NAT IP; `connection.resource_ip` = private resource IP
- `location` field is a **stringified JSON** (double-encoded), not a native JSON object

## Prerequisites
- Running Twingate Connector (Docker, systemd, or Kubernetes/Helm)
- SIEM or log aggregator configured to read from stdout/journald

## Configuration Values

### Environment Variables
| Variable | Values | Default | Purpose |
|---|---|---|---|
| `TWINGATE_LOG_LEVEL` | `3`, `4`, `5`, `7` | `3` | Service log verbosity |
| `TWINGATE_LOG_ANALYTICS` | `v2` | unset | Enable real-time traffic logs |

**Log levels:** 3=ERROR, 4=WARN, 5=INFO, 7=DEBUG (each includes lower levels)

## Step-by-Step: Enable Real-Time Traffic Logs

**Docker:**
```bash
--env TWINGATE_LOG_ANALYTICS="v2"
```

**systemd** — add to `/etc/twingate/connector.conf`:
```
TWINGATE_LOG_ANALYTICS=v2
```

**Kubernetes (Helm):** Set via `env` parameter in Helm chart values.

**View systemd logs:**
```bash
journalctl -u twingate-connector -n 100 -f
```

## JSON Schema (v2) Key Fields
```
connection.id          # Shared across events for same connection
connection.client_ip   # Client's public/NAT IP
connection.resource_ip # Private IP of resource
connection.rx / .tx    # Bytes received/transmitted
connection.duration    # Connection lifetime
connection.protocol    # tcp/udp
connection.tunnel_proto # e.g., quic/udp
event_type             # established_connection | closed_connection
resource.address       # As defined in Admin console (DNS name)
device.id              # Twingate internal device ID
location               # Stringified JSON with geoip data
timestamp              # Unix milliseconds
```

## Vector SIEM Integration Example
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
drop_on_abort = true
```

## Gotchas
- Log level 7 is very verbose; avoid long-duration use if disk space is limited
- `TWINGATE_LOG_ANALYTICS` must be set **before** the Connector starts
- `location` field requires double-parsing (stringified JSON inside JSON)
- `device.id` may not match OS-reported device IDs (standardization planned)
- Error state connections will **not** emit a `closed_connection` event

## Related Docs
- Exporting network traffic (historical data)
- How DNS Works with Twingate
- Twingate Helm Chart README