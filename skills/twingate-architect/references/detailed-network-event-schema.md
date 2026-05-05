## Detailed Network Event Schema

Schema reference for network event exports: CSV format from the Admin Console and JSON format from AWS S3 sync. Each completed connection is one row or line.

**CSV Columns (Admin Console Export):**
- `start_time`, `end_time` -- connection window (end_time empty on error)
- `user`, `user_id` -- connecting user email and ID
- `device_id` -- unique device identifier
- `client_ip` -- public IPv4 of the client
- `connector`, `connector_id` -- Connector used
- `resource_ip`, `resource_port`, `resource_domain`, `resource_id` -- Resource details (domain empty for IP-only connections)
- `protocol` -- `tcp`, `udp`, or `icmp`
- `status` -- `NORMAL`, `DNS_ERROR`, or `CONNECTION_FAILED`
- `bytes_transferred`, `bytes_received` -- cumulative bytes (empty on error)
- `remote_network`, `remote_network_id` -- Remote Network name and ID
- `applied_rule` -- the Resource definition matched (e.g., `*.twingate.com` for connection to `foo.twingate.com`)
- `relays`, `relay_ips`, `relay_ports` -- Relay routing info (empty if P2P)

**JSON Schema (S3 Export):**
- `event_type`: `"network"`
- `event.status`: `closed_connection`, `denied_access`, `established_connection`, `failed_to_connect`
- `event.connection`: client_ip, protocol, bytes_received, bytes_transferred, error_message (optional)
- `event.connector`: id, name
- `event.resource`: address, applied_rule, id, ip, port
- `event.relays`: list of relay objects (ip, name, port); empty list if P2P
- `event.user` OR `event.service_account`: one present per event
- `event.time`: UTC ISO 8601

**Related Docs:**
- /docs/network-events-ac-export -- How to generate the network event export
- /docs/network-summary-export -- Aggregated summary export
- /docs/syncing-data-to-s3 -- S3 sync setup
