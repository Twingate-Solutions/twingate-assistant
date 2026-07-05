# Detailed Network Event Schemas

## Page Title
Detailed Network Event Schemas

## Summary
Twingate exports network events in two formats: CSV (from Admin Console download) and JSON (via AWS S3 sync). Each event represents a single completed connection regardless of duration or data volume. Established connections are only reported after completion.

## Key Information

### CSV Export (Admin Console)
Each row = one connection event.

| Column | Notes |
|--------|-------|
| `start_time` / `end_time` | `end_time` empty on error |
| `user` / `user_id` | Email + numeric ID |
| `device_id` | Device identifier |
| `client_ip` | Public IPv4 of client |
| `connector` / `connector_id` | Connector name + numeric ID |
| `resource_ip` | Empty on DNS error |
| `resource_port` | Target port |
| `resource_domain` | FQDN; empty if direct IP connection |
| `resource_id` | ID of matching Resource definition (wildcard resources share one ID) |
| `protocol` | `tcp`, `udp`, or `icmp` |
| `status` | `NORMAL`, `DNS_ERROR`, `CONNECTION_FAILED` |
| `bytes_transferred` / `bytes_received` | Empty on error |
| `remote_network` / `remote_network_id` | Remote Network name + ID |
| `applied_rule` | Actual Resource definition matched (e.g., `*.twingate.com`) |
| `relays` / `relay_ips` / `relay_ports` | Relay identifiers/IPs/ports |

### JSON Export (AWS S3)
One JSON object per line (NDJSON).

**Top-level structure:**
```json
{
  "event_type": "network",
  "event": { ... }
}
```

**`event.status` values:** `closed_connection`, `denied_access`, `established_connection`, `failed_to_connect`

**Key nested objects:**
- `connection`: `client_ip`, `protocol`, `bytes_received`, `bytes_transferred`, `error_message` (optional)
- `connector`: `id`, `name`
- `device`: `id`
- `relays`: array of `{ip, name, port}` — empty list if no relay used
- `remote_network`: `id`, `name`
- `resource`: `address`, `applied_rule`, `id`, `ip`, `port`
- `user`: `email`, `id` (optional — either user OR service_account present)
- `service_account`: `name`, `id`, `key`, `key_id` (optional)
- `time`: ISO 8601 UTC string

## Gotchas

- **Wildcard resources**: `resource_id` and `applied_rule` reflect the *defined* resource pattern, not the specific hostname accessed. Multiple connections to different subdomains share the same `resource_id`.
- **Error conditions**: `resource_ip`, `end_time`, `bytes_transferred`, `bytes_received` are empty in CSV when errors occur.
- **User vs. Service Account**: JSON events contain *either* a `user` object or a `service_account` object, never both (or neither explicitly stated).
- **`error_message`** in JSON only appears when status is `denied_access` or `failed_to_connect`.
- **Relay field**: Empty array `[]` in JSON means direct connection (no relay). CSV has separate relay columns.
- **Timestamps**: JSON `time` field is always UTC ISO 8601.

## Related Docs
- Network Events reporting (Admin Console)
- AWS S3 integration for log syncing
- Twingate Connectors and Remote Networks configuration