# Connector Real-Time Logs

## Summary
Twingate Connectors support configurable service logging levels and real-time traffic logging output as single-line JSON to stdout. Traffic logs can be ingested by SIEM platforms (CloudWatch, Datadog, Splunk, Loki, etc.) by filtering for lines prefixed with `ANALYTICS`.

## Key Information
- Service logs and traffic logs are mixed in stdout; filter on `ANALYTICS` prefix for traffic data
- Traffic logs output as single-line JSON (`event_type`: `established_connection` or `closed_connection`)
- Error states produce no corresponding `closed_connection` event
- `connection.id` links related events for the same network connection
- `connection.client_ip` = internet-facing NAT address (not internal device IP)
- `connection.resource_ip` = private IP as resolved by Connector (for DNS resources)
- `location` field is a **stringified JSON** (not a nested object)

## Prerequisites
- Connector already deployed (Docker, systemd, or Kubernetes)
- Log collection agent if exporting to SIEM

## Configuration Values

| Variable | Value | Purpose |
|---|---|---|
| `TWINGATE_LOG_LEVEL` | `3` (default), `4`, `5`, `7` | Service log verbosity |
| `TWINGATE_LOG_ANALYTICS` | `v2` | Enable real-time traffic logging |

**Log levels:**
- `3` = ERROR only (default)
- `4` = WARN+
- `5` = INFO+
- `7` = DEBUG+ (very verbose, avoid long-term use)

## Step-by-Step: Enable Traffic Logging

**Docker:**
```bash
docker run --env TWINGATE_LOG_ANALYTICS="v2" ...
```

**systemd** — add to `/etc/twingate/connector.conf`:
```
TWINGATE_LOG_ANALYTICS=v2
```

Read logs:
```bash
journalctl -u twingate-connector -n 100 -f
```

**Kubernetes (Helm):** Set via `env` parameter in values — see Helm Chart README.

## JSON Schema (v2) Key Fields

```json
{
  "connection": { "id", "client_ip", "resource_ip", "resource_port",
                  "protocol", "duration", "rx", "tx",
                  "tunnel_path", "tunnel_proto", "cbct_freshness" },
  "connector":  { "id", "name" },
  "device":     { "id" },
  "resource":   { "address", "applied_rule", "id" },
  "remote_network": { "id", "name" },
  "user":       { "email", "id" },
  "event_type": "established_connection | closed_connection",
  "location":   "<stringified JSON with geoip>",
  "relays":     [],
  "timestamp":  1698356150045
}
```

## SIEM Filtering Example (Vector)

```toml
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
- Log level `7` is extremely verbose — can exhaust disk on low-capacity hosts
- `device.id` is Twingate-internal and may not match OS-reported device IDs (standardization planned)
- `location` must be parsed as a string before accessing geoip subfields
- Must restart Connector after changing env vars for changes to take effect

## Related Docs
- Exporting historical network traffic
- How DNS Works with Twingate
- Twingate Helm Chart README