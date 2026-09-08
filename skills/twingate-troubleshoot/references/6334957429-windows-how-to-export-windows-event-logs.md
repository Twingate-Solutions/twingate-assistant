---
source: https://help.twingate.com/articles/6334957429-windows-how-to-export-windows-event-logs
type: help
fetched: 2026-09-06
source_version: 12b2638fecd0976da8dc311e41df46b3f6a431e41861e925eeee39894d50adf8
---

# [Windows] How To Export Windows Event Logs

## Summary
Describes how to export Windows Event Logs in `.evtx` format for Twingate Client troubleshooting. Both Application and System logs are typically required when diagnosing client startup or runtime issues.

## Key Information
- Export both **Application** and **System** event logs
- Files saved in `.evtx` format (Windows Event Log format)
- Logs are used to diagnose Twingate Client failures to start or run correctly

## Prerequisites
- Windows OS with Event Viewer access
- IT/Security team may need to grant access if restricted

## Step-by-Step

1. Press **Windows key** → type `Event` → open **Event Viewer**
2. Expand **Windows Logs** section (double-click)
3. Select **Application** log
4. Right panel → **Actions** → click **Save All Events As...**
5. Enter filename, confirm **Save as type** = `Event files (*.evtx)` → Save
6. Repeat steps 3–5 for the **System** log

## Configuration Values
- File format: `.evtx`
- Log sources required: `Application`, `System`

## Gotchas
- Log files can be large — zip/compress before sending to support
- Access to Event Viewer may be restricted by IT/Security policy in managed environments

## Related Docs
- Twingate Client troubleshooting (Windows platform)