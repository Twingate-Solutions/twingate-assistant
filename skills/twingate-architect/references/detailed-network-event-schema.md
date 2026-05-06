# Detailed Network Event Schema

## Page Title
Detailed Network Event Schemas

## Summary
Twingate exports network events in two formats: CSV (from Admin Console download) and JSON (synced to AWS S3). Each event represents a single connection regardless of duration, and established connections are only reported after completion.

## Key Information

- Two export formats: **CSV** (Admin Console) and **JSON** (AWS S3 sync)
- Each network event = one line/record per connection
- Connections only reported after they complete
- `end_time` and byte counts are empty if an error occurred
- JSON events are newline-delimited

## CSV Column Reference

| Column | Notes |
|---|---|
| `start_time` / `end_time` | `end_time` empty on error |
| `user` / `user_id` | Email + numeric ID |
| `device_id` | Unique device identifier |
| `client_ip` | Public IPv4 of client |
| `connector` / `connector_id` | Name + numeric ID |
| `resource_ip` | Empty on DNS error |
| `resource_port` / `resource_domain` / `resource_id` | `resource_domain` empty for direct IP connections |
| `protocol` | `tcp`, `udp`, or `icmp` |
| `status` | `NORMAL`, `DNS_ERROR`, `CONNECTION_FAILED` |
| `bytes_transferred` / `bytes_received` | Empty on error |
| `remote_network` / `remote_network_id` | Network container for the resource |
| `applied_rule` | Matched resource definition (e.g., `*.twingate.com`) |
| `relays` / `relay_ips` / `relay_ports` | Relay routing details |

## JSON Schema (S3 Export)

**Top-level fields:**
- `event_type`: always `"network"`
- `event.status`: `closed_connection`, `denied_access`, `established_connection`, `failed_to_connect`
- `event.time`: ISO 8601 UTC timestamp

**Nested objects:**
- `connection`: `client_ip`, `protocol`, `bytes_received`, `bytes_transferred`, `error_message` *(optional, only on `denied_access` or `failed_to_connect`)*
- `connector`: `id`, `name`
- `device`: `id`
- `relays`: array of `{ip, name, port}`; empty list if no relay used
- `remote_network`: `id`, `name`
- `resource`: `address`, `applied_rule`, `id`, `ip`, `port`
- `user`: `email`, `id` *(optional — mutually exclusive with `service_account`)*
- `service_account`: `name`, `id`, `key`, `key_id` *(optional — mutually exclusive with `user`)*

## Gotchas

- **`applied_rule` vs `resource_id`**: A wildcard resource like `*.twingate.com` gives all matching connections the same `resource_id`, but `applied_rule` shows the wildcard pattern, not the actual destination
- **Mutually exclusive fields**: JSON events have either `user` OR `service_account`, never both
- **Empty relay list**: Relay fields present but empty when connection is direct (no relay)
- **Error records**: `bytes_transferred`, `bytes_received`, and `end_time` are omitted/empty on failed connections

## Related Docs
- Network Events reporting (Admin Console)
- AWS S3 integration for log export
- Twingate Connectors and Remote Networks configuration