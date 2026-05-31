# How Twingate Forwards DNS

## Summary
Twingate Client resolves DNS `A` records locally using CGNAT IPs (`100.64.0.0/10`) and routes traffic through its local network interface. Non-`A` record types (e.g., `TXT`, `MX`) are forwarded to the Remote Network via the Connector using the private DNS server. DNS forwarding is blocked when port 53/UDP is restricted on a Resource.

## Key Information
- Client resolves `A` records locally → assigns CGNAT IP → routes via Twingate interface → proxied to Connector
- Routing range used: `100.96/12` (subset of `100.64.0.0/10`)
- Non-`A` queries forwarded to Remote Network's private DNS server via Connector
- DNS traffic is treated as standard UDP traffic on port 53 — no special-casing
- DNS server used for forwarded queries appears as `100.95.0.251` (CGNAT address)

## Prerequisites
For explicit DNS forwarding support:
| Platform | Min Version |
|----------|-------------|
| Connector | 1.46.0+ |
| macOS Client | 1.0.26+ |
| Linux Client | 1.0.74+ |
| iOS | 1.0.26+ |
| Android | 1.0.23+ |
| Windows | Not yet released |

## When DNS Forwarding Fails
- If a Resource has **port 53/UDP blocked**, non-`A` queries return an **empty response** (status: NOERROR, 0 answers)
- This is expected behavior — Twingate applies Resource port restrictions to DNS traffic targeting that Resource
- Most applications behave normally when non-`A` requests are blocked

## Explicit DNS Forwarding Workaround

**Approach:** Direct DNS queries to a private Resource that acts as a DNS server (with port 53/UDP allowed).

```bash
# Returns real IP (not CGNAT) for nas.home.int
dig @10.0.0.2 A nas.home.int

# Returns TXT record even if nas.home.int has port 53/UDP blocked
dig @10.0.0.2 TXT nas.home.int
```

**Requirements:**
1. DNS server IP (e.g., `10.0.0.2`) must be configured as a **Twingate Resource**
2. Port 53/UDP must be **allowed** on the DNS server Resource
3. Port 53/UDP on the target Resource does **not** need to be open (the resolver's policy applies)

## Gotchas
- Querying `dig @dns-server A nas.home.int` returns the **real** private IP, not the CGNAT address assigned by Twingate
- Port restrictions on the **DNS server Resource** govern DNS forwarding, not the target Resource's port config
- Windows explicit DNS forwarding is **not yet available**
- Twingate intentionally avoids special-casing DNS — behavior is a direct consequence of port restriction architecture

## Related Docs
- [How DNS works with Twingate](https://www.twingate.com/docs/dns)
- [Port restrictions](https://www.twingate.com/docs/port-restrictions)