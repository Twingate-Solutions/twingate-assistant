# Twingate FAQ

## Page Title
Twingate FAQ / Frequently Asked Questions

## Summary
Reference glossary and Q&A covering Twingate core concepts, deployment requirements, performance characteristics, and security model. Clarifies common misconceptions about infrastructure changes, VPN coexistence, and traffic routing behavior.

## Key Information

### Glossary
- **Resource**: Any TCP/UDP destination (host, server, app) defined by address — protocol-agnostic
- **Connector**: Software proxy (Docker container or Linux service) deployed on private network; all traffic appears to originate from Connector host
- **Security Policy**: Access controls (e.g., MFA) applied per Group, independent of protocol
- **Group**: Set of Users + associated Resources + one Security Policy

### Architecture
- Split tunnel by default — only Twingate Resources route through private infrastructure
- No inbound public internet exposure required; Connectors initiate outbound connections only
- Transport: TLS v1.2 with standard ciphers
- WireGuard not currently supported (being monitored)

### Deployment
- No network infrastructure changes required
- No firewall rule changes, IP remapping, or hardware appliances needed
- Can run alongside existing VPN (no rip-and-replace)
- One Connector per network minimum; **two recommended** for failover redundancy
- Subdomain/URL **cannot be changed** after network creation

### Client Platforms
- macOS, Windows, Linux, ChromeOS, Android, iOS, iPadOS
- Native Apple M1 support via Mac App Store
- Download: `https://get.twingate.com`
- No pre-configuration required by org; users authenticate via SSO

## Prerequisites
- Internal IP addresses or domain names of target resources
- Ability to run Docker container (or Linux service) on a host in target network
- SSO/identity provider (Okta, Entra ID, Google Workspace, OneLogin supported)

## Configuration Values
| Parameter | Value/Note |
|-----------|-----------|
| Connector delivery | Docker container or native Linux service |
| Supported cloud | AWS, Azure, GCP, DigitalOcean, on-prem |
| Transport protocol | TLS v1.2 |
| Tunnel mode | Split tunnel (default) |
| Billing unit | Per user/seat (monthly or annual) |

## Gotchas
- Twingate URL (subdomain) is **permanent** — choose carefully at network creation
- Connectors are not directly accessed by users and have no public internet listener — do not treat like a VPN gateway
- Twingate does not store passwords; credentials handled entirely by identity provider
- Scaling one Connector per network is sufficient but single point of failure without a pair

## Related Docs
- How Twingate Works (architecture overview)
- Connector deployment / deployment options
- Identity provider integrations
- Role-based access controls
- API documentation
- Service Reliability
- Twingate Security
- Subscription management
- `get.twingate.com` (client downloads)