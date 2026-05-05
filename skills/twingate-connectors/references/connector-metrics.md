# Connector Metrics Overview

## Page Title
Twingate Connector Metrics Overview

## Summary
Twingate Connectors can export operational metrics in Prometheus format for monitoring traffic patterns, connection efficiency, and connector health. Metrics are enabled via an environment variable and compatible with standard monitoring tools like Prometheus and Grafana.

## Key Information
- Metrics exported in standard Prometheus format
- Minimum connector version: **v1.80.0**
- Enable by setting `TWINGATE_METRICS_PORT=9999`
- Data scraping endpoint exposed on configured port

## Available Metrics

| Metric | Description |
|--------|-------------|
| `twingate_inbound_bytes_total` | Total inbound bytes, labeled by transport type |
| `twingate_outbound_bytes_total` | Total outbound bytes, labeled by transport type |
| `twingate_connector_uptime_seconds` | Connector uptime in seconds |
| Resource counts | Number of resources handled per connector |

**Transport labels:** `direct`, `relay`

## Prerequisites
- Twingate Connector v1.80.0 or later
- Prometheus-compatible monitoring system

## Step-by-Step Setup
1. Set `TWINGATE_METRICS_PORT=9999` on Connector deployment
2. Configure Prometheus scrape job targeting `<connector-host>:9999`
3. Build dashboards in Grafana or preferred visualization tool

## Configuration Values

| Variable | Value | Description |
|----------|-------|-------------|
| `TWINGATE_METRICS_PORT` | `9999` (example) | Port for Prometheus metrics endpoint |

## Example Metric Output
```
twingate_inbound_bytes_total{transport="direct"} 1234567890
twingate_outbound_bytes_total{transport="relay"} 987654321
twingate_connector_uptime_seconds 86400
```

## Gotchas
- Feature requires connector v1.80.0+; older connectors will not expose metrics
- More metrics are planned but not yet available — do not build critical alerting on completeness of current metric set
- Port `9999` is shown as example; confirm actual default in the full setup guide

## Related Docs
- [Complete Setup Guide](https://www.twingate.com/docs/connector-metrics) — detailed implementation instructions
- Prometheus documentation for scrape configuration
- Grafana dashboard setup