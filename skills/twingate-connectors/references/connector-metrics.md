# Connector Metrics Overview

## Page Title
Twingate Connector Metrics Overview

## Summary
Twingate Connectors can export operational metrics in Prometheus format, providing visibility into traffic patterns, connection efficiency, and connector health. Metrics are enabled via environment variable and compatible with standard monitoring stacks like Prometheus and Grafana.

## Key Information
- Metrics exported in standard Prometheus format
- Two metric categories: **Traffic Monitoring** and **Connector Health**
- Available metrics:
  - `twingate_inbound_bytes_total{transport="direct|relay"}` — inbound data by transport type
  - `twingate_outbound_bytes_total{transport="direct|relay"}` — outbound data by transport type
  - `twingate_connector_uptime_seconds` — connector availability duration
  - Resource counts per connector
- Transport labels distinguish `direct` connections vs `relay` usage
- More metrics planned

## Prerequisites
- Twingate Connector **v1.80.0 or later**
- Prometheus-compatible monitoring system

## Step-by-Step Setup
1. Set `TWINGATE_METRICS_PORT=9999` on the Connector
2. Configure Prometheus to scrape the metrics endpoint
3. Build dashboards in Grafana or preferred visualization tool

## Configuration Values

| Variable | Value | Description |
|---|---|---|
| `TWINGATE_METRICS_PORT` | `9999` (example) | Port to expose Prometheus metrics endpoint |

## Gotchas
- Requires Connector v1.80.0+; older versions do not support metrics export
- Metrics collection is still expanding — available metrics may be limited compared to future releases
- Port value `9999` shown as example; confirm actual default in the [complete setup guide](https://www.twingate.com/docs/connector-metrics-setup)

## Related Docs
- [Complete Setup Guide](https://www.twingate.com/docs/connector-metrics-setup) — detailed implementation instructions