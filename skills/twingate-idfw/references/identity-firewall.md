# Twingate Identity Firewall

## Summary
Twingate Identity Firewall extends Zero Trust and PAM controls to users, resources, and agents via a Layer 7 reverse proxy (Twingate Gateway). It propagates IdP identity to protected resources without static credentials. Currently supports Kubernetes API and SSH, with HTTPS, databases, and MCP planned.

## Key Information
- Free for up to 5 Resources on all plans
- Uses **Twingate Gateway**: open-source Layer 7 reverse proxy deployed in your environment
- Identity flows from existing IdP through to every resource (no separate auth tokens)
- Access is just-in-time; permissions auto-revoke when no longer needed
- Session recording and per-request audit tied to specific user/agent
- Planned protocol support: HTTPS, database protocols, MCP (for remote MCP servers)

## Current Protocol Support
| Protocol | Status |
|----------|--------|
| Kubernetes API | Available |
| SSH | Available |
| HTTPS | Planned |
| Database protocols | Planned |
| MCP | Planned |

## Prerequisites
- Existing IdP configured with Twingate
- Twingate Gateway deployed within target environment
- Resources defined in Twingate (free tier: up to 5)

## How It Works
1. User authenticates once via existing IdP
2. Twingate evaluates access policy (identity, device posture, location, context)
3. Twingate Gateway proxies request to protected resource with identity propagated
4. Every request logged with user/agent attribution; sessions recorded

## Gotchas
- Gateway must be **self-hosted** within your environment (open-source component)
- No static credentials or separate authentication tokens used — existing credential-based workflows may need reconfiguration
- MCP support not yet available; monitor release notes if building AI agent workflows

## Related Docs
- [Privileged Access for Kubernetes](https://www.twingate.com/docs/privileged-access-kubernetes)
- [Privileged Access for SSH](https://www.twingate.com/docs/privileged-access-ssh)