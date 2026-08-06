---
source: https://help.twingate.com/articles/4982245028-using-nslookup-with-manually-defined-nameserver-fails-on-windows-with-twingate-client-running
type: help
fetched: 2026-08-06
source_version: 1f38e2509022091119261687dc3e8bc54d58be91eddd6bdf53610d7ccdf8d0dd
---

# Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running

## Summary
When the Twingate Client is active on Windows, it routes all DNS through an internal transparent DNS proxy. Manually specifying a DNS server (e.g., `nslookup google.com 8.8.8.8`) bypasses this proxy and is blocked by design to prevent information leakage and maintain secure resource resolution.

## Key Information
- Twingate intercepts all DNS queries via a transparent DNS proxy on a virtual network interface
- Proxy IP is typically in the `100.95.0.x` range (e.g., `100.95.0.251`)
- Manual DNS server specification in `nslookup` is **blocked by design** — not a bug
- Standard `nslookup` without a specified server works normally through the Twingate proxy
- Applies to Windows only (this specific behavior/doc)

## Behavior Details

**Fails (manual nameserver specified):**
```
nslookup google.com 8.8.8.8
# Result: DNS request timed out (repeated), then times out
```

**Works (system default via Twingate proxy):**
```
nslookup google.com
# Result: Resolves via 100.95.0.251
```

## Why Requests Are Blocked
1. DNS request would leave the Twingate-controlled resolution path
2. Private resources may not be resolvable via public DNS
3. Twingate enforces proxy routing to prevent information leakage

## Gotchas
- Timeout errors (`DNS request timed out`) can look like a network failure — they are actually enforcement behavior
- Server shows as `UnKnown` with the manually specified IP, which may be mistaken for a configuration error
- Any tool or application that hardcodes a DNS resolver will encounter the same blocking behavior, not just `nslookup`
- This is **expected behavior**, not a defect to troubleshoot

## Prerequisites
- Twingate Client installed and running on Windows
- Virtual network interface active (assigned `100.95.0.x` address)

## Related Docs
- Twingate DNS proxy behavior / DNS resolution architecture
- Private resource DNS configuration