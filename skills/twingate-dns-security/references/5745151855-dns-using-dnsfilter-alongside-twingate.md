---
source: https://help.twingate.com/articles/5745151855-dns-using-dnsfilter-alongside-twingate
type: help
fetched: 2026-09-06
source_version: 969b7a99b8cf240fbbfe1b11a22f1842080967c676b1feaee4408543a3658892
---

# DNS: Using DNSFilter alongside Twingate

## Summary
Twingate and DNSFilter can coexist with minimal configuration depending on the DNSFilter deployment method. Network-level deployments require no changes, but the DNSFilter Roaming Client requires DNS-over-TLS configuration to avoid connectivity failures caused by Twingate blocking the client's test DNS requests.

## Key Information
- **Network Deployment / Relay**: Works automatically with Twingate — non-Twingate traffic forwards to DNSFilter servers with no extra config
- **Roaming Client issue**: Twingate blocks TCP/UDP test DNS requests made during Roaming Client startup, causing the client to report no internet connectivity
- **Fix**: Configure Roaming Client to use DNS-over-TLS (not blocked by Twingate by default)

## Prerequisites
- DNSFilter Roaming Client installed on device
- Admin/elevated privileges (registry access on Windows, sudo on macOS)

## Step-by-Step: Configure DNS-over-TLS for Roaming Client

### Windows — Retail Version
```
reg add "HKLM\Software\DNSFilter\Agent" /v UpstreamOrder /d "tcp-tls" /f
```

### Windows — MSP/Whitelabel Version
```
reg add "HKLM\Software\DNSAgent\Agent" /v UpstreamOrder /d "tcp-tls" /f
```

### macOS — Retail Version
```bash
sudo nano "/Library/Application Support/DNSFilter Agent/daemon.conf"
```
Add at the **top** of the file:
```
upstream_order = [ "tcp-tls"]
```

### macOS — MSP/Whitelabel Version
Same file path and edit as retail version above.

After editing, restart the DNSFilter Roaming Client for changes to take effect.

## Configuration Values

| Platform | Key/Setting | Value |
|----------|-------------|-------|
| Windows (registry) | `UpstreamOrder` | `tcp-tls` |
| macOS (daemon.conf) | `upstream_order` | `[ "tcp-tls"]` |

## Gotchas
- DNS-over-TLS config must be placed at the **top** of `daemon.conf` on macOS
- Two different registry paths exist for retail vs. MSP/whitelabel Windows clients — use the correct one
- Roaming Client restart is required after making changes
- Standard TCP/UDP DNS from the Roaming Client is blocked by Twingate by design; this is expected behavior, not a bug

## Deployment Method Summary

| DNSFilter Method | Extra Config Needed? |
|-----------------|----------------------|
| Network Deployment | None |
| DNSFilter Relay | None |
| Roaming Client | Yes — enable DNS-over-TLS |

## Related Docs
- [DNSFilter Network Deployment](https://help.dnsfilter.com)
- [DNSFilter Roaming Client](https://help.dnsfilter.com)
- Twingate DNS handling documentation