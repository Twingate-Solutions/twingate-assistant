# Twingate Identity Firewall

## Summary
Twingate Identity Firewall extends Zero Trust and PAM controls to users, resources, and agents via a Layer 7 reverse proxy (Twingate Gateway). It propagates IdP identity to protected resources without static credentials. Currently supports Kubernetes API and SSH, with HTTPS, database protocols, and MCP planned.

## Key Information
- Free for up to 5 Resources on all plans
- Uses **Twingate Gateway**: open-source Layer 7 reverse proxy deployed in your environment
- Authentication handled before requests reach protected resources — no static credentials or separate auth tokens
- Supports session recording and forensic-level audit trails per user/agent
- Just-in-time access based on identity, device posture, location, and context

## Current Protocol Support
| Protocol | Status |
|----------|--------|
| Kubernetes API | Available |
| SSH | Available |
| HTTPS | Planned |
| Database protocols | Planned |
| Model Context Protocol (MCP) | Planned |

## Prerequisites
- Existing IdP (Identity Provider) configured with Twingate
- Twingate network deployed
- Twingate Gateway deployed within target environment (per protocol-specific docs)

## Architecture
1. User authenticates once via existing IdP
2. Twingate enforces access policies at the Gateway before requests reach resources
3. Identity context propagates through to backend resource (Kubernetes, SSH, etc.)
4. All commands/API calls logged with user attribution; session replay available

## Gotchas
- Gateway must be self-hosted within your environment — not a Twingate-managed cloud component
- No static credentials means existing workflows relying on service account tokens or SSH keys may need reconfiguration
- MCP support (for securing AI tool access) is not yet available

## Related Docs
- [Privileged Access for Kubernetes](https://www.twingate.com/docs/privileged-access-kubernetes)
- [Privileged Access for SSH](https://www.twingate.com/docs/privileged-access-ssh)