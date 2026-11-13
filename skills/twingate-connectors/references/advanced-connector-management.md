---
source: https://www.twingate.com/docs/advanced-connector-management
type: docs
fetched: 2026-11-13
source_version: c20d0f38ed5796465e9e5334d30c6c9ce0f4ead157e5d82c9a6c21a81e7e9711
trust: official
---

# Advanced Connector Management

## Summary
This page is an index of advanced Twingate Connector features for monitoring, management, and automated deployment. It briefly describes each capability and links to a dedicated page for details. It has no configuration steps or values of its own.

## Key Information
- **Real-time connection logs:** Connectors can write network connection logs to `stdout` on the host. This lets you feed a SIEM or custom system with no delay.
- **Connector details:** Connectors report metadata about their current state and host machine. It appears on the Connector management page in the Admin Console.
- **Custom deployment metadata:** You can attach custom metadata to Connectors at deployment time. It is also shown on the Connector management page in the Admin Console.
- **Unqualified domain names:** To support unqualified domain names as Resources without device-level configuration, configure search domain(s) on the Connector host machine.
- **Health checks:** Connectors deployed as Docker containers report process health automatically. Specialized deployments may need to check Connector health directly.
- **Metrics:** Connectors can expose Prometheus-compatible metrics for monitoring and observability.
- **Automated deployment:** Deploying Connectors through the Admin API or a custom script requires following specific best practices.

## Prerequisites
None are listed on this page. Each linked subpage may have its own.

## Step-by-Step
Not applicable. Follow the linked pages for each feature.

## Configuration Values
This page lists no env vars, CLI flags, or API parameters. Check the linked pages for:
- Enabling real-time connection logs
- Adding custom metadata
- Exposing metrics
- Direct health checking

## Gotchas
- This is a landing page only, so the implementation details are on the subpages.
- Automatic health reporting applies only to Docker container deployments. Other deployment types need direct health checks.
- Unqualified domain name support is configured on the Connector host (search domains), not on client devices.

## Related Docs
- Enabling real-time connection logs
- Viewing Connector details
- Adding custom metadata to Connectors
- Supporting unqualified domain names
- Checking Connector health directly
- Connector metrics
- Deployment automation best practices (Admin API or custom script)