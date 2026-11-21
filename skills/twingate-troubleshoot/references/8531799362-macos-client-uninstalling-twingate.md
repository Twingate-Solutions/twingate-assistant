---
source: https://help.twingate.com/articles/8531799362-macos-client-uninstalling-twingate
type: help
fetched: 2026-11-19
source_version: f7e6deaa9c5c2202a9ef7987a514eb1ee9349ab99dc0b8d7eaa0d05ff22ffd6f
trust: official
---

# Page Title
[macOS Client] Uninstalling Twingate

## Summary
Describes how to remove the Twingate macOS Client by quitting the app and moving it to the Bin. For the Standalone Client, which includes a System Extension, uninstalling also removes the extension after a confirmation prompt.

## Key Information
- Uninstall is a simple drag-to-Bin operation. No separate uninstaller is mentioned.
- Two equivalent methods:
  - Drag the application to the Bin.
  - Right-click the application and select **Move to Bin**.
- The Standalone Client bundles a System Extension. Removing the app also removes the extension.
- During Standalone Client removal, a prompt appears. Click **Continue** to proceed.
- Page last updated roughly 2 months before the scrape.

## Prerequisites
- Twingate macOS Client is installed.
- The application must be quit before removal.
- Permission to approve the System Extension removal prompt (Standalone Client only).

## Step-by-Step
1. Quit the Twingate application.
2. Open the Applications folder (or wherever the app is located).
3. Either drag Twingate to the Bin, or right-click it and choose **Move to Bin**.
4. If using the Standalone Client, click **Continue** when prompted to remove the System Extension.

## Configuration Values
None. No environment variables, CLI flags, or API parameters are documented for this process.

## Gotchas
- Quit the app first, or removal may not complete cleanly.
- The System Extension prompt appears only for the Standalone Client. Declining or dismissing it may leave the extension installed.
- The page does not cover removal of leftover configuration, logs, or preferences. It also does not cover removing the device from the Twingate Admin Console. Verify these separately if a full cleanup is required.
- The page does not describe MDM-based or scripted uninstall.

## Related Docs
- Other Twingate macOS Client articles on help.twingate.com (installation, Standalone vs. App Store client, System Extension setup)
- Source: https://help.twingate.com/articles/8531799362-macos-client-uninstalling-twingate