# Twingate Troubleshooting Guide

## Page Title
How to Troubleshoot User Issues with the Twingate Service

## Summary
Structured methodology for diagnosing Twingate ZTNA connection failures by tracing the connection chain across five stages: authentication, device/client, DNS resolution, routing/tunnel establishment, and connector-to-resource. Distinguishes between control plane (policy/identity) and data plane (network/connectivity) failures. Conventional network probing tools (ping, tracert from outside) are ineffective due to ZTNA's invisible infrastructure design.

## Key Information
- **Connection chain stages:** Identity Auth → Device/Client ACL → DNS Resolution → Tunnel Establishment → Connector-to-Resource forwarding
- **Control plane** (Controller) = decides *if* access is allowed; **Data plane** (Client/Connector/Relays) = handles *how* connection is made
- **Relays** provide fallback if P2P connection fails; P2P preferred for performance
- Connectors make **outbound-only** connections — no inbound firewall ports required
- Resource Activity Report is the most critical first diagnostic tool

## Diagnostic Quick Reference

| Symptom | Failure Point | First Tool |
|---|---|---|
| Can't log in | Authentication/IdP | IdP Console (Okta, Entra ID) |
| App won't connect | Client/Device | Client logs, OS services |
| Can't reach internal hostname | DNS Resolution | `nslookup`/`dig`, Admin Console Activity |
| No one can access a resource | Connector | Admin Console Connector status |
| Slow performance | Firewall/NAT | Admin Console — P2P vs Relayed status |
| Home printer breaks | IP/Split tunnel conflict | `ipconfig`, Resource definitions |
| SaaS app partially loads | Missing Resource definitions | Browser DevTools Network tab |

## Step-by-Step Methodology
1. **Define scope** — one user vs. all, one resource vs. all, one location vs. all; correlate with recent changes
2. **Check status page** — verify no active Twingate incidents at status page
3. **Verify identity/device posture** — confirm user group membership in Admin Console and IdP; check Trusted Device policy compliance
4. **Trace connection attempt** — use Resource Activity Report (Network > Resources > Activity)

## Activity Report Interpretations
- **No events logged** → traffic never reached Connector; problem is on client side (Client app, local network, DNS blocking)
- **"DNS lookup error"** → Connector cannot resolve hostname; fix DNS config on Connector host
- **"Unable to connect"** → Connector can't route to destination; check firewall/security groups between Connector and Resource
- **Successful events + user still fails** → destination application issue (permissions, app config)
- **Successful events + web app partially loads** → missing Resource definitions for dependent domains (CDNs, auth endpoints); use browser DevTools to identify

## Configuration Values / Tools
- **Admin Console paths:** `Network > Overview` (Activity Events), `Network > Connectors` (status/clock drift), `Settings > Reports > Audit Logs`
- **Client logs:** enable detailed logging, upload via Client app
- **Connector logs:** `docker logs <container>` or `journalctl` (systemd)
- **Support ticket:** Admin Console → Help > Support

## Gotchas
- Split tunnel by default — undefined domains bypass the tunnel entirely; web apps with multiple domains require each defined as a Resource
- Resource IP ranges overlapping user's local network causes local device access failures (e.g., home printer on 192.168.1.x)
- Relayed connections indicate blocked outbound UDP ports — investigate firewall rules
- Clock drift on Connector host causes authentication/connection failures — check Connector Details in Admin Console
- `ping`/`tracert` ineffective for testing Resources from outside — no open inbound ports by design

## Related Docs
- How Twingate Works (architecture overview)
- Identity Providers troubleshooting
- Device or Client Failures
- DNS Resolution Problems
- Connector Issues
- Firewall Issues
- Split Tunneling Issues
- Engaging Technical Support
- Self-Serve Troubleshooting Guide