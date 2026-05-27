# Advanced Connector Management

## Page Title
Advanced Connector Management

## Summary
This page serves as a hub for advanced Connector management features including logging, monitoring, metadata, and deployment automation. Each topic links to dedicated documentation covering configuration details for specific scenarios.

## Key Information
- **Real-time connection logs**: Connectors can output network connection logs to `stdout` for SIEM ingestion or custom monitoring
- **Connector details**: State and host machine metadata visible in Admin console → Connector management page
- **Custom metadata**: Can be attached to Connectors at deploy time; visible in Admin console
- **Unqualified domain names**: Supported via search domain configuration on the Connector host (no device-level config needed)
- **Health checks**: Automatic in Docker container deployments; manual checking available for specialized scenarios
- **Prometheus metrics**: Connectors can expose Prometheus-compatible metrics endpoints
- **Deployment automation**: Admin API or custom scripts supported with documented best practices

## Prerequisites
- Connector already deployed
- Access to Admin console for viewing details/metadata
- Docker deployment (for automatic health checks)
- Prometheus infrastructure (for metrics feature)

## Configuration Values
| Feature | Configuration Method |
|---|---|
| Real-time logs | Connector config (stdout output) |
| Custom metadata | Set at deployment time |
| Search domains | Configured on Connector host machine |
| Prometheus metrics | Connector config (exposes metrics endpoint) |
| Automated deployment | Admin API or custom scripts |

## Gotchas
- Health checks are **automatic only in Docker** container deployments; other deployment types require direct health check configuration
- Unqualified domain name support requires search domain config on the **Connector host**, not on client devices
- Custom metadata must be added **at deployment time** — unclear if it can be modified post-deployment from this page

## Related Docs
- Real-time connection logs configuration
- Connector details (Admin console)
- Custom metadata for Connectors
- Unqualified domain names support
- Connector health checks (direct)
- Connector Prometheus metrics
- Deployment automation best practices
- Admin API documentation