---
source: https://help.twingate.com/articles/5745151855-dns-using-dnsfilter-alongside-twingate
type: help
fetched: 2026-08-06
source_version: a708cd78c0316b2d244d89bdf6bf03f2c794cc1de82501f5a343fee52f393dcc
---

# DNS: Using DNSFilter alongside Twingate

## Summary
DNSFilter and Twingate can coexist with minimal configuration depending on the DNSFilter deployment method. Network-level deployments require no changes, but the DNSFilter Roaming Client requires DNS-over-TLS configuration to avoid connectivity issues caused by Twingate blocking the client's startup DNS test requests.

## Key Information
- Twingate forwards non-resource DNS queries to configured DNS servers, making network-level DNSFilter deployments transparent
- DNSFilter Roaming Client's TCP/UDP startup "test" DNS requests are blocked by Twingate, causing the roaming client to report no internet connectivity
- DNS-over-TLS (DoT) is **not** blocked by Twingate by default and is the fix for roaming client conflicts

## Prerequisites
- DNSFilter Roaming Client installed on endpoint
- Admin/registry access on Windows or sudo access on macOS

## Configuration by Deployment Type

### Network Deployment / DNSFilter Relay
No configuration required. Twingate passes non-resource traffic to the configured DNS servers automatically.

### DNSFilter Roaming Client — Windows

**Retail version:**
```
reg add "HKLM\Software\DNSFilter\Agent" /v UpstreamOrder /d "tcp-tls" /f
```

**MSP/whitelabel version:**
```
reg add "HKLM\Software\DNSAgent\Agent" /v UpstreamOrder /d "tcp-tls" /f
```

### DNSFilter Roaming Client — macOS

Open config file (both retail and MSP versions use same path):
```
sudo nano /Library/Application\ Support/DNSFilter\ Agent/daemon.conf
```

Add at the **top** of the file:
```
upstream_order = [ "tcp-tls"]
```

## Configuration Values

| Parameter | Value | Purpose |
|-----------|-------|---------|
| `UpstreamOrder` (Windows registry) | `tcp-tls` | Forces DoT on Windows |
| `upstream_order` (macOS config) | `[ "tcp-tls"]` | Forces DoT on macOS |

## Gotchas
- The `upstream_order` line must be placed at the **top** of `daemon.conf` on macOS
- Restart both DNSFilter and Twingate clients after making changes
- Two different registry paths exist for retail vs. MSP/whitelabel Windows editions — use the correct one
- Without this fix, symptom is "limited or no internet connectivity" after both clients are installed

## Related Docs
- [DNSFilter Network Deployment documentation](https://help.dnsfilter.com)
- [DNSFilter Roaming Client documentation](https://help.dnsfilter.com)
- Twingate DNS configuration guides