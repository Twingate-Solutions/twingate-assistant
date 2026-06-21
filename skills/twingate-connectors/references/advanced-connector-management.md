# Advanced Connector Management

## Page Title
Advanced Connector Management

## Summary
This page serves as a navigation hub for advanced Connector management features in Twingate. It covers monitoring, logging, health checks, metrics, and deployment automation topics. Each section links to dedicated documentation pages.

## Key Information
- **Real-time connection logs**: Connectors can stream network connection logs to `stdout` for SIEM integration or custom monitoring
- **Connector details**: State and host machine metadata visible in Admin console → Connector management page
- **Custom metadata**: Can be attached to Connectors at deploy time, visible in Admin console
- **Unqualified domain names**: Supported by configuring search domains on the Connector host (no device-level config needed)
- **Health checks**: Docker deployments report health automatically; direct health checks available for specialized scenarios
- **Prometheus metrics**: Connectors can expose Prometheus-compatible metrics endpoint
- **Deployment automation**: Admin API or custom scripts supported, with documented best practices

## Prerequisites
- Connector deployed and registered to a Twingate network
- Access to Admin console for viewing metadata and details
- Docker (for automatic health reporting); direct health check method available for non-Docker deployments

## Configuration Areas (links to sub-pages)

| Feature | Configuration Method |
|---|---|
| Real-time connection logs | `stdout` configuration on Connector |
| Custom metadata | Set at deployment time |
| Search domains | Configured on Connector host machine |
| Health checks | Direct endpoint (non-Docker) |
| Metrics | Prometheus endpoint configuration |
| Automated deployment | Admin API or custom scripts |

## Gotchas
- Health checks are **automatic only in Docker** deployments; other deployment types require explicit health check configuration
- Unqualified domain name support requires search domain config on the **Connector host**, not on client devices
- Custom metadata must be added **at deployment time** — unclear if it can be modified post-deployment without redeployment
- Real-time logs go to `stdout` only — no built-in log forwarding; external tooling required for SIEM integration

## Related Docs
- Real-time connection logs (sub-page)
- Connector details (sub-page)
- Custom metadata for Connectors (sub-page)
- Unqualified domain names (sub-page)
- Connector health checks (sub-page)
- Connector metrics / Prometheus (sub-page)
- Deployment automation best practices (sub-page)
- Twingate Admin API