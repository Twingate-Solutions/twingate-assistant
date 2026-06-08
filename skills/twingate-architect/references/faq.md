# Twingate FAQ

## Page Title
Twingate Frequently Asked Questions

## Summary
Reference glossary and FAQ covering Twingate's core concepts, deployment requirements, performance characteristics, and security model. Addresses common implementation questions for administrators evaluating or deploying Twingate.

## Key Information

### Core Concepts
- **Resource**: Any TCP/UDP destination (host, server, app) defined by address — protocol-agnostic
- **Connector**: Software proxy running on destination network; all traffic appears to originate from Connector host; deployed as Docker container or Linux service
- **Security Policy**: Access controls applied per-user for Resource access (e.g., MFA enforcement)
- **Group**: User collection mapped to Resources + single Security Policy

### Architecture
- Split tunnel by default — only Twingate Resources route through infrastructure
- No inbound public internet exposure required
- Transport: TLS v1.2 with standard ciphers
- WireGuard not currently supported

## Prerequisites
- Know internal IPs or domain names of target Resources
- Ability to run Docker container on a network host
- No firewall rule changes, IP remapping, or hardware appliances required

## Deployment Notes
- Deploy minimum one Connector per network; **recommended: two Connectors per network** for failover
- Coexists with existing VPN — no rip-and-replace needed
- Twingate subdomain/URL **cannot be changed** after network creation
- Client requires no pre-configuration; users authenticate via SSO

## Configuration Values
| Item | Value |
|------|-------|
| Client download | `https://get.twingate.com` |
| Supported client platforms | macOS, Windows, Linux, ChromeOS, Android, iOS, iPadOS |
| Connector deployment | Docker container or native Linux systemd service |
| Supported cloud platforms | AWS, Azure, GCP, DigitalOcean, on-premise |
| Supported IdPs | Okta, Entra ID (Azure AD), Google Workspace, OneLogin |
| Protocol support | Any TCP or UDP |
| Encryption | TLS v1.2 |

## Gotchas
- Twingate URL/subdomain is permanent — choose carefully at network creation
- Billing is per-seat; seats must be reassigned or purchased when exhausted
- Twingate does **not** store user credentials — delegates entirely to IdP
- M1 Mac support available via Mac App Store

## Related Docs
- How Twingate Works (architecture overview)
- Connector Deployment (step-by-step + best practices)
- Deployment Options (service-specific connector configs)
- Identity Provider Integrations
- Twingate API (programmatic configuration)
- Security overview
- Subscription Management
- Service Reliability
- Client Documentation