---
source: https://www.twingate.com/docs/detailed-network-event-schema
type: docs
fetched: 2026-08-14
source_version: 62d545d747fce24baab28c5bd832c69b55b9646a0de7a7010552fb919fc47310
---

# Detailed Network Event Schema

## Page Title
Detailed Network Event Schemas

## Summary
Twingate exports network events in two formats: CSV (Admin Console download) and JSON (AWS S3 sync). Each event represents a single connection regardless of duration. Established connections are only reported after completion.

## Key Information

**CSV Export (Admin Console):**
- One line per network event
- Contains timing, user, device, connector, resource, protocol, traffic, and relay fields

**JSON Export (AWS S3):**
- One JSON object per line (NDJSON)
- `event_type` is always `"network"`
- Events have either a `user` or `service_account`, never both
- Empty relay list if connection didn't use a relay
- Timestamps always UTC, ISO 8601 format

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
| `resource_id` | ID of defined Resource (wildcard resources share one ID) |
| `protocol` | `tcp`, `udp`, or `icmp` |
| `status` | `NORMAL`, `DNS_ERROR`, `CONNECTION_FAILED` |
| `bytes_transferred` / `bytes_received` | Empty on error |
| `remote_network` / `remote_network_id` | Name + numeric ID |
| `applied_rule` | Actual resource pattern matched (e.g., `*.twingate.com`) |
| `relays` / `relay_ips` / `relay_ports` | Relay identifiers |

## JSON Field Reference

**Event status values:** `closed_connection`, `denied_access`, `established_connection`, `failed_to_connect`

**Optional fields:**
- `error_message` — only present when status is `denied_access` or `failed_to_connect`
- `user` or `service_account` — mutually exclusive; service account includes `name`, `id`, `key`, `key_id`
- `relays` — empty array `[]` if no relay used

## Gotchas

- **Wildcard resources:** `resource_id` is the same for all connections matching a wildcard resource; use `applied_rule` (JSON) or `resource_domain` (CSV) to see the actual target
- **Error rows:** `end_time`, `bytes_transferred`, `bytes_received`, and `resource_ip` are all empty when a connection error occurs
- **Completion only:** Events are not streamed in real-time; connections appear only after they close
- **Relay field discrepancy:** CSV has flat `relays`/`relay_ips`/`relay_ports` columns; JSON has a structured array of relay objects with `ip`, `name`, `port`
- JSON timestamps are always UTC regardless of account timezone settings

## Related Docs
- Network Events Report (Admin Console)
- AWS S3 Integration for event sync
- Twingate Connectors documentation
- Remote Networks configuration