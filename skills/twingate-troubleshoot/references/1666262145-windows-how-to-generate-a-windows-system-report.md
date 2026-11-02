---
source: https://help.twingate.com/articles/1666262145-windows-how-to-generate-a-windows-system-report
type: help
fetched: 2026-11-01
source_version: e05c29fbc5c014e008f446338f8223351c41f2463ed8f773d551501b2e57e33b
trust: official
---

# [Windows] How To Generate a Windows System Report

## Summary
Instructions for capturing a Windows System Information report using the built-in `msinfo32` tool. Used to collect system diagnostics when requested by Twingate support.

## Key Information
- Uses the native Windows System Information utility (`msinfo32`)
- Output is a `.nfo` file containing hardware, OS, and driver details
- Typically requested alongside other Twingate diagnostic logs

## Prerequisites
- Windows OS
- No admin rights required

## Step-by-Step

1. Press the **Windows key** and type `sys`
2. Click **System Information** from the search results
3. Click **File** → **Save**
4. Choose a filename and save location (desktop recommended)
5. Compress the `.nfo` file with any other requested logs before sending to support

## Gotchas
- The file can be large; compress it (zip) before sharing
- Combine with other requested logs (e.g., Twingate client logs) into a single archive for support tickets

## Related Docs
- Twingate client log collection (Windows)
- Twingate support ticket submission