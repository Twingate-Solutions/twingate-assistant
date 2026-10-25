---
source: https://help.twingate.com/articles/3646943674-checking-for-blocked-outbound-ports
type: help
fetched: 2026-10-25
source_version: d3436a905dbd58a24af4f0e58b92cc86b757f163669e8c6479bf6f1238589490
trust: official
---

# Checking for Blocked Outbound Ports

## Summary
Diagnose network-level port blocking that prevents Twingate Clients from connecting to Resources. Uses `portquiz.net` (accepts all TCP ports) as a neutral test target since Twingate Relay addresses are dynamic. Applies when Client works on one network but not another, or when sign-in succeeds but Resources fail.

## Key Information
- Twingate Client requires three outbound port categories:
  - **TCP 443** — Controller and Relay communication
  - **TCP 30000–31000** — Relay fallback (when peer-to-peer unavailable)
  - **UDP 1–65535** — Peer-to-peer / QUIC / HTTP3 (optimal performance)
- Most common failure pattern: TCP 443 passes, ports 30000–31000 are filtered (network allows web traffic only)

## Prerequisites
- One of: `nc` (Linux/macOS native), PowerShell (Windows), or `nmap` (optional, cross-platform)
- Install `nmap`: Linux (native), macOS (`brew install nmap`), Windows (binary download)

## Diagnostic Commands

### Test TCP 443
**macOS/Linux:**
```bash
nc -vz -w 5 portquiz.net 443
```
**Windows (PowerShell):**
```powershell
Test-NetConnection portquiz.net -Port 443
```

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
> Do not scan the full 30000–31000 range; it may trigger security alerts.

## Result Interpretation

| Result | Meaning |
|--------|---------|
| `nc: succeeded` / `TcpTestSucceeded: True` / `nmap: open` | Port allowed |
| `nc: Operation timed out` / `False` (long wait) / `nmap: filtered` | Silently dropped — outbound firewall rule |
| `nc: Connection refused` / `nmap: closed` | FW on path actively rejected — treat as blocked |
| `nmap: Host seems down` | Discovery probe blocked; re-run with `-Pn` |

## Gotchas
- If **443 fails**: not a Twingate port issue — check for a captive portal (hotel/in-flight WiFi)
- Ignore nmap's `SERVICE` column (e.g., `pago-services1`) — it's nmap's label for that port number, unrelated to Twingate
- Twingate Relays only accept Twingate traffic, so you cannot test against them directly

## Resolution Steps
1. If relay ports blocked: ask network admin to allow outbound TCP 30000–31000
2. Test on mobile hotspot to confirm Twingate works when ports are unblocked

## Related Docs
- Client Endpoint Requirements
- Twingate Troubleshooting Guide
- UDP/QUIC/HTTP3 guide (peer-to-peer connectivity)