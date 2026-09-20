---
source: https://help.twingate.com/articles/9450787885-macos-client-twingate-menu-bar-icon-not-visible
type: help
fetched: 2026-09-20
source_version: b0a43d58d90e7834c7c532afbe333546752200f58b1554f722be8e25e3b5aaca
---

# [macOS Client] Twingate Icon Not Visible in Menu Bar

## Summary
On MacBook devices with a camera notch, menu bar icons are truncated when too many applications occupy the menu bar. The Twingate client runs normally but its icon is hidden behind the notch area.

## Key Information
- Affects MacBook devices with camera notch (e.g., MacBook Pro M1 Pro and later)
- Twingate process runs correctly — this is purely a display/visibility issue
- macOS 27 introduces native menu bar expansion that resolves this natively

## Prerequisites
- Confirm Twingate is actually running via Activity Monitor before troubleshooting
- Issue only occurs when menu bar is crowded enough to reach the notch

## Symptoms
- Twingate icon absent from menu bar after launch
- Activity Monitor shows Twingate process is running

## Resolution Options

1. **External monitor** — Connect a monitor without a notch; all icons including Twingate will display
2. **Third-party menu bar managers** — Use apps that collapse/expand menu bar icons (use at own discretion; not endorsed by Twingate)
3. **Quit other menu bar apps** — Close other menu bar applications until Twingate icon becomes visible

### Reordering Icons (once visible)
- Hold `Command` + click and drag icons to reorder them in the menu bar

## Configuration Values
None — no config changes required.

## Gotchas
- macOS native fix requires macOS 27; older versions need workarounds
- Icon being hidden does **not** indicate a crash or failed connection
- Third-party apps are not endorsed by Twingate — use at your own risk

## Related Docs
- Twingate macOS Client documentation