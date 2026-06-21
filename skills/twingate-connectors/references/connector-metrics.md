# Connector Metrics Overview

## Page Title
Connector Metrics Overview

## Summary
Twingate Connectors (v1.80.0+) export operational metrics in Prometheus format via a configurable HTTP endpoint. Metrics cover traffic bytes, transport type (direct vs relay), uptime, and resource counts. Integrates with standard Prometheus/Grafana monitoring stacks.

## Key Information
- Metrics exported in standard Prometheus exposition format
- Available metric types:
  - `twingate_inbound_bytes_total{transport="direct|relay"}` — total inbound data
  - `twingate_outbound_bytes_total{transport="direct|relay"}` — total outbound data
  - `twingate_connector_uptime_seconds` — connector availability duration
  - Resource counts per Connector
- Transport label distinguishes direct connections from relay-routed traffic
- Additional metrics planned (not yet available)

## Prerequisites
- Connector version **v1.80.0 or later**
- Prometheus-compatible monitoring system (Prometheus, Grafana, etc.)

## Step-by-Step Setup
1. Set environment variable `TWINGATE_METRICS_PORT=9999` on the Connector
2. Configure Prometheus scrape job targeting the Connector host on the specified port
3. (Optional) Build dashboards in Grafana or equivalent tool

## Configuration Values

| Variable | Value | Description |
|----------|-------|-------------|
| `TWINGATE_METRICS_PORT` | `9999` (example) | Port exposing the Prometheus metrics endpoint |

- Metrics endpoint path not explicitly documented on this page — see linked setup guide
- Port value is configurable; `9999` used as example

## Gotchas
- Requires Connector **v1.80.0+**; older versions do not support metrics export
- Metric set is incomplete/expanding — do not rely on current list as exhaustive
- No authentication mechanism for the metrics endpoint mentioned; treat as internal-only exposure

## Related Docs
- [Complete Setup Guide](https://www.twingate.com/docs/connector-metrics) (linked from page as "complete setup guide") — detailed implementation instructions