## Advanced Connector Management

Index of advanced Connector configuration and management features beyond basic deployment. Each item links to a dedicated reference.

**Available Advanced Features:**

- **Real-time connection log output** -- configure Connectors to stream network connection logs to stdout for SIEM ingestion without delay; see /docs/connector-real-time-logs

- **Connector details** -- Connectors report metadata about current state and the host machine; viewable in the Admin Console Connector management page; see /docs/connector-details

- **Custom deployment metadata** -- add custom labels/metadata at deploy time (e.g., environment, region, team); exposed in the Admin Console Connector management page; see /docs/connector-metadata

- **Supporting unqualified domain names** -- configure search domain(s) on the Connector host to support short hostnames as Resources without device-level config; see /docs/supporting-unqualified-domain-names

- **Connector health checks** -- Docker-deployed Connectors report health automatically; direct health check endpoint available for specialized deployment scenarios; see /docs/connector-health-checks

- **Connector metrics** -- expose Prometheus-compatible metrics for monitoring and observability; see /docs/connector-metrics

- **Automated deployment guidelines** -- considerations for scripting or API-driven Connector provisioning; see /docs/deployment-semi-automation

**Related Docs:**
- /docs/connector-real-time-logs -- Real-time log output setup
- /docs/connector-metrics -- Prometheus metrics
- /docs/siem-guide -- SIEM integration options
