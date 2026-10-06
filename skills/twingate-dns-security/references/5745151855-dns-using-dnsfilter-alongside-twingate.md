---
source: https://help.twingate.com/articles/5745151855-dns-using-dnsfilter-alongside-twingate
type: help
fetched: 2026-10-04
source_version: ace33ab218b86ca810dffcf2643b0b3c70f0422dce9aa4cb9f11176ceb582add
trust: official
---

# DNS: Using DNSFilter Alongside Twingate

## Summary
DNSFilter and Twingate can coexist, but configuration requirements depend on the DNSFilter deployment method. Network deployments require no changes; the Roaming Client requires DNS-over-TLS to be enabled to avoid connectivity failures caused by Twingate blocking DNSFilter's startup DNS test requests.

## Key Information
- Twingate intercepts DNS requests by default; this conflicts with the DNSFilter Roaming Client's TCP/UDP startup checks
- Network-level and Relay deployments work transparently — non-Twingate resources pass through to DNSFilter servers automatically
- Roaming Client failure mode: device ends up with limited/no internet connectivity because DNSFilter misreads blocked test requests as "no internet"
- Fix: configure Roaming Client to use DNS-over-TLS (not blocked by Twingate by default)

## Prerequisites
- DNSFilter Roaming Client installed on target devices
- Admin/sudo access to modify registry (Windows) or config files (macOS)

## Deployment Method Matrix

| DNSFilter Method | Extra Config Needed |
|---|---|
| Network Deployment | None |
| DNSFilter Relay | None |
| Roaming Client | Enable DNS-over-TLS (see below) |

## Step-by-Step: Enable DNS-over-TLS for Roaming Client

### Windows — Retail Edition
```
reg add "HKLM\Software\DNSFilter\Agent" /v UpstreamOrder /d "tcp-tls" /f
```

### Windows — MSP/Whitelabel Edition
```
reg add "HKLM\Software\DNSAgent\Agent" /v UpstreamOrder /d "tcp-tls" /f
```

### macOS — Both Editions
1. Open config file:
   - Retail: `sudo nano /Library/Application\ Support/DNSFilter\ Agent/daemon.conf`
   - MSP/Whitelabel: same path as retail (identical for both editions)
2. Add at the **top** of the file:
   ```
   upstream_order = [ "tcp-tls"]
   ```
3. Restart the DNSFilter Roaming Client

## Configuration Values

| Platform | Key/Setting | Value |
|---|---|---|
| Windows (Retail) | `HKLM\Software\DNSFilter\Agent\UpstreamOrder` | `tcp-tls` |
| Windows (MSP) | `HKLM\Software\DNSAgent\Agent\UpstreamOrder` | `tcp-tls` |
| macOS | `upstream_order` in `daemon.conf` | `[ "tcp-tls"]` |

## Gotchas
- Setting must be added at the **top** of `daemon.conf` on macOS — placement matters
- Client restart may be required after making changes
- DNS-over-TLS is not blocked by Twingate by default; plain TCP/UDP DNS startup probes are blocked
- MSP/whitelabel registry path differs from retail (`DNSAgent` vs `DNSFilter`)

## Related Docs
- [DNSFilter Network Deployment](https://help.dnsfilter.com)
- [DNSFilter Roaming Client documentation](https://help.dnsfilter.com)
- Twingate DNS handling documentation