---
source: https://help.twingate.com/articles/3646943674-checking-for-blocked-outbound-ports
type: help
fetched: 2026-10-18
source_version: 537fa8a8f3c18f9c25bce6744c7c459ae7900b629304bc975936638fcce12cf9
trust: official
---

# Checking for Blocked Outbound Ports

## Summary
Diagnose network-level port blocking that prevents Twingate Client from connecting to Resources. Uses `nc`, PowerShell, or `nmap` against `portquiz.net` (a public server accepting all TCP ports) as a proxy for Twingate Relay reachability, since Relay IPs are dynamic.

## Key Information
- Twingate Relays only accept Twingate traffic and have no fixed IPs to test directly
- `portquiz.net` accepts connections on every TCP port — a failure means the network is blocking that port
- Typical failure pattern: port 443 open, relay range (30000–31000) filtered/timed out

## Required Outbound Ports

| Port/Range | Protocol | Purpose |
|---|---|---|
| 443 | TCP | Controller + Relay basic communication |
| 30000–31000 | TCP | Relay fallback (when peer-to-peer unavailable) |
| 1–65535 | UDP/QUIC (HTTP/3) | Peer-to-peer optimal performance |

## Diagnostic Commands

**Test port 443:**
```bash
# macOS/Linux
nc -vz -w 5 portquiz.net 443

# Windows PowerShell
Test-NetConnection portquiz.net -Port 443
```

**Test relay port range (sample beginning, middle, end):**
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
> Do not scan the full 30000–31000 range — may trigger security alerts.

## Result Interpretation

| Tool | Result | Meaning |
|---|---|---|
| `nc` | `succeeded` | Port allowed |
| PowerShell | `TcpTestSucceeded: True` | Port allowed |
| `nmap` | `open` | Port allowed |
| `nc` | `Operation timed out` | Silently dropped — firewall rule likely |
| PowerShell | `False` (after long wait) | Silently dropped |
| `nmap` | `filtered` | Silently dropped |
| `nc`/`nmap` | `Connection refused` / `closed` | Active rejection by firewall — treat as blocked |
| `nmap` | `Host seems down` | Discovery probe blocked; re-run with `-Pn` |

## Gotchas
- If port 443 fails, suspect a **captive portal** (hotel/in-flight WiFi) — not a Twingate issue
- Ignore `nmap`'s `SERVICE` column (e.g., `pago-services1`) — it's nmap's label for the port number, unrelated to Twingate
- `nmap` is native on Linux; install via `brew` on macOS or binary on Windows

## Resolution
- If relay ports are blocked: ask network admin to allow outbound TCP 30000–31000
- Test on a mobile hotspot to confirm Twingate functions when ports are unblocked

## Related Docs
- [Client Endpoint Requirements](https://help.twingate.com/articles/client-endpoint-requirements)
- Twingate Troubleshooting Guide