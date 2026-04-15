## Page Title
FAQ — Frequently Asked Questions

## Summary
Covers the most common questions about Twingate's concept, deployment, and performance. Includes a built-in glossary for core Twingate terms. Good first-stop reference for understanding the fundamentals before diving into technical docs.

## Key Information

### Glossary
- **Resource**: any destination host, server, or application reachable by TCP/UDP; defined by its address
- **Connector**: software component deployed on the private network; all resource traffic originates from the Connector host; delivered as Docker container (no special privileges)
- **Security Policy**: defines what security controls (e.g. MFA) are applied to users accessing a Resource
- **Group**: logical grouping of Users; all Group members access all Resources associated with the Group; one Security Policy per Group

### General
- Twingate = Zero Trust Networking; every access verified regardless of network location
- Does not grant broad network access — only specific authorized Resources
- Clients available for: macOS, Windows, Linux, ChromeOS, Android, iOS, iPadOS — download from `get.twingate.com`
- Supports any TCP or UDP application out of the box

### Deployment
- **No infrastructure changes required**: no IP address remapping, no firewall rule changes, no new hardware
- Deploy Connector (Docker or native Linux service) on any host that can reach your private resources
- Can run alongside existing VPN — no rip-and-replace needed; phase rollout gradually
- Users install Client themselves from `get.twingate.com`; authenticate via existing SSO credentials
- Twingate URL (subdomain) **cannot be changed** after network creation
- Integrates with Okta, Entra ID (Azure AD), Google Workspace, OneLogin

### Performance
- **Split tunnel by default**: only Twingate resource traffic routes through your infrastructure; public internet traffic goes direct
- Transport protocol: TLS v1.2 with standard ciphers
- Supports WireGuard (open-source VPN protocol for point-to-point connections)

## Prerequisites
None — reference/FAQ page.

## Step-by-Step
Not applicable.

## Configuration Values
- Client download: `get.twingate.com`
- Supported client platforms: macOS, Windows, Linux, ChromeOS, Android, iOS, iPadOS

## Gotchas
- Twingate subdomain/URL cannot be changed after account creation — choose carefully
- Connectors should be deployed in pairs (HA); a single Connector is a single point of failure
- Split tunnel is the default — full-tunnel (routing all traffic through Connector) requires explicit configuration

## Related Docs
- `/docs/architecture` — how Twingate works
- `/docs/twingate-vs-vpn` — detailed VPN comparison
- `/docs/quick-start` — deployment steps
