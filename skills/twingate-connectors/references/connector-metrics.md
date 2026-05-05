## Connector Metrics

Twingate Connectors can export operational metrics in Prometheus format for monitoring and observability. Requires Connector v1.80.0 or later.

**Enabling Metrics:**
- Set `TWINGATE_METRICS_PORT=9999` (or any unused port) as an environment variable on each Connector
- Metrics exposed at `http://<connector-ip>:<port>/metrics`

**Available Metrics:**
- `twingate_inbound_bytes_total{transport="direct"|"relay"}` -- inbound bytes by transport type
- `twingate_outbound_bytes_total{transport="direct"|"relay"}` -- outbound bytes by transport type
- `twingate_connector_uptime_seconds` -- Connector uptime
- Resource counts per Connector (additional metrics in development)

**Integration:**
- Compatible with Prometheus, Grafana, and any Prometheus-compatible monitoring tool
- See /docs/connector-monitoring for a full Prometheus + Grafana setup guide with alerting

**Use Cases:**
- Monitor relay vs. direct connection ratios (high relay % indicates P2P issues)
- Track Connector uptime and set alerts for downtime
- Capacity planning based on bytes-transferred trends

**Related Docs:**
- /docs/connector-monitoring -- Full Prometheus + Grafana setup walkthrough
- /docs/advanced-connector-management -- Advanced Connector features index
