---
source: https://www.twingate.com/docs/faq
type: docs
fetched: 2026-08-14
source_version: 9f3675c826230ec2676574fdf825086b0790c9ce58684aa6d1e7014e01faa993
---

# Twingate FAQ Reference

## Page Title
Twingate FAQ & Glossary

## Summary
Reference document covering core Twingate concepts, deployment requirements, performance characteristics, and security model. Answers common questions about how Twingate differs from VPNs and what infrastructure changes are required for deployment.

## Key Information

### Core Concepts
- **Resource**: Any TCP/UDP destination (host, server, app) defined by address — protocol-agnostic
- **Connector**: Software proxy deployed on destination network; all traffic appears to originate from Connector host; delivered as Docker container (no special host privileges required)
- **Security Policy**: Access controls applied per-user/group (e.g., MFA requirements)
- **Group**: Logical user grouping mapped to Resources + single Security Policy

### Architecture
- Split tunnel by default — only Twingate Resources route through infrastructure
- No inbound public internet exposure required — Connectors make outbound connections only
- Transport: TLS v1.2 with standard ciphers
- Does **not** use WireGuard currently

## Prerequisites
- Know internal IP addresses or domain names of target resources
- Ability to run a Docker container (or Linux systemd service) on a network host
- No networking expertise required; no firewall rule changes, IP remapping, or hardware appliances needed

## Deployment Notes

### Connector Placement
- One Connector per network minimum
- **Recommended**: Deploy in pairs for failover redundancy
- Supported deployment targets: Linux VM, Docker, AWS/Azure/GCP native container services

### Client Deployment
- Download: `https://get.twingate.com` or platform app stores
- Platforms: macOS (M1 native), Windows, Linux, ChromeOS, Android, iOS, iPadOS
- No pre-configuration required; users authenticate via SSO

### Identity Provider Integration
- Supported: Okta, Entra ID (Azure AD), Google Workspace, OneLogin
- Twingate delegates auth entirely — does not store passwords

## Configuration Values
- Twingate subdomain/URL: **cannot be changed** after network creation
- Billing: per-seat, monthly or annual

## Gotchas
- Twingate URL (subdomain) is permanent — choose carefully at network creation
- Coexists with existing VPN infrastructure — no rip-and-replace needed
- Connectors are not directly accessed by users and have no public-facing ports

## Related Docs
- How Twingate Works (architecture)
- Connector deployment & best practices
- Deployment options (cloud-specific)
- Identity provider integrations
- Twingate Security article
- API documentation
- Subscription management
- Service Reliability