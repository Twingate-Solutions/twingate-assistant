# Advanced Connector Management

## Page Title
Advanced Connector Management

## Summary
This page is a top-level index for advanced Connector management features in Twingate. It covers monitoring, metadata, health checks, metrics, and automated deployment guidance. Each section links to dedicated documentation pages.

## Key Information
- **Real-time connection logs**: Connectors can stream network connection logs to `stdout` for SIEM integration or custom monitoring
- **Connector details**: State and host machine metadata visible in Admin console → Connector management page
- **Custom metadata**: Deployable at Connector creation time; visible in Admin console
- **Unqualified domain names**: Supported via search domain configuration on the Connector host (no device-level config needed)
- **Health checks**: Docker deployments report health automatically; direct health checking available for other scenarios
- **Prometheus metrics**: Connectors can expose Prometheus-compatible metrics endpoints
- **Automated deployment**: Best practices exist for API-based or script-based Connector provisioning

## Prerequisites
- Connector deployed and registered to a Twingate network
- Admin console access
- For automation: access to Twingate Admin API

## Feature Quick Reference

| Feature | Method | Output Location |
|---|---|---|
| Connection logs | `stdout` config | Host stdout / SIEM |
| Connector details | Automatic | Admin console |
| Custom metadata | Set at deploy time | Admin console |
| Unqualified domains | Host search domain config | N/A |
| Health checks | Direct HTTP/container | Container runtime |
| Metrics | Prometheus endpoint | Prometheus-compatible systems |

## Gotchas
- Health checks are **automatic only in Docker** deployments; other deployment types require manual health check configuration
- Custom metadata must be added **at deployment time** — not retroactively via the console (see linked doc for specifics)
- Unqualified domain support requires **host-level** search domain configuration on the Connector machine, not on client devices

## Related Docs
- Real-time connection log output configuration
- Connector details (Admin console)
- Custom metadata for Connectors
- Unqualified domain name support
- Connector health checks (direct)
- Connector Prometheus metrics
- Admin API reference
- Deployment automation best practices