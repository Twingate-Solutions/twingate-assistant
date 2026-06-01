# Detailed Network Event Schema

## Page Title
Detailed Network Event Schemas

## Summary
Twingate exports network events in two formats: CSV (via Admin Console download) and JSON (via AWS S3 sync). Each event represents a single completed connection regardless of duration or data volume. Established connections are only reported after completion.

## Key Information

- **CSV export**: Admin Console download, one line per connection
- **JSON export**: AWS S3 bucket sync, one JSON object per line
- Connections only reported **after completion** (not in real-time)
- `end_time` is empty if an error occurred
- `bytes_transferred`/`bytes_received` are empty if an error occurred
- `resource_ip` is empty on DNS errors
- Network events have either a `user` OR `service_account` (not both)

## CSV Column Reference

| Column | Notes |
|---|---|
| `start_time` / `end_time` | end_time empty on error |
| `user` / `user_id` | Email + numeric ID |
| `device_id` | Unique device identifier |
| `client_ip` | Public IPv4 of client |
| `connector` / `connector_id` | Name + numeric ID |
| `resource_ip` / `resource_port` / `resource_domain` / `resource_id` | ip empty on DNS error; domain empty for direct-IP connections |
| `protocol` | `tcp`, `udp`, or `icmp` |
| `status` | `NORMAL`, `DNS_ERROR`, `CONNECTION_FAILED` |
| `bytes_transferred` / `bytes_received` | Empty on error |
| `remote_network` / `remote_network_id` | |
| `applied_rule` | Matched resource pattern (e.g., `*.twingate.com`) |
| `relays` / `relay_ips` / `relay_ports` | Relay routing info |

## JSON Schema (S3 Export)

**Top-level structure:**
- `event_type`: `"network"`
- `event.status`: `closed_connection`, `denied_access`, `established_connection`, `failed_to_connect`
- `event.time`: ISO 8601 UTC datetime

**Key nested objects:**
- `connection`: `client_ip`, `protocol`, `bytes_received`, `bytes_transferred`, `error_message` *(optional, only on `denied_access`/`failed_to_connect`)*
- `connector`: `id`, `name`
- `device`: `id`
- `relays`: array of `{ip, name, port}` — **empty list if no relay used**
- `remote_network`: `id`, `name`
- `resource`: `address`, `applied_rule`, `id`, `ip`, `port`
- `user`: `email`, `id` *(optional)*
- `service_account`: `name`, `id`, `key`, `key_id` *(optional)*

## Gotchas

- `resource_id` is the Twingate-defined resource; wildcard resources (e.g., `*.twingate.com`) share one ID across all matching connections
- `applied_rule` shows the **pattern** matched, not the actual hostname accessed
- JSON export: `user` and `service_account` are mutually exclusive fields
- Relay list in JSON is empty `[]` when connection is direct (no relay)
- CSV `status` values differ from JSON `status` values (different naming conventions)

## Related Docs
- Network Events reporting configuration
- AWS S3 integration setup
- Twingate Admin Console export