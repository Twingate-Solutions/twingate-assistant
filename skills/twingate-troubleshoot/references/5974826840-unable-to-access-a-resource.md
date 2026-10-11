---
source: https://help.twingate.com/articles/5974826840-unable-to-access-a-resource
type: help
fetched: 2026-10-11
source_version: 74184f09f8862e1903f9f7c1de23d7d7614dc809e5d1c80642fc76d7edcbfbe0
trust: official
---

# Unable to Access a Twingate Resource

## Page Title
Unable to access a Resource

## Summary
Troubleshooting guide for when a Twingate Client cannot access an expected Resource. Covers authorization, DNS, software conflicts, network connectivity, and Connector-side issues in order of most-to-least common.

## Key Information (Ordered by Frequency)

1. **Authorization** – User must belong to a Group that includes the Resource; if the Resource doesn't appear in the tray menu, access will not work
2. **DNS interception** – `nslookup`/`dig` against the Resource should return a CGNAT IP; if it returns the real IP, Twingate is not intercepting DNS
3. **Local hosts file override** – Remove conflicting entries:
   - Windows: `C:\windows\system32\drivers\etc\hosts`
   - macOS/Linux: `/etc/hosts`
4. **Incompatible software** – Endpoint security, DNS tools, VPNs, or VPN-like software may block access (see Known Incompatibilities)
5. **Outbound Internet access** – Devices must be able to reach `*.twingate.com` and all Google Cloud Platform external IPs
6. **Network Traffic in Admin Console** – Check if flows reach the Connector; no flow = Client-side issue; flow present = investigate Connector-side
7. **Destination availability** – Verify the target service is running; test from Connector (not Client):
   ```
   curl -v telnet://<host>:<port>
   ```
8. **DNS Resource resolution from Connector** – Run `dig`/`nslookup` from the Connector to confirm correct IP resolution
9. **Geo-blocking** – Google Cloud Platform blocks some regions; check Unsupported Regions docs
10. **DNS Rebind Protection** – Consumer routers/ISPs may block private IP DNS lookups; `dig`/`nslookup` returns empty response

## Prerequisites
- Twingate Client installed and signed in
- Remote Network status is green (Connector reachable)
- SSH access to Connector for port/DNS tests (systemd or AWS AMI deployments)

## Configuration Values

| Item | Value |
|------|-------|
| Allowed outbound domain | `*.twingate.com` |
| Also required | Full GCP external IP range (updated by Google) |
| Expected DNS response for Resource | CGNAT IP (not the real IP) |

## Gotchas
- **Port tests from the Client side produce false positives** – always test connectivity from the Connector, not the Client
- DNS Resources resolve first at the Client (ACL match), then a second lookup is made from the Connector — both must succeed
- GCP geo-blocking may allow `*.twingate.com` in a browser but still block Controller or Relay services

## Related Docs
- How DNS Works with Twingate
- Known Incompatibilities
- Network Traffic in Admin Console
- Address Resolution of Resources
- Unsupported Regions
- TCP/IP port tests or scans produce inaccurate results
- Detailed client logs (for support escalation)
- Technical Support Entitlement