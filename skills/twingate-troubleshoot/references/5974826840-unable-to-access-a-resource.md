---
source: https://help.twingate.com/articles/5974826840-unable-to-access-a-resource
type: help
fetched: 2026-10-04
source_version: 8a7b884f7a56fe029d59e9a052f7a83ac0b0640fedd1dbac3d687b00c285e655
trust: official
---

# Unable to Access a Twingate Resource

## Page Title
Unable to access a Resource

## Summary
Troubleshooting guide for diagnosing why a user cannot access a Twingate Resource. Covers authorization, DNS, software conflicts, network restrictions, and Connector-side issues in order of most to least common cause.

## Key Information (Ordered by Frequency)

1. **Authorization** – User must belong to a Group that has the Resource assigned. If Resource doesn't appear in the Client tray menu, access will fail.
2. **DNS interception** – Run `nslookup` or `dig` against the Resource; result should be a CGNAT IP, not the real IP. If real IP is returned, Twingate isn't intercepting DNS.
3. **Local hosts file override** – Remove conflicting entries:
   - Windows: `C:\Windows\System32\drivers\etc\hosts`
   - macOS/Linux: `/etc/hosts`
4. **Third-party software conflicts** – Endpoint security, VPN, or DNS software may interfere. See Known Incompatibilities docs.
5. **Outbound firewall blocking** – Allow outbound access to `*.twingate.com` and all Google Cloud Provider external IPs (list maintained by Google).
6. **Network Traffic in Admin Console** – Check if flows reach the Connector. No flow = Client-side issue; flow present = investigate Connector-to-Resource path.
7. **Destination service unavailable** – SSH to Connector and test port: `curl -v telnet://<host>:<port>`
8. **DNS Resources** – Connector must resolve the DNS Resource to the correct IP. Run `dig`/`nslookup` from the Connector directly.
9. **Geo-blocking** – Google Cloud Platform blocks some regions; affects Twingate Controller/Relay even if `*.twingate.com` loads in browser. See Unsupported Regions.
10. **DNS Rebind Protection** – Consumer routers/ISPs may block DNS lookups returning private IPs. `dig`/`nslookup` returns empty response.

## Configuration Values

| Item | Value |
|------|-------|
| Allowed domain | `*.twingate.com` |
| Required IP ranges | Full GCP external IP list (Google-maintained) |
| Expected DNS result | CGNAT IP (not real Resource IP) |

## Gotchas

- Port tests from the **Client side** to a Twingate Resource return **false positives** — always test from the Connector.
- DNS Resources are first matched client-side against ACL, then resolved via the Connector — both sides must work.
- GCP geo-blocks may allow browser access to `*.twingate.com` but still block Relay/Controller traffic.
- DNS rebind protection produces empty DNS responses (not NXDOMAIN), which can be mistaken for a Twingate issue.

## Prerequisites

- Admin Console access (to check Groups, Resources, Network Traffic)
- SSH access to Connector host (for port/DNS testing)
- Technical Support Entitlement (for opening support requests)

## Related Docs

- How DNS Works with Twingate
- Known Incompatibilities
- Network Traffic in the Admin Console
- TCP/IP port tests or scans produce inaccurate results
- Address Resolution of Resources
- Unsupported Regions
- Detailed client logs (collection guide)