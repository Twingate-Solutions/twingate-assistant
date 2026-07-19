# Connector Real-Time Logs

## Summary
Twingate Connectors support multiple service log levels and real-time traffic logging output as single-line JSON to stdout. Traffic logs can be ingested by SIEM platforms (CloudWatch, Datadog, Splunk, Loki, etc.) by filtering for lines prefixed with `ANALYTICS`.

## Key Information
- Service logs have 4 levels: 3 (ERROR/default), 4 (WARN), 5 (INFO), 7 (DEBUG)
- Real-time traffic logs output as single-line JSON to stdout when `TWINGATE_LOG_ANALYTICS=v2` is set
- Filter log output for lines starting with `ANALYTICS` to isolate traffic logs
- Each connection generates `established_connection` and `closed_connection` events sharing the same `connection.id`
- Error states do **not** generate a corresponding `closed_connection` event

## Configuration Values

| Variable | Values | Purpose |
|----------|--------|---------|
| `TWINGATE_LOG_LEVEL` | `3` (default), `4`, `5`, `7` | Service log verbosity |
| `TWINGATE_LOG_ANALYTICS` | `v2` | Enable real-time traffic logging |

**Config file (systemd):** `/etc/twingate/connector.conf`

**Docker flag:** `--env TWINGATE_LOG_ANALYTICS="v2"`

**Helm:** Set via `env` parameter in values

## JSON Schema Fields (v2)

```
connection.id          - shared across established/closed events for same connection
connection.client_ip   - internet-facing NAT IP of client
connection.resource_ip - private IP of resource (DNS resolved by Connector)
connection.rx / .tx    - bytes received/transmitted
connection.duration    - connection lifetime
connection.protocol    - tcp/udp
connection.tunnel_path - direct or relay
connection.tunnel_proto
device.id              - internal Twingate device ID
resource.address       - as defined in Admin console (DNS name if applicable)
location               - stringified JSON with geoip data
event_type             - established_connection | closed_connection
timestamp              - Unix ms
user.email / user.id
connector.id / connector.name
remote_network.id / remote_network.name
```

## Step-by-Step: Enable Traffic Logging (systemd)

1. Edit `/etc/twingate/connector.conf`
2. Add: `TWINGATE_LOG_ANALYTICS=v2`
3. Restart Connector
4. View logs: `journalctl -u twingate-connector -n 100 -f`
5. Filter for traffic lines: grep for `ANALYTICS` prefix

## Gotchas
- Log level 7 is very verbose — avoid long-duration use if storage is limited
- `connection.client_ip` is the NAT/internet-facing IP, not the device's local IP
- `device.id` is internal to Twingate and may not match OS-reported device IDs (standardization planned)
- `location` field is a **stringified** JSON string, not a nested object — requires double-parse
- Service logs and traffic logs are mixed in stdout; must filter by `ANALYTICS` prefix

## SIEM Integration (Vector Example)
Filter with `starts_with!(.message, "ANALYTICS")`, then parse with grok pattern:
```
ANALYTICS%{SPACE}%{GREEDYDATA:json_event}
```

## Related Docs
- Exporting historical network traffic
- How DNS Works with Twingate
- Twingate Helm Chart README