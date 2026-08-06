---
source: https://help.twingate.com/articles/1666262145-windows-how-to-generate-a-windows-system-report
type: help
fetched: 2026-08-06
source_version: b2c362efb8358bfa5f5757c3ee6ec7a70f00d5b66c51ead092e09822b19755cb
---

# [Windows] How To Generate a Windows System Report

## Summary
Instructions for generating a Windows System Information report using the built-in `msinfo32` tool. The output file is used for diagnostic purposes when troubleshooting Twingate on Windows.

## Key Information
- Uses Microsoft's built-in System Information tool (`msinfo32`)
- Produces a `.nfo` file containing system configuration details
- Typically requested alongside other Twingate diagnostic logs

## Prerequisites
- Windows OS
- Access to Start menu

## Step-by-Step

1. Press the **Windows key** and type `sys`
2. Click **System Information** app from search results
3. Click **File** → **Save**
4. In the **Save As** dialog, choose a name and location (desktop recommended)
5. Compress the `.nfo` file with any other requested logs before submitting

## Configuration Values
None applicable.

## Gotchas
- Save may take a moment to complete as it collects full system info
- Typically submitted alongside other logs (e.g., Twingate client logs) — collect all requested files before compressing

## Related Docs
- Twingate Windows client troubleshooting guides
- Log collection procedures for Windows