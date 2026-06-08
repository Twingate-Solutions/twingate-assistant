# Connector Metrics Overview

## Page Title
Twingate Connector Metrics Overview

## Summary
Twingate Connectors can export operational metrics in Prometheus format for monitoring traffic patterns, connection efficiency, and connector health. Metrics are compatible with standard tools like Prometheus and Grafana. Requires Connector v1.80.0 or later.

## Key Information
- Metrics exported in standard Prometheus format
- Two metric categories: **Traffic Monitoring** and **Connector Health**
- More metrics planned for future releases

### Available Metrics
| Metric | Description |
|--------|-------------|
| `twingate_inbound_bytes_total{transport="..."}` | Total inbound bytes, labeled by transport type |
| `twingate_outbound_bytes_total{transport="..."}` | Total outbound bytes, labeled by transport type |
| `twingate_connector_uptime_seconds` | Connector uptime duration |
| Resource counts | Number of resources handled per Connector |

**Transport label values:** `direct`, `relay`

## Prerequisites
- Twingate Connector **v1.80.0 or later**
- Prometheus-compatible monitoring system

## Step-by-Step Setup
1. Set `TWINGATE_METRICS_PORT=9999` on the Connector
2. Configure Prometheus to scrape the metrics endpoint (e.g., `http://<connector-host>:9999`)
3. Build dashboards in Grafana or preferred visualization tool

## Configuration Values
| Variable | Value | Description |
|----------|-------|-------------|
| `TWINGATE_METRICS_PORT` | `9999` (example) | Enables metrics export on specified port |

## Gotchas
- Feature requires Connector **v1.80.0+**; older versions do not support metrics
- `transport` label distinguishes direct vs. relay traffic — useful for optimizing direct connection ratios
- Metrics set is actively expanding; metric names/availability may change

## Related Docs
- [Complete Setup Guide](https://www.twingate.com/docs/connector-metrics) — detailed implementation instructions (linked as "complete setup guide" on source page)