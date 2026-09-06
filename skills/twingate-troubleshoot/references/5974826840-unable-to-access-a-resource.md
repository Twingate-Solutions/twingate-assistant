---
source: https://help.twingate.com/articles/5974826840-unable-to-access-a-resource
type: help
fetched: 2026-09-06
source_version: 980794a167350fe1febdd153ed684cd15778e80dca87e9abcb0b07aa0085c43b
---

# Unable to Access a Twingate Resource

## Summary
Troubleshooting guide for users who cannot access a Twingate Resource. Covers common causes from authorization issues to DNS misconfiguration, incompatible software, and network blocking. Steps are ordered by frequency of occurrence.

## Key Information
- Resource must appear in the Client tray menu (Windows/macOS) to be reachable
- DNS resources should return a CGNAT IP (not the real IP) when queried via `nslookup`/`dig`
- Port tests from the Client side to a Twingate Resource produce false positives — test from the Connector instead
- DNS Resources resolve first at the Client (ACL check), then request DNS lookup from the Connector

## Troubleshooting Steps (Most → Least Common)

1. **Authorization** — Confirm user belongs to a Group that includes the Resource; if Resource doesn't appear in tray menu, access will fail
2. **Client DNS interception** — Run `nslookup`/`dig` on the resource; must return a CGNAT IP; if not, something upstream is resolving it before Twingate
3. **Local hosts file override** — Remove conflicting entries:
   - Windows: `C:\Windows\System32\drivers\etc\hosts`
   - macOS/Linux: `/etc/hosts`
4. **Incompatible software** — Endpoint security, DNS software, VPNs can interfere; check [Known Incompatibilities](https://help.twingate.com)
5. **Outbound firewall blocking** — Ensure outbound access to `*.twingate.com` and all Google Cloud Provider external IPs
6. **Check Network Traffic in Admin Console** — If no flows reach the Connector, issue is Client-side; if flows exist, investigate Connector→Resource path
7. **Destination availability** — Verify the service is running; test from Connector:
   ```bash
   curl -v telnet://<host>:<port>
   ```
8. **DNS Resource resolution from Connector** — Run `dig`/`nslookup` from the Connector to confirm it resolves the correct real IP
9. **Geo-blocking** — GCP blocks certain regions/countries; access to `*.twingate.com` in browser may work but Controller/Relay services may still be blocked; see [Unsupported Regions](https://help.twingate.com)
10. **DNS Rebind Protection** — Consumer routers/ISPs may block DNS lookups returning private IPs; `dig`/`nslookup` will return empty response

## Configuration Values
| Item | Value |
|------|-------|
| Required outbound domain | `*.twingate.com` |
| Required IPs | Full GCP external IP range (Google-maintained list) |

## Gotchas
- TCP/IP port tests from the **Client side** return false positives — always test connectivity from the Connector
- DNS Resources have a two-step resolution: Client (ACL match) → Connector (actual DNS lookup); failure at either step breaks access
- GCP geo-blocking can selectively block Relay/Controller even when the Twingate website loads

## Prerequisites
- Business or Enterprise account required to open support requests
- Collect detailed client logs before contacting support

## Related Docs
- How DNS Works with Twingate
- Known Incompatibilities
- Network Traffic in Admin Console
- Address Resolution of Resources
- Unsupported Regions
- TCP/IP port tests produce inaccurate results