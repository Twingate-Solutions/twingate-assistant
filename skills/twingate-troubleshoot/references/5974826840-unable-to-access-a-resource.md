---
source: https://help.twingate.com/articles/5974826840-unable-to-access-a-resource
type: help
fetched: 2026-09-27
source_version: 84851bc8b01426f0bd19e88bdf8e4fb00898309731b30a7e972cb53dd6e064a0
---

# Unable to Access a Resource

## Page Title
Unable to Access a Resource

## Summary
Troubleshooting guide for cases where a Twingate Client cannot reach an expected Resource. Covers authorization, DNS, software conflicts, network access, and connector-level diagnostics in order of most-to-least common cause.

## Key Information
- Resource must appear in the Client tray menu (Windows/macOS); if not visible, it's unreachable regardless of other config
- DNS lookups for Resources should return a CGNAT IP, not the real IP — if returning real IP, Twingate is not intercepting DNS
- DNS Resources resolve first at the Client (ACL match), then request lookup from Connector — both hops must succeed
- Port tests from the Client side to a Twingate Resource return false positives; test from the Connector instead

## Troubleshooting Steps (in order)

1. **Authorization**: Confirm user is in a Group that contains the Resource. Check Admin Console group/resource assignments.

2. **DNS interception**: Run `nslookup` or `dig` on the Resource — expect a CGNAT IP in response. If real IP returned, DNS is being resolved before reaching Twingate.

3. **Hosts file override**: Remove conflicting entries.
   - Windows: `c:\windows\system32\drivers\etc\hosts`
   - macOS/Linux: `/etc/hosts`

4. **Third-party software**: Check for incompatible endpoint security, DNS, VPN, or VPN-like software. See [Known Incompatibilities].

5. **Outbound internet access**: Ensure device can reach:
   - `*.twingate.com`
   - Full Google Cloud Provider external IP range (list updated periodically by Google)

6. **Admin Console — Network Traffic**: Check for flows reaching the Connector.
   - No flow → Client-level issue
   - Flow present → investigate Connector-to-Resource connectivity

7. **Destination availability**: SSH to Connector and test:
   ```bash
   curl -v telnet://<host>:<port>
   ```

8. **DNS Resource resolution from Connector**: Run `dig` or `nslookup` from the Connector to verify correct IP is returned.

9. **Geo-blocking**: GCP blocks some regions/countries. Access to `*.twingate.com` in browser may succeed while Relay/Controller services are blocked. See [Unsupported Regions].

10. **DNS Rebind Protection**: Consumer routers/ISPs may block DNS responses returning private IPs. Symptom: empty `dig`/`nslookup` response. See [Address Resolution of Resources].

## Gotchas
- False positives on TCP/IP port tests run from the Client side — always test from the Connector
- GCP IP list is updated periodically; firewall rules may become stale
- DNS Resources have a two-stage resolution (Client → Connector); failure at either stage breaks access
- Geo-blocking may be partial — browser access works but other Twingate services are blocked

## Prerequisites
- Admin Console access for group/resource and network traffic verification
- SSH access to Connector for port/DNS testing
- Technical Support Entitlement required to open a support request

## Related Docs
- How DNS Works with Twingate
- Known Incompatibilities
- Network Traffic in the Admin Console
- TCP/IP port tests or scans produce inaccurate results
- Unsupported Regions
- Address Resolution of Resources
- Detailed Client Logs (for support escalation)