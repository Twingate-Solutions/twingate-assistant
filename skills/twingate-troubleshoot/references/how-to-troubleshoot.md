# Twingate Troubleshooting Guide

## Page Title
How to Troubleshoot User Issues with the Twingate Service

## Summary
Structured guide for diagnosing Twingate ZTNA connection failures by tracing the connection chain across five stages: authentication, client/device, DNS resolution, routing/tunnel establishment, and connector-to-resource delivery. Troubleshooting requires interrogating components rather than probing the perimeter, since infrastructure is invisible by design. Issues stem from either the control plane (policy/identity) or data plane (network connectivity).

## Key Information
- **Architecture**: Client → Relay (NAT traversal/fallback) → Connector → Resource
- **Control plane** (Controller): decides *if* access is allowed (policy, identity, device posture)
- **Data plane** (Client, Connectors, Relays): handles *how* connection is made
- Connectors make **outbound-only** connections; no inbound firewall ports required
- Resource Activity Events are the primary data-plane diagnostic tool

## Connection Chain Stages
1. Identity & Authentication (IdP: Okta, Entra ID, Google Workspace)
2. Device & Client (ACL delivered after auth)
3. DNS Resolution (Client intercepts DNS queries)
4. Routing & Tunnel (P2P preferred via NAT traversal; Relay as fallback)
5. Connector → Resource (Connector forwards decrypted traffic)

## Diagnostic Tools
| Tool | Purpose |
|------|---------|
| Admin Console → Network > Overview | Resource Activity Events (real-time) |
| Admin Console → Network > Connectors | Status, P2P vs. Relayed, clock drift |
| Admin Console → Settings > Reports > Audit Logs | Config change history |
| Client Logs | Device-side diagnostics |
| Connector Logs | `docker logs` or `journalctl` |
| `nslookup`/`dig` | DNS diagnosis |
| `nmap -p <port> <resource>` | Port connectivity testing |
| Browser DevTools (Network tab) | Missing domain dependencies for web apps |

## Step-by-Step Methodology
1. **Define scope**: One user vs. all? One resource vs. all? One location vs. all? When did it start?
2. **Check known states**: Visit [Twingate status page](https://status.twingate.com) for active incidents
3. **Verify control plane**: User in correct Groups? Device posture meets Security Policy? Trusted Device status?
4. **Trace connection** via Resource Activity Events:
   - No events → problem on client side (Client, local network, DNS blocked locally)
   - "DNS lookup error" → Connector's host DNS misconfigured
   - "Unable to connect" → Connector can't route to Resource (firewall, security group, app blocking)
   - Success but app broken → missing dependent domains not defined as Resources

## Symptom Quick Reference
| Symptom | Likely Cause | First Check |
|---------|-------------|------------|
| Can't log in | IdP authentication | User active in IdP + assigned to Twingate app? |
| App won't connect | Client/daemon | Is Twingate service running? |
| Can't reach internal hostname | DNS resolution | `nslookup` on client; Activity for DNS error at Connector |
| No one can access a resource | Connector down | Connector status + clock sync in Admin Console |
| Slow performance | Relay fallback (no P2P) | Connector Details: P2P or Relayed? UDP ports blocked? |
| Local printer broken | IP/subnet conflict | Resource CIDR overlapping local network? |
| SaaS app partially loads | Missing Resource definitions | Browser DevTools Network tab for blocked domains |

## Gotchas
- `ping`/`tracert` from external networks are ineffective — no open inbound ports to probe
- Split-tunnel design: undefined domains bypass the tunnel entirely, causing partial app failures
- Clock drift on Connector host breaks connections — check in Connector Details
- Policy failures (device posture, geo-block) look like connectivity failures

## Related Docs
- How Twingate Works (architecture overview)
- Identity Providers configuration
- Device/Client Failures
- DNS Resolution Problems
- Connector Issues
- Firewall Issues
- Split Tunneling Issues
- Engaging Technical Support
- Self