---
source: https://help.twingate.com/articles/3646943674-checking-for-blocked-outbound-ports
type: help
fetched: 2026-10-11
source_version: e9aa0fcb11199b8b6ed5cc533ffa699c789f6f1b2b54cb0f5b42629f1d446a6d
trust: official
---

# Checking for Blocked Outbound Ports

## Summary
Diagnostic guide for testing whether a network blocks outbound ports required by the Twingate Client. Uses `portquiz.net` (a server accepting all TCP ports) as a proxy test target since Twingate Relay addresses are dynamic. Applicable when the Client works on one network but not another, or when Resources fail to connect.

## Key Information
- Twingate Relay addresses are assigned dynamically — no fixed IP to test against directly
- `portquiz.net` accepts connections on every TCP port, making it suitable as a stand-in
- Typical blocked scenario: port 443 passes, but 30000–31000 are filtered (network only permits web traffic)

## Prerequisites
- `nc` (netcat) — native on Linux/macOS
- `nmap` — native on Linux; install via `brew` on macOS; binary available on Windows
- PowerShell — available on Windows natively

## Required Outbound Ports

| Port(s) | Protocol | Purpose |
|---|---|---|
| 443 | TCP | Controller and Relay communication |
| 30000–31000 | TCP | Relay fallback (when P2P unavailable) |
| 1–65535 | UDP/QUIC (HTTP/3) | Peer-to-peer connectivity |

## Step-by-Step Tests

**Test port 443:**
```bash
# macOS/Linux
nc -vz -w 5 portquiz.net 443

# Windows PowerShell
Test-NetConnection portquiz.net -Port 443
```

**Test Relay port range (sample points):**
```bash
# macOS/Linux
for p in 30000 30500 31000; do nc -vz -w 5 portquiz.net $p; done

# Windows PowerShell
30000,30500,31000 | % { Test-NetConnection portquiz.net -Port $_ } | ft RemotePort,TcpTestSucceeded
```

**Optional nmap scan:**
```bash
nmap -Pn -p 443,30000,30500,31000 portquiz.net
```

## Reading Results

| Result | Meaning |
|---|---|
| `nc: succeeded` / `TcpTestSucceeded: True` / `nmap: open` | Port allowed |
| `nc: Operation timed out` / `False` after long wait / `nmap: filtered` | Silently dropped — likely outbound firewall rule |
| `nc: Connection refused` / `nmap: closed` | Firewall on path rejected connection — treat as blocked |
| `nmap: Host seems down` | Discovery check blocked — re-run with `-Pn` |

## Gotchas
- **Captive portals** (hotel/in-flight WiFi): if port 443 fails, complete the captive portal login first — not a Twingate issue
- **nmap `SERVICE` column**: ignore it (e.g., `pago-services1`) — it's nmap's label for the port number, unrelated to Twingate
- **Do not scan the full 30000–31000 range** with nmap — may trigger security alerts; sampling beginning/middle/end is sufficient

## Resolution if Ports Are Blocked
1. Ask network admin to allow outbound TCP 30000–31000 (reference: [Client Endpoint Requirements](https://help.twingate.com/articles/client-endpoint-requirements))
2. Test on a mobile hotspot to confirm Twingate functions without the restrictive network

## Related Docs
- Client Endpoint Requirements
- Twingate Troubleshooting Guide
- UDP/QUIC HTTP/3 connectivity guide