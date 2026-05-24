# Connector Metrics Overview

## Page Title
Twingate Connector Metrics Overview

## Summary
Twingate Connectors can export operational metrics in Prometheus format, providing visibility into traffic patterns, connection efficiency, and connector health. Metrics are enabled via an environment variable and scraped by standard Prometheus-compatible tools.

## Key Information
- Metrics exported in standard Prometheus format
- Compatible with Prometheus, Grafana, and similar monitoring stacks
- Minimum connector version: **v1.80.0**
- Metrics endpoint enabled by setting `TWINGATE_METRICS_PORT`

## Available Metrics
| Metric | Description |
|--------|-------------|
| `twingate_inbound_bytes_total{transport="direct\|relay"}` | Inbound data transferred, by transport type |
| `twingate_outbound_bytes_total{transport="direct\|relay"}` | Outbound data transferred, by transport type |
| `twingate_connector_uptime_seconds` | Connector uptime in seconds |
| Resource counts | Number of resources handled per connector |

## Prerequisites
- Twingate Connector **v1.80.0 or later**
- Prometheus-compatible monitoring system
- Access to configure connector environment variables

## Step-by-Step Setup
1. Set `TWINGATE_METRICS_PORT=9999` on your Twingate Connector
2. Configure Prometheus to scrape the connector's metrics endpoint (e.g., `http://<connector-host>:9999/metrics`)
3. Connect Prometheus to Grafana or preferred visualization tool
4. Build dashboards and configure alerts

## Configuration Values
| Variable | Value | Description |
|----------|-------|-------------|
| `TWINGATE_METRICS_PORT` | `9999` (example) | Enables metrics endpoint on specified port |

## Gotchas
- Metrics collection is described as actively expanding — metric names/labels may change in future versions
- Port `9999` is shown as an example; verify actual default or allowed port range in the full setup guide
- Transport label values are `direct` or `relay` — useful for identifying relay-heavy traffic that may indicate NAT traversal issues

## Related Docs
- [Complete Setup Guide](https://www.twingate.com/docs/connector-metrics-setup) — detailed implementation instructions (linked from overview page)
- Twingate Connector deployment documentation