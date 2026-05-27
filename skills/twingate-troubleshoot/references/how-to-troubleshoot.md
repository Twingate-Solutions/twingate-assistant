# Twingate Troubleshooting Guide

## Page Title
How to Troubleshoot User Issues with the Twingate Service

## Summary
Structured methodology for diagnosing Twingate ZTNA connection failures by tracing the connection chain across five stages: authentication, client/device, DNS resolution, routing/tunnel establishment, and connector-to-resource delivery. Troubleshooting requires interrogating components rather than probing perimeters since infrastructure is invisible by design. Issues fall into either control plane (policy/identity) or data plane (network/connectivity) problems.

## Key Information
- **Connection chain**: Identity Auth → Client/ACL → DNS Resolution → Tunnel/Routing → Connector → Resource
- **Control plane** (Controller): decides *if* access is allowed (policy, identity, device posture)
- **Data plane** (Client, Connectors, Relays): handles *how* connection is made
- Connectors make **outbound-only** connections; no inbound firewall ports required
- Relays facilitate P2P NAT traversal; act as fallback if P2P fails
- `ping`/`tracert` ineffective from external networks (no open inbound ports)

## Diagnostic Quick Reference

| Symptom | Likely Failure | First Tool |
|---|---|---|
| Can't log in | IdP authentication | IdP Admin Console |
| App won't connect | Client/daemon not running | Client logs / OS services |
| Connected, can't reach internal host | DNS resolution | `nslookup`/`dig` + Admin Console Activity |
| No one can reach a resource | Connector down | Admin Console → Connector Status |
| Slow performance | Relayed instead of P2P | Admin Console → Connector Details (connection type) |
| Local printer breaks | IP/subnet conflict | `ipconfig` + Resource CIDR definitions |
| SaaS app partially loads | Missing Resource definitions | Browser DevTools Network tab |

## Step-by-Step Methodology

1. **Define scope**: One user vs. all users? One resource vs. all? One location vs. all? When did it start?
2. **Check known states**: Review [Twingate status page](https://www.twingatestatus.com) for active incidents
3. **Verify identity/device posture**: Confirm group membership in Admin Console and IdP; check Trusted Device policy compliance
4. **Trace connection**: Check Resource Activity (`Network > Resources > [Resource] > Activity`)

## Admin Console Diagnostic Locations
- **Resource Activity Events**: `Network > Overview`
- **Connector Status/Details**: `Network > Connectors`
- **Audit Logs**: `Settings > Reports > Audit Logs`
- **Support Tickets**: `Help > Support`

## Activity Log Interpretations
- **No events logged**: Traffic never reached Connector → Client, local network, or DNS issue on user side
- **DNS lookup error**: Connector cannot resolve hostname → DNS config on Connector host
- **Unable to connect**: Connector cannot route to destination → firewall, security group, or app blocking
- **Success but app broken**: Missing dependent domain Resources (CDNs, auth endpoints) → add as Resources

## Gotchas
- Web apps often depend on multiple domains (CDNs, subdomains); all must be defined as Resources or they bypass the tunnel
- Twingate is **split tunnel by design**; undefined domains route normally and may be blocked by destination services
- Resource CIDR definitions overlapping with user's local subnet breaks local network access (printers, NAS, etc.)
- Slow connections usually indicate **Relayed** rather than P2P — check if outbound UDP ports are blocked

## Tools
- **Client logs**: Enable detailed logging in Client app, upload to Twingate
- **Connector logs**: `docker logs` (container) or `journalctl` (systemd)
- **General**: `ping`, `traceroute`, `nslookup`/`dig`, `nmap`, `curl`, `ipconfig`/`ifconfig`, Wireshark, browser DevTools

## Related Docs
- How Twingate Works (architecture overview)
- Identity Providers configuration
- Device/Client Failures
- DNS Resolution Problems
- Connector Issues
- Firewall Issues
- Split Tunneling Issues
- Engaging Technical Support