---
source: https://help.twingate.com/articles/9450787885-macos-client-twingate-menu-bar-icon-not-visible
type: help
fetched: 2026-10-04
source_version: fd778f23f9f7379294a2e9eb3b888c8912c5ec9a059a2c492e5c11244526e1eb
trust: official
---

# [macOS Client] Twingate Icon Not Visible in Menu Bar

## Summary
On MacBook devices with a camera notch, menu bar icons are truncated when too many apps occupy the menu bar. The Twingate client may be running (visible in Activity Monitor) but its icon is hidden behind or beyond the notch area.

## Key Information
- **Affected devices:** MacBook models with camera notch in the top menu bar (e.g., MacBook Pro M1 Pro and later)
- **Root cause:** macOS truncates menu bar icons as they approach the camera notch
- **Confirmation:** Twingate process visible in Activity Monitor despite icon not appearing in menu bar
- **macOS 27+:** Includes native menu bar expansion to handle the notch natively (no workaround needed)

## Prerequisites
- Twingate macOS client installed and launched
- MacBook with camera notch in menu bar
- Multiple other menu bar icons present

## Workarounds (Pre-macOS 27)

1. **External monitor** — Connect a monitor without a notch; all menu bar icons including Twingate will display
2. **Third-party menu bar managers** — Use apps that collapse/expand menu bar icons to free up space (use at own discretion; Twingate does not endorse specific apps)
3. **Quit other menu bar apps** — Close other menu bar applications until the Twingate icon becomes visible

## Icon Reordering (Once Visible)
- Hold **Command (⌘)** + click and drag menu bar icons to reorder them
- Reorder to position Twingate icon away from the notch area to prevent future truncation

## Gotchas
- The Twingate client **is running** even when the icon is not visible — do not reinstall assuming a broken installation
- macOS 27 resolves this natively; no workaround needed on that version or later
- Third-party menu bar management apps are unsupported by Twingate

## Related Docs
- Twingate macOS Client documentation
- [Twingate Help Center](https://help.twingate.com)