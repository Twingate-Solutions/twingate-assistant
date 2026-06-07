# Connector Real-Time Logs

## Summary
Twingate Connectors support multiple service log levels and real-time traffic logging via environment variables. Traffic logs output as single-line JSON to stdout, prefixed with `ANALYTICS`, enabling ingestion by SIEM tools. Service and traffic logs are mixed in output and must be filtered separately.

## Key Information
- Service logs have 4 levels: 3 (ERROR/default), 4 (WARN), 5 (INFO), 7 (DEBUG)
- Real-time traffic logs require `TWINGATE_LOG_ANALYTICS=v2` set before Connector starts
- All logs output to **stdout** in single-line JSON format
- Traffic log lines are prefixed with `ANALYTICS` followed by JSON object
- Two event types: `established_connection` and `closed_connection`; errors lack a `closed_connection` event
- `connection.id` links related events for the same network connection

## Prerequisites
- Running Twingate Connector (systemd, Docker, or Kubernetes)
- SIEM/log aggregation tool configured to read from stdout or journald

## Configuration Values

| Variable | Values | Purpose |
|----------|--------|---------|
| `TWINGATE_LOG_LEVEL` | `3`(default), `4`, `5`, `7` | Service log verbosity |
| `TWINGATE_LOG_ANALYTICS` | `v2` | Enable real-time traffic logs |

**Config file location (systemd):** `/etc/twingate/connector.conf`

**Docker flag:** `--env TWINGATE_LOG_ANALYTICS="v2"`

**Helm Chart:** Set via `env` parameter in values

## JSON Schema Fields (v2)

```
connection.{id, client_ip, resource_ip, resource_port, protocol, 
            tunnel_path, tunnel_proto, rx, tx, duration, cbct_freshness}
connector.{id, name}
device.{id}
resource.{id, address, applied_rule}
remote_network.{id, name}
user.{id, email}
event_type          # "established_connection" | "closed_connection"
timestamp           # Unix ms
location            # stringified JSON with geoip data
relays              # array
```

## Step-by-Step: Enable Traffic Logs

**systemd:**
1. Add `TWINGATE_LOG_ANALYTICS=v2` to `/etc/twingate/connector.conf`
2. Restart connector
3. View logs: `journalctl -u twingate-connector -n 100 -f`
4. Filter for lines starting with `ANALYTICS`

**Docker:**
```bash
docker run --env TWINGATE_LOG_ANALYTICS="v2" ...
```

## Gotchas
- Level 7 logging is very verbose — avoid long-duration use if disk space is limited
- `connection.client_ip` is the internet-facing NAT address, not the device's actual IP
- `connection.resource_ip` is the private IP as resolved by the Connector (DNS resources resolve locally)
- `device.id` is Twingate-internal and may not match OS-reported device IDs (standardization planned)
- `location` field is a **stringified** JSON string, not a nested object — requires double-parsing
- Error connections have no `closed_connection` event; only `established_connection`

## SIEM Filter Example (Vector)
```toml
condition = """starts_with!(.message, "ANALYTICS")"""
# Parse: strip "ANALYTICS " prefix, then parse_json
```

## Related Docs
- [Exporting Network Traffic](#) (historical data export)
- [How DNS Works with Twingate](#)
- Twingate Helm Chart README