# Twingate Connector Monitoring with Prometheus & Grafana

## Summary
Configure Twingate Connectors to expose Prometheus metrics, then collect and visualize them using a Prometheus + Grafana stack. Metrics include traffic bytes, direct vs relay connection breakdown, and connector uptime.

## Key Information
- Connectors expose metrics via HTTP endpoint at `/metrics`
- Metrics format is standard Prometheus text exposition
- Dashboard JSON available at: `https://github.com/Twingate-Community/dashboards`
- Grafana minimum compatible version: 12.2.1+

## Prerequisites
- Twingate deployment with at least one Connector
- Docker and Docker Compose installed
- Network access to Connector IPs on the metrics port

## Configuration Values

### Connector Environment Variables
| Variable | Value | Notes |
|---|---|---|
| `TWINGATE_METRICS_PORT` | `9999` (any unused port) | Enables metrics endpoint |

### Linux Service Config File
- Path: `/etc/twingate/connector.conf`
- Add: `TWINGATE_METRICS_PORT=9999`

### Available Metrics
- `twingate_inbound_bytes_total{transport="direct|relay"}`
- `twingate_outbound_bytes_total{transport="direct|relay"}`
- `twingate_connector_uptime_seconds`

## Step-by-Step

1. **Enable metrics on each Connector** — set `TWINGATE_METRICS_PORT=9999` in Docker env or `/etc/twingate/connector.conf`; restart connector
2. **Verify endpoint** — `curl http://<connector-ip>:9999/metrics`
3. **Create `prometheus.yml`** — add connector IPs under `scrape_configs`, `metrics_path: /metrics`
4. **Create monitoring `docker-compose.yml`** — Prometheus on port 9090, Grafana on port 3000
5. **Start stack** — `docker-compose up -d`
6. **Configure Grafana data source** — URL: `http://prometheus:9090`
7. **Import dashboard** — from GitHub repo `grafana/insights.json`

## Key Config Snippets

**Prometheus scrape config:**
```yaml
scrape_configs:
  - job_name: 'twingate-connectors'
    static_configs:
      - targets: ['connector1-ip:9999']
    scrape_interval: 30s
    metrics_path: /metrics
```

**Grafana env vars:**
```
GF_SECURITY_ADMIN_PASSWORD=admin123
GF_USERS_ALLOW_SIGN_UP=false
```

**Prometheus retention:**
```
--storage.tsdb.retention.time=200h
```

## Gotchas
- Port 9999 must be open on Connector host firewall for Prometheus to scrape
- Docker Connectors need explicit port mapping: `"9999:9999"`
- Must restart Connector after adding `TWINGATE_METRICS_PORT` to Linux service config
- After adding connectors to `prometheus.yml`, restart Prometheus: `docker-compose restart prometheus`
- Grafana data source URL uses container name `http://prometheus:9090` (not localhost) when both run in Docker Compose

## Troubleshooting
| Problem | Check |
|---|---|
| No data in dashboard | `http://localhost:9090/targets` — targets must show "UP" |
| Connection refused to metrics | Firewall, port mapping, connector restart |
| Dashboard import fails | Grafana version ≥ 12.2.1, valid JSON, data source configured |

## Related Docs
- [Twingate Community Dashboards](https://github.com/Twingate-Community/dashboards)
- Twingate Connector configuration (official docs)