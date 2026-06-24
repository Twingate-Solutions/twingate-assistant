# Twingate Troubleshooting Guide

## Page Title
How to Troubleshoot User Issues with the Twingate Service

## Summary
Structured methodology for diagnosing Twingate ZTNA connection failures by tracing the connection chain across five stages: authentication, device/client, DNS, routing/tunnel establishment, and connector-to-resource. Troubleshooting distinguishes between control plane (policy/identity) and data plane (network/connectivity) failures. Traditional tools like `ping`/`tracert` are ineffective externally due to ZTNA's invisible infrastructure design.

## Key Information
- **Architecture components**: Client (end-user device), Connectors (private network, outbound-only), Relays (NAT traversal/P2P fallback), Controller (control plane)
- **Control plane vs. data plane**: Controller decides *if* access is granted; Client/Connector/Relays handle *how* connection is made
- **Connection chain**: Identity Auth → Client/ACL → DNS Resolution → Tunnel Establishment → Connector-to-Resource
- Connectors make **outbound-only** connections; no inbound firewall ports needed
- Failed connections may be policy violations, not network failures

## Prerequisites
- Access to Twingate Admin Console
- Access to Identity Provider admin console
- Ability to retrieve Client logs and Connector logs from affected hosts

## Step-by-Step Troubleshooting Methodology

1. **Define scope**: One vs. all users? One vs. all resources? One vs. all locations? When did it start?
2. **Check known states**: Verify [Twingate status page](https://www.twingatestatus.com) for active incidents; review recent config changes
3. **Verify identity/device posture**: Confirm user group membership in Admin Console and IdP; check device trust status against applied Security Policy
4. **Trace connection attempt**: Check Resource Activity Report (`Network > Resources > [Resource] > Activity`)

## Configuration Values / Admin Console Paths
- Resource activity events: `Network > Overview`
- Connector status/details: `Network > Connectors`
- Audit logs: `Settings > Reports > Audit Logs`
- Support ticket: `Help > Support`
- Connector logs (Docker): `docker logs <container>`
- Connector logs (systemd): `journalctl -u twingate-connector`

## Diagnostic Quick Reference

| Symptom | Likely Cause | First Tool |
|---|---|---|
| Can't log in | IdP/Authentication | IdP admin console |
| App won't connect | Client/daemon not running | `services.msc`, `launchctl`, Client logs |
| Connected, can't reach resource | DNS resolution | `nslookup`/`dig` + Admin Console Activity |
| No one can reach resource | Connector down | Admin Console Connector status |
| Slow performance | Relayed instead of P2P; UDP blocked | Admin Console Connector details |
| Local printer broken | IP/subnet conflict with Resource definition | `ipconfig`/`ifconfig` |
| SaaS app partially loads | Missing Resource definitions for dependent domains | Browser DevTools Network tab |

## Activity Report Interpretation
- **No events logged**: Traffic never reached Connector — check Client, local network, or DNS filtering on device
- **"DNS lookup error"**: Connector cannot resolve hostname — check DNS config on Connector host
- **"Unable to connect"**: Connector can't route to destination — check firewall, security groups, app-level blocking
- **Successful events + user still fails**: Application-layer issue (permissions, app config)
- **Successful events + web app partially loads**: Missing dependent domains (CDNs, APIs) not defined as Resources

## Gotchas
- `ping`/`tracert` from external network won't work — no open inbound ports by design
- Split tunnel is default; undefined domains bypass the tunnel entirely and may be blocked by destination services
- Resource CIDR definitions overlapping with user's local subnet cause local resource access failures (e.g., home printer)
- P2P connection requires outbound UDP; if blocked, traffic falls back to Relay (higher latency)
- Clock drift on Connector host can cause connection failures — check Connector Details in Admin Console

## Related Docs
- How Twingate Works (architecture overview)
- Identity Providers configuration
- Device/Client Failures
- DNS Resolution Problems
- Connector Issues
-