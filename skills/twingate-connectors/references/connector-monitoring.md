# Twingate Connector Monitoring with Prometheus & Grafana

## Summary
Configure Twingate Connectors to export Prometheus metrics, then collect and visualize them using a Prometheus + Grafana stack. Connectors expose metrics via HTTP endpoint when `TWINGATE_METRICS_PORT` is set.

## Key Information
- Metrics exposed: bytes transferred, transfer rates, direct vs relay breakdown, uptime, resource counts
- Metrics endpoint path: `/metrics` (Prometheus format)
- Dashboard source: `https://github.com/Twingate-Community/dashboards` (grafana/insights.json)
- Minimum Grafana version: 12.2.1+

## Prerequisites
- Twingate deployment with at least one Connector
- Docker and Docker Compose installed
- Network access to Connector hosts on chosen metrics port

## Step-by-Step

### 1. Enable Metrics on Connector

**Docker:** Add to `docker-compose.yml`:
```yaml
environment:
  - TWINGATE_METRICS_PORT=9999
ports:
  - "9999:9999"
```

**Linux service:** Add to `/etc/twingate/connector.conf`, then `sudo systemctl restart twingate-connector`

**Verify:** `curl http://<connector-ip>:9999/metrics`

### 2. Set Up Prometheus (`prometheus.yml`)
```yaml
global:
  scrape_interval: 15s
scrape_configs:
  - job_name: 'twingate-connectors'
    static_configs:
      - targets: ['connector1-ip:9999']
    scrape_interval: 30s
    metrics_path: /metrics
```

### 3. Start Monitoring Stack
```bash
docker-compose up -d
curl http://localhost:9090/api/v1/targets  # verify Prometheus
```

### 4. Configure Grafana
- URL: `http://localhost:3000` | Login: `admin` / `admin123`
- Add Prometheus data source: URL = `http://prometheus:9090`
- Import dashboard: Dashboards → Import → upload `insights.json`

## Configuration Values

| Variable | Value | Location |
|----------|-------|----------|
| `TWINGATE_METRICS_PORT` | Any unused port (e.g., `9999`) | Connector env |
| `GF_SECURITY_ADMIN_PASSWORD` | `admin123` (change this) | Grafana env |
| `GF_USERS_ALLOW_SIGN_UP` | `false` | Grafana env |
| `--storage.tsdb.retention.time` | `200h` | Prometheus flag |
| Prometheus port | `9090` | Docker |
| Grafana port | `3000` | Docker |

## Gotchas
- Connector must be **restarted** after adding `TWINGATE_METRICS_PORT` for changes to take effect
- Firewall must allow inbound access on the metrics port (9999) from Prometheus host
- Prometheus scrape target must use IP/hostname accessible from Prometheus container—use actual Connector IP, not `localhost`
- Dashboard import requires Grafana 12.2.1+; older versions may fail
- Adding connectors to `prometheus.yml` requires `docker-compose restart prometheus`

## Key Metrics
```
twingate_inbound_bytes_total{transport="direct"|"relay"}
twingate_outbound_bytes_total{transport="direct"|"relay"}
twingate_connector_uptime_seconds
up{job="twingate-connectors"}  # for alerting on connector down
```

## Related Docs
- [Twingate Community Dashboards](https://github.com/Twingate-Community/dashboards)
- Twingate Connector configuration docs
- Prometheus alerting: reference `alerts.yml` example with `ConnectorDown` rule (threshold: `up == 0` for 1m)