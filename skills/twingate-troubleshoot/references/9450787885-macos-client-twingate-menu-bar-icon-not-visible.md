---
source: https://help.twingate.com/articles/9450787885-macos-client-twingate-menu-bar-icon-not-visible
type: help
fetched: 2026-10-11
source_version: 4dd559f9b40657e8b9e10a5fde0ee8ca053393e2cedfa9a0f2afa89411d66b76
trust: official
---

# [macOS Client] Twingate Menu Bar Icon Not Visible

## Summary
On MacBooks with a camera notch, the menu bar truncates icons when too many apps occupy the menu bar area, causing the Twingate icon to disappear. The Twingate client is still running (verifiable via Activity Monitor) — this is purely a display issue.

## Key Information
- **Affected devices:** MacBooks with camera notch (e.g., MacBook Pro M1 Pro and similar)
- **Symptom:** Twingate icon missing from menu bar, but `Activity Monitor` shows Twingate process is running
- **Root cause:** macOS truncates menu bar icons that would overlap the notch area
- **macOS 26+:** Native menu bar expansion handles the notch — no workaround needed

## Prerequisites
- Twingate macOS client installed and launched
- Affected only on notched MacBook displays running macOS versions prior to macOS 26

## Workarounds (pre-macOS 26)

1. **Use an external monitor** — Connect a display without a notch; all menu bar icons become visible including Twingate
2. **Use a third-party menu bar manager** — Apps that collapse/expand menu bar icons can surface hidden icons (use at your own discretion; Twingate does not endorse specific tools)
3. **Quit other menu bar apps** — Close non-essential menu bar applications until the Twingate icon appears

## Icon Reordering (Once Visible)
- Hold **Command (⌘)** + click and drag menu bar icons to reorder them, bringing Twingate closer to the visible area

## Gotchas
- Twingate is **functional even when the icon is hidden** — absence from menu bar does not mean the client is disconnected or broken
- Reordering icons persists after the fix, so moving Twingate leftward reduces future truncation risk
- Third-party menu bar managers are not officially supported or endorsed by Twingate

## Related Docs
- Twingate macOS Client documentation
- [Twingate Help Center](https://help.twingate.com)