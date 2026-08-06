---
source: https://help.twingate.com/articles/9450787885-macos-client-twingate-menu-bar-icon-not-visible
type: help
fetched: 2026-08-06
source_version: b147d69eec3b82f442be96879ec43063f375e59c74c961f8d3023bbd15d1c6e1
---

# [macOS Client] Twingate Menu Bar Icon Not Visible

## Summary
On MacBook devices with a camera notch, the menu bar truncates icons when too many applications occupy the menu bar space. The Twingate client process runs normally but its icon is hidden behind the notch area.

## Key Information
- Affects MacBook devices with camera notch (e.g., MacBook Pro M1 Pro and later)
- Twingate process **is running** — this is purely a display/visibility issue
- macOS truncates menu bar icons that would overlap the notch rather than showing them

## Prerequisites
- Verify Twingate is actually running: check Activity Monitor for the Twingate process
- Confirm this is a notch-related issue, not a crash or launch failure

## Resolution Options (in order of ease)

1. **External monitor** — Connect a monitor without a notch; all icons including Twingate will appear on the extended display menu bar
2. **Third-party menu bar managers** — Apps like Bartender or similar tools collapse/expand menu bar icons to reclaim space (use at own discretion)
3. **Quit other menu bar apps** — Close other menu bar applications until the Twingate icon becomes visible

**Once icon is visible:** Hold `Command` + click and drag to reorder icons, positioning Twingate away from the notch boundary.

## Gotchas
- No built-in macOS fix — this is an OS-level truncation behavior
- Reordering icons (`Command` + drag) only works after the icon is visible; do this to prevent recurrence
- Twingate does not endorse any specific third-party menu bar management applications

## Related Docs
- Apple Community discussion: https://discussions.apple.com/thread/253393969
- Twingate Component: Client | Platform: macOS