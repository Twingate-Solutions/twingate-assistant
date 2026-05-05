# How Twingate Forwards DNS

## Summary
Twingate Client resolves DNS `A` records locally using CGNAT IPs (100.64.0.0/10) and routes traffic through the local Twingate interface. Non-`A` record types (e.g., `TXT`, `MX`) are forwarded to the Remote Network via the Connector using the private DNS server. DNS forwarding can be blocked by Resource port restrictions.

## Key Information
- Client resolves `A` records locally → assigns CGNAT IP → routes via Twingate interface to Connector
- Traffic routed through CGNAT subnet: `100.96.0.0/12`
- Non-`A` queries forwarded to Remote Network Connector → resolved by private DNS server
- DNS uses port `53/UDP`; Twingate treats it as standard UDP traffic (no special-casing)

## When DNS Forwarding Fails
- If a Resource has port `53/UDP` blocked, non-`A` queries return **empty responses** (status: NOERROR, ANSWER: 0)
- This is a side effect of port restriction enforcement — not a DNS-specific behavior
- Most applications function normally when non-`A` DNS requests are blocked

## Explicit DNS Forwarding (Workaround)

### Prerequisites
| Component | Minimum Version |
|-----------|----------------|
| Connector | 1.46.0+ |
| macOS Client | 1.0.26+ |
| Linux Client | 1.0.74+ |
| iOS Client | 1.0.26+ |
| Android Client | 1.0.23+ |
| Windows Client | Not yet released |

### How It Works
Point DNS queries directly at a **private Resource** configured as a DNS server. Twingate will not intercept traffic explicitly targeting a private Resource acting as DNS resolver.

**Example:**
```bash
dig @10.0.0.2 TXT nas.home.int
```
- `10.0.0.2` must be both a **private Resource** and a **DNS server**
- Port `53/UDP` must be **allowed** on the DNS server Resource (not on the queried Resource)

## Use Cases for Explicit DNS Forwarding
- `dig @dns-server A nas.home.int` → returns real IP, not CGNAT address
- `dig @dns-server TXT nas.home.int` → returns TXT record even if `nas.home.int` blocks port 53/UDP

## Gotchas
- Port `53/UDP` restriction is evaluated on the **targeted Resource**, not the queried hostname — so blocking it on a Resource prevents all non-`A` DNS resolution through that Resource
- Explicit forwarding bypasses CGNAT resolution for `A` records (returns real IP)
- Windows explicit DNS forwarding not yet supported

## Related Docs
- [How DNS works with Twingate](#)
- [Port restrictions](#)