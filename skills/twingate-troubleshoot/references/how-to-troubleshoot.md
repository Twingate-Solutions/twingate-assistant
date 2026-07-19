# Twingate Troubleshooting Guide

## Page Title
How to Troubleshoot User Issues with the Twingate Service

## Summary
Structured methodology for diagnosing Twingate ZTNA connection failures by tracing the logical connection path across five stages. Distinguishes between control plane (policy/identity) and data plane (network/connectivity) failures. Provides a symptom-to-cause quick reference table.

## Key Information
- **Architecture components**: Client (end-user device) → Relay (NAT traversal/fallback) → Connector (deployed in private network) → Resource
- **Control plane**: Controller determines *if* access is allowed (policy, identity)
- **Data plane**: Client + Connectors + Relays handle *how* connection is made
- **Connection chain**: Identity Auth → Client ACL → DNS Resolution → Routing/Tunnel → Connector-to-Resource
- Connectors make **outbound-only** connections; no inbound firewall ports needed
- Traditional tools (`ping`, `tracert` externally) are ineffective; probe components instead

## Diagnostic Quick Reference

| Symptom | Likely Cause | First Tool |
|---|---|---|
| Can't log in | Identity/IdP | IdP Console |
| App won't connect | Client/daemon | Client logs / OS services |
| Can't reach internal hostname | DNS resolution | `nslookup`/`dig` + Admin Console Activity |
| No one can reach a resource | Connector down | Admin Console → Connector Status |
| Slow performance | Relayed (not P2P) | Admin Console → Connector Details |
| Local printer breaks | IP/subnet conflict | `ipconfig` + Resource definitions |
| SaaS app partially loads | Missing Resource definitions | Browser DevTools Network tab |

## Troubleshooting Methodology (4 Steps)

1. **Define scope**: One user vs. all? One resource vs. all? One location vs. all? When did it start?
2. **Check known states**: Review [Twingate Status Page](https://www.twingatestatus.com) for active incidents; check recent config changes
3. **Verify identity/device posture**: Confirm group membership in Admin Console + IdP sync; check Trusted Device policy compliance
4. **Trace the connection**: Admin Console → Network → Resources → Activity

## Admin Console Activity Event Interpretation

- **No events logged**: Traffic never reached Connector → Client-side issue (local network, DNS blocked by another service)
- **"DNS lookup error"**: Connector cannot resolve hostname → DNS config on Connector host
- **"Unable to connect"**: Connector can't route to destination → firewall, security group, or app blocking Connector IP
- **Successful events + user still fails**: Application-layer issue (permissions, app config)
- **Successful events + web app partially loads**: Missing Resource definitions for dependent domains (CDNs, auth endpoints)

## Key Admin Console Locations
- `Network > Overview` → Resource Activity Events (real-time connection attempts/errors)
- `Network > Connectors` → Status, connection type (P2P vs. Relayed), clock drift
- `Settings > Reports > Audit Logs` → Administrative config changes

## Diagnostic Tools
- **Twingate Client logs**: User-uploadable via Client app
- **Connector logs**: `docker logs <container>` or `journalctl -u twingate-connector`
- `nslookup`/`dig`: DNS diagnostics
- `nmap -p <port> <resource>`: Test port connectivity
- Browser DevTools Network tab: Identify missing dependent domains for web apps
- Wireshark: Deep packet inspection

## Gotchas
- Clock drift on Connector host breaks connections; check in Connector Details
- Split tunnel by design: undefined domains bypass the tunnel and may fail
- Local subnet conflicts: Resource CIDR overlapping user's home/office network breaks local access
- P2P connection requires outbound UDP; firewall blocking UDP forces Relayed path (slower)
- SaaS apps often depend on multiple subdomains — all must be defined as Resources

## Prerequisites
- Access to Twingate Admin Console
- Access to Identity Provider admin console
- Connector host access (for log retrieval)

## Related Docs
- [How Twingate Works](https://www.twingate.com/docs/how-twingate-works)
- [Client Logs