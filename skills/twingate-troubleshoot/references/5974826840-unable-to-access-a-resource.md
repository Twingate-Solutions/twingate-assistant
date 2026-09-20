---
source: https://help.twingate.com/articles/5974826840-unable-to-access-a-resource
type: help
fetched: 2026-09-20
source_version: db5adfda44986a7e7b117fe36742e18a8fbcd233ecb67a367c06b1c1c2599c09
---

# Unable to Access a Resource

## Summary
Troubleshooting guide for when a Twingate Client cannot access an expected Resource. Covers authorization, DNS, software conflicts, network access, and connectivity verification in order of most-to-least common causes.

## Key Information
- Issues are ordered by frequency: permissions → DNS → software conflicts → firewall → network flows → destination availability → geo-blocking → DNS rebind
- Port tests from the **Client side** to a Twingate Resource return false positives; test from the Connector instead
- DNS Resources resolve first at the Client (ACL check), then request DNS lookup from the Connector

## Troubleshooting Steps

1. **Check authorization** — Confirm user's Group includes the Resource; if Resource doesn't appear in tray menu, it's not accessible
2. **Verify DNS interception** — Run `nslookup` or `dig` on the Resource; should return a CGNAT IP (not real IP); if not, DNS is not being intercepted
3. **Check local hosts file** — Remove conflicting entries
   - Windows: `C:\Windows\System32\drivers\etc\hosts`
   - macOS/Linux: `/etc/hosts`
4. **Check for incompatible software** — Endpoint security, DNS tools, VPNs may conflict (see Known Incompatibilities doc)
5. **Verify outbound internet access** — Allow `*.twingate.com` and all Google Cloud Provider external IPs
6. **Review Network Traffic in Admin Console** — If no flows reach the Connector, issue is at Client level; if flows exist, investigate Connector-to-Resource access
7. **Test destination availability** — SSH to Connector and run:
   ```bash
   curl -v telnet://<host>:<port>
   ```
8. **DNS Resource: verify resolution from Connector** — Run `dig` or `nslookup` from the Connector to confirm correct IP resolves
9. **Check geo-blocking** — GCP blocks some regions; `*.twingate.com` may load but Controller/Relay services may still be blocked
10. **Check DNS rebind protection** — Consumer routers/ISPs may block private IP lookups via public DNS; `dig`/`nslookup` returns empty response

## Configuration Values
- Required outbound access: `*.twingate.com` + full Google Cloud Provider external IP range

## Gotchas
- Resource not appearing in tray menu = not accessible, regardless of other config
- TCP/IP port tests from Client side produce false positives — always test from Connector
- DNS Resources: Connector must resolve the correct IP or connection fails silently
- GCP geo-blocks may allow browser access to `twingate.com` but block Controller/Relay services

## Prerequisites for Support Escalation
- Active Technical Support Entitlement
- Collect detailed Client logs
- Document: timestamps, Resource name/IP, steps already attempted

## Related Docs
- How DNS Works with Twingate
- Known Incompatibilities
- Network Traffic in Admin Console
- Address Resolution of Resources
- Unsupported Regions
- TCP/IP port tests or scans produce inaccurate results
- Detailed Client Logs collection guide