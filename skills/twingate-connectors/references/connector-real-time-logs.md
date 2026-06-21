# Connector Real-Time Logs

## Summary
Twingate Connectors support configurable service logging levels and real-time traffic logging via environment variables. Traffic logs output as single-line JSON to stdout, prefixed with `ANALYTICS`, enabling ingestion by SIEM platforms. Historical data export is handled separately.

## Key Information
- Service logs have 4 levels: 3 (ERROR/default), 4 (WARN), 5 (INFO), 7 (DEBUG)
- Real-time traffic logs output to stdout as single-line JSON, prefixed with `ANALYTICS`
- Supported SIEM platforms: AWS CloudWatch, Datadog, Splunk, Promtail/Loki, Vector
- Each log level is cumulative (level 7 includes all lower levels)
- Level 7 is very verbose; avoid long-term use if log storage is limited

## Configuration Values

| Variable | Values | Purpose |
|---|---|---|
| `TWINGATE_LOG_LEVEL` | `3` (default), `4`, `5`, `7` | Service log verbosity |
| `TWINGATE_LOG_ANALYTICS` | `v2` | Enables real-time traffic logging |

### Setting by deployment type:
- **Docker**: `--env TWINGATE_LOG_ANALYTICS="v2"` in run command
- **systemd**: Add `TWINGATE_LOG_ANALYTICS=v2` to `/etc/twingate/connector.conf`
- **Kubernetes/Helm**: Set via `env` parameter in Helm chart values

## JSON Schema (v2) Key Fields

```json
{
  "connection": {
    "id": "e755ba99-24",        // shared across established/closed events
    "client_ip": "192.0.2.0",  // internet-facing NAT IP
    "resource_ip": "1.2.3.4",  // always private IP
    "resource_port": 443,
    "protocol": "tcp",
    "tunnel_proto": "quic/udp",
    "tunnel_path": "direct",
    "rx": 234867,               // bytes received
    "tx": 23363,                // bytes transmitted
    "duration": 3034753
  },
  "event_type": "closed_connection",  // or "established_connection"
  "resource": { "address": "app.website.com", "applied_rule": "*.website.com" },
  "user": { "email": "user@twingate.com", "id": "113256" },
  "device": { "id": "200903" },
  "connector": { "id": "84014", "name": "nondescript-caterpillar" },
  "location": "{\"geoip\":{...}}",    // stringified JSON
  "timestamp": 1698356150045
}
```

## Step-by-Step (systemd setup)
1. Edit `/etc/twingate/connector.conf`
2. Add `TWINGATE_LOG_ANALYTICS=v2`
3. Restart connector
4. Read logs: `journalctl -u twingate-connector -n 100 -f`
5. Filter for lines starting with `ANALYTICS`

## Gotchas
- `connection.client_ip` is the NAT/internet-facing IP, not the device's actual IP
- `location` field is a **stringified JSON** (not a nested object)—requires double-parsing
- Error states do NOT generate a `closed_connection` event
- `device.id` is Twingate-internal and may not match OS-reported device IDs (standardization planned)
- Service logs and traffic logs are mixed in output; must filter on `ANALYTICS` prefix

## Vector SIEM Filter Example
```toml
[transforms.tg_analytics_filter]
type = "filter"
inputs = ["twingate_connector"]
condition = """starts_with!(.message, "ANALYTICS")"""

[transforms.tg_analytics_transform]
type = "remap"
inputs = ["tg_analytics_filter"]
source = """.message = parse_json!(parse_grok!(.message, "ANALYTICS%{SPACE}%{GREEDYDATA:json_event}").json_event)"""
```

## Related