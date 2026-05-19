# Twingate Troubleshooting Guide

## Page Title
How to Troubleshoot User Issues with the Twingate Service

## Summary
Structured methodology for diagnosing Twingate ZTNA connection failures by tracing the connection chain across identity, DNS, routing, and Connector layers. Distinguishes between control plane (policy) and data plane (connectivity) failures. Provides symptom-to-cause mapping for rapid triage.

## Key Information
- **Control plane** (Controller): Decides *if* access is allowed — policy/identity issues
- **Data plane** (Client + Connectors + Relays): Handles *how* connection is made — network/connectivity issues
- Connectors make **outbound-only** connections; no inbound ports needed
- Relays facilitate P2P via NAT traversal; fallback to relayed traffic if P2P fails
- Traditional tools (`ping`, `tracert`) ineffective for external probing — troubleshoot by interrogating components

## Connection Chain (In Order)
1. Identity & Authentication (IdP)
2. Client receives signed ACL from Controller
3. DNS interception by Client
4. Encrypted tunnel to Connector (P2P preferred)
5. Connector forwards traffic to Resource

## Diagnostic Quick Reference

| Symptom | Likely Cause | First Tool |
|---|---|---|
| Can't log in | IdP/Authentication | IdP Console |
| Client won't connect | Device/Client app | Client logs / OS services |
| Can't reach internal hostname | DNS resolution | `nslookup`/`dig` + Admin Console Activity |
| No one can reach a Resource | Connector down | Admin Console → Connector Status |
| Slow performance | Relayed (not P2P) | Admin Console → Connector Details |
| Home printer breaks | IP/subnet conflict | `ipconfig` + Resource definitions |
| SaaS app partially loads | Missing Resource definitions | Browser DevTools Network tab |

## Admin Console Locations
- **Activity Events**: Network → Overview (real-time connection attempts/errors)
- **Connector Status**: Network → Connectors (status, P2P vs Relayed, clock drift)
- **Audit Logs**: Settings → Reports → Audit Logs
- **Support Tickets**: Help → Support

## Activity Event Interpretations
- **No events logged**: Traffic never reached Connector — Client-side or DNS issue
- **DNS lookup error**: Connector can't resolve hostname — Connector host DNS misconfigured
- **Unable to connect**: Connector can't route to Resource — firewall/security group blocking
- **Successful but app fails**: Application-level issue, not Twingate
- **Successful but partial load**: Missing domain definitions — add CDN/API subdomains as Resources

## Four-Step Troubleshooting Methodology
1. **Define scope**: One user vs. all? One resource vs. all? One location vs. all?
2. **Check known states**: Visit [Twingate Status Page](https://status.twingate.com) first
3. **Verify identity/device posture**: Group membership, Trusted Device policy, IdP sync
4. **Trace connection**: Use Resource Activity Report in Admin Console

## Gotchas
- Split-tunnel design means undefined domains bypass the tunnel — web apps requiring CDN/auth subdomains will break unless all dependent domains are added as Resources
- Twingate is invisible to unauthorized users — external port scanning won't work for diagnosis
- Clock drift on Connector host causes authentication failures — check under Connector Details
- Local subnet overlap with Resource CIDR definitions breaks local network access (e.g., printers)

## Related Docs
- How Twingate Works (architecture)
- Identity Providers
- Connector Issues
- DNS Resolution Problems
- Firewall Issues
- Split Tunneling Issues
- Client Logs guide
- Connector Logs guide
- Engaging Technical Support