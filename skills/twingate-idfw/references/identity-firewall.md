# Twingate Identity Firewall

## Summary
Twingate Identity Firewall extends Zero Trust and PAM controls to users, resources, and agents by propagating IdP identity through a Layer 7 reverse proxy (Twingate Gateway). It supports just-in-time access with automatic revocation and session recording. Currently supports Kubernetes API and SSH, with HTTPS, database protocols, and MCP planned.

## Key Information
- Free for up to 5 Resources on all plans
- Uses **Twingate Gateway**: open-source Layer 7 reverse proxy deployed in your environment
- No static credentials or separate authentication tokens required
- Provides session recording and forensic-level audit trails per user/agent
- Identity sourced from existing IdP (single authentication flow)
- Access is just-in-time; permissions auto-revoked when no longer needed

## Current Protocol Support
| Protocol | Status |
|----------|--------|
| Kubernetes API | Available |
| SSH | Available |
| HTTPS | Planned |
| Database protocols | Planned |
| Model Context Protocol (MCP) | Planned |

## Architecture
- Twingate Gateway deployed **within your environment** (not SaaS-side)
- Acts as reverse proxy between clients and protected resources
- Authentication and policy enforcement happen **before** requests reach protected resources
- Identity propagated from IdP through to each resource

## Prerequisites
- Existing IdP configured with Twingate
- Twingate account (any plan)
- Ability to deploy Twingate Gateway in target environment

## Gotchas
- Gateway must be self-hosted in your environment — it is not managed by Twingate
- MCP support not yet available (planned)
- 5-Resource free tier limit applies across all Identity Firewall resources

## Related Docs
- [Privileged Access for Kubernetes](https://www.twingate.com/docs/kubernetes)
- [Privileged Access for SSH](https://www.twingate.com/docs/ssh)