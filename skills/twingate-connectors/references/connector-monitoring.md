# Twingate Connector Monitoring with Prometheus & Grafana

## Summary
Configure Twingate Connectors to export Prometheus metrics, then collect and visualize them using a Prometheus + Grafana stack. Metrics include traffic bytes, direct vs relay connection breakdown, and connector uptime.

## Key Information
- Metrics endpoint: `http://<connector-ip>:<TWINGATE_METRICS_PORT>/metrics`
- Grafana dashboards available at: `https://github.com/Twingate-Community/dashboards`
- Dashboard JSON: `grafana/insights.json`
- Requires Grafana 12.2.1+

## Prerequisites
- Twingate deployment with at least one Connector
- Docker and Docker Compose installed
- Network access to Connector hosts on the metrics port

## Configuration Values

### Connector Environment Variables
| Variable | Value | Notes |
|---|---|---|
| `TWINGATE_METRICS_PORT` | `9999` (any unused port) | Enables metrics endpoint |

### Prometheus Settings
| Setting | Value |
|---|---|
| `scrape_interval` | `15s` (global), `30s` (connectors job) |
| `metrics_path` | `/metrics` |
| `storage.tsdb.retention.time` | `200h` |

### Grafana Environment Variables
| Variable | Value |
|---|---|
| `GF_SECURITY_ADMIN_PASSWORD` | `admin123` (change this) |
| `GF_USERS_ALLOW_SIGN_UP` | `false` |

## Step-by-Step

1. **Enable metrics on each Connector** — set `TWINGATE_METRICS_PORT=9999`
   - Docker: add to `docker-compose.yml` environment + expose port
   - Linux service: edit `/etc/twingate/connector.conf`, then `sudo systemctl restart twingate-connector`

2. **Verify endpoint**: `curl http://<connector-ip>:9999/metrics`

3. **Create `prometheus.yml`** with connector IPs listed under `targets`

4. **Create monitoring `docker-compose.yml`** with Prometheus (port 9090) and Grafana (port 3000)

5. **Start stack**: `docker-compose up -d`

6. **Configure Grafana data source**: Configuration → Data Sources → Prometheus → URL: `http://prometheus:9090`

7. **Import dashboard**: Dashboards → Import → upload/paste `grafana/insights.json`

8. **Verify**: Check `http://localhost:9090/targets` — all connectors should show "UP"

## Available Metrics
```
twingate_inbound_bytes_total{transport="direct|relay"}
twingate_outbound_bytes_total{transport="direct|relay"}
twingate_connector_uptime_seconds
```

## Gotchas
- Connector must be **restarted** after adding `TWINGATE_METRICS_PORT` for changes to take effect
- Docker connector requires explicit **port mapping** (`"9999:9999"`) in addition to the env var
- Firewall must allow access to the metrics port from the Prometheus host
- Grafana data source URL must use service name `http://prometheus:9090` (not localhost) when both run in Docker Compose

## Scaling
To add connectors, update `targets` list in `prometheus.yml` and run `docker-compose restart prometheus`.

## Related Docs
- [Twingate Community Dashboards](https://github.com/Twingate-Community/dashboards)
- Twingate Connector configuration docs