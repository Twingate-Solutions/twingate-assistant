# Connector Real-Time Logs

## Summary
Twingate Connectors support configurable service logging levels and real-time traffic logging output as JSON to stdout. Traffic logs can be ingested by SIEM platforms (CloudWatch, Datadog, Splunk, Loki, etc.) by filtering for lines prefixed with `ANALYTICS`.

## Key Information
- Service logs and traffic logs are mixed in stdout; filter on `ANALYTICS` prefix to isolate traffic logs
- Traffic logs output as single-line JSON per connection event
- Two event types: `established_connection` and `closed_connection` (errors omit `closed_connection`)
- `connection.id` links events for the same network connection
- `connection.client_ip` = internet-facing NAT address; `connection.resource_ip` = private resource IP

## Prerequisites
- Connector deployed via Docker, Kubernetes (Helm), or systemd
- For historical data export, see Exporting Network Traffic docs

## Configuration Values

### Environment Variables
| Variable | Values | Description |
|---|---|---|
| `TWINGATE_LOG_LEVEL` | `3` (default), `4`, `5`, `7` | Service log verbosity |
| `TWINGATE_LOG_ANALYTICS` | `v2` | Enables real-time traffic logging |

### Log Levels
- `3` — ERROR only (default)
- `4` — WARN+
- `5` — INFO+
- `7` — DEBUG+ (very verbose, avoid long-term use)

## Step-by-Step: Enable Real-Time Traffic Logging

**Docker:**
```bash
--env TWINGATE_LOG_ANALYTICS="v2"
```

**systemd** — add to `/etc/twingate/connector.conf`:
```
TWINGATE_LOG_ANALYTICS=v2
```

**Kubernetes Helm** — set via `env` parameter in values:
```yaml
env:
  TWINGATE_LOG_ANALYTICS: "v2"
```

**View systemd logs:**
```bash
journalctl -u twingate-connector -n 100 -f
```

## JSON Schema (v2) Key Fields
```
connection.id          - shared across established/closed events for same connection
connection.client_ip   - client's internet-facing NAT IP
connection.resource_ip - private IP of accessed resource
connection.rx/tx       - bytes received/transmitted (lifetime)
connection.duration    - connection duration
connection.tunnel_path - direct or relay
connection.tunnel_proto - e.g., quic/udp
resource.address       - resource address as defined in Admin console
resource.applied_rule  - matching wildcard rule
device.id              - Twingate internal device ID
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
drop_on_abort = true
```

## Gotchas
- Level 7 logging is very verbose — avoid sustained use if log storage is limited
- `TWINGATE_LOG_ANALYTICS` must be set **before** Connector starts
- `device.id` is Twingate-internal and may not match OS-reported device IDs (standardization planned)
- DNS-defined resources: `resource.address` shows the DNS name; `connection.resource_ip` shows resolved private IP
- Error states do not emit a `closed_connection` event

## Related Docs
- Exporting Network Traffic (historical data)
- How DNS Works with Twingate
- Twingate Helm Chart README