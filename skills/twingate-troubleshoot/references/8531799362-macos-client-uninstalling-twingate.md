---
source: https://help.twingate.com/articles/8531799362-macos-client-uninstalling-twingate
type: help
fetched: 2026-10-18
source_version: 3267f98d2e7d7b53867fbf29d4216f83287499527fe97428cde4f48f593123dc
trust: official
---

# [macOS Client] Uninstalling Twingate

## Summary
Describes how to remove the Twingate macOS client. The process is a standard macOS application removal with no special tooling required. Standalone Client installations (which include a System Extension) prompt for confirmation during removal.

## Key Information
- No dedicated uninstaller required
- Two removal methods available: drag-to-Bin or right-click menu
- System Extension is automatically removed alongside the Standalone Client
- A confirmation prompt appears when removing the Standalone Client variant

## Prerequisites
- Twingate macOS client must be quit before removal

## Step-by-Step

### Method 1: Drag to Bin
1. Quit the Twingate application
2. Drag the Twingate app to the Bin

### Method 2: Right-click
1. Quit the Twingate application
2. Right-click the Twingate app
3. Select **Move to Bin**

### Standalone Client (System Extension)
- Follow either method above
- When prompted to remove the System Extension, click **Continue**

## Configuration Values
None applicable.

## Gotchas
- Must quit the app before attempting removal
- Standalone Client includes a System Extension; removal triggers an OS-level confirmation prompt — do not skip it or the extension may persist

## Related Docs
- macOS Client installation documentation
- System Extension configuration (for enterprise/MDM deployments)