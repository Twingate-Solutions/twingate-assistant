---
source: https://www.twingate.com/docs/how-to-troubleshoot
type: docs
fetched: 2026-08-14
source_version: e4bb2e7eb42819a4ae28bce2e9cb5d8f9cbe6f3c3624b1419ce95cf40557fafe
---

# Twingate Troubleshooting Guide

## Page Title
How to Troubleshoot User Issues with the Twingate Service

## Summary
Structured methodology for diagnosing Twingate ZTNA connection failures by tracing the logical connection path across five stages: authentication, device/client, DNS resolution, routing/connection, and connector-to-resource. Troubleshooting requires interrogating components rather than probing perimeters since infrastructure is intentionally invisible. Issues stem from either control plane (policy) or data plane (network connectivity) failures.

## Key Information
- **Connection path stages**: Identity/Auth → Device/Client ACL → DNS Resolution → Routing/P2P tunnel → Connector-to-Resource forwarding
- **Control plane vs data plane**: Controller decides *if* access is allowed; Client/Connector/Relays handle *how* connection is made
- **Relay fallback**: Direct P2P preferred via NAT traversal; Relays serve as backup if P2P fails
- **Connectors**: Outbound-only connections—no inbound firewall ports required
- **Resource Activity Events**: Primary diagnostic tool located at `Network > Overview`

## Prerequisites
- Access to Twingate Admin Console
- Access to Identity Provider admin console (Okta, Entra ID, Google Workspace)
- Ability to retrieve Client and/or Connector logs

## Step-by-Step Troubleshooting Methodology

1. **Define scope**: One user vs. all users? One resource vs. all resources? One location vs. all?
2. **Check Twingate status page** for ongoing incidents
3. **Verify identity/device posture**: Group membership in Admin Console + IdP sync; Trusted Device policy status
4. **Trace connection attempt** via Resource Activity Report (`Network > Resources > [Resource] > Activity`)

## Diagnostic Quick Reference

| Symptom | Tool | First Check |
|---|---|---|
| Can't log in | IdP Console | User active + assigned to Twingate app? |
| App won't connect | Client Logs / OS Services | Twingate service/daemon running? |
| Can't reach internal hostname | `nslookup`/`dig` + Activity | DNS error at connector or client? |
| No one can access resource | Admin Console Connector Status | Connectors online? Clock in sync? |
| Slow performance | Admin Console Connector Details | P2P or Relayed connection? UDP ports open? |
| Local printer broken | `ipconfig`/`ifconfig` | Resource CIDR overlapping local network? |
| SaaS app partially loads | Browser DevTools Network tab | All dependent domains defined as Resources? |

## Activity Event Interpretations
- **No events logged**: Traffic never reached Connector—problem is Client-side (DNS blocker, local network)
- **"DNS lookup error"**: Connector cannot resolve hostname—check Connector host DNS config
- **"Unable to connect"**: Connector can't route to destination—check firewall/security group between Connector and Resource
- **Successful events + user still fails**: Application-layer issue (permissions, app config)
- **Successful events + web app partially loads**: Missing Resource definitions for dependent domains (CDNs, auth endpoints)

## Configuration Values / Log Access
- **Connector logs (Docker)**: `docker logs <container>`
- **Connector logs (systemd)**: `journalctl -u twingate-connector`
- **Admin Console paths**: `Network > Overview` (Activity), `Network > Connectors` (status/clock drift), `Settings > Reports > Audit Logs`
- **Support tickets**: Admin Console `Help > Support`

## Gotchas
- `ping`/`tracert` from external networks won't work—no open inbound ports by design
- Split tunnel architecture means undefined domains bypass the tunnel; web apps depending on external CDNs/subdomains must have those added as Resources
- Resource CIDR ranges overlapping user's local subnet cause local device access failures (printers, NAS, etc.)
- Clock drift on Connector host causes authentication failures—check in Connector Details

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