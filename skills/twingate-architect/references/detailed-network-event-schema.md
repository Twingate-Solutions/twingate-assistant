# Detailed Network Event Schema

## Page Title
Detailed Network Event Schemas

## Summary
Twingate exports network events in two formats: CSV (Admin Console download) and JSON (AWS S3 sync). Each event represents a single completed connection. Events are only reported after connections complete.

## Key Information
- CSV exports: one line per connection event
- JSON exports: one JSON object per line (newline-delimited)
- Established connections reported only after completion
- Both formats support relay, resource, user/service account, and connector metadata

## CSV Column Reference

| Column | Notes |
|--------|-------|
| `start_time` / `end_time` | `end_time` empty on error |
| `user` / `user_id` | Email + numeric ID |
| `device_id` | Device identifier |
| `client_ip` | Public IPv4 of client |
| `connector` / `connector_id` | Name + numeric ID |
| `resource_ip` | Empty on DNS error |
| `resource_port` | Target port |
| `resource_domain` | FQDN; empty if direct IP |
| `resource_id` | ID of defined Resource (wildcard resources share one ID) |
| `protocol` | `tcp`, `udp`, or `icmp` |
| `status` | `NORMAL`, `DNS_ERROR`, `CONNECTION_FAILED` |
| `bytes_transferred` / `bytes_received` | Empty on error |
| `remote_network` / `remote_network_id` | |
| `applied_rule` | Matched Resource definition (e.g., `*.twingate.com`) |
| `relays` / `relay_ips` / `relay_ports` | Relay identifiers |

## JSON Schema (S3 Export)

**Top-level fields:**
- `event_type`: always `"network"`
- `event.status`: `closed_connection`, `denied_access`, `established_connection`, `failed_to_connect`
- `event.time`: ISO 8601 UTC timestamp

**Nested objects:**
- `event.connection`: `client_ip`, `protocol`, `bytes_received`, `bytes_transferred`, `error_message` *(optional: only on `denied_access` or `failed_to_connect`)*
- `event.connector`: `id`, `name`
- `event.device`: `id`
- `event.relays`: array of `{ip, name, port}`; empty list if no relay used
- `event.remote_network`: `id`, `name`
- `event.resource`: `address`, `applied_rule`, `id`, `ip`, `port`
- `event.user` OR `event.service_account`: mutually exclusive; user has `email` + `id`; service account has `name`, `id`, `key`, `key_id`

## Gotchas
- `resource_id` is the **defined** resource ID — wildcard resources (e.g., `*.twingate.com`) give the same ID to all matched connections
- `applied_rule` shows the **defined** resource pattern, not the actual hostname connected to
- `end_time`, `resource_ip`, `bytes_transferred`, `bytes_received` are **empty** on error conditions
- JSON events have **either** `user` or `service_account`, never both
- Relay list is empty `[]` if connection did not use a relay
- JSON timestamps always UTC; CSV timestamp format not specified

## Related Docs
- Network Events reporting (Admin Console)
- AWS S3 integration for event sync
- Twingate Connectors and Remote Networks configuration