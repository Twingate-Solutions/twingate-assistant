---
source: https://help.twingate.com/articles/1666262145-windows-how-to-generate-a-windows-system-report
type: help
fetched: 2026-10-04
source_version: 9fface5dd9f2e815fff5d8c9930fcc0f4eed9238f4a2823dcd679e66c8331c09
trust: official
---

# [Windows] How To Generate a Windows System Report

## Summary
Instructions for capturing a Windows System Information report using the built-in `msinfo32` tool. Used to provide system diagnostics when troubleshooting Twingate issues on Windows.

## Key Information
- Uses the native Windows System Information utility (`msinfo32`)
- Produces a `.nfo` file containing detailed hardware/software/OS info
- Typically requested alongside other Twingate logs by support

## Prerequisites
- Windows OS
- No admin rights required

## Step-by-Step

1. Press the **Windows key** and type `sys`
2. Click **System Information** from the search results
3. Click **File → Save** to open the Save As dialog
4. Choose a filename and location (desktop recommended)
5. Compress the `.nfo` file with any other requested logs before sending

## Gotchas
- The file can be large; compress it before attaching to a support ticket
- Ensure you save (not export) — "Save" produces a single `.nfo` file; "Export" produces a `.txt` file with less detail

## Related Docs
- Twingate Windows client logs (check Twingate Help Center for companion log collection steps)