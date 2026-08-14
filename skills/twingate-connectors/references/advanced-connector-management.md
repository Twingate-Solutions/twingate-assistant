---
source: https://www.twingate.com/docs/advanced-connector-management
type: docs
fetched: 2026-08-14
source_version: 5ab2c3fcbb6529ff9c51e89f058bfcc6ddef754ec35990845f8be6e4f8147625
---

# Advanced Connector Management

## Page Title
Advanced Connector Management

## Summary
This page is an index of advanced Connector management topics covering monitoring, observability, metadata, health checks, and automated deployment. Each section links to dedicated documentation for implementation details.

## Key Information
- **Real-time connection logs**: Connectors can output network connection logs to `stdout` for SIEM integration or custom monitoring
- **Connector details**: State and host machine metadata visible in Admin console > Connector management page
- **Custom metadata**: Deployable at Connector creation time, visible in Admin console
- **Unqualified domain names**: Supported by configuring search domains on the Connector host (no client-side config needed)
- **Health checks**: Containers (Docker) report health automatically; direct health check available for other scenarios
- **Prometheus metrics**: Connectors can expose Prometheus-compatible metrics endpoint
- **Automated deployment**: Best practices exist for API-based or script-based Connector provisioning

## Prerequisites
- Connector(s) deployed in your Twingate network
- Admin console access for viewing metadata and details
- Docker deployment for automatic health reporting (other scenarios require manual health check configuration)

## Features Summary (with sub-page references)

| Feature | Use Case | Details At |
|---|---|---|
| Real-time connection logs | SIEM integration, live monitoring | `/docs/real-time-logs` (linked) |
| Connector details | State visibility | Admin console |
| Custom metadata | Tagging/organizational labeling | `/docs/custom-metadata` (linked) |
| Unqualified domain names | Support short hostnames as Resources | `/docs/unqualified-domains` (linked) |
| Health checks | Non-Docker deployments, direct probing | `/docs/health-checks` (linked) |
| Prometheus metrics | Observability stack integration | `/docs/metrics` (linked) |
| Automated deployment | CI/CD, infrastructure-as-code | `/docs/deployment-automation` (linked) |

## Gotchas
- Health checks are **automatic only in Docker**; other deployment types (systemd, bare metal, etc.) require explicit health check configuration
- Custom metadata must be added **at deployment time** — unclear if it can be modified post-deployment without redeployment
- Real-time logs go to `stdout` only — requires log shipping agent or container log driver for persistence
- Unqualified domain name support requires config on the **Connector host**, not the client device

## Related Docs
- Real-time connection logs
- Connector details (Admin console)
- Custom metadata
- Unqualified domain names
- Connector health checks
- Connector metrics (Prometheus)
- Deployment automation best practices
- Twingate Admin API