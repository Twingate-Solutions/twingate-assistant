---
source: https://www.twingate.com/docs/device-failures
type: docs
fetched: 2026-08-14
source_version: af78e8f69cfaa342fb5e258fa24b1162f9e4211754e67e80d1590f0e40125c9d
---

# Device Failures - Twingate Troubleshooting

## Summary
Covers diagnosis and resolution of Twingate Client application failures at the OS networking stack level. Addresses service/daemon issues, missing virtual network adapters, and software conflicts that prevent connectivity or Resource access.

## Key Information
- Client UI is a frontend only; background service does the actual work
- Virtual network adapter is required for traffic handling
- Software conflicts (other VPNs, AV/EDR, network optimizers) are a very common cause
- Empty Resource list while connected typically indicates a DNS issue, not a Client failure

## Common Symptoms
- Client UI stuck on "Disconnected" with unresponsive connect button
- Windows errors: `TapAdapterExistence` or "Twingate adapter is missing" in logs
- Connected but Resource list is empty

## Step-by-Step Troubleshooting

### 1. Check Background Service
| OS | Command/Method |
|----|---------------|
| Windows | `services.msc` → find "Twingate Service" → verify Running + Automatic startup; check Event Viewer Application Log for crashes |
| macOS | `log show --process Twingate --last 1h` |
| Linux | `sudo journalctl -u twingate --since "1 hour ago"` |

### 2. Verify Virtual Network Adapter
| OS | Command | Expected |
|----|---------|----------|
| Windows | `ipconfig \| findstr "Twingate"` | "Twingate TAP-Windows Adapter" present |
| macOS | `scutil --nc list` | Twingate network extension listed |
| Linux | `ip a` | Interface `sdwan0` present |

**Fix:** Reinstall Twingate Client if adapter is missing.

### 3. Identify Software Conflicts
Conflicting software categories:
- Other VPNs/ZTNA clients (routing table conflicts)
- Antivirus/EDR/Firewall with deep packet inspection
- OEM-installed network optimizers/traffic shapers

**Testing method:** Fully *uninstall* (not just disable) suspected software, restart machine, retest. Driver-level components remain active even when software is "disabled."

**Resolution:** If conflict confirmed, reinstall other software and add exceptions for Twingate processes and `*.twingate.com`.

### 4. Collect Client Logs
**Via UI:** More → Troubleshoot → View Logs

| OS | Log Location |
|----|-------------|
| Windows | `%LOCALAPPDATA%\Twingate\logs\` — key files: `Twingate.log` (UI), `Twingate.Service.log` (service) |
| macOS | `~/Library/Group Containers/6GX8KVTR9H.com.twingate.com/Logs/private/var/log/twingate/` |

## Gotchas
- Disabling AV/EDR is insufficient for conflict testing — kernel drivers remain loaded; full uninstall required
- Connected + empty Resource list = DNS problem, not Client failure (separate investigation path)
- Windows TAP adapter missing always requires Client reinstall

## Related Docs
- DNS troubleshooting (for empty Resource list when connected)
- Client logs analysis
- Software conflict exceptions configuration