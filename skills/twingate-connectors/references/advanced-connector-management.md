# Advanced Connector Management

## Page Title
Advanced Connector Management

## Summary
This page is an index of advanced Connector management features covering monitoring, logging, metadata, health checks, and deployment automation. Each section links to dedicated documentation for implementation details.

## Key Information
- **Real-time connection logs**: Connectors can stream network connection logs to `stdout` for SIEM integration or custom monitoring
- **Connector details**: State and host machine metadata visible in Admin console Connector management page
- **Custom metadata**: Deployable at Connector creation time; visible in Admin console
- **Unqualified domain names**: Supported by configuring search domains on the Connector host (no device-level config required)
- **Health checks**: Containers report health automatically in Docker; direct health check endpoint available for other scenarios
- **Prometheus metrics**: Connectors can expose Prometheus-compatible metrics endpoint
- **Deployment automation**: Best practices documented for Admin API and script-based automation

## Prerequisites
- Deployed Connector(s)
- Access to Admin console for viewing metadata/details
- Docker (for automatic health reporting)
- Prometheus (optional, for metrics collection)

## Sub-Topics & Links

| Feature | Link |
|---|---|
| Real-time connection logs | Enable real-time connection logs |
| Connector details | View Connector details |
| Custom metadata | Add custom metadata |
| Unqualified domain names | Supporting unqualified domain names |
| Health checks | Checking Connector health directly |
| Connector metrics | Connector metrics (Prometheus) |
| Deployment automation | Deployment automation best practices |

## Gotchas
- Health checks are **automatic only in Docker**; non-container deployments require direct health check configuration
- Unqualified domain name support requires search domain configuration **on the Connector host**, not on client devices
- Custom metadata must be added **at deployment time** — unclear if editable post-deployment without redeployment
- Real-time logs go to `stdout` only — requires external log collection tooling for persistence

## Related Docs
- Admin API documentation
- Connector deployment guides
- Prometheus monitoring setup
- Admin console Connector management page