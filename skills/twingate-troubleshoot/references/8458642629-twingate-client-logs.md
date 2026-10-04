---
source: https://help.twingate.com/articles/8458642629-twingate-client-logs
type: help
fetched: 2026-10-04
source_version: 7f610e0fbcb10e8479c38bd17df9d2116084c57536b87e521419c3b61b466373
trust: official
---

# Twingate Client Logs

## Page Title
Twingate Client Logs

## Summary
Instructions for collecting and uploading Twingate Client diagnostic logs across Android, iOS, Linux, macOS, and Windows. Detailed logging must be enabled **before** reproducing an issue, as it is not retroactive. Logs can be uploaded automatically (Windows/Mac preferred) or retrieved manually.

---

## Key Information
- Detailed logs must be enabled first, then the issue reproduced, before collecting logs
- Three collection methods: Client upload UI, manual file retrieval, or CLI (Linux)
- Logs must be linked to an existing support ticket ID

---

## Prerequisites
- Active Twingate support ticket (create at help.twingate.com → "Open a Support Request")
- "Collect Detailed Logs" enabled on the client before reproducing the issue

---

## Step-by-Step by Platform

### macOS / Windows — Enable Detailed Logs
1. Click Twingate system tray icon → **More > Troubleshoot**
2. Verify checkmark next to **Collect Detailed Logs**

### macOS / Windows — Method 1: Upload (Preferred)
1. **More > Troubleshoot > Upload Logs...**
2. Click **Create Ticket** at prompt
3. Enter existing ticket ID, description → **Upload Logs**

### macOS / Windows — Method 2: Manual Retrieval
- **Windows log paths:**
  - `%LOCALAPPDATA%\Twingate\logs\`
  - `%PROGRAMDATA%\Twingate\logs\`
- **macOS App Store log path:** `~/Library/Group Containers/group.com.twingate/Logs/`
- **macOS Standalone log paths:**
  - `~/Library/Group Containers/6GX8KVTR9H.com.twingate.com/Logs/`
  - `/private/var/log/twingate/`
- Compress and attach to support ticket

### Linux
1. Check log level: `sudo twingate config`
2. Enable debug: `sudo twingate config log-level debug`
3. Restart client: `twingate stop` then `twingate start`
4. Reproduce the issue
5. Generate log bundle: `sudo twingate report` (saves ZIP to current directory)
6. If `journalctl` unavailable (containers/headless): retrieve `/var/log/twingated.log`
7. Live log review: `sudo journalctl -u twingate --since "1 hour ago"`

### iOS
- **Not logged in:** Settings gear → **Share with Developer > Save to Files**
- **Logged in:** Profile image → **Share with Developer > Save to Files**
- Enable detailed logs: gear icon → **Collect Detailed Logs**

### Android / ChromeOS
- Burger menu (top left) → **Advanced > Share Logs with Developer**
- Enable detailed logs: burger menu → **Advanced > Collect Detailed Logs**

---

## Configuration Values
| Setting | CLI Command |
|---|---|
| Check log level | `sudo twingate config` |
| Set debug logging | `sudo twingate config log-level debug` |
| Generate report bundle | `sudo twingate report` |

---

## Gotchas
- Detailed logging is **not retroactive** — must enable before reproducing the issue
- Support ticket queue is **unmonitored**; always reference an active ticket ID
- In containerized/headless Linux, `journalctl` may be absent; use `/var/log/twingated.log`
- Client restart required after changing Linux log level

---

## Related Docs
- Twingate Help Center: help.twingate.com
- Support requests: help.twingate.com → "Open a Support Request"