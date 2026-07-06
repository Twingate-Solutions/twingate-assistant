# How Twingate Forwards DNS

## Summary
Twingate Client resolves DNS `A` records locally using CGNAT IPs (100.64.0.0/10) and routes traffic through its network interface to the Connector. Non-`A` record queries are forwarded to the Remote Network's private DNS server via the Connector. DNS forwarding can be blocked by Resource port restrictions on port 53/UDP.

## Key Information
- Client resolves `A` records locally → assigns CGNAT IP → routes via Twingate interface → proxied to Connector
- CGNAT range used: `100.64.0.0/10`; routing range: `100.96.0.0/12`
- Non-`A` queries (TXT, MX, etc.) are forwarded to Remote Network and resolved by Connector using private DNS
- DNS traffic is treated as standard UDP traffic on port 53/UDP — no special-casing

## Prerequisites
For explicit DNS forwarding:
- Connector version **≥ 1.46.0**
- Client versions:
  - macOS ≥ 1.0.26
  - Linux ≥ 1.0.74
  - iOS ≥ 1.0.26
  - Android ≥ 1.0.23
  - Windows: not yet supported

## When DNS Forwarding Fails
- If a Resource has **port 53/UDP blocked**, non-`A` queries return empty responses (`ANSWER: 0`)
- This is expected behavior — Twingate applies port restrictions uniformly to all UDP traffic including DNS

## Explicit DNS Forwarding Workaround
To bypass automatic DNS handling, specify a **private Resource** as the DNS resolver directly:

```bash
dig @10.0.0.2 TXT nas.home.int
```

**Requirements:**
1. The DNS server (e.g., `10.0.0.2`) must be a configured Twingate Resource
2. Port 53/UDP must be **allowed** on that DNS server Resource
3. The target domain's Resource port restrictions don't matter — only the DNS server Resource's port config matters

**Use cases:**
- `dig @dns-server A nas.home.int` → returns real IP (not CGNAT address)
- `dig @dns-server TXT nas.home.int` → returns TXT record even if the target Resource blocks port 53/UDP

## Configuration Values
| Parameter | Value |
|-----------|-------|
| DNS port | 53/UDP |
| CGNAT local resolution range | `100.64.0.0/10` |
| Twingate routing range | `100.96.0.0/12` |

## Gotchas
- Port 53/UDP blocked on a Resource → all non-`A` DNS queries for that Resource return empty (no error, just no answer)
- Explicit `@server` DNS queries bypass Twingate's automatic handling only when the server is a private Resource
- `dig @dns-server A domain` returns the real IP, not the CGNAT IP assigned by Twingate

## Related Docs
- How DNS works with Twingate (prerequisite reading)
- Twingate port restrictions