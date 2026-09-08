---
source: https://help.twingate.com/articles/4982245028-using-nslookup-with-manually-defined-nameserver-fails-on-windows-with-twingate-client-running
type: help
fetched: 2026-09-06
source_version: 38425da823b01cd00849ee3092c52c99c252a799cd3eac4b44ae679ecb468a5e
---

# Using nslookup with Manually Defined Nameserver Fails on Windows with Twingate Client Running

## Summary
When the Twingate Client is active on Windows, it routes all DNS through an internal transparent proxy, blocking any attempt to manually specify an alternate DNS server. This is intentional behavior to enforce access control and prevent DNS leakage outside the Twingate-controlled path.

## Key Information
- Twingate installs a transparent DNS proxy on a virtual network interface (IP range: `100.95.0.x`)
- All DNS queries are intercepted and routed through this proxy
- Manually specifying a DNS resolver (e.g., `8.8.8.8`) bypasses the proxy path and is blocked
- Standard `nslookup` without a specified server works correctly via the Twingate proxy
- Behavior is by design — not a bug or misconfiguration

## Symptoms
**Fails:**
```
nslookup google.com 8.8.8.8
# DNS request timed out (4x), then "Request to UnKnown timed-out"
```

**Succeeds:**
```
nslookup google.com
# Resolves via 100.95.0.251 (Twingate proxy)
```

## Why It's Blocked
Two reasons DNS bypass attempts fail:
1. The request exits the Twingate-controlled network path
2. Private/internal domains may not be resolvable via public DNS servers

## Gotchas
- The Twingate proxy IP (`100.95.0.x`) may look unfamiliar but is expected — it's the virtual interface address
- Tools or scripts that hardcode DNS servers (e.g., `dig @8.8.8.8`, `nslookup domain server`) will fail the same way
- This applies system-wide on Windows when the client is running — no per-app exceptions
- Not a network connectivity issue; the timeout is a deliberate block, not packet loss

## Workaround
Use standard system DNS resolution (no manually specified nameserver) while Twingate Client is active. All resolvable domains — public and private — are handled by the Twingate proxy.

## Related Docs
- Twingate DNS proxy architecture
- Private resource name resolution configuration
- Windows client behavior and virtual network interface