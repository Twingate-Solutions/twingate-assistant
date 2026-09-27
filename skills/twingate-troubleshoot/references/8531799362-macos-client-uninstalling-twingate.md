---
source: https://help.twingate.com/articles/8531799362-macos-client-uninstalling-twingate
type: help
fetched: 2026-09-27
source_version: a20694342afec4fb812c7bf7abb19715bfb69874078cd6a71c2f6b7f8261cab5
---

# [macOS Client] Uninstalling Twingate

## Summary
Instructions for removing the Twingate macOS client. Two removal methods are supported: drag-to-Bin or right-click menu. System Extension variants prompt for additional confirmation during removal.

## Key Information
- Quit the application before uninstalling
- Two methods: drag to Bin, or right-click → "Move to Bin"
- Standalone Client (includes System Extension) removes the System Extension as part of uninstall
- System Extension removal triggers a confirmation prompt — click "Continue" to proceed

## Step-by-Step

### Method 1: Drag to Bin
1. Quit Twingate from the menu bar
2. Open Applications folder
3. Drag Twingate to the Bin

### Method 2: Right-Click
1. Quit Twingate from the menu bar
2. Right-click Twingate in Applications
3. Select "Move to Bin"

### If Using Standalone Client (System Extension)
- During uninstall, a system prompt will appear
- Click **Continue** to confirm System Extension removal

## Gotchas
- Must quit the app before dragging to Bin to avoid incomplete removal
- Standalone Client users must respond to the System Extension prompt — dismissing it may leave the extension installed
- No mention of config file or credential cleanup; manual removal of `~/Library` artifacts may be needed if reinstalling cleanly

## Related Docs
- macOS Client installation guide
- Twingate System Extension documentation