# Device Failures - Twingate Troubleshooting

## Page Title
Device Failures: How to Troubleshoot User Device Issues

## Summary
Covers troubleshooting Twingate Client failures caused by service/daemon issues, missing virtual network adapters, and software conflicts. Applies when the Client UI is stuck, the adapter is missing, or the Resource list is empty despite connection.

## Key Information
- Client UI is a front-end only; actual work runs as a background service
- Twingate creates a virtual network interface per OS to handle traffic
- Software conflicts (VPNs, AV/EDR, network optimizers) are a very common failure cause
- Empty Resource list while connected typically indicates a DNS issue (not covered here)

## Common Symptoms
- Client UI stuck on "Disconnected" with unresponsive connect button
- Windows logs show `TapAdapterExistence` errors or "Twingate adapter is missing"
- Connected but Resource list is empty

## Step-by-Step Troubleshooting

### 1. Check Background Service
| OS | Command/Action |
|----|---------------|
| Windows | `services.msc` → find "Twingate Service" → verify Running + Automatic startup |
| macOS | `log show --process Twingate --last 1h` |
| Linux | `sudo journalctl -u twingate --since "1 hour ago"` |

### 2. Verify Virtual Network Adapter
| OS | Command | Expected |
|----|---------|----------|
| Windows | `ipconfig \| findstr "Twingate"` | "Twingate TAP-Windows Adapter" present |
| macOS | `scutil --nc list` | Twingate network extension listed |
| Linux | `ip a` | Interface `sdwan0` present |

**Fix:** If adapter missing → reinstall the Twingate Client

### 3. Check for Software Conflicts
- Temporarily **uninstall** (not just disable) suspected conflicting software
- Restart machine, then test Twingate
- If resolved, reinstall other software and add exceptions for Twingate processes and `*.twingate.com`

### 4. Collect Client Logs
- UI path: **More → Troubleshoot → View Logs**

| OS | Log Location |
|----|-------------|
| Windows | `%LOCALAPPDATA%\Twingate\logs` (`Twingate.log` + `Twingate.Service.log`) |
| macOS | `~/Library/Group Containers/6GX8KVTR9H.com.twingate.com/Logs/private/var/log/twingate/` |

## Conflict Sources to Investigate
- Other VPN or ZTNA clients (routing table conflicts)
- Antivirus/EDR/Firewall with deep packet inspection
- OEM-preinstalled network optimization/traffic shaping software

## Gotchas
- Disabling security software is insufficient—drivers may remain active in the network stack; full uninstall required for conflict testing
- Windows Event Viewer (Application Log) needed if service fails to start entirely
- Empty Resource list = likely DNS issue, not a Client/adapter failure

## Related Docs
- DNS troubleshooting (implied for empty Resource list scenarios)
- Client logs reference
- Twingate Client installation/reinstallation