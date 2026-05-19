# Connector Metrics Overview

## Page Title
Twingate Connector Metrics Overview

## Summary
Twingate Connectors can export operational metrics in Prometheus format, providing visibility into traffic patterns, connection efficiency, and connector health. Metrics are enabled via an environment variable and compatible with standard monitoring stacks like Prometheus and Grafana.

## Key Information
- Metrics exported in standard Prometheus format
- Two metric categories: **Traffic Monitoring** and **Connector Health**
- Available metrics:
  - `twingate_inbound_bytes_total{transport="direct|relay"}`
  - `twingate_outbound_bytes_total{transport="direct|relay"}`
  - `twingate_connector_uptime_seconds`
  - Resource counts per Connector
- Transport label distinguishes direct connections vs relay traffic

## Prerequisites
- Twingate Connector **v1.80.0 or later**
- Prometheus-compatible monitoring system

## Step-by-Step Setup
1. Set `TWINGATE_METRICS_PORT=9999` on the Connector
2. Configure Prometheus to scrape the metrics endpoint (`http://<connector-host>:9999`)
3. Build dashboards in Grafana or preferred visualization tool

## Configuration Values

| Variable | Value | Description |
|----------|-------|-------------|
| `TWINGATE_METRICS_PORT` | `9999` (example) | Enables metrics endpoint on specified port |

## Gotchas
- Requires Connector v1.80.0+; older versions do not support metrics export
- Metrics collection is described as expanding — available metrics may change
- Full implementation details are in a separate setup guide (linked as "complete setup guide")

## Related Docs
- [Complete Setup Guide](https://www.twingate.com/docs/connector-metrics-setup) (linked from page)
- Connector deployment documentation