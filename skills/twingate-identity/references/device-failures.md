# Device Failures - Twingate Troubleshooting

## Summary
Covers diagnosis and resolution of Twingate Client failures caused by service/daemon issues, missing virtual network adapters, or conflicts with third-party software. Applies when the Client UI is stuck, won't start, or shows an empty Resource list.

## Common Symptoms
- Client UI stuck on "Disconnected" with unresponsive connect button
- Windows errors: `TapAdapterExistence` or "Twingate adapter is missing" in logs
- Client connects but Resource list is empty

## Troubleshooting Steps

### 1. Check Background Service
| OS | Command/Action |
|---|---|
| Windows | `services.msc` → find "Twingate Service" → verify Running + Automatic startup |
| macOS | `log show --process Twingate --last 1h` |
| Linux | `sudo journalctl -u twingate --since "1 hour ago"` |

### 2. Verify Virtual Network Adapter
| OS | Command | Expected |
|---|---|---|
| Windows | `ipconfig \| findstr "Twingate"` | "Twingate TAP-Windows Adapter" present |
| macOS | `scutil --nc list` | Twingate network extension listed |
| Linux | `ip a` | Interface named `sdwan0` present |

**Fix:** If adapter missing → reinstall Twingate Client.

### 3. Identify Software Conflicts
Common conflict sources:
- **Other VPNs/ZTNA clients** – routing table ownership conflicts
- **Antivirus/EDR/Firewall** – deep packet inspection blocks Twingate operations
- **OEM network optimizers** – traffic shaping interferes with routing

**Testing conflicts:** Fully *uninstall* (not just disable) suspected software, restart machine, retest. Drivers may remain active even when software is "disabled."

**If conflict confirmed:** Reinstall other software with exceptions for:
- Twingate processes
- Domain: `*.twingate.com`

### 4. Collect Client Logs
Access via: **More → Troubleshoot → View Logs**

| OS | Log Location |
|---|---|
| Windows | `%LOCALAPPDATA%\Twingate\logs\` |
| Windows files | `Twingate.log` (UI), `Twingate.Service.log` (service) |
| macOS | `~/Library/Group Containers/6GX8KVTR9H.com.twingate.com/Logs/private/var/log/twingate/` |

## Gotchas
- The Client UI is only a front-end; the background service does the actual work — always check service status first
- "Disabling" security software is insufficient for conflict testing; drivers remain in the network stack
- If Client appears healthy but a specific Resource is unreachable by name → issue is DNS, not device failure (separate troubleshooting path)
- Windows requires the TAP adapter specifically; its absence prevents service startup entirely

## Related Docs
- DNS troubleshooting (referenced for Resource name resolution failures)
- Client Logs guide