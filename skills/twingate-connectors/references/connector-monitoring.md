# Twingate Connector Monitoring with Prometheus & Grafana

## Summary
Guide for setting up metrics collection from Twingate Connectors using Prometheus and Grafana. Connectors expose a Prometheus-compatible metrics endpoint via a configurable port. The full stack runs via Docker Compose.

## Key Information
- Connectors export metrics: bytes transferred, transfer rates, direct vs relay connection breakdown, uptime, resource counts
- Metrics endpoint path: `/metrics` (Prometheus format)
- Dashboard JSON available at: `https://github.com/Twingate-Community/dashboards` (`grafana/insights.json`)
- Minimum Grafana version: 12.2.1+

## Prerequisites
- Twingate deployment with at least one Connector
- Docker and Docker Compose installed
- Network access to Connector hosts on the metrics port

## Configuration Values

| Variable | Value | Location |
|---|---|---|
| `TWINGATE_METRICS_PORT` | Any unused port (e.g., `9999`) | Docker env or `/etc/twingate/connector.conf` |
| `GF_SECURITY_ADMIN_PASSWORD` | Set in docker-compose | Grafana container env |
| `GF_USERS_ALLOW_SIGN_UP` | `false` | Grafana container env |
| Prometheus scrape interval | `15s` global, `30s` per job | `prometheus.yml` |
| Prometheus retention | `200h` | CLI flag `--storage.tsdb.retention.time` |
| Prometheus URL (from Grafana) | `http://prometheus:9090` | Grafana data source config |

## Step-by-Step

1. **Enable metrics on Connector**
   - Docker: Add `TWINGATE_METRICS_PORT=9999` env var and expose port in `docker-compose.yml`
   - Linux service: Add `TWINGATE_METRICS_PORT=9999` to `/etc/twingate/connector.conf`, then `sudo systemctl restart twingate-connector`

2. **Verify endpoint**: `curl http://<connector-ip>:9999/metrics`

3. **Create `prometheus.yml`** listing all Connector IPs as targets under `job_name: 'twingate-connectors'`

4. **Start stack**: `docker-compose up -d` (Prometheus on `:9090`, Grafana on `:3000`)

5. **Configure Grafana**: Add Prometheus data source → import dashboard JSON from GitHub

6. **Verify**: Check `http://localhost:9090/targets` all show "UP"; confirm dashboard panels populate

## Adding Connectors / Alerting
- Add IPs to `prometheus.yml` targets, then `docker-compose restart prometheus`
- Alerting requires separate `alerts.yml` and Alertmanager; example rule checks `up{job="twingate-connectors"} == 0` for 1 minute

## Gotchas
- Firewall must allow inbound access on the metrics port (e.g., 9999) to each Connector host
- Grafana data source URL must use container name `prometheus` (not `localhost`) when both run in Docker Compose
- Connector must be restarted after adding `TWINGATE_METRICS_PORT` for changes to take effect
- Dashboard import requires Grafana 12.2.1+

## Related Docs
- [Twingate Community Dashboards (GitHub)](https://github.com/Twingate-Community/dashboards)
- Twingate official Connector configuration docs