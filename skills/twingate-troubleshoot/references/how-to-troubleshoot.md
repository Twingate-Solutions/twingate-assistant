# Twingate Troubleshooting Guide

## Page Title
How to Troubleshoot User Issues with the Twingate Service

## Summary
Structured methodology for diagnosing Twingate ZTNA connection failures by tracing the connection chain across five stages: authentication, device/client, DNS, routing/connection, and connector-to-resource. Distinguishes between control plane (policy) failures and data plane (network) failures. Emphasizes "interrogating components" rather than probing perimeters since infrastructure is invisible by design.

## Key Information
- **Four components**: Client (end device), Connectors (private network), Relays (P2P facilitation/fallback), Controller (policy enforcement)
- **Control plane vs data plane**: Controller decides *if* access is allowed; Client/Connector/Relays handle *how* connection is made
- **Relays**: Fallback when P2P fails; P2P vs Relayed status visible in Admin Console → Connector Details
- Traditional tools (`ping`, `tracert`) ineffective from external networks—no inbound ports are open

## Diagnostic Quick Reference

| Symptom | First Tool | Key Question |
|---|---|---|
| Can't log in | IdP Console | User active and assigned in IdP? |
| App won't connect | Client Logs / OS Services | Is Twingate service/daemon running? |
| Can't reach internal hostname | `nslookup`/Admin Console Activity | DNS error at Connector or Client? |
| No one can access a resource | Admin Console Connector Status | Are Connectors online, clock in sync? |
| Slow performance | Admin Console Connector Details | P2P or Relayed? UDP ports blocked? |
| Local printer breaks | `ipconfig` / Resource Definitions | Resource CIDR overlapping local subnet? |
| SaaS app partially loads | Browser DevTools Network tab | All dependency domains defined as Resources? |

## Step-by-Step Methodology

1. **Define scope**: One user vs. all? One resource vs. all? One location vs. all? When did it start?
2. **Check known states**: Visit [Twingate status page](https://status.twingate.com) for active incidents
3. **Verify identity/device posture**: Confirm user group membership in Admin Console and IdP; check Trusted Device status against Security Policy
4. **Trace connection** via Admin Console → Network → Resources → Activity:
   - **No events**: Traffic never reached Connector; issue is Client-side (DNS blocked, local network)
   - **DNS lookup error**: Connector cannot resolve hostname; check Connector host DNS config
   - **Unable to connect**: Connector can't route to destination; check firewall/security groups
   - **Success but app fails**: Application-layer issue (permissions, app config)
   - **Success but web app partially loads**: Missing Resource definitions for dependency domains (CDNs, APIs)

## Configuration Values / Tools

| Tool | Usage |
|---|---|
| Admin Console → Network → Overview | Resource Activity Events |
| Admin Console → Network → Connectors | Status, P2P vs Relayed, clock drift |
| Admin Console → Settings → Reports → Audit Logs | Admin config changes |
| `nmap -p <port> resource.internal` | Test port connectivity from Client/Connector |
| `journalctl` / `docker logs` | Connector logs (systemd/Docker) |

## Gotchas
- **Split tunnel by design**: Requests to domains not defined as Resources bypass the tunnel—SaaS apps with multiple subdomains/CDNs require all dependency domains defined as Resources
- **IP overlap**: Resource CIDR definitions that overlap a user's local subnet (e.g., `192.168.1.0/24`) break local device access (printers, NAS)
- **Clock drift**: Connector clock out of sync causes authentication failures; visible in Connector Details
- **Relayed connections**: Indicate outbound UDP is blocked; resolve firewall rules to restore P2P performance

## Related Docs
- How Twingate Works (architecture overview)
- Identity Providers
- Device/Client Failures
- DNS Resolution Problems
- Connector Issues
- Firewall Issues
- Split Tunneling Issues
- Engaging Technical Support
- Self-Serve Troubleshooting Guide