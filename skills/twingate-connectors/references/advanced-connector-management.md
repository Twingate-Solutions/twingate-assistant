# Advanced Connector Management

## Page Title
Advanced Connector Management

## Summary
This page serves as an index for advanced Connector management topics including logging, monitoring, metadata, health checks, and deployment automation. Each section links to dedicated documentation covering specific operational capabilities.

## Key Information
- **Real-time connection logs**: Connectors can stream network connection logs to `stdout` for SIEM integration or custom monitoring
- **Connector details**: State and host machine metadata visible in Admin console Connector management page
- **Custom metadata**: Deployable at runtime, visible in Admin console
- **Unqualified domain names**: Supported by configuring search domains on the Connector host (no device-level config required)
- **Health checks**: Automatic in Docker container deployments; manual checking available for specialized scenarios
- **Prometheus metrics**: Connectors can expose Prometheus-compatible metrics endpoint
- **Deployment automation**: Best practices documented for API-driven or scripted Connector deployments

## Prerequisites
- Connector deployed and registered to Twingate network
- Access to Admin console for viewing details/metadata
- Docker deployment assumed for automatic health checks; other scenarios need direct health check configuration

## Sub-Topics (with links referenced)
| Feature | Reference |
|---|---|
| Real-time connection logs | Enable real-time connection logs |
| Connector details | View Connector details |
| Custom metadata | Add custom metadata |
| Unqualified domain names | Supporting unqualified domain names |
| Health checks | Checking Connector health directly |
| Prometheus metrics | Connector metrics |
| Automated deployment | Deployment automation best practices |

## Configuration Values
- Connection logs output to: `stdout`
- Metrics format: Prometheus-compatible
- Metadata: Set at deployment time (specific flags/env vars documented in sub-pages)
- Search domains: Configured at OS level on Connector host machine

## Gotchas
- Health checks are **automatic only in Docker**; non-Docker deployments require manual health check configuration
- Custom metadata must be added **at deployment time** — not post-deployment via console
- Unqualified domain name support requires search domain config on the **Connector host**, not on client devices

## Related Docs
- Real-time connection logs (sub-page)
- Connector metrics / Prometheus (sub-page)
- Deployment automation best practices (sub-page)
- Admin API documentation
- Connector health checks (sub-page)
- Custom metadata (sub-page)