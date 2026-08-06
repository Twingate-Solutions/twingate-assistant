---
source: https://github.com/Twingate-Community/dashboards
type: github
fetched: 2026-08-06
source_version: ae406597be8e8b24c16452ab8fe16940daf18ea2
---

<!-- triage: unassigned -->

# Twingate Community Dashboards

## Summary
Community-maintained collection of Grafana dashboards for monitoring Twingate deployments. Currently includes one dashboard (`grafana/insights.json`) that visualizes connector metrics via Prometheus. Intended to grow through community contributions.

## Key Information
- Single dashboard available: **Twingate Insights** (`grafana/insights.json`)
- Panels cover transport breakdown (direct/relay-hydra/relay-quic), inbound/outbound traffic, connector uptime, and resource counts
- Data source: Prometheus fed by Twingate Connector metrics export
- License: MIT

## Prerequisites
- Grafana v12.2.1 or higher
- Prometheus data source configured in Grafana
- Twingate Connector(s) with metrics/health export enabled (connector configuration docs not yet linked in repo)

## Usage / Step-by-Step

1. Download `grafana/insights.json` from the repo (Raw → Save, or copy JSON)
2. In Grafana, go to **Dashboards → Import**
3. Upload the `.json` file or paste the JSON content
4. Select your Prometheus data source when prompted
5. Adjust time ranges, connector filters, and aggregation variables as needed

## Configuration Values
No environment variables or CLI flags. Dashboard-level variables (set inside Grafana after import):
- Connector filters
- Time range
- Aggregation levels
- Alert thresholds (customizable per environment)

## Gotchas
- Requires Grafana **12.2.1+**; older versions may fail to import or render correctly
- Connector metrics export must be enabled on the Twingate Connector side — setup link is noted as a TODO in the README and not yet provided
- No automated provisioning scripts included; import is manual only

## Related Docs
- [GitHub Issues](https://github.com/Twingate-Community/dashboards/issues) — bug reports and dashboard requests
- [Twingate Community Reddit](https://www.reddit.com/r/twingate/)
- Grafana import docs: `https://grafana.com/docs/grafana/latest/dashboards/manage-dashboards/#import-a-dashboard`