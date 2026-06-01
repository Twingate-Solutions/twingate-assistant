# Twingate Troubleshooting Guide

## Page Title
How to Troubleshoot User Issues with the Twingate Service

## Summary
Structured methodology for diagnosing Twingate ZTNA connection failures. Covers architecture fundamentals, tooling, and a repeatable 4-step process for isolating faults across control plane (policy) vs. data plane (connectivity) issues.

## Key Information
- **Architecture components**: Client (device), Connector (private network), Relay (P2P facilitation/fallback), Controller (policy/auth)
- **Control plane vs. data plane**: Controller decides *if* access is allowed; Client/Connector/Relay handle *how* connection is made
- Conventional tools (`ping`, `tracert`) ineffective from external networks — no inbound ports exposed by design
- Connection chain: Identity Auth → Client receives ACL → DNS resolution → Tunnel to Connector → Connector forwards to Resource

## Prerequisites
- Access to Twingate Admin Console
- Access to Identity Provider admin console (Okta, Entra ID, Google Workspace)
- Log access on Client devices and Connector hosts

## Step-by-Step: 4-Step Methodology

1. **Define scope**: One user vs. all? One resource vs. all? One location vs. all? When did it start?
2. **Check known states**: Visit [Twingate status page](https://status.twingate.com) for active incidents; review recent config changes
3. **Verify identity/device posture**: Confirm user Group membership in Admin Console + IdP sync; check Trusted Device status against Security Policy
4. **Trace connection**: Admin Console → Network → Resources → [Resource] → Activity tab

## Configuration Values / Tool Locations
| Tool | Path |
|------|------|
| Resource Activity Events | Admin Console → Network → Overview |
| Connector Status/Details | Admin Console → Network → Connectors |
| Audit Logs | Admin Console → Settings → Reports → Audit Logs |
| Support Ticket | Admin Console → Help → Support |
| Connector logs (Docker) | `docker logs <container>` |
| Connector logs (systemd) | `journalctl` |

## Diagnostic Quick Reference
| Symptom | First Tool | Key Question |
|---------|-----------|--------------|
| Can't log in | IdP Console | User active + assigned in IdP? |
| App won't connect | Client Logs / OS services | Is Twingate daemon running? |
| Can't reach internal hostname | `nslookup`/`dig` + Admin Console Activity | DNS error at Connector? |
| No one can reach a resource | Admin Console Connector Status | Connectors online? Clock in sync? |
| Slow performance | Admin Console Connector Details | P2P or Relayed? UDP ports blocked? |
| Home printer breaks | `ipconfig`/`ifconfig` | Resource CIDR overlapping local network? |
| SaaS app partially loads | Browser DevTools Network tab | All dependent domains defined as Resources? |

## Gotchas
- **Activity tab shows no events** → traffic never reached Connector; problem is on Client side (local DNS, another security tool intercepting traffic)
- **"DNS lookup error" in Activity** → Connector's host machine can't resolve the hostname; check Connector-side DNS config
- **"Unable to connect" in Activity** → Connector can't route to destination; check firewall/security groups between Connector and Resource
- **Successful events but user still fails** → Twingate path is fine; issue is application-level (permissions, auth)
- **SaaS app breaks** → Twingate is split-tunnel by default; CDN/auth subdomains not defined as Resources will bypass tunnel and may be blocked
- **Clock drift** on Connector host causes connection failures — check in Connector Details

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