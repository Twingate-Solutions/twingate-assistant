---
source: https://help.twingate.com/articles/6334957429-windows-how-to-export-windows-event-logs
type: help
fetched: 2026-11-01
source_version: 978856bc178db4bb8958b62caa06141778157063b0242fcfe8ae17aa9f840a42
trust: official
---

# [Windows] How To Export Windows Event Logs

## Summary
Describes how to view and export Windows Event Logs for troubleshooting Twingate Client startup or runtime issues. Both Application and System logs are needed. Files are exported in `.evtx` format via the Event Viewer GUI.

## Key Information
- Two logs required: **Application** and **System** event logs
- Export format: `.evtx` (Event files)
- Access may be restricted by IT/Security teams in managed environments
- Large logs should be compressed (zip) before sharing

## Prerequisites
- Windows OS with Event Viewer access
- Permissions to read and export event logs (may require IT approval)

## Step-by-Step

1. Press **Windows key**, type `Event`, select **Event Viewer**
2. Double-click **Windows Logs** to expand the section
3. Highlight **Application** log
4. In the right-hand **Actions** panel, click **Save All Events As...**
5. Enter a filename; confirm **Save as type** is set to `Event files (*.evtx)`
6. Click Save
7. Repeat steps 3–6 for the **System** log

## Configuration Values
- Save as type: `Event files (*.evtx)`
- Logs to export: `Application`, `System`

## Gotchas
- Access to Event Viewer logs may be restricted in enterprise/managed environments — check with IT before attempting
- Log files can be large; zip before sending to Twingate support
- Both Application and System logs are typically needed — exporting only one may be insufficient for diagnosis

## Related Docs
- Twingate Client troubleshooting (Windows)
- Twingate support ticket submission