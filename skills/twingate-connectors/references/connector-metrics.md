---
source: https://www.twingate.com/docs/connector-metrics
type: docs
fetched: 2026-08-14
source_version: 6b61ee1c3ab271b8d01b6bcfa98f76ed95e85f052bfff930b78cc9bbb7d5426b
---

# Connector Metrics Overview

## Page Title
Twingate Connector Metrics Overview

## Summary
Twingate Connectors can export operational metrics in Prometheus format, providing visibility into traffic patterns, connection efficiency, and connector health. Metrics are enabled via an environment variable and scraped by standard Prometheus-compatible tools.

## Key Information
- Metrics exported in standard Prometheus format
- Compatible with Prometheus, Grafana, and similar monitoring stacks
- Minimum Connector version: **v1.80.0**
- Metrics endpoint enabled by setting `TWINGATE_METRICS_PORT`

## Available Metrics

| Metric | Description |
|--------|-------------|
| `twingate_inbound_bytes_total{transport="..."}` | Total inbound bytes, split by transport type |
| `twingate_outbound_bytes_total{transport="..."}` | Total outbound bytes, split by transport type |
| `twingate_connector_uptime_seconds` | Connector uptime in seconds |
| Resource count metrics | Count of resources handled per Connector |

**Transport label values:** `direct`, `relay`

## Prerequisites
- Twingate Connector v1.80.0 or later
- Prometheus-compatible monitoring system (Prometheus, Grafana, etc.)

## Step-by-Step Setup
1. Set `TWINGATE_METRICS_PORT=9999` on the Connector
2. Configure Prometheus to scrape the metrics endpoint at `http://<connector-host>:9999`
3. Build dashboards in Grafana or preferred visualization tool

## Configuration Values

| Variable | Value | Description |
|----------|-------|-------------|
| `TWINGATE_METRICS_PORT` | `9999` (example) | Enables metrics endpoint on specified port |

## Example Prometheus Output
```
twingate_inbound_bytes_total{transport="direct"} 1234567890
twingate_outbound_bytes_total{transport="relay"} 987654321
twingate_connector_uptime_seconds 86400
```

## Gotchas
- Feature requires Connector **v1.80.0+** — older versions will not support metrics export
- Metrics collection is described as actively expanding; available metrics may change
- Port `9999` is used in examples but any available port can be configured

## Related Docs
- [Complete Setup Guide](https://www.twingate.com/docs/) — detailed implementation instructions (linked from page as "complete setup guide")