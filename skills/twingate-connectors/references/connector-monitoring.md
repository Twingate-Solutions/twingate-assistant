---
source: https://www.twingate.com/docs/connector-monitoring
type: docs
fetched: 2026-11-13
source_version: ae63b96d2bf8f236974a23f1aef6ee18c5c92863c3c7ddce0e80d3b13e3456ba
trust: official
---

# Twingate Connector Monitoring with Prometheus & Grafana

## Summary
Guide to exposing metrics from Twingate Connectors via `TWINGATE_METRICS_PORT`, scraping them with Prometheus, and visualizing them in Grafana using a community dashboard. Uses Docker Compose for the Prometheus/Grafana stack.

## Key Information
- Connectors expose a Prometheus-format `/metrics` endpoint once `TWINGATE_METRICS_PORT` is set (any unused port; examples use 9999).
- Metric categories: traffic (bytes, rates), transport analytics (direct vs relay), health (uptime, resource counts).
- Example metrics: `twingate_inbound_bytes_total{transport="direct"}`, `twingate_outbound_bytes_total{transport="relay"}`, `twingate_connector_uptime_seconds`.
- Community dashboard: `grafana/insights.json` in https://github.com/Twingate-Community/dashboards (import via Dashboards → Import).

## Prerequisites
- Twingate deployment with at least one Connector
- Docker and Docker Compose
- Network access from Prometheus to each Connector's metrics port
- Grafana 12.2.1+ (per troubleshooting note)

## Step-by-Step
1. **Enable metrics on Connector**
   - Docker: add `TWINGATE_METRICS_PORT=9999` to environment and map `"9999:9999"`.
   - Linux service: add `TWINGATE_METRICS_PORT=9999` to `/etc/twingate/connector.conf`, then `sudo systemctl restart twingate-connector`.
2. **Verify**: `curl http://<connector-ip>:9999/metrics`
3. **Prometheus**: create `prometheus.yml` with a `twingate-connectors` job listing `<connector-ip>:9999` targets (`scrape_interval: 30s`, `metrics_path: /metrics`).
4. **Compose stack**: `prom/prometheus` (port 9090, retention `200h`, `--web.enable-lifecycle`) and `grafana/grafana` (port 3000). Run `docker-compose up -d`.
5. **Grafana**: log in at http://localhost:3000, add Prometheus data source with URL `http://prometheus:9090`, then import `insights.json`.
6. **Verify**: Prometheus Status → Targets should show UP; query the metrics above; check dashboard panels.
7. **Scale**: add more targets to `prometheus.yml`, then `docker-compose restart prometheus`.

## Configuration Values
- `TWINGATE_METRICS_PORT` – Connector metrics port (e.g., 9999)
- `GF_SECURITY_ADMIN_PASSWORD` (example uses `admin123`), `GF_USERS_ALLOW_SIGN_UP=false`
- Prometheus flags: `--config.file`, `--storage.tsdb.path`, `--storage.tsdb.retention.time=200h`, `--web.enable-lifecycle`
- Alerting: `rule_files: alerts.yml`, Alertmanager target `alertmanager:9093`; example rule `ConnectorDown` with `expr: up{job="twingate-connectors"} == 0`, `for: 1m`, severity critical.

## Gotchas
- Change the default Grafana password (`admin123`) in the example; don't use it in production.
- Restart the Connector after config changes.
- Firewall must allow the metrics port from Prometheus to Connectors; with Docker, confirm port mapping.
- The metrics port is unauthenticated HTTP; restrict network access to it.
- The example compose file mounts `./grafana/provisioning`; create it or remove the mount.
- Alertmanager is referenced but not defined in the example compose file.
- "No data" in dashboards: check targets are UP, the endpoint is reachable, and the time range; check `docker-compose logs prometheus`.
- Pin image versions rather than `latest` for stability.

## Related Docs
- Twingate Connector configuration docs
- Twingate-Community dashboards repo (GitHub Issues for setup help)
- Prometheus alerting documentation