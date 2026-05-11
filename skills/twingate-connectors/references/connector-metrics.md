# Connector Metrics Overview

## Page Title
Twingate Connector Metrics Overview

## Summary
Twingate Connectors can export operational metrics in Prometheus format, providing visibility into traffic patterns, connection efficiency, and connector health. Metrics are enabled via an environment variable and are compatible with standard monitoring tools like Prometheus and Grafana.

## Key Information
- Metrics exported in standard Prometheus format
- Minimum connector version: **v1.80.0**
- Metrics endpoint enabled via `TWINGATE_METRICS_PORT` environment variable

## Available Metrics
| Metric | Description |
|--------|-------------|
| `twingate_inbound_bytes_total{transport="direct\|relay"}` | Inbound bytes by transport type |
| `twingate_outbound_bytes_total{transport="direct\|relay"}` | Outbound bytes by transport type |
| `twingate_connector_uptime_seconds` | Connector uptime in seconds |
| Resource counts | Total resources handled per connector |

## Prerequisites
- Twingate Connector v1.80.0 or later
- Prometheus-compatible monitoring system
- (Optional) Grafana or other visualization tool

## Step-by-Step Setup
1. Set `TWINGATE_METRICS_PORT=9999` on the Connector
2. Configure Prometheus to scrape the metrics endpoint (e.g., `http://<connector-host>:9999/metrics`)
3. Build dashboards in Grafana or preferred visualization tool

## Configuration Values
| Variable | Value | Description |
|----------|-------|-------------|
| `TWINGATE_METRICS_PORT` | `9999` (example) | Enables metrics HTTP endpoint on specified port |

## Gotchas
- Connector must be **v1.80.0 or later** — older versions do not support metrics export
- Transport label values are `direct` or `relay` — useful for identifying relay-heavy traffic that may indicate NAT traversal issues
- Metrics collection is described as actively expanding; available metrics may change

## Related Docs
- [Complete Setup Guide](https://www.twingate.com/docs/connector-metrics) (linked as "complete setup guide" on source page)
- Prometheus documentation for scrape configuration
- Grafana dashboard setup