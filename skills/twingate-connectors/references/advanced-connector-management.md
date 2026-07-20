# Advanced Connector Management

## Page Title
Advanced Connector Management

## Summary
This page serves as a navigation hub for advanced Connector management features in Twingate. It covers monitoring, observability, metadata, health checks, and deployment automation capabilities available to Connectors.

## Key Information
- **Real-time connection logs**: Connectors can stream network connection logs to `stdout` for SIEM integration or custom monitoring
- **Connector details**: State and host machine metadata visible in Admin console Connector management page
- **Custom metadata**: Deployable at Connector creation time, surfaced in Admin console
- **Unqualified domain names**: Supported by configuring search domains on the Connector host (no device-level config required)
- **Health checks**: Automatic health reporting for Docker container deployments; direct health checks available for specialized scenarios
- **Prometheus metrics**: Connectors can expose Prometheus-compatible metrics endpoints
- **Deployment automation**: Best practices documented for API-based or scripted Connector deployments

## Prerequisites
- Twingate Connector deployed (Docker, Linux service, or other supported method)
- Admin console access for viewing metadata and Connector details
- Prometheus scraper configured separately if using metrics (implied)

## Configuration Areas (Sub-topics)

| Feature | Key Action |
|---|---|
| Real-time logs | Configure `stdout` log output on Connector |
| Custom metadata | Add at deployment time via Admin API or console |
| Search domains | Set on Connector host machine OS |
| Health checks | Query Connector health endpoint directly |
| Prometheus metrics | Enable metrics exposure on Connector |
| Deployment automation | Follow Admin API best practices |

## Gotchas
- Health checks are **automatic only for Docker** deployments; other deployment types require manual health check configuration
- Custom metadata must be added **at deployment time** — unclear if it can be modified post-deployment without redeployment
- Unqualified domain name support requires changes to the **Connector host**, not client devices
- Real-time logs go to `stdout` only — log forwarding to SIEM requires an external log collection agent

## Related Docs
- [Real-time connection logs](#)
- [Connector details](#)
- [Custom metadata for Connectors](#)
- [Unqualified domain names](#)
- [Connector health checks](#)
- [Connector metrics (Prometheus)](#)
- [Deployment automation best practices](#)
- [Admin API](https://www.twingate.com/docs/api)