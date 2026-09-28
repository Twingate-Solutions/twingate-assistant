---
source: https://help.twingate.com/articles/3646943674-checking-for-blocked-outbound-ports
type: help
fetched: 2026-09-27
source_version: fa4e67df3c43fbd411b61b6bd947c0376c6fc140881668e05c799ecf247490af
---

# Checking for Blocked Outbound Ports

## Summary
Diagnose network-level port blocking when Twingate Client connects on some networks but not others. Uses `portquiz.net` (accepts all TCP ports) as a test target since Twingate Relay addresses are dynamic with no fixed IP. Tests confirm whether outbound firewall rules are dropping required traffic.

## Key Information
- Twingate Client requires three outbound port categories:
  - **TCP 443** – Controller and Relay communication
  - **TCP 30000–31000** – Relay fallback when peer-to-peer unavailable
  - **UDP 1–65535** – Peer-to-peer (QUIC/HTTP3) for optimal performance
- `portquiz.net` accepts every TCP port; unreachability indicates network blocking, not Twingate issues

## Prerequisites
- `nc` (netcat) – native on Linux/macOS
- `nmap` – native Linux, `brew install nmap` on macOS, binary on Windows
- PowerShell available on Windows

## Step-by-Step

### Test TCP 443
**macOS/Linux:**
```bash
nc -vz -w 5 portquiz.net 443
```
**Windows (PowerShell):**
```powershell
Test-NetConnection portquiz.net -Port 443
```
> If 443 fails: check for captive portal (hotel/in-flight WiFi), not a Twingate issue.

### Test Relay Port Range (30000–31000)
**macOS/Linux:**
```bash
for p in 30000 30500 31000; do nc -vz -w 5 portquiz.net $p; done
```
**Windows (PowerShell):**
```powershell
30000,30500,31000 | % { Test-NetConnection portquiz.net -Port $_ } | ft RemotePort,TcpTestSucceeded
```
**nmap (optional):**
```bash
nmap -Pn -p 443,30000,30500,31000 portquiz.net
```

## Result Interpretation

| Result | Meaning |
|--------|---------|
| `nc: succeeded` / `TcpTestSucceeded: True` / `nmap: open` | Port allowed |
| `nc: Operation timed out` / PowerShell `False` after long wait / `nmap: filtered` | Silent drop — outbound firewall rule blocking |
| `nc: Connection refused` / `nmap: closed` | FW on path rejected connection — treat as blocked |
| `nmap: Host seems down` | Discovery probe blocked — rerun with `-Pn` |

**Typical blocked pattern:** 443 open, 30000/30500/31000 `filtered` or timed out (network allows web traffic only).

## Gotchas
- Do **not** scan the full 30000–31000 range with nmap — may trigger security alerts
- Ignore nmap's `SERVICE` column (e.g., `pago-services1`) — irrelevant port name mappings
- `Connection refused` from `portquiz.net` means a network firewall rejected it (not the server), treat same as blocked
- UDP ports cannot be tested with this method; only TCP is covered here

## Resolution
- Ask network admin to allow outbound **TCP 30000–31000**
- Test with mobile hotspot to confirm ports are the issue

## Related Docs
- Client Endpoint Requirements
- QUIC/HTTP3 UDP guide
- Twingate Troubleshooting Guide