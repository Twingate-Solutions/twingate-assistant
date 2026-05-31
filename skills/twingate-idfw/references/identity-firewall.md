# Twingate Identity Firewall

## Summary
Twingate Identity Firewall extends Zero Trust and PAM controls to users, resources, and agents by deploying a Layer 7 reverse proxy (Twingate Gateway) within your environment. It propagates identity from your IdP through to protected resources without static credentials. Currently supports Kubernetes API and SSH, with HTTPS, database protocols, and MCP planned.

## Key Information
- Free for up to 5 Resources on all plans
- Uses **Twingate Gateway**: open-source Layer 7 reverse proxy deployed in your environment
- No static credentials or separate authentication tokens required
- Provides session recording and forensic-level audit tied to individual users/agents
- Just-in-time access with automatic revocation
- Identity sourced from existing IdP (single authentication)

## Prerequisites
- Existing Twingate deployment
- Identity Provider (IdP) configured with Twingate
- Environment access to deploy the Twingate Gateway (self-hosted within your infrastructure)

## Supported Protocols
| Protocol | Status |
|----------|--------|
| Kubernetes API | Available |
| SSH | Available |
| HTTPS | Planned |
| Database protocols | Planned |
| Model Context Protocol (MCP) | Planned |

## How It Works
1. User authenticates once via existing IdP
2. Twingate enforces access policies before request reaches protected resource
3. Twingate Gateway (Layer 7 reverse proxy) propagates identity into the target environment
4. Sessions are recorded; every command/API call tied to specific user identity
5. Access revoked automatically when no longer needed

## Gotchas
- Gateway must be **self-deployed within your environment** (not a cloud-managed component)
- MCP support is forward-looking — not yet available
- Database and HTTPS support not yet available despite being listed as roadmap items
- Free tier caps at 5 Resources; larger deployments require paid plan

## Related Docs
- [Privileged Access for Kubernetes](https://www.twingate.com/docs/privileged-access-kubernetes)
- [Privileged Access for SSH](https://www.twingate.com/docs/privileged-access-ssh)