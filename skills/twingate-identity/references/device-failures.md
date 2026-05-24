# Device Failures - Twingate Troubleshooting

## Page Title
Device Failures: How to Troubleshoot User Device Issues

## Summary
Covers diagnosing and resolving Twingate Client failures caused by service/daemon issues, missing virtual network adapters, or conflicts with third-party software. Applies to Windows, macOS, and Linux. DNS issues are out of scope here (handled separately).

## Common Symptoms
- Client UI stuck on "Disconnected" with unresponsive connect button
- Client fails to start; Windows logs show `TapAdapterExistence` errors or "Twingate adapter is missing"
- Client connected but Resource list is empty

## Diagnostic Steps

### 1. Check Background Service
| Platform | Command/Method |
|----------|---------------|
| Windows | `services.msc` → find "Twingate Service" → verify Running + Automatic startup |
| macOS | `log show --process Twingate --last 1h` |
| Linux | `sudo journalctl -u twingate --since "1 hour ago"` |

### 2. Verify Virtual Network Adapter
| Platform | Command | Expected |
|----------|---------|----------|
| Windows | `ipconfig \| findstr "Twingate"` | "Twingate TAP-Windows Adapter" present |
| macOS | `scutil --nc list` | Twingate network extension listed |
| Linux | `ip a` | Interface `sdwan0` present |

**Fix:** If adapter is missing → reinstall Twingate Client.

### 3. Check for Software Conflicts
Common conflict sources:
- **Other VPNs/ZTNA clients** – routing table contention
- **Antivirus/EDR/Firewall** – deep packet inspection blocking operations
- **OEM network optimizers** – traffic shaping interference

**Testing conflicts:** Fully *uninstall* (not just disable) suspected software, restart machine, retest. Drivers can remain active in network stack even when software is "disabled."

**Resolution if conflict confirmed:** Reinstall other software and add exceptions for Twingate processes and `*.twingate.com`.

### 4. Collect Client Logs
**Via UI:** `More > Troubleshoot > View Logs`

| Platform | Log Location |
|----------|-------------|
| Windows | `%LOCALAPPDATA%\Twingate\logs` |
| Windows key files | `Twingate.log` (UI), `Twingate.Service.log` (service) |
| macOS | `~/Library/Group Containers/6GX8KVTR9H.com.twingate.com/Logs/private/var/log/twingate/` |

## Gotchas
- Client UI is frontend only; actual connectivity is handled by background service — UI appearing healthy doesn't mean the service is healthy
- Disabling security software is insufficient for conflict testing; kernel-level drivers remain active
- Connected + empty Resource list is a different symptom than disconnected — check DNS docs
- If client is connected but a specific Resource is unreachable by name → DNS issue, not a device failure

## Related Docs
- DNS troubleshooting (for Resource-name resolution failures)
- Client Logs reference