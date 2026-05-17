# Connector Real-Time Logs

## Summary
Twingate Connectors support configurable service logging levels and real-time traffic logging output. Traffic logs are emitted as single-line JSON to stdout, prefixed with `ANALYTICS`, enabling ingestion by SIEM platforms. Service and traffic logs are mixed in the same output stream.

## Key Information
- Service logs have 4 levels: 3 (ERROR), 4 (WARN), 5 (INFO), 7 (DEBUG)
- Real-time traffic logs require `TWINGATE_LOG_ANALYTICS=v2` env var set before Connector starts
- All logs go to `stdout` as single-line JSON
- Filter for lines starting with `ANALYTICS` to isolate traffic logs
- Two `event_type` values: `established_connection` and `closed_connection`
- Error states produce no `closed_connection` event

## Prerequisites
- Running Twingate Connector (Docker, systemd, or Kubernetes)
- Log collector/SIEM configured to read from stdout or journald

## Configuration Values

| Variable | Values | Description |
|---|---|---|
| `TWINGATE_LOG_LEVEL` | `3` (default), `4`, `5`, `7` | Service log verbosity |
| `TWINGATE_LOG_ANALYTICS` | `v2` | Enables real-time traffic logging |

**Config file location (systemd):** `/etc/twingate/connector.conf`

**Enable per deployment type:**
- **Docker:** `--env TWINGATE_LOG_ANALYTICS="v2"` in run command
- **systemd:** Add `TWINGATE_LOG_ANALYTICS=v2` to `/etc/twingate/connector.conf`
- **Kubernetes/Helm:** Set via `env` parameter in Helm chart values

**Read systemd logs:**
```bash
journalctl -u twingate-connector -n 100 -f
```

## JSON Schema Fields (v2)

| Field | Notes |
|---|---|
| `connection.id` | Shared across events for same connection |
| `connection.client_ip` | Internet-facing NAT IP of client |
| `connection.resource_ip` | Private IP of resource (DNS resolved by Connector) |
| `connection.rx` / `tx` | Bytes received/transmitted |
| `connection.duration` | Connection lifetime |
| `connection.tunnel_proto` | e.g., `quic/udp` |
| `device.id` | Internal Twingate device ID (not OS device ID) |
| `resource.address` | Address as defined in Admin console |
| `location` | Stringified JSON with GeoIP data |
| `event_type` | `established_connection` or `closed_connection` |

## Gotchas
- Log level 7 is very verbose; avoid long-term use if log storage is limited
- `device.id` does not correspond to OS-reported device IDs (standardization planned)
- `connection.resource_ip` is the Connector-resolved IP, not the DNS name
- Traffic logs only generated when `TWINGATE_LOG_ANALYTICS=v2` is set **before** Connector starts
- Error connections will not have a matching `closed_connection` event

## Vector SIEM Config Example
```toml
[transforms.tg_analytics_filter]
type = "filter"
condition = """starts_with!(.message, "ANALYTICS")"""

[transforms.tg_analytics_transform]
type = "remap"
source = """.message = parse_json!(parse_grok!(.message, "ANALYTICS%{SPACE}%{GREEDYDATA:json_event}").json_event)"""
```

## Related Docs
- Exporting network traffic (historical data)
- How DNS Works with Twingate
- Twingate Helm Chart README