---
source: https://help.twingate.com/articles/3646943674-checking-for-blocked-outbound-ports
type: help
fetched: 2026-08-06
source_version: 8584403de7dbc6f68e95d0922628cb0d7e9bd27a6d247a1c89e7f0f3a9109a23
---

# Checking for Blocked Outbound Ports

## Summary
Twingate Clients connect to Twingate's Relay infrastructure on ports 30000–31000. Some networks block non-standard outbound ports, which can prevent Twingate from functioning. This page explains how to test if those ports are blocked.

## Key Information
- Twingate Relay infrastructure uses port range **30000–31000**
- Networks that only allow ports 80/443 outbound will block Twingate Relay connections
- Test tool: `nmap` against `portquiz.net`

## Prerequisites
- `nmap` installed:
  - **Linux**: typically native
  - **Mac**: `brew install nmap`
  - **Windows**: download binary from nmap.org

## Step-by-Step

1. Run the following command to test outbound port 30001:
   ```bash
   time nmap -p 30001 portquiz.net
   ```

2. **Expected output (port open):**
   ```
   PORT      STATE  SERVICE
   30001/tcp open   pago-services1
   ```

3. **If port is blocked**, the state will show `filtered` or `closed` instead of `open`, indicating a firewall or network policy is blocking outbound traffic on that port range.

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Relay port range | 30000–31000 |
| Test port (example) | 30001 |
| Test host | `portquiz.net` |

## Gotchas
- Testing only port 30001 is a representative sample — the full range is 30000–31000; a network could block some ports but not others
- Corporate firewalls, hotel/airport Wi-Fi, and some ISPs commonly restrict non-standard ports
- `portquiz.net` is a third-party service that accepts connections on all ports — availability depends on that service remaining operational

## Related Docs
- Twingate Relay infrastructure documentation (port requirements)
- Twingate troubleshooting guide (parent page)