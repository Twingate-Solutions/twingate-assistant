---
source: https://help.twingate.com/articles/5745151855-dns-using-dnsfilter-alongside-twingate
type: help
fetched: 2026-11-01
source_version: 9c1a01c51dfb9320b20bd0f0c85351ec0b154bded2ef8b5d5a16889ecd2b4909
trust: official
---

# DNS: Using DNSFilter Alongside Twingate

## Page Title
DNS: Using DNSFilter alongside Twingate

## Summary
DNSFilter and Twingate can coexist, but the DNSFilter Roaming Client requires additional configuration to work properly. Network-level and Relay deployments require no changes. The Roaming Client must be configured to use DNS-over-TLS to avoid connectivity issues caused by Twingate blocking standard TCP/UDP DNS test requests.

## Key Information
- **Network Deployment / DNSFilter Relay**: No extra configuration needed. Non-Twingate traffic is forwarded to DNSFilter servers automatically.
- **Roaming Client (default)**: Conflicts with Twingate. The client's startup DNS test requests (TCP/UDP) are blocked by Twingate, causing the Roaming Client to report no internet connectivity.
- **Fix**: Configure Roaming Client to use DNS-over-TLS (`tcp-tls`), which Twingate does not block by default.

## Prerequisites
- DNSFilter Roaming Client installed on target device
- Admin/sudo access on the device
- Twingate client installed

## Configuration Values

### Windows — Registry Key
**Retail version:**
```
reg add "HKLM\Software\DNSFilter\Agent" /v UpstreamOrder /d "tcp-tls" /f
```
**MSP/Whitelabel version:**
```
reg add "HKLM\Software\DNSAgent\Agent" /v UpstreamOrder /d "tcp-tls" /f
```

### macOS — Config File
**File path (both retail and MSP/whitelabel):**
```
/Library/Application Support/DNSFilter Agent/daemon.conf
```
**Setting to add at the top of the file:**
```
upstream_order = [ "tcp-tls"]
```

## Step-by-Step (Roaming Client Fix)

**Windows:**
1. Install the DNSFilter Roaming Client.
2. Run the appropriate `reg add` command above (retail vs. MSP) in an elevated terminal.
3. Restart the DNSFilter Roaming Client.

**macOS:**
1. Open `daemon.conf` using `sudo nano` with the path above.
2. Add `upstream_order = [ "tcp-tls"]` at the **top** of the file.
3. Save and restart the DNSFilter Roaming Client.

## Gotchas
- The `upstream_order` / `UpstreamOrder` setting must target the correct registry path or config file depending on whether you have the **retail** or **MSP/whitelabel** edition — paths differ.
- The setting must be placed at the **top** of `daemon.conf` on macOS.
- A client restart is required for changes to take effect.
- Default TCP/UDP DNS requests from the Roaming Client startup are blocked by Twingate by design — this is expected behavior, not a bug.

## Related Docs
- [DNSFilter Network Deployment](https://www.dnsfilter.com)
- [DNSFilter Relay documentation](https://www.dnsfilter.com)
- [DNSFilter Roaming Client documentation](https://www.dnsfilter.com)
- Twingate DNS configuration documentation