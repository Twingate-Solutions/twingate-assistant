# Connector Metrics Overview

## Page Title
Twingate Connector Metrics Overview

## Summary
Twingate Connectors can export operational metrics in Prometheus format, providing visibility into traffic patterns, connection efficiency, and connector health. Metrics are compatible with standard monitoring tools like Prometheus and Grafana. Enabled via a single environment variable on Connector v1.80.0+.

## Key Information
- **Metrics format**: Standard Prometheus exposition format
- **Available metrics**:
  - `twingate_inbound_bytes_total{transport="direct"|"relay"}` — total inbound data
  - `twingate_outbound_bytes_total{transport="direct"|"relay"}` — total outbound data
  - `twingate_connector_uptime_seconds` — connector availability
  - Resource counts per connector
- Transport label distinguishes **direct** connections vs **relay** usage
- More metrics planned but not yet available

## Prerequisites
- Twingate Connector **v1.80.0 or later**
- Prometheus-compatible monitoring system (Prometheus, Grafana, etc.)

## Step-by-Step Setup
1. Set `TWINGATE_METRICS_PORT=9999` on the Connector
2. Configure Prometheus to scrape the metrics endpoint (e.g., `http://<connector-host>:9999/metrics`)
3. Build dashboards in Grafana or preferred visualization tool

## Configuration Values
| Variable | Value | Description |
|---|---|---|
| `TWINGATE_METRICS_PORT` | `9999` (example) | Port to expose Prometheus metrics endpoint |

## Gotchas
- Feature requires **v1.80.0+**; older connectors do not support metrics export
- Port `9999` is shown as an example — verify actual default or allowed port range in the full setup guide
- Metrics collection is described as actively expanding; available metrics may change

## Related Docs
- [Complete Setup Guide](https://www.twingate.com/docs/connector-metrics-setup) — detailed implementation instructions (linked from page as "complete setup guide")