# Device Failures - Twingate Troubleshooting

## Summary
Covers diagnosis and resolution of Twingate Client application failures at the OS networking stack level. Addresses stuck/disconnected state, missing adapter errors, and empty resource lists. Conflicts with other network software are the most common root cause.

## Key Information
- Client UI is a front-end only; background service does the actual work
- Twingate creates a virtual network adapter per platform (TAP on Windows, network extension on macOS, `sdwan0` on Linux)
- If connected but cannot access a specific Resource by name → DNS issue (not covered here)
- Simply "disabling" conflicting software is insufficient; their drivers may remain active in the network stack

## Common Symptoms
- Client UI stuck on "Disconnected," connect button unresponsive
- Windows log errors: `TapAdapterExistence` or "Twingate adapter is missing"
- Connected but Resource list is empty

## Diagnostic Steps

### 1. Check Background Service
| Platform | Command |
|----------|---------|
| Windows | `services.msc` → find "Twingate Service" → verify Running + Automatic startup |
| macOS | `log show --process Twingate --last 1h` |
| Linux | `sudo journalctl -u twingate --since "1 hour ago"` |

### 2. Verify Virtual Network Adapter
| Platform | Command | Expected |
|----------|---------|---------|
| Windows | `ipconfig \| findstr "Twingate"` | TAP-Windows Adapter present |
| macOS | `scutil --nc list` | Twingate network extension listed |
| Linux | `ip a` | Interface `sdwan0` present |

**Fix:** Missing adapter → reinstall Twingate Client

### 3. Check for Software Conflicts
Conflicting software categories:
- Other VPNs / ZTNA clients (routing table conflicts)
- Antivirus / EDR / Firewall with deep packet inspection
- OEM network optimization / traffic shaping tools

**Resolution process:**
1. Fully **uninstall** (not just disable) suspected software
2. Restart machine
3. Test Twingate
4. If resolved, reinstall other software with explicit exceptions for Twingate processes and `*.twingate.com`

### 4. Collect Client Logs
**Access via UI:** `More > Troubleshoot > View Logs`

| Platform | Log Location |
|----------|-------------|
| Windows | `%LOCALAPPDATA%\Twingate\logs\` — key files: `Twingate.log` (UI), `Twingate.Service.log` (service) |
| macOS | `~/Library/Group Containers/6GX8KVTR9H.com.twingate.com/Logs/private/var/log/twingate/` |

## Gotchas
- Windows Event Viewer (Application Log) needed if service fails to start entirely
- Security software drivers persist in network stack even when the application is "disabled"
- Empty resource list ≠ connectivity failure; check DNS separately

## Related Docs
- DNS troubleshooting (for resource-name-specific access failures)
- Client Logs reference