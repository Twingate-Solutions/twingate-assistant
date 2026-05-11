# How Twingate Forwards DNS

## Summary
Twingate Client resolves DNS `A` records locally using CGNAT IPs (`100.64.0.0/10`) and routes traffic through its local network interface. Non-`A` record types (TXT, MX, etc.) are forwarded to the Remote Network via the Connector using the private DNS server. Port restrictions on Resources can block DNS forwarding.

## Key Information
- Client resolves `A` records locally → assigns CGNAT IP → routes via Twingate interface to Connector
- CGNAT range used: `100.64.0.0/10`; routing range: `100.96.0.0/12`
- Non-`A` queries (TXT, MX, etc.) forwarded to Remote Network, resolved by Connector via private DNS
- DNS traffic travels over port `53/UDP` and is treated as standard UDP traffic — no special-casing
- If a Resource blocks port `53/UDP`, non-`A` queries return empty responses (status NOERROR, 0 answers)

## Prerequisites
For explicit DNS forwarding support:
- Connector: `>= 1.46.0`
- macOS Client: `>= 1.0.26`
- Linux Client: `>= 1.0.74`
- iOS Client: `>= 1.0.26`
- Android Client: `>= 1.0.23`
- Windows: not yet supported

## When DNS Forwarding Fails
- Resource has port `53/UDP` blocked in Twingate Resource configuration
- Result: non-`A` queries return empty response (NOERROR with 0 answers)
- Most applications behave normally when non-`A` requests are blocked

## Explicit DNS Forwarding Workaround
Target a private Resource configured as a DNS server directly:

```bash
dig @10.0.0.2 TXT nas.home.int
```

**Requirements:**
1. The DNS server IP (e.g., `10.0.0.2`) must be configured as a private Resource in Twingate
2. Port `53/UDP` must be **allowed** on that DNS server Resource

**Use cases:**
- `dig @dns-server A nas.home.int` → returns real IP (not CGNAT address)
- `dig @dns-server TXT nas.home.int` → returns TXT record even if target Resource blocks port 53

## Gotchas
- Port `53/UDP` restriction applies to the **queried Resource**, not the target hostname — blocking it on `nas.home.int` blocks DNS queries routed through it, but not through a separate DNS server Resource with port open
- Windows explicit DNS forwarding not yet released
- Empty response on blocked DNS returns `NOERROR` status — can be misleading to debug

## Related Docs
- [How DNS Works with Twingate](https://www.twingate.com/docs/dns)
- [Port Restrictions](https://www.twingate.com/docs/port-restrictions)