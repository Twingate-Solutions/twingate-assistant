---
source: https://www.twingate.com/docs/how-twingate-forwards-dns
type: docs
fetched: 2026-10-25
source_version: 3d60ae648962a8328044113f06789c01f9965d3a7999b5e44a95b67199a8e235
trust: official
---

# How Twingate Forwards DNS

## Summary
Twingate Client resolves DNS `A` records locally using CGNAT IPs (`100.64.0.0/10`) and routes traffic through its local network interface to the Connector. Non-`A` record types (e.g., `TXT`, `MX`) are forwarded to the Remote Network's private DNS server via the Connector, unless port 53/UDP is blocked on the Resource.

## Key Information
- **`A` records**: Resolved locally by the Client; assigned a CGNAT IP from `100.64.0.0/10`; traffic routed via `100.96/12` through Twingate's local interface
- **Non-`A` records** (TXT, MX, etc.): Forwarded to Remote Network and resolved by Connector using the network's private DNS server
- DNS traffic uses port **53/UDP**; Twingate treats it as standard UDP traffic — no special-casing
- DNS queries for a Resource with port 53/UDP blocked return an **empty response** (status: NOERROR, ANSWER: 0)

## When DNS Forwarding Does NOT Work
- Port 53/UDP is blocked on the target Resource's Twingate configuration
- Result: non-`A` queries return empty responses (not errors)
- Most applications behave normally when non-`A` requests are blocked

## Explicit DNS Forwarding (Workaround)
Point DNS queries at a **private Resource** that is also a DNS server with port 53/UDP **open**.

```bash
# Forward query to a specific private DNS server
dig @10.0.0.2 TXT nas.home.int

# Returns real IP (not CGNAT) when using explicit DNS server
dig @dns-server A nas.home.int

# Works even if nas.home.int has port 53/UDP blocked,
# as long as 10.0.0.2 (the DNS Resource) allows port 53/UDP
dig @10.0.0.2 TXT nas.home.int
```

## Configuration Values
| Parameter | Value |
|---|---|
| CGNAT range (full) | `100.64.0.0/10` |
| CGNAT range (routed) | `100.96.0.0/12` |
| DNS port | `53/UDP` |

## Gotchas
- Port restrictions on a Resource apply to **DNS traffic targeting that Resource**, not just application traffic — blocking 53/UDP blocks non-`A` DNS queries for that Resource
- Explicit `@dns-server` queries bypass the local resolver and return the **real IP**, not the Twingate CGNAT IP
- The private DNS server used for explicit forwarding **must** be configured as a Twingate Resource with port 53/UDP allowed
- DNS forwarding failure returns `NOERROR` with empty answers — may be hard to distinguish from "record doesn't exist"

## Related Docs
- [How DNS works with Twingate](https://www.twingate.com/docs/how-dns-works-with-twingate)
- [Port restrictions](https://www.twingate.com/docs/port-restrictions)