---
source: https://www.twingate.com/docs/how-twingate-forwards-dns
type: docs
fetched: 2026-08-14
source_version: 96032b36e4c58aeec541d3adf55b9f3105784f9c9961bbe9f91582001c134382
---

# How Twingate Forwards DNS

## Summary
Twingate Client resolves DNS `A` records locally using CGNAT IPs (`100.64.0.0/10`) and routes traffic through the Twingate network interface. Non-`A` record types (e.g., `TXT`, `MX`) are forwarded to the Remote Network via the Connector using the private DNS server. DNS forwarding fails silently when port 53/UDP is blocked on a Resource.

## Key Information
- Client resolves `A` records locally → assigns CGNAT IP from `100.64.0.0/10`
- Traffic routing uses `100.96/12` subnet via local Twingate network interface
- Non-`A` queries forwarded to Connector → answered by network's private DNS server
- DNS traffic treated as standard UDP traffic to port 53 — no special-casing
- Queries for non-`A` records return **empty response** (not an error) when port 53/UDP is blocked on the Resource
- Explicit DNS forwarding: query directly against a private Resource acting as DNS server bypasses Client interference

## Prerequisites
For explicit DNS forwarding support:
- Connector: v1.46.0+
- macOS Client: v1.0.26+
- Windows Client: not yet released
- Linux Client: v1.0.74+
- iOS Client: v1.0.26+
- Android Client: v1.0.23+

## Configuration Values
| Parameter | Value |
|-----------|-------|
| CGNAT range (DNS resolution) | `100.64.0.0/10` |
| Routing range | `100.96/12` |
| DNS port | `53/UDP` |

## Step-by-Step: Explicit DNS Forwarding
1. Add private DNS server IP (e.g., `10.0.0.2`) as a Twingate Resource
2. Ensure port `53/UDP` is **allowed** in that Resource's port restrictions
3. Query using `@<dns-resource-ip>` syntax:
   ```
   dig @10.0.0.2 TXT nas.home.int
   ```
4. Client routes traffic to Remote Network; Connector forwards to specified DNS server

## Gotchas
- **Blocked port 53/UDP on a Resource** → non-`A` queries for that Resource return empty `ANSWER` section with `status: NOERROR` — silent failure, not an error code
- **Port restriction applies per Resource**: blocking 53/UDP on the target resource doesn't matter if you query an explicitly specified DNS server Resource that has 53/UDP open
- **Explicit `@dns-server` queries return real IPs**, not CGNAT addresses — useful when you need the actual private IP
- Windows explicit DNS forwarding not yet supported

## Related Docs
- [How DNS works with Twingate](https://www.twingate.com/docs/how-does-dns-work-with-twingate)
- [Port restrictions](https://www.twingate.com/docs/port-restrictions)