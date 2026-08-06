---
source: https://help.twingate.com/articles/8531799362-macos-client-uninstalling-twingate
type: help
fetched: 2026-08-06
source_version: fc26c9838b9287d35eca836ee5d70f62684e2f00c8b9cf9802887656c611aef5
---

# [macOS Client] Uninstalling Twingate

## Summary
Uninstalling the Twingate macOS client is done by quitting and moving the app to Bin. The Standalone Client on macOS 15.3+ requires additional manual steps to remove an orphaned System Extension due to an Apple bug.

## Key Information
- Standard uninstall: quit app + drag to Bin (or right-click → Move to Bin)
- Standalone Client uninstall also removes the System Extension (click "Continue" when prompted)
- macOS 15.3+ has an Apple bug that orphans the System Extension after standard uninstall

## Prerequisites
- Admin username and password required for macOS 15.3+ System Extension removal
- Applies only to **Standalone Client** (not the App Store client)

## Step-by-Step

### Standard Uninstall (all macOS versions)
1. Quit the Twingate application
2. Drag app to Bin, or right-click → **Move to Bin**
3. If prompted about System Extension removal, click **Continue**

### Additional Steps for Standalone Client on macOS 15.3+
1. Navigate to: **System Settings → General → Login Items & Extensions**
2. Click the **ⓘ (information)** button next to **Network Extensions**
3. Click the **⋯ (three dots)** next to Twingate
4. Select **Delete Extension**
5. Click **Uninstall**
6. Enter admin username and password

## Gotchas
- macOS 15.3+ orphans the System Extension even though the UI appears to complete removal successfully — manual deletion is required
- Skipping the extra steps on 15.3+ leaves a residual Network Extension active in the system

## Related Docs
- Twingate macOS Client installation guides
- Standalone Client vs. App Store Client documentation