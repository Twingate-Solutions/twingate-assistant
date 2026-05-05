## Connector Real-Time Logs

How to enable, read, and integrate Twingate Connector logs including service logs and per-connection network traffic logs.

**Service Log Levels (TWINGATE_LOG_LEVEL):**
- Level 3 (default): ERROR only
- Level 4: WARN+
- Level 5: INFO+
- Level 7: DEBUG (verbose — not recommended for extended periods due to storage impact)
- Set in `/etc/twingate/connector.conf` or Docker environment

**Real-Time Traffic Logs (TWINGATE_LOG_ANALYTICS=v2):**
- Outputs per-connection logs to stdout as single-line JSON prefixed with `ANALYTICS`
- Enable per deployment type:
  - Docker: `--env TWINGATE_LOG_ANALYTICS="v2"` in the run command
  - systemd: add `TWINGATE_LOG_ANALYTICS=v2` to `/etc/twingate/connector.conf`
  - Helm: set via the `env` parameter in the Helm chart
- Read systemd logs: `journalctl -u twingate-connector -n 100 -f`
- Filter lines: starts with `ANALYTICS`

**Connection Log Schema (v2) Key Fields:**
- `event_type`: `established_connection`, `closed_connection`, or error state
- `connection.id`: shared across established + closed events for the same connection
- `connection.client_ip`: internet-facing NAT address of the client
- `connection.resource_ip`: private IP resolved by the Connector (not the DNS name)
- `connection.rx` / `connection.tx`: bytes received/transmitted over the connection lifetime
- `connection.tunnel_path`: `direct` or `relay`
- `connection.tunnel_proto`: e.g., `quic/udp`
- `connection.duration`: connection duration in milliseconds
- `resource.address`: Resource address as defined in Admin Console
- `resource.applied_rule`: the wildcard rule that matched (e.g., `*.website.com`)
- `location`: stringified JSON with GeoIP data for the client IP
- `user.email`, `device.id`, `connector.name`, `remote_network.name`

**SIEM Integration (Vector example):**
- Source: `journald`, filter for lines starting with `ANALYTICS`, then parse the JSON payload with a grok pattern
- See /docs/siem-guide for the full Vector configuration snippet

**Related Docs:**
- /docs/siem-guide -- SIEM integration options (Syslog, Vector, Datadog, S3)
- /docs/exporting-network-traffic -- Historical network traffic export
- /docs/advanced-connector-management -- Advanced Connector features index
