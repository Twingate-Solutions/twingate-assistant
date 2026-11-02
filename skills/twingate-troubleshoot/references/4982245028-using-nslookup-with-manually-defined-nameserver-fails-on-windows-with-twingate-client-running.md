---
source: https://help.twingate.com/articles/4982245028-using-nslookup-with-manually-defined-nameserver-fails-on-windows-with-twingate-client-running
type: help
fetched: 2026-11-01
source_version: 4caf46e766051cd5bd1cb9fc7e2a4e27f985a6f2c97d659ea622262cdb306582
trust: official
---

# Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running

## Summary
When the Twingate Client is active on Windows, it routes all DNS through an internal transparent DNS proxy, blocking any attempt to manually specify an alternate DNS server (e.g., `nslookup google.com 8.8.8.8`). This is intentional behavior to enforce access control and prevent DNS leakage outside the Twingate-controlled path.

## Key Information
- Twingate installs a transparent DNS proxy on a virtual network interface, typically at `100.95.0.x`
- All DNS queries are intercepted by this proxy — manually specifying resolvers bypasses it and gets blocked
- Standard `nslookup` without a custom resolver works correctly (routes through Twingate proxy)
- This behavior applies on Windows with the Twingate Client running

## Behavior Reference

| Command | Result |
|---|---|
| `nslookup google.com` | ✅ Succeeds — uses Twingate proxy at `100.95.0.x` |
| `nslookup google.com 8.8.8.8` | ❌ Fails — request blocked, times out |

## Why Requests Are Blocked
- Manually specifying a resolver routes DNS outside Twingate's controlled path
- Private resources may not be resolvable via public DNS (e.g., `8.8.8.8`)
- Twingate blocks this to prevent DNS information leakage

## Gotchas
- The timeout failure when specifying a custom DNS server is **expected and by design** — not a bug or misconfiguration
- Tools that hardcode a DNS resolver (not just `nslookup`) will similarly fail while Twingate is active
- Diagnostic tools relying on alternate nameservers for DNS testing will not work while the client is running
- No workaround exists by design; use standard system DNS resolution instead

## Related Docs
- Twingate DNS proxy and private resource resolution documentation
- Twingate Client network interface configuration