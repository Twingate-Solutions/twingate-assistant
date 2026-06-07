# Detailed Network Event Schema

## Page Title
Detailed Network Event Schemas

## Summary
Twingate network events can be exported in two formats: CSV (via Admin Console download) or JSON (via AWS S3 sync). Each event represents a single completed connection regardless of duration or data volume. Established connections are only reported after completion.

## Key Information

- **Two export formats**: CSV (Admin Console) and JSON (AWS S3)
- Connections reported once completed; `end_time` empty if error occurred
- JSON events stream as newline-delimited single-line records
- JSON supports service accounts OR users (mutually exclusive fields)

## CSV Column Reference

| Column | Notes |
|--------|-------|
| `start_time` / `end_time` | `end_time` empty on error |
| `user` / `user_id` | Email + numeric ID |
| `device_id` | Unique device identifier |
| `client_ip` | Public IPv4 of client |
| `connector` / `connector_id` | Name + numeric ID |
| `resource_ip` | Empty on DNS error |
| `resource_port` / `resource_domain` / `resource_id` | Domain empty if direct IP connection |
| `protocol` | `tcp`, `udp`, or `icmp` |
| `status` | `NORMAL`, `DNS_ERROR`, `CONNECTION_FAILED` |
| `bytes_transferred` / `bytes_received` | Empty on error |
| `remote_network` / `remote_network_id` | |
| `applied_rule` | Actual Resource definition matched (e.g., `*.twingate.com`) |
| `relays` / `relay_ips` / `relay_ports` | Relay routing info |

## JSON Schema Key Fields

```json
{
  "event_type": "network",
  "event": {
    "status": "closed_connection",  // denied_access | established_connection | failed_to_connect
    "time": "2021-08-15T14:30Z",    // ISO 8601, always UTC
    "connection": { "client_ip", "protocol", "bytes_received", "bytes_transferred", "error_message" },
    "connector": { "id", "name" },
    "device": { "id" },
    "resource": { "address", "applied_rule", "id", "ip", "port" },
    "remote_network": { "id", "name" },
    "relays": [{ "ip", "name", "port" }],  // empty list if no relay
    "user": { "email", "id" },             // OR service_account (not both)
    "service_account": { "name", "id", "key", "key_id" }
  }
}
```

## Configuration Values

- **JSON status values**: `closed_connection`, `denied_access`, `established_connection`, `failed_to_connect`
- **CSV status values**: `NORMAL`, `DNS_ERROR`, `CONNECTION_FAILED`
- **Protocols**: `tcp`, `udp`, `icmp`
- **Timestamps**: ISO 8601, always UTC

## Gotchas

- `applied_rule` vs `resource_id`: A wildcard resource like `*.twingate.com` will show the wildcard in `applied_rule` but connections to any subdomain share the same `resource_id`
- `error_message` in JSON only appears when status is `denied_access` or `failed_to_connect`
- `relays` returns empty list `[]` if connection didn't use a relay
- JSON events have either `user` OR `service_account` — never both; handle both cases in parsing logic
- `bytes_transferred`/`bytes_received` are absent in CSV and JSON when errors occur

## Related Docs
- Network Events reporting (Admin Console export)
- AWS S3 integration for log streaming
- Twingate Connectors and Remote Networks configuration