---
source: https://help.twingate.com/articles/3646943674-checking-for-blocked-outbound-ports
type: help
fetched: 2026-09-06
source_version: 9fdb13219706b754253ce5d4934b798281916f080f936d4b169071bb0941af6e
---

# Checking for Blocked Outbound Ports

## Page Title
Checking for Blocked Outbound Ports

## Summary
Twingate Clients connect to Twingate's Relay infrastructure on ports 30000–31000. Some networks block non-standard outbound ports, which can prevent Twingate from functioning. Use `nmap` to verify these ports are reachable.

## Key Information
- Twingate Relay port range: **30000–31000**
- Common blocking occurs at networks that only allow ports **80** and **443** outbound
- Test target: `portquiz.net` (accepts connections on any port)

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

2. Check output for port state:

   **Success (port open):**
   ```
   PORT      STATE  SERVICE
   30001/tcp open   pago-services1
   ```

   **Failure (port blocked):** State will show `filtered` or `closed` instead of `open`

3. If blocked, test additional ports in the range (30000–31000) to determine scope of blocking.

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Relay port range | 30000–31000 |
| Test port (example) | 30001 |
| Test host | `portquiz.net` |

## Gotchas
- A single port test (30001) is representative but doesn't confirm the full range is open — test multiple ports if thorough verification is needed
- Firewalls may allow the test but block specific IPs used by Twingate Relays; this test only validates port accessibility generically
- `filtered` state in nmap typically means a firewall is dropping packets; `closed` means the host rejected the connection (different issue)

## Related Docs
- [Twingate Relay infrastructure / port requirements](https://help.twingate.com)
- Twingate Troubleshooting Guide (parent page)