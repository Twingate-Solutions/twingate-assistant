## Connector Monitoring with Prometheus & Grafana

Complete guide to setting up a Prometheus + Grafana monitoring stack for Twingate Connectors. Covers metrics enablement, Prometheus config, Grafana setup, and alerting.

**Prerequisites:**
- Twingate deployment with at least one Connector
- Docker and Docker Compose installed
- Network access to Connector hosts on the metrics port

**Step 1 — Enable Metrics on Connectors:**
Set `TWINGATE_METRICS_PORT=9999` (or any unused port) on each Connector:
- Docker: add to environment in docker-compose.yml + expose port
- Linux service: add to `/etc/twingate/connector.conf`, then `systemctl restart twingate-connector`
- Verify: `curl http://<connector-ip>:9999/metrics`

**Available Metrics:**
- `twingate_inbound_bytes_total{transport}` / `twingate_outbound_bytes_total{transport}` -- bytes by transport type
- `twingate_connector_uptime_seconds` -- uptime
- Transport label distinguishes `direct` vs `relay` connections

**Step 2 — Prometheus Configuration:**
```yaml
scrape_configs:
  - job_name: 'twingate-connectors'
    static_configs:
      - targets: ['connector1-ip:9999']
    scrape_interval: 30s
    metrics_path: /metrics
```
Run Prometheus + Grafana via docker-compose; Prometheus storage retention configurable via `--storage.tsdb.retention.time`.

**Step 3 — Grafana Dashboard:**
- Add Prometheus data source: URL = `http://prometheus:9090`
- Import community dashboard JSON from: github.com/Twingate-Community/dashboards (`grafana/insights.json`)
- Requires Grafana 12.2.1+

**Alerting Example:**
```yaml
- alert: ConnectorDown
  expr: up{job="twingate-connectors"} == 0
  for: 1m
  labels:
    severity: critical
```

**Gotchas:**
- Firewall must allow access to the metrics port (9999) from Prometheus host to Connector hosts
- High relay percentage in metrics indicates P2P connection failures

**Related Docs:**
- /docs/connector-metrics -- Connector metrics reference
- /docs/connector-real-time-logs -- Real-time log output from Connectors
