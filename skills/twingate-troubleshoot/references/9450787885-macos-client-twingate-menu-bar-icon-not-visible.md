---
source: https://help.twingate.com/articles/9450787885-macos-client-twingate-menu-bar-icon-not-visible
type: help
fetched: 2026-09-27
source_version: 0e32f5443112fad0f86fc8e5cf731d688eb5dc46175d135c4cac6f1e551e3e9b
---

# [macOS Client] Twingate Icon Not Visible in Menu Bar

## Summary
On MacBook devices with a camera notch, menu bar icons get truncated when too many applications occupy the menu bar. The Twingate client runs normally but its icon is hidden behind the notch area.

## Key Information
- **Affected devices**: MacBooks with camera notch (e.g., MacBook Pro M1 Pro and later)
- **Symptom**: Twingate icon missing from menu bar, but process confirmed running in Activity Monitor
- **Root cause**: macOS truncates menu bar icons that approach the notch area
- **macOS 27+**: Introduces native menu bar expansion to handle the notch — no workaround needed

## Prerequisites
- Twingate macOS client installed and launched
- Activity Monitor available to verify process is running

## Verification Step
Confirm Twingate is running (not crashed) before troubleshooting:
1. Open **Activity Monitor**
2. Search for "Twingate"
3. Confirm process is listed as running

## Workarounds (Pre-macOS 27)

1. **External monitor** — Connect a monitor without a notch; all menu bar icons will display fully
2. **Third-party menu bar managers** — Tools that collapse/expand menu bar icons can surface hidden icons (use at own discretion; Twingate does not endorse specific apps)
3. **Quit other menu bar apps** — Close other menu bar applications until the Twingate icon appears
   - Once visible, hold **Command** + click and **drag** to reorder icons to a preferred position

## Gotchas
- The Twingate client is functional even when the icon is not visible — connectivity may still work
- Icon reordering (Command + drag) only possible once the icon is visible
- Third-party app recommendation is unofficial; compatibility and security are user's responsibility
- macOS 27 fix is version-specific — earlier macOS versions require manual workarounds

## Related Docs
- Twingate macOS Client documentation
- macOS Activity Monitor usage