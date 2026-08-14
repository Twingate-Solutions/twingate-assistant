---
source: https://www.twingate.com/docs/identity-firewall
type: docs
fetched: 2026-08-14
source_version: b10eb97cdac189a465ef24ecf1a78f09a6448cd3e6d41e76f346db62638918da
---

# Twingate Identity Firewall Overview

## Summary
Twingate Identity Firewall extends Zero Trust and PAM controls to users, resources, and agents via a Layer 7 reverse proxy (Twingate Gateway). It propagates identity from your IdP through to protected resources (Kubernetes, SSH, Web Apps) without static credentials. Session recording and forensic logging are included.

## Key Information
- **Availability**: All plans; free for up to 5 Resources
- **Supported protocols**: Kubernetes API, SSH, Web Apps; database protocols and MCP (Model Context Protocol) coming soon
- **Core component**: Twingate Gateway — open-source Layer 7 reverse proxy deployed in your environment
- **Authentication**: Single IdP authentication; identity passes through to all accessed resources
- **Access model**: Just-in-time, dynamic; permissions auto-revoked when no longer needed
- **Visibility**: Per-user/agent logging of commands, API calls, queries; session replay capability
- **No hardware appliances or static credentials required**

## Prerequisites
- Existing IdP configured with Twingate
- Twingate account (any plan)
- Resources to protect (Kubernetes cluster, SSH hosts, or Web Apps)

## How It Works
1. User authenticates once via configured IdP
2. Twingate enforces access policies before requests reach the protected environment
3. Twingate Gateway (Layer 7 reverse proxy) proxies requests into the environment
4. Identity context propagates to the target resource
5. Sessions are recorded; access revoked automatically when conditions no longer met

## Configuration Values
- No specific env vars or CLI flags documented on this page
- Protocol-specific configuration covered in linked docs (see Related Docs)

## Gotchas
- MCP support is not yet available (listed as future)
- Database protocol support is also pending
- Gateway must be deployed **within your environment** (self-hosted component)
- Free tier caps at 5 Resources regardless of plan

## Related Docs
- [Privileged Access for Kubernetes](https://www.twingate.com/docs/privileged-access-kubernetes)
- [Privileged Access for SSH](https://www.twingate.com/docs/privileged-access-ssh)
- [Identity Firewall for Web Apps](https://www.twingate.com/docs/identity-firewall-web-apps)