---
source: https://help.twingate.com/articles/4982245028-using-nslookup-with-manually-defined-nameserver-fails-on-windows-with-twingate-client-running
type: help
fetched: 2026-11-08
source_version: 4152e0233e329fd74de75ca883accf4306ae9e32fc910f6a2a2ade170921ce3e
trust: official
---

# Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running

## Summary
When the Twingate Client is active on Windows, it routes all DNS through an internal transparent DNS proxy. Manually specifying a nameserver in `nslookup` (or similar tools) bypasses this proxy and is intentionally blocked.

## Key Information
- Twingate deploys a transparent DNS proxy on a virtual interface, typically at `100.95.0.x`
- All DNS queries must route through this proxy for private resource resolution and access control
- Manually specifying a resolver (e.g., `8.8.8.8`) causes the request to be blocked/timeout — this is by design
- Standard `nslookup` without a custom resolver works correctly via the Twingate proxy

## Behavior Examples

**Fails (manual nameserver specified):**
```
nslookup google.com 8.8.8.8
# Result: DNS request timed out (4x), then *** Request to UnKnown timed-out
```

**Works (system default resolver via Twingate proxy):**
```
nslookup google.com
# Result: Resolves via 100.95.0.251
```

## Why This Is Blocked
1. Manually specified DNS requests exit the Twingate-controlled path
2. Private resources are only resolvable via the Twingate proxy — not public DNS
3. Twingate blocks bypass attempts to prevent information leakage and enforce secure resolution

## Gotchas
- This is **not a bug** — it is intentional enforcement behavior
- Affects any tool that allows manual DNS server specification (not just `nslookup`)
- The Twingate proxy IP (`100.95.0.x`) is a virtual interface address, not a physical network DNS server
- Troubleshooting DNS issues should use `nslookup` without specifying a nameserver, or tools that respect system DNS settings

## Configuration Values
| Value | Description |
|-------|-------------|
| `100.95.0.x` | Twingate virtual interface / DNS proxy address (Windows) |

## Related Docs
- Twingate DNS proxy behavior and private resource resolution
- Twingate Client network architecture (Windows)