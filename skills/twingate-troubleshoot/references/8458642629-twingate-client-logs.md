---
source: https://help.twingate.com/articles/8458642629-twingate-client-logs
type: help
fetched: 2026-11-01
source_version: 895c8446ddf68b6ab3cf45eaeffbba19437b1d7d3749aad2b764ca137fdd3d65
trust: official
---

# Twingate Client Logs

## Page Title
Twingate Client Logs

## Summary
Describes how to collect and upload Twingate Client diagnostic logs across Android, iOS, Linux, macOS, and Windows. Detailed logging must be enabled before reproducing an issue, as it is not retroactive. Logs are submitted via in-app upload or manual file retrieval attached to a support ticket.

## Key Information
- **Platforms:** Android, ChromeOS, iOS, Linux, macOS, Windows
- Detailed logging must be enabled **before** reproducing the issue
- Two primary collection methods: in-app upload (Windows/Mac preferred) or manual file retrieval
- All logs must be linked to an existing support ticket ID

## Prerequisites
- Active Twingate support ticket (create at help.twingate.com → "Open a Support Request")
- "Collect Detailed Logs" enabled on the client before reproducing the issue

## Step-by-Step

### Enable Detailed Logs
| Platform | Steps |
|---|---|
| macOS/Windows | System tray icon → More → Troubleshoot → Collect Detailed Logs (checkmark) |
| iOS | Gear icon → Enable Collect Detailed Logs |
| Android | Burger menu → Advanced → Enable Collect Detailed Logs |
| Linux | `sudo twingate config log-level debug`, then restart |

### Method 1: In-App Upload (Windows/Mac)
1. System tray icon → More → Troubleshoot → Upload Logs
2. Click **Create Ticket** to approve upload
3. Enter existing ticket ID, description → **Upload Logs**

### Method 2: Manual Retrieval (Windows/Mac)
1. System tray icon → More → Troubleshoot → View Logs
2. Compress and attach to support ticket

### Linux Log Collection
```bash
# Check current log level
sudo twingate config

# Enable debug logging
sudo twingate config log-level debug

# Restart client
twingate stop
twingate start

# Generate report bundle (ZIP saved to current directory)
sudo twingate report

# Live log review
sudo journalctl -u twingate --since "1 hour ago"
```

### Mobile
- **iOS (logged out):** Settings gear → Share with Developer → Save to Files → attach to ticket
- **iOS (logged in):** Profile image → Share with Developer → Save to Files → attach to ticket
- **Android/ChromeOS:** Burger menu → Advanced → Share Logs with Developer

## Configuration Values
| Parameter | Command | Value |
|---|---|---|
| Linux log level | `sudo twingate config log-level` | `debug` |

## Log File Locations
| Platform | Path |
|---|---|
| Windows | `%LOCALAPPDATA%\Twingate\logs\` and `%PROGRAMDATA%\Twingate\logs\` |
| macOS (App Store) | `~/Library/Group Containers/group.com.twingate/Logs/` |
| macOS (Standalone) | `~/Library/Group Containers/6GX8KVTR9H.com.twingate.com/Logs/` and `/private/var/log/twingate/` |
| Linux (no journalctl) | `/var/log/twingated.log` |

## Gotchas
- Detailed logging is **not retroactive** — must enable first, then reproduce the issue
- Linux: client must be **restarted** after changing log level
- Linux in containers/headless: `journalctl` may be unavailable; use `/var/log/twingated.log`
- Support ticket upload queue is **unmonitored** — always reference an active ticket ID

## Related Docs
- Twingate Help Center: help.twingate.com
- Linux CLI reference: `sudo twingate config` / `sudo twingate report`