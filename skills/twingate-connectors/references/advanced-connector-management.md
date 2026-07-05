# Advanced Connector Management

## Page Title
Advanced Connector Management

## Summary
This page serves as a navigation hub for advanced Connector management features in Twingate. It covers monitoring, observability, metadata, health checks, and deployment automation capabilities available to Connector operators.

## Key Information
- **Real-time connection logs**: Connectors can stream network connection logs to `stdout` for SIEM integration or custom monitoring
- **Connector details**: State and host machine metadata visible in Admin console Connector management page
- **Custom metadata**: Deployable at Connector creation time, visible in Admin console
- **Unqualified domain names**: Supported by configuring search domains on the Connector host (no device-level config required)
- **Health checks**: Docker deployments report health automatically; specialized scenarios can query health directly
- **Prometheus metrics**: Connectors can expose Prometheus-compatible metrics endpoint
- **Deployment automation**: Admin API or custom scripts supported with documented best practices

## Prerequisites
- Deployed Twingate Connector
- Admin console access
- For container health checks: Docker deployment
- For metrics: Prometheus-compatible monitoring stack

## Feature Subtopics (with linked guidance)

| Feature | Notes |
|---|---|
| Real-time connection logs | Enable via Connector config; outputs to `stdout` |
| Connector details | View in Admin console |
| Custom metadata | Added at deployment time |
| Unqualified domain names | Configure search domains on host machine |
| Health checks | Automatic in Docker; manual check available |
| Prometheus metrics | Requires configuration to expose endpoint |
| Automated deployment | See Admin API best practices doc |

## Gotchas
- Custom metadata must be added **at deployment time** — not retroactively added after deployment without redeployment
- Health checks are **automatic only in Docker** — other deployment targets (bare metal, VMs) require manual health check configuration
- Unqualified domain name support requires search domain config on the **Connector host**, not on end-user devices

## Related Docs
- Real-time connection logs configuration
- Connector details (Admin console)
- Custom metadata for Connectors
- Unqualified domain name support
- Connector health checks
- Connector Prometheus metrics
- Deployment automation best practices (Admin API)