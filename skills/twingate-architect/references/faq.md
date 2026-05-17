# Twingate FAQ

## Page Title
Frequently Asked Questions

## Summary
Reference page covering Twingate core concepts, deployment requirements, performance characteristics, and security model. Defines key terminology and addresses common implementation questions for administrators evaluating or deploying Twingate.

## Key Information

### Core Concepts
- **Resource**: Any TCP/UDP destination (host, server, app) defined by address
- **Connector**: Software proxy deployed on destination network; all traffic appears to originate from Connector host
- **Group**: Logical user grouping tied to a set of Resources and a single Security Policy
- **Security Policy**: Defines authentication/authorization controls (e.g., MFA) applied per Resource regardless of protocol

### Architecture
- Split tunnel by default — only Twingate Resources route through your infrastructure
- Connectors make outbound connections; no inbound ports exposed to public internet
- Transport: TLS v1.2 with standard ciphers
- WireGuard not currently supported (under monitoring)

### Platform Support
- Clients: macOS, Windows, Linux, ChromeOS, Android, iOS, iPadOS
- Download: `get.twingate.com`
- Apple M1: Native support via Mac App Store
- Connector: Docker container or native Linux service; runs on AWS, GCP, Azure, DigitalOcean, on-prem

## Prerequisites
- Know internal IP addresses or domain names of target Resources
- Ability to run a Docker container on a host within the target network
- No firewall rule changes, hardware appliances, or network reconfiguration required

## Configuration Notes
- Deploy Connectors in **pairs** for failover redundancy (one minimum per network)
- Twingate subdomain/URL **cannot be changed** after network creation
- Coexists with existing VPN infrastructure — no rip-and-replace required

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Transport protocol | TLS v1.2 |
| Connector delivery | Docker container or Linux service |
| Tunnel mode | Split tunnel (default) |
| Billing unit | Per user/seat (monthly or annual) |

## Identity Provider Integrations
- Okta, Entra ID (Azure AD), Google Workspace, OneLogin
- Twingate delegates authentication; does not store user credentials/passwords

## API
- Full API available for programmatic configuration
- Supports automated Resource registration and Group assignment
- See [API docs](https://www.twingate.com/docs/api)

## Gotchas
- **Subdomain is permanent** — choose Twingate network URL carefully at creation
- Connector host must have outbound connectivity; Connectors are not publicly accessible
- One seat = one individual user; exceeding seat count requires purchase or reassignment
- Groups have a single Security Policy — plan Group structure around policy requirements

## Related Docs
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- [Deploying Connectors](https://www.twingate.com/docs/connector)
- [Connector Deployment Options](https://www.twingate.com/docs/deployment-options)
- [Identity Provider Integrations](https://www.twingate.com/docs/idp-integrations)
- [API Documentation](https://www.twingate.com/docs/api)
- [Security Overview](https://www.twingate.com/docs/security)
- [Service Reliability](https://www.twingate.com/docs/service-reliability)
- [Subscription Management](https://www.twingate.com/docs/subscription-management)