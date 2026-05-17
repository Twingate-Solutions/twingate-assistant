# Advanced Connector Management

## Page Title
Advanced Connector Management

## Summary
This page serves as an index for advanced Connector management features including logging, monitoring, metadata, health checks, and deployment automation. Each topic links to dedicated documentation covering the specific implementation details.

## Key Information
- **Real-time connection logs**: Connectors can output network connection logs to `stdout` for SIEM integration or custom monitoring
- **Connector details**: State and host machine metadata visible in Admin Console → Connector management page
- **Custom metadata**: Can be attached to Connectors at deployment time, visible in Admin Console
- **Unqualified domain names**: Supported by configuring search domains on the Connector host machine (no device-level config required)
- **Health checks**: Docker deployments report health automatically; specialized scenarios can query health directly
- **Prometheus metrics**: Connectors can expose Prometheus-compatible metrics endpoint
- **Deployment automation**: Admin API or custom scripts supported with documented best practices

## Prerequisites
- Connector deployed and registered to Twingate network
- Access to Admin Console for viewing details/metadata
- Docker used for automatic health reporting (optional)

## Sub-Topics & Links
| Feature | Reference |
|---|---|
| Real-time connection logs | Enable real-time connection logs doc |
| Connector details | View Connector details doc |
| Custom metadata | Add custom metadata doc |
| Unqualified domain names | Unqualified domain names doc |
| Health checks | Connector health checks doc |
| Prometheus metrics | Connector metrics doc |
| Automated deployment | Deployment automation best practices doc |

## Configuration Values
- Logs output to: `stdout` on host machine
- Metrics format: Prometheus-compatible
- Automation interface: Admin API

## Gotchas
- Docker deployments get automatic health reporting; **non-Docker deployments require explicit health check configuration**
- Unqualified domain name support requires search domain configuration on the **Connector host**, not on client devices
- Custom metadata must be added **at deployment time**, not retroactively via the console

## Related Docs
- Admin API documentation
- Connector deployment guides
- Prometheus monitoring integration
- SIEM integration guides