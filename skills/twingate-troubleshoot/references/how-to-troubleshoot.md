# Twingate Troubleshooting Guide

## Page Title
How to Troubleshoot User Issues with the Twingate Service

## Summary
Structured methodology for diagnosing Twingate ZTNA connection failures by tracing the connection chain: authentication → Client/ACL → DNS → tunnel establishment → Connector-to-Resource. Troubleshooting requires interrogating components rather than probing perimeters, since inbound ports are closed by design.

## Key Information
- **Control plane vs. data plane**: Controller decides *if* access is allowed; Client/Connector/Relays handle *how* — failures can be policy or network issues
- **Connection chain**: Identity Auth → Client receives ACL → DNS interception → P2P tunnel to Connector → Connector forwards to Resource
- **Relays**: Used as fallback if P2P/NAT traversal fails; P2P is preferred for performance
- **Split tunnel by default**: Undefined domains bypass the tunnel — critical for SaaS app failures

## Prerequisites
- Access to Twingate Admin Console
- Access to Identity Provider admin console (Okta, Entra ID, Google Workspace)
- Ability to retrieve Client logs and Connector logs

## Step-by-Step Methodology

1. **Define scope**: One user vs. all? One resource vs. all? One location vs. all? When did it start?
2. **Check Twingate status page** for active incidents
3. **Verify identity/device posture**: Group membership in IdP, trusted device status, Security Policy requirements
4. **Trace connection via Resource Activity Report** (`Network > Resources > [Resource] > Activity`)

## Configuration Values / Admin Console Paths
- Resource activity: `Network > Overview` (Activity Events)
- Connector status: `Network > Connectors`
- Audit logs: `Settings > Reports > Audit Logs`
- Support tickets: `Help > Support`
- Connector logs (Docker): `docker logs`
- Connector logs (systemd): `journalctl`

## Diagnostic Quick Reference

| Symptom | First Tool | Key Question |
|---|---|---|
| Can't log in | IdP Console | User active and assigned to Twingate app? |
| App won't connect | Client Logs / OS Services | Is Twingate daemon running? |
| Can't reach internal host | `nslookup` + Activity Report | DNS error at Connector or no events at all? |
| No one can reach resource | Admin Console Connector Status | Connectors online? Clock in sync? |
| Slow performance | Admin Console Connector Details | P2P or Relayed? UDP ports blocked? |
| Local printer broken | `ipconfig` + Resource definitions | Resource CIDR overlapping local subnet? |
| SaaS app partially loads | Browser DevTools Network tab | All dependency domains defined as Resources? |

## Gotchas
- **No events in Activity Report** = traffic never reached Connector (Client-side issue: local network, DNS, or security software blocking)
- **"DNS lookup error"** = Connector host can't resolve the Resource hostname (fix: Connector host DNS config)
- **"Unable to connect"** = Connector reached but can't route to Resource (firewall, security group, or app blocking)
- **Successful events + user still fails** = application-layer issue, not Twingate
- **`ping`/`tracert` from external networks won't work** — no inbound ports open by design
- **Clock drift on Connector** causes connection failures — check via Connector Details page
- **SaaS apps with CDN/API subdomains** require all dependent domains added as separate Resources

## Related Docs
- How Twingate Works (architecture overview)
- Identity Providers configuration
- Device/Client Failures
- DNS Resolution Problems
- Connector Issues
- Firewall Issues
- Split Tunneling Issues
- Engaging Technical Support
- Self-Serve Troubleshooting Guide