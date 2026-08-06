---
source: https://help.twingate.com/articles/6334957429-windows-how-to-export-windows-event-logs
type: help
fetched: 2026-08-06
source_version: 5e0c3387450d57561e2b83fb4e6ff3c9162439bc22562e1063584dc772d3b8fd
---

# [Windows] How To Export Windows Event Logs

## Summary
Explains how to export Windows Event Logs for Twingate Client troubleshooting. Two logs are needed: Application and System. Files are saved in `.evtx` format via Event Viewer.

## Key Information
- Export both **Application** and **System** event logs
- Output format: `.evtx` (Event files)
- Used when Twingate Client fails to start or run correctly
- Compress exported files with zip before sending if logs are large

## Prerequisites
- Windows OS with Event Viewer access
- IT/Security team may restrict access in managed environments

## Step-by-Step

1. Press **Windows key** → type `Event` → open **Event Viewer**
2. Expand **Windows Logs** section (double-click)
3. Select **Application** log
4. Right panel → **Actions** → click **Save All Events As...**
5. Enter filename, confirm **Save as type** = `Event files (*.evtx)` → Save
6. Select **System** log → repeat steps 4–5

## Configuration Values
| Field | Value |
|-------|-------|
| Save as type | `Event files (*.evtx)` |
| Logs to export | `Application`, `System` |

## Gotchas
- Access to Event Viewer may be restricted by IT/Security policy — verify permissions before attempting
- Large log files should be zipped before sharing
- Both Application **and** System logs are required, not just one

## Related Docs
- Twingate Windows Client troubleshooting guides
- Windows Event Viewer documentation (Microsoft)