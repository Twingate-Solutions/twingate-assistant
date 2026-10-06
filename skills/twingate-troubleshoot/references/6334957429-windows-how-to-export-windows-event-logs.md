---
source: https://help.twingate.com/articles/6334957429-windows-how-to-export-windows-event-logs
type: help
fetched: 2026-10-04
source_version: 2868db75d6fa02c75384fa79ed230d76f677ea1c03f714eae04e8950ba931a81
trust: official
---

# [Windows] How To Export Windows Event Logs

## Summary
Describes how to export Windows Event Logs (Application and System logs) for Twingate Client troubleshooting. These logs help diagnose issues with the Twingate Client failing to start or run correctly.

## Key Information
- Two log types needed: **Application** and **System** event logs
- Export format: `.evtx` (Event files)
- Tool used: Windows built-in **Event Viewer**
- Compression recommended for large log files before sharing

## Prerequisites
- Access to Event Viewer application
- Permission to read/export event logs (may be restricted by IT/Security teams in some environments)

## Step-by-Step

1. Press **Windows key**, type `Event`, select **Event Viewer**
2. Double-click **Windows Logs** to expand the section
3. Highlight **Application** log
4. In the right-hand **Actions** panel, click **Save All Events As...**
5. Enter a filename; confirm **Save as type** is set to `Event files (*.evtx)`
6. Highlight **System** log and repeat steps 4–5

## Configuration Values
- Export file type: `*.evtx`
- Logs to export: `Windows Logs > Application`, `Windows Logs > System`

## Gotchas
- Access to Event Viewer may be blocked by IT/Security policy — confirm permissions before troubleshooting
- Large log files should be zipped before sending to support

## Related Docs
- Twingate Windows Client troubleshooting guides