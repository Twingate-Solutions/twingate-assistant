# Twingate Connector Monitoring with Prometheus & Grafana

## Summary
Configure Twingate Connectors to expose Prometheus metrics, then collect and visualize them using a Prometheus + Grafana stack. Metrics include traffic bytes, direct vs relay connection breakdown, and uptime.

## Key Information
- Connectors expose metrics via HTTP endpoint at `/metrics`
- Metrics format is Prometheus text exposition
- Dashboard JSON available at: `https://github.com/Twingate-Community/dashboards` (`grafana/insights.json`)
- Grafana version 12.2.1+ required for dashboard import

## Prerequisites
- Twingate deployment with at least one Connector
- Docker and Docker Compose installed
- Network access to Connector hosts on the metrics port

## Configuration Values

### Connector Environment Variable
| Variable | Value | Description |
|---|---|---|
| `TWINGATE_METRICS_PORT` | any unused port (e.g. `9999`) | Enables metrics endpoint |

### Prometheus Settings
| Parameter | Value |
|---|---|
| `scrape_interval` | `15s` (global), `30s` (per job) |
| `metrics_path` | `/metrics` |
| `storage.tsdb.retention.time` | `200h` |

### Grafana Environment
| Variable | Value |
|---|---|
| `GF_SECURITY_ADMIN_PASSWORD` | `admin123` (change this) |
| `GF_USERS_ALLOW_SIGN_UP` | `false` |

## Step-by-Step

1. **Enable metrics on Connector**
   - Docker: add `TWINGATE_METRICS_PORT=9999` to env and expose port in `docker-compose.yml`
   - Linux service: add to `/etc/twingate/connector.conf`, then `sudo systemctl restart twingate-connector`

2. **Verify metrics endpoint**: `curl http://<connector-ip>:9999/metrics`

3. **Create `prometheus.yml`** listing all connector targets under `twingate-connectors` job

4. **Start stack**: `docker-compose up -d`

5. **Configure Grafana** at `http://localhost:3000` (admin/admin123):
   - Add Prometheus data source: `http://prometheus:9090`
   - Import dashboard JSON from GitHub

6. **Verify**: Check `http://localhost:9090/targets` — all connectors should show status `UP`

## Available Metrics
```
twingate_inbound_bytes_total{transport="direct|relay"}
twingate_outbound_bytes_total{transport="direct|relay"}
twingate_connector_uptime_seconds
```

## Gotchas
- Connector must be **restarted** after config changes for metrics to activate
- Firewall must allow inbound access to metrics port (9999) from Prometheus host
- Prometheus container references Grafana as `http://prometheus:9090` (Docker network hostname), not `localhost`
- Dashboard import requires Grafana 12.2.1+
- Adding new connectors to `prometheus.yml` requires `docker-compose restart prometheus`

## Alert Example
```yaml
- alert: ConnectorDown
  expr: up{job="twingate-connectors"} == 0
  for: 1m
  labels:
    severity: critical
```

## Related Docs
- [Twingate Community Dashboards](https://github.com/Twingate-Community/dashboards)
- Twingate official Connector configuration docs
- Prometheus alerting: requires separate Alertmanager on port 9093