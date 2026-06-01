# Twingate Connector Monitoring with Prometheus & Grafana

## Summary
Guide for setting up metrics collection on Twingate Connectors and visualizing them via Prometheus and Grafana. Connectors expose a Prometheus-compatible metrics endpoint configured via environment variable. A Docker Compose stack runs the full monitoring pipeline.

## Key Information
- Connectors expose metrics at `http://<connector-ip>:<TWINGATE_METRICS_PORT>/metrics`
- Metrics include: bytes transferred, transfer rates, direct vs relay connection breakdown, uptime, resource counts
- Dashboard JSON available at: `https://github.com/Twingate-Community/dashboards` (`grafana/insights.json`)
- Grafana minimum version: 12.2.1+

## Prerequisites
- Twingate deployment with ≥1 Connector
- Docker and Docker Compose installed
- Network access to Connector hosts on the metrics port

## Configuration Values

### Connector Environment Variable
| Variable | Value | Notes |
|---|---|---|
| `TWINGATE_METRICS_PORT` | Any unused port (e.g., `9999`) | Enables metrics endpoint |

### Linux Service Config (`/etc/twingate/connector.conf`)
```
TWINGATE_METRICS_PORT=9999
```

### Prometheus (`prometheus.yml`) Key Settings
```yaml
scrape_interval: 15s
scrape_configs:
  - job_name: 'twingate-connectors'
    static_configs:
      - targets: ['connector1-ip:9999']
    scrape_interval: 30s
    metrics_path: /metrics
```

### Grafana Docker Env Vars
| Variable | Default |
|---|---|
| `GF_SECURITY_ADMIN_PASSWORD` | `admin123` |
| `GF_USERS_ALLOW_SIGN_UP` | `false` |

## Step-by-Step

1. **Enable metrics** — Set `TWINGATE_METRICS_PORT=9999` on each Connector; restart service
2. **Verify endpoint** — `curl http://<connector-ip>:9999/metrics`
3. **Create `prometheus.yml`** — Add all Connector IPs as targets
4. **Create `docker-compose.yml`** — Deploy Prometheus (port 9090) + Grafana (port 3000)
5. **Start stack** — `docker-compose up -d`
6. **Configure Grafana** — Add Prometheus data source at `http://prometheus:9090`
7. **Import dashboard** — Upload `grafana/insights.json` from community repo
8. **Verify** — Check `http://localhost:9090/targets` for UP status

## Gotchas
- Port `9999` must be open on Connector hosts (firewall rules)
- Docker Connectors require explicit port mapping (`"9999:9999"` in `ports:`)
- Connector must be **restarted** after adding `TWINGATE_METRICS_PORT`
- Prometheus data source URL inside Docker stack must use service name `prometheus:9090`, not `localhost`
- Adding connectors to Prometheus requires `docker-compose restart prometheus`

## Key Metrics
```
twingate_inbound_bytes_total{transport="direct|relay"}
twingate_outbound_bytes_total{transport="direct|relay"}
twingate_connector_uptime_seconds
```

## Related Docs
- [Twingate Community Dashboards](https://github.com/Twingate-Community/dashboards)
- Twingate Connector configuration docs (official)
- Prometheus alerting rules configuration