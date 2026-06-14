# Detailed Network Event Schemas

## Summary
Twingate exports network events in two formats: CSV (from Admin Console download) and JSON (via AWS S3 sync). Each event represents a single completed connection. Established connections are only reported after completion.

## Key Information

- CSV exports: one line per connection, downloaded from Admin Console
- JSON exports: one line per connection, synced to AWS S3 buckets
- Connections reported only after completion; `end_time` empty if error occurred
- JSON events include 4 status types; CSV uses 3 status values
- Events can belong to either a User or Service Account (mutually exclusive in JSON)

## CSV Column Reference

| Column | Notes |
|---|---|
| `start_time` / `end_time` | `end_time` empty on error |
| `user` / `user_id` | Email + numeric ID |
| `device_id` | Unique device identifier |
| `client_ip` | Public IPv4 of client |
| `connector` / `connector_id` | Name + numeric ID |
| `resource_ip` | Empty on DNS error |
| `resource_port` | Target port |
| `resource_domain` | FQDN; empty if direct IP connection |
| `resource_id` | ID of matching Twingate Resource definition |
| `protocol` | `tcp`, `udp`, or `icmp` |
| `status` | `NORMAL`, `DNS_ERROR`, `CONNECTION_FAILED` |
| `bytes_transferred` / `bytes_received` | Empty on error |
| `remote_network` / `remote_network_id` | Name + numeric ID |
| `applied_rule` | Actual Resource definition matched (e.g., `*.twingate.com`) |
| `relays` / `relay_ips` / `relay_ports` | Relay routing info |

## JSON Schema (S3)

**Top-level fields:**
- `event_type`: `"network"`
- `event.status`: `closed_connection`, `denied_access`, `established_connection`, `failed_to_connect`
- `event.time`: ISO 8601 UTC timestamp

**Nested objects:**
- `connection`: `client_ip`, `protocol`, `bytes_received`, `bytes_transferred`, `error_message` (only on `denied_access`/`failed_to_connect`)
- `connector`: `id`, `name`
- `device`: `id`
- `relays`: array of `{ip, name, port}`; empty list if no relay used
- `remote_network`: `id`, `name`
- `resource`: `address`, `applied_rule`, `id`, `ip`, `port`
- `user` OR `service_account`: mutually exclusive; `user` has `email` + `id`

## Gotchas

- **`applied_rule` vs `resource_id`**: `resource_id`/`applied_rule` reflect the *defined* Resource pattern (e.g., `*.twingate.com`), not the specific hostname connected to — all matching connections share the same ID
- **`resource_ip` empty**: occurs on DNS resolution failure, not connection failure
- **`end_time` empty**: only on error conditions in CSV
- **`error_message`** in JSON only appears for `denied_access` or `failed_to_connect` statuses
- **JSON has more granular statuses** (4) than CSV (3)
- **Service Account vs User**: JSON events contain one or the other, never both

## Related Docs
- Network Events reporting (Admin Console)
- AWS S3 integration for event sync
- Twingate Connectors and Remote Networks configuration