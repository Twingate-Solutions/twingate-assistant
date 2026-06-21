# Twingate FAQ

## Page Title
Twingate Frequently Asked Questions

## Summary
Reference page covering Twingate's core concepts, deployment model, performance characteristics, and security architecture. Defines key terminology and addresses common implementation questions for administrators evaluating or deploying Twingate.

## Key Information

### Core Concepts (Glossary)
- **Resource**: Any TCP/UDP destination host, server, or application defined by its address
- **Connector**: Software proxy deployed on the destination network (Docker container or Linux service); all traffic appears to originate from Connector host
- **Security Policy**: Access controls applied to users for Resource access (e.g., MFA requirements)
- **Group**: Logical user grouping with permissions to a set of Resources; each Group has one Security Policy

### Architecture Facts
- Split tunnel by default — only Twingate Resources route through your infrastructure
- No inbound public internet exposure required; Connectors make outbound connections only
- Transport protocol: TLS v1.2 with standard ciphers
- WireGuard not currently supported (monitored for future adoption)

### Deployment Facts
- Requires zero network infrastructure changes
- Can coexist with existing VPN infrastructure
- Twingate URL/subdomain **cannot be changed** after network creation
- Recommend deploying Connectors in pairs for failover redundancy
- Only one Connector required per network minimum

### Platform Support
- Clients: macOS (M1 native), Windows, Linux, ChromeOS, Android, iOS, iPadOS
- Client download: `https://get.twingate.com` or device app stores
- Connector deployment: Docker container or native Linux system service
- Cloud platforms: AWS, Azure, GCP, DigitalOcean, on-premise

## Prerequisites
- Knowledge of internal IP addresses or domain names of target resources
- Ability to run a Docker container on a host within the target network
- Identity provider for SSO (Okta, Entra ID/Azure AD, Google Workspace, OneLogin)

## Configuration Values
| Parameter | Value/Note |
|-----------|------------|
| Transport | TLS v1.2 |
| Connector delivery | Docker container or Linux system service |
| Client config required | None (zero pre-configuration) |
| Billing model | Per-user seat, monthly or annual |

## Gotchas
- **Subdomain is permanent**: Twingate network URL cannot be modified post-creation
- **Credentials not stored**: Twingate delegates auth entirely to IdP; does not handle passwords
- **Seats are allocated**: Exceeding seat count requires purchase or reassignment — no automatic overflow
- **Connector host visibility**: All Resource traffic appears to originate from Connector host IP

## Related Docs
- How Twingate Works (architecture overview)
- Connector Deployment (step-by-step + best practices)
- Deployment Options (service-specific connector methods)
- Identity Provider Integrations
- Twingate API (programmatic configuration)
- Role-Based Access Controls
- Service Reliability
- Subscription Management
- Twingate Security