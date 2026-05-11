# Device Failures - Twingate Troubleshooting

## Page Title
Device or Client Application Failures

## Summary
Covers troubleshooting Twingate Client failures caused by service/daemon issues, missing virtual network adapters, or software conflicts. Focuses on diagnosing why the Client UI is stuck, the Resource list is empty, or the Client fails to start entirely.

## Key Information
- Client UI is a front-end only; background service does the actual work
- Virtual network adapter is required for traffic handling
- Software conflicts (VPNs, EDR, AV) are a very common root cause
- DNS issues are likely if Client appears healthy but a specific Resource is unreachable

## Common Symptoms
- Client UI stuck on "Disconnected" with unresponsive connect button
- Windows log errors: `TapAdapterExistence` or "Twingate adapter is missing"
- Connected but Resource list is empty

## Diagnostics by Platform

### Check Service Status
| Platform | Command |
|----------|---------|
| Windows | `services.msc` → find "Twingate Service" → verify Running + Automatic |
| macOS | `log show --process Twingate --last 1h` |
| Linux | `sudo journalctl -u twingate --since "1 hour ago"` |

### Verify Virtual Network Adapter
| Platform | Command | Expected |
|----------|---------|----------|
| Windows | `ipconfig \| findstr "Twingate"` | "Twingate TAP-Windows Adapter" present |
| macOS | `scutil --nc list` | Twingate network extension listed |
| Linux | `ip a` | Interface `sdwan0` present |

## Log Locations
- **UI access:** Client → More → Troubleshoot → View Logs
- **Windows:** `%LOCALAPPDATA%\Twingate\logs\`
  - `Twingate.log` (UI)
  - `Twingate.Service.log` (service)
- **macOS:** `~/Library/Group Containers/6GX8KVTR9H.com.twingate.com/Logs/private/var/log/twingate/`

## Gotchas
- Simply "disabling" security software is insufficient—drivers may remain active in network stack; **uninstall** to properly test conflicts
- Missing TAP adapter on Windows requires Client reinstall to resolve
- Missing `sdwan0` on Linux also typically requires reinstall
- If Client looks healthy but one Resource fails → check DNS, not the Client itself
- Conflicts domain for exceptions: `*.twingate.com`

## Software Conflict Sources
- Other VPN/ZTNA clients (routing table conflicts)
- Antivirus/EDR with deep packet inspection
- OEM pre-installed network optimizer/traffic shaping software

## Conflict Resolution Steps
1. Temporarily **uninstall** (not disable) suspected software
2. Restart machine
3. Test Twingate
4. If resolved, reinstall other software with explicit exceptions for Twingate processes and `*.twingate.com`

## Related Docs
- DNS troubleshooting (referenced for Resource-specific access failures)
- Client Logs documentation