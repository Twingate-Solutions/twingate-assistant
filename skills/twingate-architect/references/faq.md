# Twingate FAQ

## Page Title
Twingate Frequently Asked Questions

## Summary
Reference glossary and FAQ covering Twingate's core concepts, deployment requirements, performance characteristics, and security model. Answers common questions about how Twingate differs from VPNs and what infrastructure changes are required for deployment.

## Key Information

### Core Concepts (Glossary)
- **Resource**: Any TCP/UDP destination host, server, or application (defined by address only)
- **Connector**: Software proxy deployed on destination network; runs as Docker container or Linux service; no special host privileges required
- **Security Policy**: Defines auth controls (e.g., MFA) applied per Resource, regardless of protocol
- **Group**: Logical user grouping mapped to Resources + a single Security Policy

### Architecture Facts
- Split tunnel by default — only Twingate Resources route through your infrastructure
- No inbound public internet exposure required; Connectors initiate outbound connections only
- Transport: TLS v1.2 with standard ciphers
- WireGuard: not currently implemented (monitoring adoption)

### Platform Support
- Clients: macOS, Windows, Linux, ChromeOS, Android, iOS, iPadOS (including Apple M1 native)
- Client download: `get.twingate.com`
- Connector deployment: Docker container, native Linux service, or cloud-native container services (AWS, GCP, Azure)

### Identity Providers
- Okta, Entra ID (Azure AD), Google Workspace, OneLogin
- Twingate delegates auth; does not store passwords

## Prerequisites
- Internal IP addresses or domain names of target resources
- Ability to run a Docker container on a host within the target network
- No firewall rule changes, IP remapping, or hardware appliances required

## Configuration Values
- **Connector deployment**: Docker container (no special privileges) or Linux native service
- **Recommended Connector count**: Minimum 1 per network; 2 recommended for failover redundancy
- **Twingate subdomain/URL**: Set at network creation; **cannot be changed afterward**

## Gotchas
- Twingate URL (subdomain) is **permanent** after network creation — choose carefully
- Access controls are Group-based: all Users in a Group access **all** Resources in that Group
- Per-seat billing: must purchase additional seats or reassign before adding new users
- WireGuard is not supported as transport layer currently

## Related Docs
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- [Deploying Connectors](https://www.twingate.com/docs/connectors)
- [Connector Deployment Options](https://www.twingate.com/docs/connector-deployment)
- [Identity Provider Integrations](https://www.twingate.com/docs/identity-providers)
- [Twingate API](https://www.twingate.com/docs/api)
- [Service Reliability](https://www.twingate.com/docs/service-reliability)
- [Twingate Security](https://www.twingate.com/docs/security)
- [Subscription Management](https://www.twingate.com/docs/subscription-management)