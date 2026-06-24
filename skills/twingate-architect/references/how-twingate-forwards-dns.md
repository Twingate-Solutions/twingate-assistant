# How Twingate Forwards DNS

## Summary
Twingate Client resolves DNS `A` records locally using CGNAT IPs (`100.64.0.0/10`) and routes traffic through its local network interface. Non-`A` record types (TXT, MX, etc.) are forwarded to the Remote Network via the Connector using the private DNS server. DNS forwarding can be blocked by Resource port restrictions on 53/UDP.

## Key Information
- Client resolves `A` records locally → assigns CGNAT IP from `100.64.0.0/10`
- Traffic routed through Twingate interface from `100.96.0.0/12`
- Non-`A` queries (TXT, MX, etc.) forwarded to Connector → resolved by private DNS server
- DNS traffic treated as standard UDP traffic on port 53/UDP — no special-casing
- Querying DNS server explicitly via private Resource IP bypasses CGNAT resolution (returns real IP, not CGNAT)

## Prerequisites for Explicit DNS Forwarding
| Component | Minimum Version |
|-----------|----------------|
| Connector | 1.46.0+ |
| macOS Client | 1.0.26+ |
| Linux Client | 1.0.74+ |
| iOS Client | 1.0.26+ |
| Android Client | 1.0.23+ |
| Windows Client | Not yet released |

## When DNS Forwarding Fails
- Resource has port **53/UDP blocked** → non-`A` queries return empty response (`ANSWER: 0`)
- This is expected behavior; Twingate applies Resource port restrictions to DNS traffic like any other UDP traffic

## Explicit DNS Forwarding (Workaround)

**Method:** Query a private Resource configured as a DNS server directly using `@<ip>` syntax.

```bash
dig @10.0.0.2 TXT nas.home.int
```

**Requirements:**
- The DNS server IP (`10.0.0.2`) must be a configured Twingate Resource
- Port 53/UDP must be **allowed** on the DNS server Resource (not necessarily on the target Resource)

**Use cases:**
- `dig @dns-server A nas.home.int` → returns real IP (not CGNAT)
- `dig @dns-server TXT nas.home.int` → returns TXT record even if target Resource blocks 53/UDP

## Gotchas
- Port 53/UDP blocked on a Resource silently returns empty DNS responses for non-`A` queries — not an error, no warning
- The DNS server Resource and the queried Resource port restrictions are **independent** — DNS server needs 53/UDP open; target Resource does not
- Explicit `@dns-server` queries bypass CGNAT — returns actual private IP addresses
- Most applications behave normally when non-`A` requests are blocked; explicit forwarding is only needed in edge cases

## Related Docs
- [How DNS works with Twingate](#)
- [Port restrictions](#)