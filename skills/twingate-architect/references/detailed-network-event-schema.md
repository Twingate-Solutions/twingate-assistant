# Detailed Network Event Schemas

## Summary
Twingate exports network events in two formats: CSV (from Admin Console download) and JSON (synced to AWS S3). Each event represents a single completed connection. Established connections are only reported after completion.

## Key Information

- CSV export: one line per connection event
- JSON export: newline-delimited JSON to AWS S3
- Connections only logged after completion (not in real-time)
- `end_time` / `bytes_*` fields empty on error conditions
- JSON events include either a `user` OR `service_account` object, not both
- Relay list is empty array `[]` if connection didn't use a relay

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
| `remote_network` / `remote_network_id` | Network name + ID |
| `applied_rule` | Matched resource rule (e.g., `*.twingate.com`) |
| `relays` / `relay_ips` / `relay_ports` | Relay identifiers |

## JSON Field Reference

**Event-level fields:**
- `event_type`: always `"network"`
- `event.status`: `closed_connection`, `denied_access`, `established_connection`, `failed_to_connect`
- `event.time`: ISO 8601 UTC datetime string

**Nested objects:**
- `connection`: `client_ip`, `protocol`, `bytes_received`, `bytes_transferred`, `error_message` (optional, only on `denied_access` or `failed_to_connect`)
- `connector`: `id`, `name`
- `device`: `id`
- `relays[]`: `ip`, `name`, `port` (empty array if no relay)
- `remote_network`: `id`, `name`
- `resource`: `address`, `applied_rule`, `id`, `ip`, `port`
- `user` (optional): `email`, `id`
- `service_account` (optional): `name`, `id`, `key`, `key_id`

## Gotchas

- `resource_id` and `applied_rule` reflect the **defined** resource pattern (e.g., `*.twingate.com`), not the specific hostname accessed — group by `applied_rule` for wildcard resources
- `resource_ip` empty on DNS errors; `resource_domain` empty on direct-IP connections
- JSON `event.status` values differ from CSV `status` values — not interchangeable
- Service account events have no `user` field; user events have no `service_account` field — handle both cases in parsers

## Related Docs
- Network Events reporting configuration
- AWS S3 sync setup
- Admin Console export