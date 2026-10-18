---
source: https://help.twingate.com/articles/9450787885-macos-client-twingate-menu-bar-icon-not-visible
type: help
fetched: 2026-10-18
source_version: 5973f31221d4babcb44291c01cb46037a00cd78e580deee317e14c083988acdb
trust: official
---

# [macOS Client] Twingate Menu Bar Icon Not Visible

## Summary
On MacBook devices with a camera notch, the menu bar truncates icons when too many applications occupy the menu bar. The Twingate client may be hidden behind the notch area despite running normally, as confirmed by Activity Monitor.

## Key Information
- **Affected devices**: MacBook models with a camera notch in the menu bar (e.g., MacBook Pro M1 Pro and later)
- **Root cause**: macOS truncates menu bar icons when they approach the notch — not a Twingate bug
- **Confirmation**: Twingate process visible in Activity Monitor even when icon is absent from menu bar
- macOS 27 introduces native notch-aware menu bar expansion (resolves the issue natively)

## Prerequisites
- Twingate macOS client installed and running
- MacBook with camera notch in menu bar
- Multiple third-party menu bar apps active

## Workarounds (Pre-macOS 27)

1. **External monitor**: Connect a monitor without a notch — all menu bar icons display fully, including Twingate
2. **Third-party menu bar managers**: Use apps designed to collapse/expand menu bar icons (e.g., Bartender, Ice) — *Twingate does not endorse specific apps; use at your discretion*
3. **Quit other menu bar apps**: Close other menu bar applications until the Twingate icon becomes visible

## Post-Resolution Tip
Once the Twingate icon is visible:
- Hold **Command** + click and **drag** the icon to reorder menu bar icons to a preferred position

## Gotchas
- The Twingate client is functioning normally even when the icon is not visible — this is a macOS display limitation, not a connectivity failure
- Reordering icons (Command + drag) can help prevent the issue recurring after using a workaround

## Related Docs
- Twingate macOS Client documentation
- Apple support for macOS menu bar management