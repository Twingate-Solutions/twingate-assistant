---
source: https://help.twingate.com/articles/9450787885-macos-client-twingate-menu-bar-icon-not-visible
type: help
fetched: 2026-11-19
source_version: b810b3eebd2ac23f5cab0b9a68d8658ddf5feef0da0f5c6a8bf4a25c16e57880
trust: official
---

# Page Title
[macOS Client] Twingate Icon Not Visible in Menu bar

## Summary
On MacBooks with a camera notch, menu bar icons that run into the notch are truncated and hidden. The Twingate Client may be running (visible in Activity Monitor) but its icon doesn't appear. The workarounds are to free up menu bar space, use an external display, or use a menu bar manager.

## Key Information
- **Applies to:** Twingate Client, macOS, MacBooks with a camera notch in the top menu bar.
- **Cause:** Too many menu bar icons approach the notch, so the overflow icons are truncated and hidden. This is a macOS display limitation, not a Twingate fault.
- **Symptom:** After launching the Client, no Twingate icon is in the menu bar, but Activity Monitor shows the Twingate process running.
- **Native fix:** The page says macOS 27 introduces native menu bar expansion to handle the notch.
- **Workarounds for earlier macOS versions:**
  1. Use an external monitor without a notch. All menu bar icons, including Twingate, display there.
  2. Use a third-party app that collapses and expands menu bar icons.
  3. Quit other menu bar apps until the Twingate icon appears.

## Prerequisites
- A notched MacBook with the Twingate Client installed and launched.
- Access to Activity Monitor to confirm the process is running.

## Step-by-Step (Diagnosis and Fix)
1. Launch the Twingate Client.
2. If no icon appears, open Activity Monitor and confirm the Twingate process is running.
3. Apply one of the workarounds above (external monitor, menu bar manager, or quitting other menu bar apps).
4. Once the Twingate icon appears, hold **Command** and drag icons to reorder them. Moving Twingate further from the notch helps keep it visible.

## Configuration Values
None. There are no env vars, CLI flags, or API parameters for this issue.

## Gotchas
- A missing icon doesn't mean the Client failed to launch. Check Activity Monitor before reinstalling.
- Twingate doesn't endorse any third-party menu bar manager. Their use is at the user's discretion.
- The native fix is only in the newer macOS release the page names (macOS 27). Earlier versions need a workaround.
- Reordering with Command+drag only works after the icon is visible, so you may need to quit other menu bar apps first.

## Related Docs
- Twingate Help Center: macOS Client troubleshooting articles
- Source: https://help.twingate.com/articles/9450787885-macos-client-twingate-menu-bar-icon-not-visible