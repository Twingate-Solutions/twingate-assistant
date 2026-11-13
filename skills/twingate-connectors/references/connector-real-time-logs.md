---
source: https://www.twingate.com/docs/connector-real-time-logs
type: docs
fetched: 2026-11-13
source_version: b79c749cc27b3f89a4c0b72666db989f2ee3f496049616f32c72e7c38413100e
trust: official
---

# Connector Logging

## Summary
Describes the logging available for Twingate Connectors: local service logs at configurable verbosity and real-time network connection logs emitted to stdout as single-line JSON. The connection logs can be collected by SIEM and log platforms (CloudWatch, Datadog, Splunk, Promtail/Loki). For historical data, see the "Exporting network traffic" doc.

## Key Information
- Service log levels (each includes the lower levels):
  - 3 (default): basic connectivity and ERROR
  - 4: WARN
  - 5: INFO
  - 7: DEBUG (use for diagnosing connectivity/config issues)
- Real-time traffic logging is enabled by setting `TWINGATE_LOG_ANALYTICS=v3` before the Connector starts.
- Service and traffic logs are mixed in stdout. Filter for lines starting with `ANALYTICS`, followed by one JSON object.
- Connection logs for a single connection share `connection.id`. A successful connection produces an `established_connection` event and a `closed_connection` event.

## Prerequisites
- A deployed Twingate Connector (Docker, Kubernetes Helm, or systemd).
- Access to restart the Connector, since the env var must be set before start.
- A log collector or SIEM if exporting logs.

## Step-by-Step: Enable Real-Time Traffic Logs
- **Docker:** add `--env TWINGATE_LOG_ANALYTICS="v3"` to the `docker run` command.
- **Helm:** use the chart's `env` parameter to set `TWINGATE_LOG_ANALYTICS="v3"` (see the chart README).
- **systemd:** add `TWINGATE_LOG_ANALYTICS=v3` to `/etc/twingate/connector.conf`, then restart the Connector.
- **Read logs (systemd):** `journalctl -u twingate-connector -n 100 -f`

## Configuration Values
- `TWINGATE_LOG_LEVEL`: 3 (default), 4, 5, or 7. Set in `/etc/twingate/connector.conf` or as a Docker env var.
- `TWINGATE_LOG_ANALYTICS`: `v3` enables connection logs.

### v3 JSON schema (top-level fields)
- `connection`: `cbct_freshness`, `client_ip`, `duration`, `id`, `protocol`, `resource_ip`, `resource_port`, `rx`, `tx`, `tunnel_path`, `tunnel_proto`
- `connector`: `id`, `name`
- `device`: `id`
- `event_type`
- `location`: stringified JSON with geoip data
- `relays`
- `remote_network`: `id`, `name`
- `resource`: `address`, `applied_rule`, `id`
- `timestamp`
- `user`: `email`, `id`

### Field notes
- `client_ip` is the client's internet-visible address, usually a NAT address.
- `resource_ip` is always the private IP. For DNS resources, it is the address as resolved by the Connector.
- `rx`/`tx` are bytes received/transmitted over the connection's lifetime.
- `resource.address` is as defined in the Admin Console.

### Vector example (SIEM parsing)
- Source: `journald`, `include_units = ["twingate-connector"]`, `current_boot_only = true`
- Filter transform: `starts_with!(.message, "ANALYTICS")`
- Remap transform: `parse_grok!(.message, "ANALYTICS%{SPACE}%{GREEDYDATA:json_event}")`, then `parse_json!` on `json_event`, with `drop_on_abort = true`

## Gotchas
- Level 7 is very verbose. Avoid long-term use if host log storage is limited.
- Error states have no matching `closed_connection` event.
- `device.id` is a Twingate-internal ID and may not match the ID the device itself reports. The schema is to be standardized in a future version.
- `location` is a stringified JSON string, so it needs a second parse.
- Traffic logs are not separate from service logs. Filter on the `ANALYTICS` prefix.

## Related Docs
- Exporting network traffic (historical data)
- How DNS Works with Twingate
- Twingate Helm Chart README