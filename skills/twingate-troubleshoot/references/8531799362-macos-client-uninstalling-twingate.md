---
source: https://help.twingate.com/articles/8531799362-macos-client-uninstalling-twingate
type: help
fetched: 2026-09-20
source_version: c3367afea995eec738ac78163e223782841005755e79b5954c80b9627fa72614
---

# [macOS Client] Uninstalling Twingate

## Summary
Instructions for removing the Twingate macOS client application. The process is a standard macOS uninstall via Finder. Standalone Client installations that include a System Extension handle extension removal automatically during uninstall.

## Key Information
- Standard drag-to-Bin uninstall removes the application completely
- Right-click → "Move to Bin" is an equivalent alternative method
- Standalone Client (with System Extension) removes the System Extension as part of the same uninstall process
- A confirmation prompt ("Continue") appears when removing the System Extension variant

## Prerequisites
- Twingate macOS client must be quit before dragging to Bin

## Step-by-Step

1. Quit the Twingate application
2. Locate Twingate in `/Applications`
3. Drag to Bin **or** right-click → select "Move to Bin"
4. If uninstalling the Standalone Client: when prompted, click **Continue** to confirm System Extension removal

## Gotchas
- If using the Standalone Client with System Extension, expect a system prompt — must click "Continue" to complete removal
- No mention of residual files (preferences, logs, caches) being removed; manual cleanup of `~/Library/` directories may be needed if a clean removal is required
- No MDM/enterprise silent uninstall instructions provided on this page

## Configuration Values
None applicable.

## Related Docs
- Twingate macOS Client installation guide
- System Extension configuration (for managed/enterprise deployments)