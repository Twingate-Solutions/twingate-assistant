# Connector Real-Time Logs

## Summary
Twingate Connectors support configurable service logging levels and real-time traffic logging output as single-line JSON to stdout. Traffic logs can be ingested by SIEM platforms (CloudWatch, Datadog, Splunk, Loki, etc.) by filtering for lines prefixed with `ANALYTICS`.

## Key Information
- Service logs and traffic logs are mixed in stdout; filter on `ANALYTICS` prefix for traffic data
- Traffic logs output as single-line JSON (`event_type`: `established_connection` or `closed_connection`)
- Historical data export is a separate feature (see Exporting network traffic docs)
- `connection.id` links related connection events together

## Configuration Values

### Environment Variables
| Variable | Values | Default | Purpose |
|---|---|---|---|
| `TWINGATE_LOG_LEVEL` | `3`, `4`, `5`, `7` | `3` | Service log verbosity |
| `TWINGATE_LOG_ANALYTICS` | `v2` | unset | Enable real-time traffic logs |

### Log Levels
- `3` — ERROR only
- `4` — WARN+
- `5` — INFO+
- `7` — DEBUG+ (very verbose, use temporarily)

## Prerequisites
- Connector deployed via Docker, systemd, or Kubernetes Helm chart
- Environment variables set **before** Connector starts

## Step-by-Step: Enable Traffic Logging

**Docker:**
```bash
--env TWINGATE_LOG_ANALYTICS="v2"
```

**systemd** (`/etc/twingate/connector.conf`):
```
TWINGATE_LOG_ANALYTICS=v2
TWINGATE_LOG_LEVEL=3
```

**Read systemd logs:**
```bash
journalctl -u twingate-connector -n 100 -f
```

**Helm Chart:** Set via `env` parameter in chart values.

## JSON Schema Fields (v2)
| Field | Notes |
|---|---|
| `connection.id` | Shared across `established_connection` / `closed_connection` events |
| `connection.client_ip` | Internet-facing NAT IP of client |
| `connection.resource_ip` | Private IP as resolved by Connector |
| `connection.rx` / `tx` | Bytes received/transmitted |
| `resource.address` | Address as defined in Admin console |
| `location` | Stringified JSON with GeoIP data |
| `device.id` | Internal Twingate device ID (not OS device ID) |

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
- Log level `7` is very verbose — avoid long-term use if storage is limited
- Error state connections do NOT emit a `closed_connection` event
- `device.id` is Twingate-internal and may not match OS-reported device IDs
- `TWINGATE_LOG_ANALYTICS` must be set before Connector starts (not hot-reloadable)
- DNS resources: `resource.address` shows the DNS name; resolved IP is in `connection.resource_ip`

## Related Docs
- Exporting network traffic (historical data)
- How DNS Works with Twingate
- Twingate Helm Chart README