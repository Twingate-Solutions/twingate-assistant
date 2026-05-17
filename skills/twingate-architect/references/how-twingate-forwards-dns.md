# How Twingate Forwards DNS

## Summary
Twingate Client resolves DNS `A` records locally using CGNAT IPs (`100.64.0.0/10`) and routes traffic through its network interface. Non-`A` record types are forwarded to the Remote Network via the Connector's private DNS server. DNS forwarding can be blocked by port restrictions on Resources.

## Key Information
- Client locally resolves `A` records → assigns CGNAT IP from `100.64.0.0/10`
- Traffic routing uses subset `100.96/12` via local Twingate network interface
- Non-`A` record types (TXT, MX, etc.) are proxied to Connector → resolved by private DNS server
- DNS uses port `53/UDP`; Twingate treats DNS traffic as regular UDP — no special-casing
- DNS server responding via CGNAT: `100.95.0.251:53`

## Prerequisites
For explicit DNS forwarding support, minimum versions required:
| Platform | Min Version |
|----------|-------------|
| Connector | 1.46.0 |
| macOS Client | 1.0.26 |
| Linux Client | 1.0.74 |
| iOS | 1.0.26 |
| Android | 1.0.23 |
| Windows | Not yet released |

## When DNS Forwarding Fails
- If a Resource has **port 53/UDP blocked**, non-`A` queries for that resource return **empty responses** (status: NOERROR, 0 answers)
- This is not a bug — Twingate applies port restrictions uniformly to all UDP traffic including DNS

## Explicit DNS Forwarding (Workaround)

**Method:** Query directly against a private Resource that is also a DNS server.

```bash
dig @10.0.0.2 TXT nas.home.int
```

**Requirements:**
- The DNS server IP (e.g., `10.0.0.2`) must be configured as a Twingate Resource
- Port `53/UDP` must be **allowed** on the DNS server Resource (not the target resource)

**Behavior when using explicit DNS server Resource:**
- `dig @dns-server A nas.home.int` → returns real IP, not CGNAT address
- `dig @dns-server TXT nas.home.int` → returns TXT record even if target Resource has port 53 blocked

## Gotchas
- Port `53/UDP` restriction on a Resource blocks **all** DNS queries for that resource's hostname, not just `A` records
- Using explicit `@dns-server` bypasses CGNAT resolution — `A` records return real IPs, not Twingate-assigned addresses
- Most applications function normally when non-`A` DNS requests are blocked

## Related Docs
- [How DNS works with Twingate](#) (prerequisite reading)
- [Port restrictions in Twingate](#)