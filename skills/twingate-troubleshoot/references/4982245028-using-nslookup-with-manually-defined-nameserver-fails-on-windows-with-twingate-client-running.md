---
source: https://help.twingate.com/articles/4982245028-using-nslookup-with-manually-defined-nameserver-fails-on-windows-with-twingate-client-running
type: help
fetched: 2026-10-04
source_version: e2648660dd5f751b35d5bca70eec48c83fe14ea3078e163f24b38f4a5bffba25
trust: official
---

# Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client

## Summary
When the Twingate Client is active on Windows, it intercepts all DNS queries via a transparent DNS proxy on a virtual interface. Manually specifying a DNS server in `nslookup` (or similar tools) bypasses this proxy and is blocked by design.

## Key Information
- Twingate routes all DNS through an internal proxy on a virtual NIC (typically `100.95.0.x`)
- Manual nameserver specification (e.g., `nslookup <domain> 8.8.8.8`) is **intentionally blocked**
- Standard `nslookup` without a custom resolver works correctly
- Blocking prevents DNS leakage and maintains secure private resource resolution

## Behavior Reference

| Command | Result |
|---|---|
| `nslookup google.com 8.8.8.8` | ❌ Times out |
| `nslookup google.com` | ✅ Resolves via `100.95.0.x` |

## Why It's Blocked
- DNS request bypasses Twingate-controlled path
- Private resources may not resolve via public DNS
- Enforced to prevent information leakage

## Gotchas
- This is **expected behavior**, not a bug or misconfiguration
- Applies to any tool that allows manual DNS server specification (not just `nslookup`)
- The proxy IP (`100.95.0.x`) is Twingate's virtual interface, not a misconfigured resolver

## Related Docs
- Twingate DNS proxy behavior
- Private resource name resolution