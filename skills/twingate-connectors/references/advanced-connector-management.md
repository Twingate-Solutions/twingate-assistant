# Advanced Connector Management

## Page Title
Advanced Connector Management

## Summary
This page serves as a navigation hub for advanced Connector configuration and management features in Twingate. It covers monitoring, observability, deployment automation, and specialized configuration options for Connectors beyond basic setup.

## Key Information
- **Real-time connection logs**: Connectors can output network connection logs to `stdout` for SIEM integration or custom monitoring
- **Connector details**: Metadata about Connector state and host machine is visible in the Admin console Connector management page
- **Custom metadata**: Deployment-time metadata can be attached to Connectors and viewed in Admin console
- **Unqualified domain names**: Supported by configuring search domains on the Connector host (no device-level config required)
- **Health checks**: Containers in Docker report health automatically; direct health checks available for specialized deployments
- **Prometheus metrics**: Connectors can expose Prometheus-compatible metrics endpoints
- **Deployment automation**: Best practices exist for automating via Admin API or custom scripts

## Prerequisites
- Connector already deployed
- Access to Admin console for viewing details/metadata
- Docker deployment assumed for automatic health reporting (manual health checks needed otherwise)
- Admin API access required for automated deployment scenarios

## Feature Sub-pages (Step-by-Step in linked docs)
Each feature has dedicated documentation:
1. Enabling real-time connection logs
2. Viewing Connector details
3. Adding custom metadata
4. Supporting unqualified domain names
5. Checking Connector health directly
6. Exploring Connector metrics
7. Deployment automation best practices

## Configuration Values
| Feature | Method |
|---|---|
| Connection logs | `stdout` output configuration |
| Metrics | Prometheus-compatible endpoint |
| Deployment automation | Admin API or custom scripts |
| Search domains | Configured on Connector host machine |

## Gotchas
- Docker deployments get automatic health reporting; **non-Docker deployments require manual health check configuration**
- Unqualified domain name support requires search domain config on the **Connector host**, not on client devices
- Custom metadata must be added **at deployment time** (not retroactively implied, verify in linked docs)

## Related Docs
- Real-time connection logs (sub-page)
- Connector details (sub-page)
- Custom metadata (sub-page)
- Unqualified domain names (sub-page)
- Connector health checks (sub-page)
- Connector metrics / Prometheus (sub-page)
- Deployment automation best practices (sub-page)
- Twingate Admin API