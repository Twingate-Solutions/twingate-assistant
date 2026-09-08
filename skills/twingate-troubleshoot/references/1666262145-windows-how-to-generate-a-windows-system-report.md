---
source: https://help.twingate.com/articles/1666262145-windows-how-to-generate-a-windows-system-report
type: help
fetched: 2026-09-06
source_version: d3c91127f0c4b0086aad9a437472b96edab7e6cc33b45b17558078df0ca4bbfd
---

# [Windows] How To Generate a Windows System Report

## Summary
Instructions for generating a Windows System Information report file using the built-in `msinfo32` tool. This report is typically requested by Twingate support alongside other diagnostic logs.

## Key Information
- Uses the native Windows System Information (`msinfo32`) utility
- Output is a `.nfo` file containing hardware, software, and system configuration details
- File can be compressed with other requested logs before submission

## Prerequisites
- Windows OS
- Access to Start menu

## Step-by-Step

1. Press the **Windows key** and type `sys`
2. Click **System Information** from the search results
3. Click **File** → **Save**
4. In the **Save As** dialog, choose a name and location (desktop recommended)
5. Compress the output file with any other requested logs and send to support

## Configuration Values
None — no CLI flags, environment variables, or API parameters involved.

## Gotchas
- The tool may take a moment to fully load before saving; saving too early may produce an incomplete report
- Default save format is `.nfo` — no need to change the file type

## Related Docs
- Twingate Windows client troubleshooting logs (typically requested alongside this report)