---
source: https://help.twingate.com/articles/3646943674-checking-for-blocked-outbound-ports
type: help
fetched: 2026-10-04
source_version: 1a506015ed989222d782cbf7b482d1b2c74a18361257664efc15392b689a8a01
trust: official
---

# Checking for Blocked Outbound Ports

## Summary
Diagnose network-level port blocking that prevents Twingate Client from connecting to Resources. Uses `portquiz.net` (accepts all TCP ports) as a test target since Twingate Relay addresses are dynamic. Covers TCP 443 and the Relay port range 30000–31000.

## Key Information
- Twingate Client requires **no inbound** firewall rules; only outbound ports matter
- Most common failure pattern: port 443 open, but 30000–31000 blocked (network only allows web traffic)
- `portquiz.net` used because Twingate Relay IPs are dynamic and cannot be pre-tested directly
- `nmap` optional but useful; `nc` (netcat) and PowerShell `Test-NetConnection` are simpler

## Required Outbound Ports

| Port/Range | Protocol | Purpose |
|---|---|---|
| 443 | TCP | Controller + Relay communication |
| 30000–31000 | TCP | Relay fallback (if peer-to-peer unavailable) |
| 1–65535 | UDP/QUIC (HTTP/3) | Peer-to-peer (optimal performance) |

## Diagnostic Commands

**Test TCP 443:**
```bash
# macOS/Linux
nc -vz -w 5 portquiz.net 443

# Windows PowerShell
Test-NetConnection portquiz.net -Port 443
```

**Test Relay port range (sample beginning/middle/end):**
```bash
# macOS/Linux
for p in 30000 30500 31000; do nc -vz -w 5 portquiz.net $p; done

# Windows PowerShell
30000,30500,31000 | % { Test-NetConnection portquiz.net -Port $_ } | ft RemotePort,TcpTestSucceeded
```

**Optional nmap:**
```bash
nmap -Pn -p 443,30000,30500,31000 portquiz.net
```

## Result Interpretation

| Result | Meaning |
|---|---|
| `nc: succeeded` / `TcpTestSucceeded: True` / `nmap: open` | Port allowed |
| `nc: timed out` / PowerShell `False` (slow) / `nmap: filtered` | Silently dropped — likely outbound firewall rule |
| `nc: Connection refused` / `nmap: closed` | Actively rejected by firewall en route |
| `nmap: Host seems down` | Re-run with `-Pn` flag |

## Gotchas
- If port 443 itself fails, check for a **captive portal** (hotel/in-flight WiFi) before assuming Twingate issue
- Do **not** scan the entire 30000–31000 range with nmap — may trigger security alerts; sample 3 points instead
- Ignore nmap's `SERVICE` column (e.g., `pago-services1`) — it reflects nmap's port name database, not Twingate services
- `nmap` must use `-Pn` to skip host discovery if host appears down

## Resolution if Ports Are Blocked
- Ask network admin to allow outbound TCP 30000–31000
- Temporarily test on a mobile hotspot to confirm Twingate works without the restrictive network

## Prerequisites
- `nc` (native Linux, available via Homebrew on macOS)
- `nmap` (optional; install via package manager or [nmap.org binary](https://nmap.org))
- PowerShell (Windows built-in)

## Related Docs
- Client Endpoint Requirements (linked in original article)
- UDP/QUIC HTTP/3 guide (linked in original article)
- Twingate troubleshooting guide