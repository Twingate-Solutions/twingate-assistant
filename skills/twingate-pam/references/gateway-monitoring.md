---
source: https://www.twingate.com/docs/gateway-monitoring
type: docs
fetched: 2026-11-22
source_version: c6c759645e5bec0cfa83a3e28ab6f7d649d27f106a6e3bb89019ce3d3acfba9a
trust: official
---

# Gateway Monitoring

## Summary
The Twingate Gateway exposes Prometheus metrics at `/metrics` on port `9090`. This page covers scraping those metrics (Kubernetes via Prometheus Operator, or VM via static config), adding alerting rules, and importing the Grafana dashboard.

## Key Information
- Metrics endpoint: `/metrics`, port `9090`.
- Kubernetes: use the Gateway Helm chart's `metrics.*` values to create a PodMonitor or ServiceMonitor, a PrometheusRule, and a Grafana dashboard ConfigMap.
- VM: add a static scrape target, a Prometheus alerting rules file, and import the dashboard JSON manually.
- Core metrics (all deployments): TCP connection duration/total/active, client authentication total, client connection duration, recorded session duration (Kubernetes and SSH).
- Kubernetes and Web App metrics: `twingate_gateway_http_*` (active requests, duration, request/response size, total) and `twingate_gateway_api_server_*` (active requests, duration, total). They are labeled by `resource_type` (`kubernetes` or `web_app`) and `type` (`http`, `websocket`, `spdy`, `unknown`).
- Also exported: Go runtime (`go_*`), process (`process_*`), and `promhttp_metric_handler_*` metrics.
- SSH-specific metrics are not yet available.

## Prerequisites
- Kubernetes: Prometheus Operator installed (for monitors and PrometheusRule); Grafana with the dashboard sidecar (for the dashboard).
- VM: a Prometheus instance and Grafana.

## Step-by-Step
**Scrape (Kubernetes)** – set in Gateway Helm values (choose one):
```yaml
metrics:
  podMonitor:
    enabled: true
    additionalLabels:
      release: prometheus
```
or
```yaml
metrics:
  serviceMonitor:
    enabled: true
    additionalLabels:
      release: prometheus
```
Verify on Prometheus **Status > Targets**.

**Scrape (VM)**:
```yaml
scrape_configs:
  - job_name: twingate-gateway
    static_configs:
      - targets: ["<GATEWAY_HOST>:9090"]
```

**Alerts (Kubernetes)**: set `metrics.prometheusRule.enabled: true` and define `rules`. The example rule `TwingateGatewayHighHTTPErrorRate` fires (severity `critical`, `for: 2m`) when the 5xx rate from `twingate_gateway_http_requests_total{code=~"5[0-9][0-9]"}` exceeds 0.8 requests/sec.

**Alerts (VM)**: put the same rules under a `groups` entry (e.g. name `twingate-gateway`) in a Prometheus alerting rules file.

**Dashboard (Kubernetes)**:
```yaml
metrics:
  grafanaDashboard:
    enabled: true
    labels:
      grafana_dashboard: "1"
```
**Dashboard (VM)**: in Grafana, go to **Dashboards > New > Import** and upload or paste the dashboard JSON from the Gateway repository.

## Configuration Values
- `metrics.podMonitor.enabled`, `metrics.podMonitor.additionalLabels`
- `metrics.serviceMonitor.enabled`, `metrics.serviceMonitor.additionalLabels`
- `metrics.prometheusRule.enabled`, `metrics.prometheusRule.rules`
- `metrics.grafanaDashboard.enabled`, `metrics.grafanaDashboard.labels`
- Grafana Helm chart: `sidecar.dashboards.searchNamespace`

## Gotchas
- Enable only one of `podMonitor` or `serviceMonitor`. Enabling both scrapes each Gateway twice and duplicates every metric.
- Set `additionalLabels` (e.g. `release: prometheus`) if your Prometheus selects monitors by label.
- If Grafana runs in a different namespace from the Gateway, add that namespace to `sidecar.dashboards.searchNamespace`.
- For streaming, WebSocket, and SPDY connections, `api_server_request_duration_seconds` measures setup time only.

## Related Docs
- Gateway (https://www.twingate.com/docs/gateway)
- Gateway `values.yaml` with more example rules (https://github.com/Twingate/gateway/blob/main/deploy/gateway/values.yaml)
- Gateway dashboard JSON (https://github.com/Twingate/gateway/tree/main/deploy/gateway/dashboards)
- Prometheus Operator installation (https://prometheus-operator.dev/docs/getting-started/installation/)
- Prometheus static_config (https://prometheus.io/docs/prometheus/latest/configuration/configuration/#static_config)
- Prometheus alerting rules (https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)
- Grafana Helm charts (https://github.com/grafana/helm-charts)