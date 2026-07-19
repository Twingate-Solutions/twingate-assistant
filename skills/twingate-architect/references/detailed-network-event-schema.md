# Detailed Network Event Schema

## Page Title
Detailed Network Event Schemas

## Summary
Twingate exports network events in two formats: CSV (from Admin Console download) and JSON (via AWS S3 sync). Each event represents a single completed connection. Events are reported once the connection is complete.

## Key Information

- **CSV export**: Admin Console download, one line per connection
- **JSON export**: AWS S3 bucket sync, one JSON object per line (NDJSON)
- Established connections only reported after completion
- `end_time` empty if error occurred (CSV)
- `bytes_transferred`/`bytes_received` empty if error occurred (CSV)
- `resource_ip` empty on DNS errors (CSV)
- JSON events include either `user` or `service_account` (not both)

## CSV Column Reference

| Column | Description |
|--------|-------------|
| `start_time` / `end_time` | Connection timestamps; `end_time` empty on error |
| `user` / `user_id` | User email and numeric ID |
| `device_id` | Device identifier |
| `client_ip` | Client public IPv4 |
| `connector` / `connector_id` | Connector name and numeric ID |
| `resource_ip` / `resource_port` / `resource_domain` / `resource_id` | Resource details |
| `protocol` | `tcp`, `udp`, or `icmp` |
| `status` | `NORMAL`, `DNS_ERROR`, or `CONNECTION_FAILED` |
| `bytes_transferred` / `bytes_received` | Cumulative bytes; empty on error |
| `remote_network` / `remote_network_id` | Remote network name and ID |
| `applied_rule` | Actual resource definition matched (e.g., `*.twingate.com`) |
| `relays` / `relay_ips` / `relay_ports` | Relay identifier, IP, and port |

## JSON Schema (S3 Export)

```json
{
  "event_type": "network",
  "event": {
    "status": "closed_connection",  // "denied_access" | "established_connection" | "failed_to_connect"
    "connection": {
      "client_ip": "string",
      "protocol": "tcp",
      "bytes_received": 512,
      "bytes_transferred": 512,
      "error_message": "string"  // Only on "denied_access" or "failed_to_connect"
    },
    "connector": { "id": "string", "name": "string" },
    "device": { "id": "string" },
    "relays": [{ "ip": "string", "name": "string", "port": 30015 }],  // Empty list if no relay
    "remote_network": { "id": "string", "name": "string" },
    "resource": {
      "address": "string", "applied_rule": "string",
      "id": "string", "ip": "string", "port": 443
    },
    "user": { "email": "string", "id": "string" },       // OR service_account (not both)
    "service_account": { "name": "", "id": "", "key": "", "key_id": "" },
    "time": "2021-08-15T14:30Z"  // UTC ISO 8601
  }
}
```

## Gotchas

- `applied_rule` vs `resource_id`: wildcard resources (e.g., `*.twingate.com`) match multiple FQDNs but share one `resource_id`; `applied_rule` shows the pattern used
- `relays` returns empty list `[]` in JSON if connection didn't use a relay
- JSON `time` field is always UTC
- JSON events have **either** `user` or `service_account`, never both
- CSV `resource_domain` is empty for direct IP connections

## Related Docs
- Network Events reporting / Admin Console exports
- AWS S3 SIEM integration setup
- Twingate Connector documentation