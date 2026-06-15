# Connector Real-Time Logs

## Summary
Twingate Connectors support multiple service log levels and real-time traffic logging via environment variables. Traffic logs output as single-line JSON to stdout, prefixed with `ANALYTICS`, enabling direct ingestion by SIEM platforms.

## Key Information
- Service logs have 4 levels: 3 (ERROR/default), 4 (WARN), 5 (INFO), 7 (DEBUG)
- Real-time traffic logs require `TWINGATE_LOG_ANALYTICS=v2` env var set before Connector starts
- All logs go to stdout in single-line JSON format
- Filter traffic logs by lines starting with `ANALYTICS`
- Two event types: `established_connection` and `closed_connection` (errors skip `closed_connection`)
- `connection.id` links events for the same network connection

## Configuration Values

| Variable | Values | Purpose |
|---|---|---|
| `TWINGATE_LOG_LEVEL` | `3`(default), `4`, `5`, `7` | Service log verbosity |
| `TWINGATE_LOG_ANALYTICS` | `v2` | Enable real-time traffic logs |

**Config file location (systemd):** `/etc/twingate/connector.conf`

## Setup by Deployment Type

**Docker:**
```
--env TWINGATE_LOG_ANALYTICS="v2"
```

**systemd** — add to `/etc/twingate/connector.conf`:
```
TWINGATE_LOG_ANALYTICS=v2
```
Read logs: `journalctl -u twingate-connector -n 100 -f`

**Kubernetes (Helm):** Set via `env` parameter in Helm chart values.

## JSON Schema Fields (v2)

| Field | Notes |
|---|---|
| `connection.id` | Shared across events for same connection |
| `connection.client_ip` | Internet-facing NAT address of client |
| `connection.resource_ip` | Private IP of resource (DNS resolved by Connector) |
| `connection.rx` / `tx` | Bytes received/transmitted |
| `connection.duration` | Connection lifetime |
| `connection.tunnel_proto` | e.g., `quic/udp` |
| `device.id` | Internal Twingate device ID (not OS device ID) |
| `resource.address` | Address as defined in Admin console |
| `location` | Stringified JSON with GeoIP data |
| `event_type` | `established_connection` or `closed_connection` |

## Gotchas
- Log level 7 is very verbose — avoid long-duration use if storage is limited
- `connection.client_ip` is the NAT/internet-facing IP, not the device's local IP
- `device.id` does not match OS-reported device IDs (standardization planned)
- `location` field is a **stringified JSON string**, not a nested object — requires double-parsing
- Error states produce no `closed_connection` event

## SIEM Integration (Vector Example)
Filter with `starts_with(.message, "ANALYTICS")`, then extract JSON via grok: `ANALYTICS%{SPACE}%{GREEDYDATA:json_event}`

## Related Docs
- Exporting historical network traffic
- How DNS Works with Twingate
- Twingate Helm Chart README