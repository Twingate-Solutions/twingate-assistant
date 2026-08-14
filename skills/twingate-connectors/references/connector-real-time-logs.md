---
source: https://www.twingate.com/docs/connector-real-time-logs
type: docs
fetched: 2026-08-14
source_version: 9ff25df08c60b217330768747d05d863ef54a798a610b151dc9fc2bc80f8f310
---

# Connector Real-Time Logs

## Summary
Twingate Connectors support configurable service log levels and real-time traffic logging via environment variables. Traffic logs are output as single-line JSON to stdout, prefixed with `ANALYTICS`, enabling ingestion by SIEM platforms like Splunk, Datadog, and CloudWatch.

## Key Information
- Service logs output to stdout; traffic logs also output to stdout in single-line JSON format
- Filter for lines starting with `ANALYTICS` to isolate traffic logs from service logs
- Traffic logs capture per-connection events: `established_connection` and `closed_connection`
- `connection.id` links related events for the same network connection
- Error states produce no corresponding `closed_connection` event
- `connection.client_ip` = internet-facing NAT IP; `connection.resource_ip` = private resource IP
- `location` field is a stringified JSON (double-encoded), not a native JSON object

## Prerequisites
- Twingate Connector installed (Docker, systemd, or Kubernetes/Helm)
- Access to connector config file or Docker run command

## Configuration Values

| Variable | Value | Purpose |
|---|---|---|
| `TWINGATE_LOG_LEVEL` | `3` (default), `4`, `5`, `7` | Service log verbosity |
| `TWINGATE_LOG_ANALYTICS` | `v2` | Enable real-time traffic logging |

**Log levels:**
- `3` = ERROR only (default)
- `4` = WARN+
- `5` = INFO+
- `7` = DEBUG+ (very verbose, not recommended long-term)

## Step-by-Step: Enable Traffic Logging

**Docker:**
```bash
--env TWINGATE_LOG_ANALYTICS="v2"
```

**systemd** — add to `/etc/twingate/connector.conf`:
```
TWINGATE_LOG_ANALYTICS=v2
```

**Kubernetes/Helm** — set via `env` parameter in Helm chart values.

**Read systemd logs:**
```bash
journalctl -u twingate-connector -n 100 -f
```

## JSON Schema (v2) Key Fields
```
connection.id          # Shared across events for same connection
connection.client_ip   # Internet-facing NAT IP of client
connection.resource_ip # Private IP of resource (DNS resolved by Connector)
connection.rx / .tx    # Bytes received/transmitted (lifetime of connection)
connection.duration    # Connection duration
connection.protocol    # tcp/udp
connection.tunnel_path # direct or relay
event_type             # established_connection | closed_connection
device.id              # Twingate internal device ID
resource.address       # Resource address as defined in Admin console
location               # Stringified JSON with geoip data
timestamp              # Unix milliseconds
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
- Level 7 logging is very verbose — avoid long-term use if storage is limited
- `location` is a **stringified** JSON string, requires double-parse
- `device.id` may not match OS-reported device IDs (standardization planned)
- DNS-defined resources: `resource.address` shows DNS name, `connection.resource_ip` shows resolved IP

## Related Docs
- Exporting historical network traffic (separate guide)
- How DNS Works with Twingate
- Official Twingate Helm Chart README