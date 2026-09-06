---
source: https://help.twingate.com/articles/8458642629-twingate-client-logs
type: help
fetched: 2026-09-06
source_version: 2744ff54aff83e0f47a5a60e650123d9e277b6d3ac97236c7397eed302ae68e9
---

# Twingate Client Logs

## Summary
Guidance for collecting Twingate Client diagnostic logs across all supported platforms (Android, iOS, Linux, macOS, Windows). Detailed logging must be enabled before reproducing issues, as it is not retroactive. Logs are submitted to support via upload or manual file attachment.

## Key Information
- **Detailed logging must be enabled first**, then issue reproduced, then logs collected
- Two collection methods for Windows/Mac: automated upload or manual file retrieval
- Linux uses `sudo twingate report` to generate ZIP bundle
- Mobile platforms share logs directly from within the app

## Prerequisites
- Active Twingate support ticket (required for log upload method)
- "Collect Detailed Logs" enabled before reproducing the issue
- Linux: debug log level set and client restarted before reproducing issue

## Step-by-Step

### Enable Detailed Logs
| Platform | Steps |
|----------|-------|
| macOS/Windows | Twingate tray icon → More → Troubleshoot → Collect Detailed Logs (verify checkmark) |
| iOS | Gear icon → Enable Collect Detailed Logs |
| Android | Burger menu → Advanced → Enable Collect Detailed Logs |
| Linux | `sudo twingate config log-level debug` → `twingate stop` → `twingate start` |

### Collect Logs

**Windows/Mac (Upload):** Tray icon → More → Troubleshoot → Upload Logs → Create Ticket → enter ticket ID → Upload Logs

**Windows (Manual):**
- `%LOCALAPPDATA%\Twingate\logs\`
- `%PROGRAMDATA%\Twingate\logs\`

**Mac (Manual):**
- App Store: `~/Library/Group Containers/group.com.twingate/Logs/`
- Standalone: `~/Library/Group Containers/6GX8KVTR9H.com.twingate.com/Logs/` and `/private/var/log/twingate/`

**Linux:**
```bash
sudo twingate config log-level debug
twingate stop && twingate start
# Reproduce issue, then:
sudo twingate report   # generates ZIP in current directory
# If no journalctl: /var/log/twingated.log
```

**Live Linux log review:**
```bash
sudo journalctl -u twingate --since "1 hour ago"
```

**iOS:** App → (Settings gear or Profile image) → Share with Developer → Save to Files → attach to ticket

**Android/ChromeOS:** Burger menu → Advanced → Share Logs with Developer

## Configuration Values
| Parameter | Command |
|-----------|---------|
| Check log level | `sudo twingate config` |
| Set debug logging | `sudo twingate config log-level debug` |
| Generate log bundle | `sudo twingate report` |

## Gotchas
- Enabling detailed logs is **not retroactive** — must reproduce the issue after enabling
- Linux client must be **restarted** after changing log level
- Upload method requires an existing support ticket ID; queue is unmonitored
- In containerized/headless Linux environments without `journalctl`, use `/var/log/twingated.log`

## Related Docs
- Twingate Support: [help.twingate.com](https://help.twingate.com) → Open a Support Request