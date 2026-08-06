---
source: https://help.twingate.com/articles/8458642629-twingate-client-logs
type: help
fetched: 2026-08-06
source_version: 7127371db64efb7629d6e480582db75f44afd4901efff51150634fbf056262d8
---

# Twingate Client Logs

## Summary
Guide for collecting Twingate Client diagnostic logs across all supported platforms. Detailed logging must be enabled before reproducing issues, as it is not retroactive. Logs can be uploaded directly via the client or collected manually.

## Key Information
- **Critical**: Enable "Collect Detailed Logs" before reproducing the issue — enabling is not retroactive
- Two collection methods for Windows/Mac: automated upload (preferred) or manual file retrieval
- Linux uses `sudo twingate report` to generate a ZIP bundle
- Mobile platforms use in-app "Share with Developer" flow
- Log uploads require an existing support ticket ID

## Prerequisites
- Active Twingate support ticket (get one at help.twingate.com → "Open a Support Request")
- Detailed logging enabled on the affected device
- Issue reproduced **after** enabling detailed logging

## Step-by-Step

### Windows/Mac — Upload (Preferred)
1. Click Twingate tray icon → **More > Troubleshoot**
2. Verify checkmark next to **Collect Detailed Logs** (enable if missing)
3. Reproduce the issue
4. **More > Troubleshoot > Upload Logs...**
5. Click **Create Ticket**, enter existing ticket ID, description → **Upload Logs**

### Windows — Manual
1. **More > Troubleshoot > View Logs**
2. Collect from: `%LOCALAPPDATA%\Twingate\logs\` and `%PROGRAMDATA%\Twingate\logs\`
3. Compress and attach to support ticket

### Mac — Manual
- **App Store client**: `~/Library/Group Containers/group.com.twingate/Logs/`
- **Standalone client**: `~/Library/Group Containers/6GX8KVTR9H.com.twingate.com/Logs/` and `/private/var/log/twingate/`

### Linux
```bash
sudo twingate config log-level debug
twingate stop && twingate start
# Reproduce issue, then:
sudo twingate report   # creates ZIP in current directory
```
Fallback log path (no journalctl): `/var/log/twingated.log`
Live log review: `sudo journalctl -u twingate --since "1 hour ago"`

### iOS
- Not logged in: Settings gear → **Share with Developer > Save to Files**
- Logged in: Profile image → **Share with Developer > Save to Files**
- Enable detailed logs: gear icon → **Collect Detailed Logs**

### Android/ChromeOS
- Burger menu (top left) → **Advanced > Share Logs with Developer**
- Enable detailed logs: **Advanced > Collect Detailed Logs**

## Configuration Values
| Platform | Command/Setting |
|----------|----------------|
| Linux log level | `sudo twingate config log-level debug` |
| Linux check config | `sudo twingate config` |
| Linux generate bundle | `sudo twingate report` |

## Gotchas
- Detailed logging is **not retroactive** — must reproduce issue after enabling
- Linux Client must be **restarted** after changing log level
- Upload portal is **unmonitored** — always reference an existing support ticket
- In containerized/headless Linux, `journalctl` may be unavailable; use `/var/log/twingated.log`

## Related Docs
- Twingate support portal: help.twingate.com