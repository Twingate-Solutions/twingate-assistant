# Detailed Network Event Schema

## Page Title
Detailed Network Event Schemas

## Summary
Twingate exports network events in two formats: CSV (via Admin Console download) and JSON (via AWS S3 sync). Each event represents a single completed connection, regardless of duration or data volume. Established connections are only reported after completion.

## Key Information

- **CSV export**: Admin Console download, one line per connection
- **JSON export**: AWS S3 bucket sync, one JSON object per line
- Connections reported only after completion; `end_time` empty if error occurred
- `bytes_transferred`/`bytes_received` empty if error occurred
- Wildcard resources: `resource_id` and `applied_rule` reflect the defined pattern (e.g., `*.twingate.com`), not the specific matched hostname

## CSV Column Reference

| Column | Notes |
|---|---|
| `start_time` / `end_time` | `end_time` empty on error |
| `user` / `user_id` | Email + numeric ID |
| `device_id` | Device identifier |
| `client_ip` | Public IPv4 of client |
| `connector` / `connector_id` | Connector name + numeric ID |
| `resource_ip` | Empty on DNS error |
| `resource_port` / `resource_domain` / `resource_id` | Domain empty if direct IP connection |
| `protocol` | `tcp`, `udp`, or `icmp` |
| `status` | `NORMAL`, `DNS_ERROR`, `CONNECTION_FAILED` |
| `bytes_transferred` / `bytes_received` | Empty on error |
| `remote_network` / `remote_network_id` | Network the resource belongs to |
| `applied_rule` | Matched resource pattern (e.g., `*.twingate.com`) |
| `relays` / `relay_ips` / `relay_ports` | Relay identifiers; empty if no relay used |

## JSON Schema (S3 Export)

**Event statuses**: `closed_connection`, `denied_access`, `established_connection`, `failed_to_connect`

**Key fields**:
- `event.connection.error_message` — only present on `denied_access` or `failed_to_connect`
- `event.relays` — empty array if no relay used
- `event.time` — ISO 8601 UTC timestamp
- `event.user` OR `event.service_account` — mutually exclusive; one will be present
- `event.resource.applied_rule` — matched wildcard pattern

## Gotchas

- **Wildcard resources**: Connections to `foo.twingate.com` when `*.twingate.com` is defined will show `resource_id` of the wildcard resource and `applied_rule` = `*.twingate.com`
- **Service accounts vs users**: JSON events have either `user` or `service_account` — never both; CSV does not document service account distinction
- **Error conditions**: `resource_ip` empty on DNS errors; `end_time`, `bytes_transferred`, `bytes_received` all empty on any error
- **Timing**: Established connections only appear in reports after they close — no in-progress streaming

## Related Docs
- Network Events reporting (Admin Console)
- AWS S3 log export configuration
- Twingate Connectors documentation
- Remote Networks documentation