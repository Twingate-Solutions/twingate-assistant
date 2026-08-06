---
source: https://help.twingate.com/articles/5974826840-unable-to-access-a-resource
type: help
fetched: 2026-08-06
source_version: 9327f44144c03e86504cf29dc61da284cf527bed395e5aa6d27b80cea527eb0b
---

# Unable to Access a Twingate Resource

## Summary
Troubleshooting guide for when users cannot access expected Twingate Resources. Covers issues from authorization and DNS configuration to network-level blocking and destination availability.

## Key Information
- Issues ordered most-to-least common
- Problems can occur at Client level, Connector level, or network level
- Network Traffic view in Admin Console helps isolate whether issue is Client-side or Connector-side

## Troubleshooting Steps (Priority Order)

### 1. Authorization
- Confirm user belongs to a Group that includes the Resource
- If Resource doesn't appear in Client tray menu (Windows/macOS), it won't be reachable
- Green Remote Network status does NOT guarantee access

### 2. DNS Interception
- Run `nslookup` or `dig` on the Resource — should return a **CGNAT IP**, not real IP
- If real IP returned, Twingate is not intercepting DNS
- Check `/etc/hosts` (macOS/Linux) or `c:\windows\system32\drivers\etc\hosts` (Windows) for conflicting entries — remove any Resource entries

### 3. Incompatible Third-Party Software
- Endpoint security, DNS tools, VPNs, or VPN-like software can block access
- Reference: Known Incompatibilities documentation

### 4. Outbound Internet Access
- Client must reach `*.twingate.com` and full Google Cloud Provider external IP range
- GCP IP list is updated periodically by Google

### 5. Check Network Traffic in Admin Console
- If no flows appear → issue is at Client level
- If flows appear → inspect Connector-to-Resource connectivity

### 6. Verify Destination Availability
- Test from Connector using: `curl -v telnet://<host>:<port>`
- **Do NOT test port connectivity from Client side** — produces false positives

### 7. DNS Resources (Additional Check)
- DNS lookup first resolves on Client (if matches ACL), then requests resolution from Connector
- Run `dig` or `nslookup` from Connector to verify correct IP is returned

### 8. Geo-Blocking
- GCP blocks certain regions/countries — affects Twingate Controller/Relay even if `.twingate.com` loads in browser
- Reference: Unsupported Regions documentation

### 9. DNS Rebind Protection
- Consumer routers/ISPs may block DNS lookups for private IPs via public DNS
- Symptom: `dig`/`nslookup` returns empty response

## Configuration Values
| Item | Value |
|------|-------|
| Allowed domain | `*.twingate.com` |
| Allowed IPs | Full GCP external IP range (Google-maintained) |
| Windows hosts file | `c:\windows\system32\drivers\etc\hosts` |
| macOS/Linux hosts file | `/etc/hosts` |
| Expected DNS response | CGNAT IP (not real IP) |
| Connector port test command | `curl -v telnet://<host>:<port>` |

## Gotchas
- Resource not visible in Client tray = not accessible, regardless of network status
- Port scans/tests from Client return false positives — always test from Connector
- GCP geo-blocks may allow website access but block service endpoints
- DNS rebind protection silently drops lookups for private IPs

## Related Docs
- How DNS Works with Twingate
- Known Incompatibilities
- Network Traffic in Admin Console
- TCP/IP port tests produce inaccurate results
- Address Resolution of Resources
- Unsupported Regions
- Detailed client logs collection