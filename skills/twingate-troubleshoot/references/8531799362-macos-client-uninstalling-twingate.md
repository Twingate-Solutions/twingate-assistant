---
source: https://help.twingate.com/articles/8531799362-macos-client-uninstalling-twingate
type: help
fetched: 2026-09-06
source_version: c8dc39add02cf1692d740b285303fa516417252c5cfa4f070ac52bd9efc2abdd
---

# [macOS Client] Uninstalling Twingate

## Summary
Uninstalling the Twingate macOS client involves moving the app to Bin, which also removes the System Extension for Standalone Client installs. macOS 15.3+ has a bug requiring manual System Extension removal after app deletion.

## Key Information
- Quitting app + dragging to Bin is sufficient for most macOS versions
- Uninstalling Standalone Client automatically triggers System Extension removal prompt
- macOS 15.3+ has an Apple bug that orphans the System Extension even after apparent removal

## Prerequisites
- Admin username and password (required for manual System Extension removal on macOS 15.3+)
- Identify whether you're running the **Standalone Client** (includes System Extension) vs standard client

## Step-by-Step

### Standard Uninstall (all macOS versions)
1. Quit the Twingate application
2. Drag app to Bin **or** right-click → "Move to Bin"
3. If prompted about System Extension removal, click **Continue**

### Additional Steps for Standalone Client on macOS 15.3+
1. Complete standard uninstall above first
2. Navigate to: **System Settings → General → Login Items & Extensions**
3. Click the **ⓘ (information)** button next to "Network Extensions"
4. Click the **three dots (⋯)** next to Twingate
5. Select **"Delete Extension"**
6. Click **"Uninstall"**
7. Enter admin username and password to confirm

## Gotchas
- **macOS 15.3+ bug**: System Extension appears removed but is actually orphaned — manual deletion is required even if the standard uninstall seems to complete successfully
- This extra step only applies to the **Standalone Client** (the variant that includes a System Extension)
- Admin credentials are required for the manual extension removal step

## Related Docs
- Twingate macOS Client installation documentation
- Twingate Standalone Client documentation