# Device Failures - Twingate Troubleshooting

## Summary
Covers diagnosis and resolution of Twingate Client failures caused by service/daemon state, missing virtual network adapters, and software conflicts. Applies when the Client UI is unresponsive, won't start, or shows an empty resource list.

## Key Information
- Client UI is a front-end only; background service does the actual work
- Virtual network adapter is required for traffic handling (per-OS interface name varies)
- Software conflicts are a very common root cause
- DNS issues (not covered here) are the likely cause when Client is healthy but a specific Resource is unreachable by name

## Common Symptoms
- Client stuck on "Disconnected" with unresponsive connect button
- Windows logs show `TapAdapterExistence` errors or "Twingate adapter is missing"
- Client connected but Resource list is empty

## Diagnostic Steps

### 1. Check Background Service
| OS | Command/Action |
|----|----------------|
| Windows | `services.msc` → find "Twingate Service" → verify Running + Automatic startup; check Event Viewer (Application Log) on failure |
| macOS | `log show --process Twingate --last 1h` |
| Linux | `sudo journalctl -u twingate --since "1 hour ago"` |

### 2. Verify Virtual Network Adapter
| OS | Command | Expected |
|----|---------|----------|
| Windows | `ipconfig \| findstr "Twingate"` | "Twingate TAP-Windows Adapter" present |
| macOS | `scutil --nc list` | Twingate network extension listed |
| Linux | `ip a` | Interface named `sdwan0` present |

**Fix:** Reinstall the Twingate Client if adapter is missing or disabled.

### 3. Identify Software Conflicts
Conflicting software categories:
- Other VPN/ZTNA clients (routing table conflicts)
- Antivirus/EDR/Firewall with deep packet inspection
- OEM network optimizer/traffic shaping tools

**Conflict test:** Fully **uninstall** (not just disable) suspected software, restart machine, retest. Driver-level components remain active even when the app is "disabled."

**Resolution if confirmed:** Reinstall other software and whitelist:
- Twingate processes
- Domain: `*.twingate.com`

### 4. Collect Client Logs
Access via Client UI: **More → Troubleshoot → View Logs**

| OS | Log Location |
|----|-------------|
| Windows | `%LOCALAPPDATA%\Twingate\logs\` → `Twingate.log` (UI), `Twingate.Service.log` (service) |
| macOS | `~/Library/Group Containers/6GX8KVTR9H.com.twingate.com/Logs/private/var/log/twingate/` |

## Gotchas
- Disabling security software is insufficient for conflict testing—kernel/network drivers remain loaded until uninstall + reboot
- Empty Resource list ≠ connectivity failure; check service health separately
- Resource unreachable by name when Client is healthy → DNS issue, not covered by this doc
- Linux uses `systemd`-based service management; non-systemd distros not addressed

## Related Docs
- DNS troubleshooting (for name resolution failures on specific Resources)
- Client logs documentation
- Software conflict exceptions configuration