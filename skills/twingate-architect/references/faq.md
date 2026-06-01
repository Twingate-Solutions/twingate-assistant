# Twingate FAQ

## Page Title
Frequently Asked Questions (FAQ)

## Summary
Reference page covering Twingate's core concepts, deployment model, performance characteristics, and security architecture. Provides concise answers to common questions about how Twingate differs from VPNs and how to deploy it. Serves as an entry point to more detailed documentation.

## Key Information

### Core Concepts (Glossary)
- **Resource**: Any TCP/UDP destination host/server/app defined by address
- **Connector**: Software proxy (Docker container) running on destination network; all traffic appears to originate from Connector host
- **Security Policy**: Defines auth controls (e.g., MFA) applied per Resource regardless of protocol
- **Group**: Logical user grouping linked to Resources + one Security Policy

### Architecture
- Split tunnel by default — only Twingate Resources route through your infrastructure
- No inbound public internet exposure required; Connectors make outbound connections only
- Transport: TLS v1.2 with standard ciphers
- WireGuard not currently supported (under evaluation)

### Platform Support
- Clients: macOS (incl. Apple M1), Windows, Linux, ChromeOS, Android, iOS, iPadOS
- Download: `https://get.twingate.com` or device app stores
- Connector: Docker container or native Linux system service
- Cloud: AWS, Azure, GCP, DigitalOcean, on-premise

## Prerequisites
- Internal IP addresses or domain names of target resources
- Ability to run a Docker container on a host within target network
- SSO/identity provider (Okta, Entra ID, Google Workspace, OneLogin supported)

## Configuration Notes
- Deploy **one Connector minimum** per network; **two recommended** for failover redundancy
- Twingate URL/subdomain **cannot be changed** after network creation
- Connectors require no special host privileges
- No firewall rule changes, IP remapping, or hardware appliances required

## Gotchas
- Subdomain is permanent — choose carefully at network creation
- Twingate can coexist with existing VPN infrastructure (no rip-and-replace required)
- Per-user ("seat") billing — must purchase additional seats or reassign when at capacity
- Twingate does not store user credentials; authentication delegated entirely to identity provider

## Related Docs
- How Twingate Works (architecture)
- Deploying Connectors (step-by-step + best practices)
- Connector Deployment Options (service-specific)
- Identity Provider Integration
- Twingate API (programmatic deployment)
- Security overview
- Subscription Management
- Service Reliability
- Client documentation