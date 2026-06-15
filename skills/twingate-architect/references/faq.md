# Twingate FAQ

## Page Title
Frequently Asked Questions

## Summary
Reference page covering Twingate's core concepts, deployment model, and common questions. Twingate is a zero-trust network access solution that replaces VPNs with resource-level access controls. It operates as a software overlay requiring no infrastructure changes.

## Key Information

### Core Concepts
- **Resource**: Any TCP/UDP destination (host, server, app) defined by address
- **Connector**: Software proxy (Docker container or Linux service) deployed on target network; all traffic appears to originate from Connector host
- **Security Policy**: Access controls applied to users per Resource (e.g., MFA enforcement)
- **Group**: Collection of Users mapped to Resources + one Security Policy

### Architecture
- Split-tunnel by default — only Twingate Resources route through your infrastructure
- Connectors make outbound connections only; no public-facing ports required
- Transport: TLS v1.2 with standard ciphers
- WireGuard not currently implemented

## Prerequisites
- Internal IP addresses or domain names of target resources
- Ability to run Docker on a host within the target network
- SSO/identity provider (Okta, Entra ID, Google Workspace, OneLogin supported)

## Configuration Values
- Client download: `https://get.twingate.com`
- Platforms: macOS, Windows, Linux, ChromeOS, Android, iOS, iPadOS, Apple M1 native
- Connector delivery: Docker container (no special host privileges required) or native Linux service

## Gotchas
- **Subdomain is permanent**: Twingate URL/subdomain cannot be changed after network creation
- **Seat-based billing**: Each user = one seat; must purchase more or reassign to add users
- **Connectors in pairs**: Single connector works but deploy two per network for failover redundancy
- No passwords stored by Twingate — authentication fully delegated to identity provider

## Step-by-Step (High-Level Deployment)
1. Deploy Connector (Docker/Linux service) on target network host
2. Define Resources (IP/hostname) in Admin console
3. Create Groups, assign Users and Resources
4. Apply Security Policies to Groups
5. Users download client from `get.twingate.com`, sign in via SSO
6. Access is automatic — no gateway selection required

## Related Docs
- How Twingate Works (architecture)
- Connector deployment options and best practices
- Identity provider integrations
- API documentation (programmatic deployment)
- Subscription management
- Twingate Security overview
- Service Reliability