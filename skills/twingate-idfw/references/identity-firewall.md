# Twingate Identity Firewall

## Summary
Twingate Identity Firewall extends Zero Trust and PAM controls to users, resources, and agents via a Layer 7 reverse proxy (Twingate Gateway). It propagates IdP identity to protected resources (Kubernetes, SSH, future: HTTPS, databases, MCP) without static credentials. Free for up to 5 Resources on all plans.

## Key Information
- **Protocol support**: Kubernetes API and SSH (GA); HTTPS, database protocols, MCP (upcoming)
- **Core component**: Twingate Gateway — open-source Layer 7 reverse proxy deployed in your environment
- **Auth flow**: User authenticates via existing IdP once; identity propagates to all accessed Resources
- **Access model**: Just-in-time, zero-standing access based on identity, device posture, location, context
- **Observability**: Per-user/agent logging of commands, API calls, queries; session replay capability
- **No hardware appliances** or complex infrastructure required

## Prerequisites
- Existing IdP configured with Twingate
- Twingate account (any plan)
- Twingate Gateway deployed in target environment

## Architecture
```
User → IdP Auth → Twingate Policy Enforcement → Twingate Gateway (L7 proxy) → Protected Resource
```
- Gateway handles identity propagation and session recording
- No static credentials or separate auth tokens required at the resource level

## Gotchas
- Free tier limited to **5 Resources** — additional Resources require paid plan
- MCP, HTTPS, and database protocol support is **not yet available**
- Gateway must be **self-hosted within your environment** (open-source)
- Access permissions are **automatically revoked** when context no longer meets policy — ensure applications handle session interruption gracefully

## Related Docs
- [Privileged Access for Kubernetes](https://www.twingate.com/docs/privileged-access-kubernetes)
- [Privileged Access for SSH](https://www.twingate.com/docs/privileged-access-ssh)