# Twingate FAQ

## Page Title
Frequently Asked Questions (FAQ)

## Summary
Reference page covering Twingate's core concepts, deployment requirements, performance characteristics, and security model. Defines key terminology and answers common implementation questions for administrators evaluating or deploying Twingate.

## Key Information

### Core Concepts (Glossary)
- **Resource**: Any TCP/UDP destination (host, server, app) defined by address
- **Connector**: Software proxy deployed on destination network (Docker container or Linux service); all traffic appears to originate from Connector host
- **Security Policy**: Access controls applied per-user for Resource access (e.g., MFA enforcement)
- **Group**: Collection of Users mapped to Resources; enforces a single Security Policy

### Architecture
- Split tunnel by default — only Twingate Resources route through your infrastructure
- No inbound public internet exposure required; Connectors initiate outbound connections only
- Transport protocol: TLS v1.2 with standard ciphers
- WireGuard not currently supported (monitoring adoption)

### Platform Support
- Clients: macOS, Windows, Linux, ChromeOS, Android, iOS, iPadOS (including Apple M1 native)
- Download: `get.twingate.com` or device app stores
- Supports any TCP/UDP application without additional configuration

## Prerequisites
- Internal IP addresses or domain names of target resources
- Ability to run Docker container (or Linux service) on a host within target network
- SSO/identity provider for user authentication (Okta, Entra ID, Google Workspace, OneLogin)

## Deployment Notes
- **No infrastructure changes required** — no firewall rule changes, IP remapping, or hardware appliances
- **Coexists with existing VPN** — no rip-and-replace needed; phased rollout supported
- Deploy Connectors in **pairs per network** for failover redundancy
- Twingate subdomain/URL **cannot be changed** after network creation
- Users self-install clients; no pre-configuration required on client side

## Configuration Values
| Item | Value |
|------|-------|
| Client download URL | `https://get.twingate.com` |
| Connector deployment | Docker container or native Linux service |
| Supported clouds | AWS, Azure, GCP, DigitalOcean |
| Encryption | TLS v1.2, standard ciphers |

## Gotchas
- Twingate URL/subdomain is **permanent** — choose carefully at network creation
- Billing is per-seat (user); seats must be purchased or reassigned when limit reached
- Twingate does **not** store user credentials — authentication delegated entirely to IdP
- WireGuard is **not** currently supported as transport

## Related Docs
- How Twingate Works (architecture overview)
- Connector Deployment (step-by-step + best practices)
- Deployment Options (cloud-specific Connector options)
- Identity Provider Integrations
- Role-Based Access Controls
- Twingate API (programmatic deployment)
- Subscription Management
- Service Reliability
- Twingate Security