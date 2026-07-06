# Connector Metrics Overview

## Page Title
Twingate Connector Metrics Overview

## Summary
Twingate Connectors can export operational metrics in Prometheus format, providing visibility into traffic patterns, connection efficiency, and connector health. Metrics are compatible with standard monitoring tools like Prometheus and Grafana. Feature requires Connector v1.80.0 or later.

## Key Information
- Metrics exported in standard Prometheus format
- Two metric categories: **Traffic Monitoring** and **Connector Health**
- Available metrics:
  - `twingate_inbound_bytes_total{transport="direct|relay"}` — total inbound data
  - `twingate_outbound_bytes_total{transport="direct|relay"}` — total outbound data
  - `twingate_connector_uptime_seconds` — connector availability
  - Resource counts per connector
- Transport label distinguishes **direct** connections vs **relay** usage
- More metrics planned (not yet available)

## Prerequisites
- Twingate Connector **v1.80.0 or later**
- Prometheus-compatible monitoring system (Prometheus, Grafana, etc.)

## Step-by-Step
1. Set `TWINGATE_METRICS_PORT=9999` on each Connector
2. Configure Prometheus scrape job targeting the metrics endpoint
3. Build dashboards in Grafana or equivalent tool

## Configuration Values

| Variable | Value | Description |
|---|---|---|
| `TWINGATE_METRICS_PORT` | `9999` (example) | Enables metrics export; port is configurable |

## Gotchas
- Metrics endpoint is **not enabled by default** — must set `TWINGATE_METRICS_PORT`
- Minimum Connector version **v1.80.0** required; older connectors do not support this feature
- Metrics collection is described as actively expanding — available metrics may change
- Full implementation details are in a separate setup guide (linked as "complete setup guide")

## Related Docs
- [Complete Setup Guide](https://www.twingate.com/docs/connector-metrics-setup) — detailed implementation instructions
- Twingate Connector deployment documentation