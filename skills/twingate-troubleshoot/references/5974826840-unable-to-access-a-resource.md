---
source: https://help.twingate.com/articles/5974826840-unable-to-access-a-resource
type: help
fetched: 2026-09-13
source_version: 94faaf352ed7ee6b0f6cb5c44371ada1a03259282a1c2bddc9d164bbff8a1cc6
---

# Unable to Access a Twingate Resource

## Summary
Troubleshooting guide for when users cannot access a Twingate Resource. Covers the most common causes from authorization issues to DNS configuration, incompatible software, and network connectivity problems.

## Key Information

- Issues are ordered most-to-least common
- Problems occur at two levels: **Client level** or **Connector level**
- Network Traffic in Admin Console helps identify which level the failure occurs

## Troubleshooting Steps (In Order)

1. **Authorization check** — Confirm user's Group includes the Resource. If Resource doesn't appear in the Client tray menu, it won't be reachable.

2. **DNS interception** — Run `nslookup` or `dig` against the Resource name. Should return a **CGNAT IP** (not the real IP). If it returns the real IP, Twingate isn't intercepting DNS.

3. **Local hosts file override** — Remove any Resource entries from:
   - Windows: `c:\windows\system32\drivers\etc\hosts`
   - macOS/Linux: `/etc/hosts`

4. **Incompatible software** — Check endpoint security, DNS software, VPN, or VPN-like tools against the Known Incompatibilities list.

5. **Outbound access blocked** — Ensure device can reach:
   - `*.twingate.com`
   - Full Google Cloud Provider external IP range (updated periodically by Google)

6. **Check Network Traffic in Admin Console** — If no flows appear → Client-level issue. If flows appear → investigate Connector-to-Resource connectivity.

7. **Verify destination availability** — Test from the Connector (not the Client):
   ```bash
   curl -v telnet://<host>:<port>
   ```
   > ⚠️ Port tests from the Client side return false positives

8. **DNS Resource resolution from Connector** — Run `dig` or `nslookup` from the Connector to confirm correct IP resolution. DNS Resources resolve first at the Client (ACL match), then request lookup from the Connector.

9. **Geo-blocking** — GCP blocks some regions. Browser access to `.twingate.com` may work while Controller/Relay services are still blocked. See Unsupported Regions docs.

10. **DNS Rebind Protection** — Private IP/CIDR Resources resolved via public DNS may be blocked by consumer routers/ISPs. Symptom: empty `dig`/`nslookup` response.

## Gotchas

- **False positives**: TCP/IP port tests or scans from the Client side are unreliable — always test from the Connector
- **GCP IP list changes**: Google updates the GCP external IP list periodically; firewall rules may become stale
- **DNS Resources**: Failure can occur at either the Client lookup stage or the Connector resolution stage — test both

## Prerequisites for Support Request
- Technical Support Entitlement required
- Collect detailed client logs
- Document: timestamps, Resource name/IP, steps already attempted

## Related Docs
- How DNS Works with Twingate
- Known Incompatibilities
- Network Traffic in Admin Console
- Address Resolution of Resources
- Unsupported Regions
- TCP/IP port tests or scans produce inaccurate results
- Detailed client logs collection