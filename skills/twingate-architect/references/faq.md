# Twingate FAQ

## Page Title
Twingate Frequently Asked Questions

## Summary
Reference glossary and FAQ covering Twingate's core concepts, deployment model, performance characteristics, and security approach. Covers key differentiators from VPNs and answers common implementation questions for both administrators and end users.

## Key Information

### Core Concepts (Glossary)
- **Resource**: Any TCP/UDP destination host, server, or application (protocol-agnostic)
- **Connector**: Software proxy deployed on destination network; all traffic appears to originate from Connector host; delivered as Docker container (no special host privileges required)
- **Security Policy**: Access controls applied per-user for Resource access (e.g., MFA enforcement)
- **Group**: Logical user grouping mapped to Resources + single Security Policy

### Architecture Facts
- Split tunnel by default — only configured Resources route through infrastructure
- No inbound public internet exposure required; Connectors initiate outbound connections only
- Transport: TLS v1.2 with standard ciphers
- WireGuard: not currently implemented (monitoring adoption)

### Platform Support
- Clients: macOS (including M1 native), Windows, Linux, ChromeOS, Android, iOS, iPadOS
- Client download: `https://get.twingate.com`
- Connector hosting: Docker container or native Linux service; AWS, Azure, GCP native container services supported

## Prerequisites
- Internal IP addresses or domain names of target resources
- Ability to run a Docker container on a host within the target network
- SSO/Identity Provider integration (Okta, Entra ID/Azure AD, Google Workspace, OneLogin)

## Configuration Values
| Item | Value/Note |
|------|-----------|
| Client download URL | `https://get.twingate.com` |
| Connector deployment | Docker container or Linux system service |
| Transport protocol | TLS v1.2 |
| Billing unit | Per user/seat (monthly or annual) |

## Gotchas
- **Twingate subdomain/URL cannot be changed** after network creation — choose carefully at setup
- Connectors should be deployed **in pairs** for failover redundancy (only one required minimum)
- Twingate does **not** store user credentials — authentication fully delegated to IdP
- Coexists with existing VPN infrastructure — no rip-and-replace required

## Step-by-Step (Deployment Overview)
1. Identify internal IPs/hostnames of resources to expose
2. Deploy Connector (Docker/Linux service) on target network host
3. Register resources in Twingate Admin console
4. Assign user Groups to Resources with appropriate Security Policies
5. Users download client, authenticate via SSO — no client pre-configuration needed

## Related Docs
- How Twingate Works (architecture)
- Deploying Connectors + deployment options
- Client documentation
- Identity provider integrations
- API documentation (programmatic deployment)
- Subscription management
- Twingate Security
- Service Reliability
- Role-based access controls