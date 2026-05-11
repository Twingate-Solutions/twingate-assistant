# Detailed Network Event Schema

## Page Title
Detailed Network Event Schemas

## Summary
Twingate exports network events in two formats: CSV (Admin Console download) and JSON (AWS S3 sync). Each event represents a single connection regardless of duration or data volume. Established connections are only reported after completion.

## Key Information
- **CSV export**: One line per network event, downloaded from Admin Console
- **JSON export**: One line per network event, synced to AWS S3 buckets
- Connections only appear in reports after they complete
- `end_time` (CSV) and `bytes_*` fields are empty if an error occurred

## CSV Column Reference

| Column | Description |
|--------|-------------|
| `start_time` / `end_time` | Connection timespan; `end_time` empty on error |
| `user` / `user_id` | Email + numeric ID |
| `device_id` | Device identifier |
| `client_ip` | Public IPv4 of client |
| `connector` / `connector_id` | Connector name + numeric ID |
| `resource_ip` | Empty if DNS error |
| `resource_port` | Target port |
| `resource_domain` | FQDN; empty if direct IP connection |
| `resource_id` | Numeric ID (wildcard resources share one ID) |
| `protocol` | `tcp`, `udp`, or `icmp` |
| `status` | `NORMAL`, `DNS_ERROR`, or `CONNECTION_FAILED` |
| `bytes_transferred` / `bytes_received` | Empty on error |
| `remote_network` / `remote_network_id` | Remote Network name + ID |
| `applied_rule` | Matched Resource definition (e.g., `*.twingate.com`) |
| `relays` / `relay_ips` / `relay_ports` | Relay routing info |

## JSON Schema (S3 Export)

**`event.status` values:** `closed_connection`, `denied_access`, `established_connection`, `failed_to_connect`

**Key fields:**
- `event_type`: always `"network"`
- `event.time`: ISO 8601 UTC timestamp
- `event.connection.error_message`: only present on `denied_access` or `failed_to_connect`
- `event.relays`: empty list `[]` if no relay used
- `event.user` OR `event.service_account`: mutually exclusive (one per event)
- `event.resource.applied_rule`: matched wildcard/rule definition

## Gotchas
- **Wildcard resources**: Connections to `foo.twingate.com` when `*.twingate.com` is defined will share the same `resource_id`; `applied_rule` shows the pattern, not the actual hostname
- **Error events**: `bytes_transferred`, `bytes_received`, and `end_time` are omitted/empty on errors
- **User vs. Service Account**: JSON events contain either a `user` or `service_account` object, never both
- **Relay field**: Empty list in JSON means direct connection (no relay); in CSV, field may be empty
- **Timestamps**: JSON times are always UTC; CSV format not explicitly specified

## Related Docs
- Network Events reporting (Admin Console)
- AWS S3 integration for event sync
- Twingate Connectors and Remote Networks configuration