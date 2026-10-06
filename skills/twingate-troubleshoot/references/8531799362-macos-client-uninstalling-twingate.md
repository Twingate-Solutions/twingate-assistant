---
source: https://help.twingate.com/articles/8531799362-macos-client-uninstalling-twingate
type: help
fetched: 2026-10-04
source_version: bd7b8ee596d00b4c8a5defc2fe6b11487a5c285561c185294eb67d1106984a07
trust: official
---

# [macOS Client] Uninstalling Twingate

## Summary
Describes how to uninstall the Twingate macOS client. The process is standard macOS app removal. Standalone Client installations (which include a System Extension) require one additional confirmation step.

## Key Information
- Quit the app before removing it
- Drag app to Bin **or** right-click → "Move to Bin"
- Standalone Client variant includes a System Extension; uninstalling the app also removes the extension
- A prompt appears during Standalone Client removal — click **Continue** to confirm extension removal

## Step-by-Step

1. Quit the Twingate application (menu bar icon → Quit)
2. Open Finder and locate Twingate in `/Applications`
3. Drag to Bin **or** right-click → **Move to Bin**
4. *(Standalone Client only)* When prompted about the System Extension, click **Continue**

## Gotchas
- Must quit the app first; removing while running may leave processes active
- Standalone Client users will see a System Extension removal prompt — this is expected and required to complete uninstallation
- Standard drag-to-Bin does not require a separate uninstaller tool

## Related Docs
- macOS Client installation guide
- Twingate System Extension documentation