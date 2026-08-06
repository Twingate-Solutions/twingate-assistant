---
source: https://www.twingate.com/docs/connector-monitoring
type: docs
fetched: 2026-08-05
source_version: 85afcad7ff3c7c088aa8b8a871b105c95c27d779d5e902985b0229d9f6af920c
---

# Twingate Connector Monitoring with Prometheus & Grafana

## Summary
Configure Twingate Connectors to export Prometheus metrics, then collect and visualize them using a Prometheus + Grafana stack. Connectors expose metrics via an HTTP endpoint on a configurable port. A community dashboard JSON is available for import.

## Key Information
- Metrics endpoint: `http://<connector-ip>:<TWINGATE_METRICS_PORT>/metrics`
- Available metrics: `twingate_inbound_bytes_total`, `twingate_outbound_bytes_total`, `twingate_connector_uptime_seconds`
- Transport labels: `direct` vs `relay`
- Community dashboard: `https://github.com/Twingate-Community/dashboards` → `grafana/insights.json`
- Requires Grafana 12.2.1+

## Prerequisites
- Twingate deployment with at least one Connector
- Docker and Docker Compose installed
- Network access to Connector hosts on the metrics port

## Configuration Values

| Variable | Value | Context |
|---|---|---|
| `TWINGATE_METRICS_PORT` | Any unused port (e.g., `9999`) | Connector env var |
| `GF_SECURITY_ADMIN_PASSWORD` | `admin123` (change this) | Grafana env var |
| `GF_USERS_ALLOW_SIGN_UP` | `false` | Grafana env var |
| Prometheus scrape interval | `30s` | `prometheus.yml` |
| Prometheus retention | `200h` | CLI flag |

## Step-by-Step

### 1. Enable Metrics on Connector

**Docker:** Add to `docker-compose.yml`:
```yaml
environment:
  - TWINGATE_METRICS_PORT=9999
ports:
  - "9999:9999"
```

**Linux service:** Add to `/etc/twingate/connector.conf`, then `sudo systemctl restart twingate-connector`:
```
TWINGATE_METRICS_PORT=9999
```

**Verify:** `curl http://<connector-ip>:9999/metrics`

### 2. Deploy Prometheus + Grafana
```bash
mkdir twingate-monitoring && cd twingate-monitoring
# Create prometheus.yml with connector targets
# Create docker-compose.yml with prometheus + grafana services
docker-compose up -d
```

### 3. Configure Grafana
1. Open `http://localhost:3000` → login `admin`/`admin123`
2. Add Prometheus data source: URL = `http://prometheus:9090`
3. Import dashboard: **Dashboards → Import → Upload JSON** from community repo

### 4. Add More Connectors
Update `prometheus.yml` targets, then:
```bash
docker-compose restart prometheus
```

## Alerts Example (`alerts.yml`)
```yaml
- alert: ConnectorDown
  expr: up{job="twingate-connectors"} == 0
  for: 1m
  labels:
    severity: critical
```

## Gotchas
- Firewall must allow inbound access to `TWINGATE_METRICS_PORT` on Connector hosts
- Connector must be restarted after adding `TWINGATE_METRICS_PORT` to config
- Dashboard import requires Grafana 12.2.1+
- In Docker Compose, Grafana references Prometheus as `http://prometheus:9090` (service name), not `localhost`
- Metrics download as a file via curl rather than displaying inline

## Troubleshooting
| Problem | Check |
|---|---|
| No dashboard data | `http://localhost:9090/targets` — verify targets are UP |
| Connection refused on metrics port | Confirm env var set + connector restarted + port open |
| Dashboard import fails | Validate JSON, check Grafana version ≥ 12.2.1 |

## Related Docs
- [Twingate Connector Configuration](https://www.twingate.com/docs/)
- [Community Dashboards GitHub](https://github.com/Twingate-Community/dashboards)
- [Twingate Reddit Community](https://www.reddit.com/r/Twingate/)