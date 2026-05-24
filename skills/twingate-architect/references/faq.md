# Twingate FAQ

## Page Title
Frequently Asked Questions (Twingate)

## Summary
Reference page covering Twingate's core concepts, deployment model, performance characteristics, and security approach. Provides concise answers to common questions about architecture, integration, and operational considerations. Useful as a quick-reference for evaluating or implementing Twingate.

## Key Information

### Glossary
- **Resource**: Any TCP/UDP destination (host, server, app) defined by address
- **Connector**: Software proxy deployed on destination network; all traffic appears to originate from Connector host
- **Security Policy**: Defines auth controls (e.g., MFA) applied to users accessing a Resource
- **Group**: Logical user grouping tied to Resources + a single Security Policy

### Architecture
- Split tunnel by default — only Twingate-defined Resource traffic routes through your infrastructure
- No inbound public internet exposure required; Connectors initiate outbound connections only
- Transport protocol: **TLS v1.2** with standard ciphers
- WireGuard not currently supported (monitoring adoption)

### Platform Support
- Clients: macOS, Windows, Linux, ChromeOS, Android, iOS, iPadOS (including Apple M1 native)
- Download: `https://get.twingate.com` or platform app stores
- Connector: Docker container or native Linux service; no special host privileges required

### Identity Providers
- Okta, Entra ID (formerly Azure AD), Google Workspace, OneLogin
- Twingate delegates authentication — does not store passwords

## Prerequisites
- Internal IP addresses or domain names of resources to expose
- Ability to run a Docker container (or Linux service) on a network host
- Identity provider configured for SSO

## Deployment Notes
- **No infrastructure changes required** — overlays existing network
- **No firewall rule changes, IP remapping, or hardware appliances**
- Can run **alongside existing VPN** infrastructure (no rip-and-replace)
- Deploy Connectors in **pairs** for failover redundancy (one minimum per network)
- Twingate URL/subdomain **cannot be changed** after network creation
- Users self-onboard: install client → sign in with SSO → access granted per Group membership

## Configuration Values
- **API available**: Programmatic deployment and configuration supported
- **Access control model**: Resource × Group combinations (RBAC at resource level)
- **Billing unit**: Per-user seat (monthly or annual)

## Gotchas
- Subdomain is permanent — choose carefully at network creation
- One Connector per network is functional minimum, but single point of failure; always deploy pairs
- Group is tied to exactly one Security Policy; plan Group structure accordingly
- WireGuard is **not** supported currently

## Related Docs
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- [Deploying Connectors](https://www.twingate.com/docs/connectors)
- [Connector Deployment Options](https://www.twingate.com/docs/deployment-options)
- [Identity Provider Integrations](https://www.twingate.com/docs/identity-providers)
- [Twingate API](https://www.twingate.com/docs/api)
- [Security Overview](https://www.twingate.com/docs/security)
- [Subscription Management](https://www.twingate.com/docs/subscription-management)
- [Service Reliability](https://www.twingate.com/docs/service-reliability)