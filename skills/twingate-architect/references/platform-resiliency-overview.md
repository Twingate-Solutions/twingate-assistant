---
source: https://www.twingate.com/docs/platform-resiliency-overview
type: docs
fetched: 2026-11-22
source_version: f63d6b0a5add26f487910a9a8b182c1dc5c029426a1d67864ba66525e10bbddf
trust: official
---

# Platform Resiliency Overview

## Summary
Describes how Twingate designs, operates, and tests its platform for availability. The central design principle is minimizing blast radius, using active-active multi-region infrastructure, workload isolation, and graceful degradation. Already-connected users keep access even if the control plane is fully unreachable.

## Key Information
- **SLA:** 99.95% uptime commitment. Recent uptime and incidents are listed on the Twingate status page.
- **Architecture components:** Control plane (authentication, authorization, configuration), Connectors (deployed in customer networks), Clients (user devices), Relays (broker Client–Connector connections).
- **Traffic path:** Once authenticated and connected, traffic flows Client↔Connector without needing the control plane for each request.
- **Control plane:** Active-active, stateless clusters in US East, Central, and West on Google Cloud. A global load balancer routes to the nearest healthy cluster. Traffic is proactively drained from regions showing unusual behavior.
- **Relays:** Active-active across 20 Google Cloud regions.
- **Workload isolation:** Authentication, authorization, public API, and Admin Console run as separate deployments.
- **Data layer:**
  - Primary database has automatic standby failover.
  - Read replicas are spread across zones and regions.
  - Writes are classified as critical or non-critical, and non-critical writes (e.g., "last seen") may fail without blocking users.
  - A protective read-only mode pauses admin config changes while authentication and access continue.
- **Control-plane outage behavior:** Tokens have a short renewal interval (used when the control plane is reachable) and an extended validity window (used only when it is unreachable). Both the Client and the Connector validate tokens, and the Connector independently checks control-plane reachability. New sign-ins pause during an outage, but connected users with valid tokens who remain policy-compliant keep access.
- **Retry storms:** Clients use jittered back-off for retries and token renewals.
- **Elasticity:** Absorbed 5–10x traffic surges without manual intervention.
- **Engineering practices:** Infrastructure as code, small frequent deployments, feature-flag rollouts, automated smoke tests, required reliability and metrics sections in specs, and roughly 20–30% of engineering capacity reserved for reliability.
- **Monitoring:** APM, centralized logs, alerts as code, anomaly detection, AI SRE agent analysis on alerts, external third-party synthetic checks, and 24/7 follow-the-sun on-call.
- **Incident response:** Automated incident channel, record, and bridge. Roles include incident lead and communications owner. Runbooks are linked from alerts, and written post-incident reviews are produced.
- **DR testing:** At least quarterly, covering loss of a replica, primary DB, backup restore, loss of caching, loss of a region, and building a new cluster from scratch. Part of SOC 2 controls.
- **Planned work:** Production sharding, expanded anomaly detection, more automated failure injection.

## Prerequisites
None. This is a conceptual overview.

## Step-by-Step
Not applicable.

## Configuration Values
None documented on this page.

## Gotchas
- Continued access during a control-plane outage applies only to users who already hold the necessary tokens and remain policy-compliant. New sign-ins pause.
- The read-only mode temporarily blocks admin configuration changes, though end-user access continues.
- The Admin Console being down should not affect end-user access.
- The extended token window cannot bypass normal renewal while the control plane is healthy.

## Related Docs
- Twingate status page (referenced, no URL given in source)