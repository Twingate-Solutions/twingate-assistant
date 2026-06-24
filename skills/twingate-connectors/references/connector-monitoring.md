# Twingate Connector Monitoring with Prometheus & Grafana

## Summary
Guide for setting up metrics collection on Twingate Connectors and visualizing data using a Prometheus + Grafana stack. Connectors expose a Prometheus-compatible metrics endpoint via a configurable port. Covers Docker and Linux service deployment options.

## Key Information
- Metrics exposed: bytes transferred, transfer rates, direct vs relay connection breakdown, uptime, resource counts
- Metrics endpoint: `http://<connector-ip>:<METRICS_PORT>/metrics`
- Dashboard JSON available at: `https://github.com/Twingate-Community/dashboards` (grafana/insights.json)
- Requires Grafana 12.2.1+

## Prerequisites
- Twingate deployment with at least one Connector
- Docker and Docker Compose installed
- Network access to Connector hosts on the metrics port

## Configuration Values

### Connector Environment Variable
| Variable | Value | Notes |
|---|---|---|
| `TWINGATE_METRICS_PORT` | Any unused port (e.g., `9999`) | Required to enable metrics |

### Grafana Environment Variables
| Variable | Example Value |
|---|---|
| `GF_SECURITY_ADMIN_PASSWORD` | `admin123` |
| `GF_USERS_ALLOW_SIGN_UP` | `false` |

### Prometheus Settings
- `scrape_interval`: `15s` (global), `30s` (per-job)
- `metrics_path`: `/metrics`
- `storage.tsdb.retention.time`: `200h`

## Step-by-Step

1. **Enable metrics on Connector**
   - Docker: Add `TWINGATE_METRICS_PORT=9999` to env and expose port
   - Linux service: Add to `/etc/twingate/connector.conf`, then `sudo systemctl restart twingate-connector`

2. **Verify endpoint**: `curl http://<connector-ip>:9999/metrics`

3. **Create `prometheus.yml`** with targets pointing to `connector-ip:9999`

4. **Deploy monitoring stack**: `docker-compose up -d` (runs Prometheus on `:9090`, Grafana on `:3000`)

5. **Configure Grafana**:
   - Login at `http://localhost:3000` (admin/admin123)
   - Add Prometheus datasource: URL = `http://prometheus:9090`
   - Import dashboard JSON from GitHub repo

6. **Verify**: Check `http://localhost:9090/targets` — all Connector targets should show "UP"

7. **Scale**: Add connector IPs to `prometheus.yml` targets, then `docker-compose restart prometheus`

## Gotchas
- Connector must be restarted after adding `TWINGATE_METRICS_PORT` to config
- Firewall must allow inbound access to the metrics port on Connector hosts
- Docker containerized Connectors need explicit port mapping (`"9999:9999"`)
- Grafana 12.2.1+ required for dashboard import compatibility
- Prometheus datasource URL inside Docker Compose uses service name (`http://prometheus:9090`), not `localhost`

## Alerting (Optional)
Add `rule_files` and `alerting` blocks to `prometheus.yml`; create `alerts.yml` with `ConnectorDown` alert using: `up{job="twingate-connectors"} == 0`

## Related Docs
- [Twingate Community Dashboards](https://github.com/Twingate-Community/dashboards)
- Twingate official Connector configuration docs