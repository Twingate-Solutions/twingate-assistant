# Twingate Connector Monitoring with Prometheus & Grafana

## Summary
Configure Twingate Connectors to export Prometheus metrics, then visualize them in Grafana. Requires setting `TWINGATE_METRICS_PORT` on each Connector and pointing Prometheus scrape configs at the exposed endpoints.

## Key Information
- Connectors expose metrics at `http://<connector-ip>:<port>/metrics`
- Available metrics: `twingate_inbound_bytes_total`, `twingate_outbound_bytes_total`, `twingate_connector_uptime_seconds`
- Transport labels: `direct` and `relay`
- Community dashboards available at: `https://github.com/Twingate-Community/dashboards`

## Prerequisites
- Twingate deployment with at least one Connector
- Docker and Docker Compose
- Network access to Connector IPs on the configured metrics port

## Step-by-Step

### 1. Enable Metrics on Connector
**Docker:** Add to `docker-compose.yml` environment and expose port:
```yaml
- TWINGATE_METRICS_PORT=9999
ports:
  - "9999:9999"
```

**Linux service:** Add to `/etc/twingate/connector.conf`, then `sudo systemctl restart twingate-connector`

**Verify:** `curl http://<connector-ip>:9999/metrics`

### 2. Configure Prometheus (`prometheus.yml`)
```yaml
scrape_configs:
  - job_name: 'twingate-connectors'
    static_configs:
      - targets:
          - 'connector1-ip:9999'
    scrape_interval: 30s
    metrics_path: /metrics
```

### 3. Start Monitoring Stack
```bash
docker-compose up -d
curl http://localhost:9090/api/v1/targets  # verify scraping
```

### 4. Configure Grafana
- URL: `http://localhost:3000` | Credentials: `admin` / `admin123`
- Add Prometheus data source: URL = `http://prometheus:9090`
- Import dashboard JSON from GitHub repo (`grafana/insights.json`)

## Configuration Values

| Variable/Parameter | Value | Context |
|---|---|---|
| `TWINGATE_METRICS_PORT` | Any unused port (e.g., `9999`) | Connector env var |
| `GF_SECURITY_ADMIN_PASSWORD` | `admin123` (change this) | Grafana env var |
| `GF_USERS_ALLOW_SIGN_UP` | `false` | Grafana env var |
| `--storage.tsdb.retention.time` | `200h` | Prometheus CLI flag |
| Prometheus port | `9090` | Docker port mapping |
| Grafana port | `3000` | Docker port mapping |

## Alerting Example (`alerts.yml`)
```yaml
- alert: ConnectorDown
  expr: up{job="twingate-connectors"} == 0
  for: 1m
  labels:
    severity: critical
```

## Gotchas
- Firewall must allow inbound access to `TWINGATE_METRICS_PORT` on Connector hosts
- Prometheus references Grafana as `http://prometheus:9090` (Docker network name), not `localhost`
- Dashboard import requires Grafana **12.2.1+**
- Connector must be restarted after adding `TWINGATE_METRICS_PORT` to config
- Adding new Connectors requires updating `prometheus.yml` targets and running `docker-compose restart prometheus`

## Related Docs
- [Twingate Community Dashboards](https://github.com/Twingate-Community/dashboards)
- Twingate Connector configuration docs
- Prometheus alertmanager configuration