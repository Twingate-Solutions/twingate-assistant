# Connector Real-Time Logs

## Summary
Twingate Connectors support configurable service logging levels and real-time traffic logging output as JSON to stdout. Traffic logs can be ingested by SIEM platforms (CloudWatch, Datadog, Splunk, Loki, etc.) by filtering lines prefixed with `ANALYTICS`.

## Key Information
- Service logs have 4 levels: 3 (ERROR), 4 (WARN), 5 (INFO), 7 (DEBUG)
- Real-time traffic logs output single-line JSON to stdout, prefixed with `ANALYTICS`
- Traffic logging schema version is `v2`
- Each connection generates `established_connection` and `closed_connection` events sharing the same `connection.id`
- `connection.client_ip` = internet-facing NAT IP, not device IP
- `connection.resource_ip` = private IP as resolved by Connector
- `location` field is a **stringified JSON** (double-encoded), not a JSON object

## Prerequisites
- Twingate Connector installed (Docker, systemd, or Kubernetes/Helm)
- Access to modify environment variables or `/etc/twingate/connector.conf`

## Configuration Values

| Variable | Values | Purpose |
|---|---|---|
| `TWINGATE_LOG_LEVEL` | `3` (default), `4`, `5`, `7` | Service log verbosity |
| `TWINGATE_LOG_ANALYTICS` | `v2` | Enable real-time traffic logs |

### Setting by deployment type:
- **Docker**: `--env TWINGATE_LOG_ANALYTICS="v2"` in `docker run`
- **systemd**: Add `TWINGATE_LOG_ANALYTICS=v2` to `/etc/twingate/connector.conf`
- **Helm**: Set via `env` parameter in Helm chart values

## JSON Schema (v2) Key Fields
```
connection.id          # Shared across events for same connection
connection.client_ip   # Internet-facing NAT address
connection.resource_ip # Private IP resolved by Connector
connection.rx / tx     # Bytes received/transmitted
connection.duration    # Connection lifetime
connection.protocol    # tcp/udp
connection.tunnel_proto # e.g., quic/udp
event_type             # established_connection | closed_connection
resource.address       # As defined in Admin console
location               # Stringified JSON with geoip data
timestamp              # Unix milliseconds
```

## Reading Logs (systemd)
```bash
journalctl -u twingate-connector -n 100 -f
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
- Level 7 is very verbose — avoid long-duration use if disk space is limited
- Error states do **not** produce a `closed_connection` event
- `location` is stringified JSON, must be double-parsed
- `device.id` is Twingate-internal and may not match OS device IDs
- Must filter on `ANALYTICS` prefix to separate traffic logs from service logs

## Related Docs
- Exporting historical network traffic
- How DNS Works with Twingate
- Twingate Helm Chart README