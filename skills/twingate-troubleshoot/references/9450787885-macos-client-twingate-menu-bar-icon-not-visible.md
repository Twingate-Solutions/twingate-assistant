---
source: https://help.twingate.com/articles/9450787885-macos-client-twingate-menu-bar-icon-not-visible
type: help
fetched: 2026-09-06
source_version: b9bc5d83d1919ffde540d36334e58944a1192a95447577e70a170013b923c4e9
---

# [macOS Client] Twingate Menu Bar Icon Not Visible

## Summary
On MacBook devices with a camera notch, the menu bar truncates icons when too many applications occupy the menu bar space. The Twingate client process runs normally but its icon is hidden behind or beyond the notch area.

## Key Information
- Affects MacBook devices with camera notch (e.g., MacBook Pro M1 Pro and later)
- Twingate process is running correctly — this is purely a display/UI issue
- macOS truncates menu bar icons that would overlap the notch, hiding them entirely
- Verify process is running via Activity Monitor if icon is not visible

## Prerequisites
- Twingate macOS client installed and launched
- Confirm issue is notch-related: check Activity Monitor for `Twingate` process running

## Resolution Options

1. **External monitor** — Connect a monitor without a notch; all menu bar icons including Twingate will display on the external display's menu bar

2. **Third-party menu bar managers** — Apps like Bartender or similar tools can collapse/expand menu bar icons to free up space (use at own discretion; not endorsed by Twingate)

3. **Quit other menu bar apps** — Close other menu bar applications one at a time until Twingate icon becomes visible
   - Once visible, hold **Command** + click and **drag** the Twingate icon to reorder/reposition it closer to the center or a preferred location

## Gotchas
- The Twingate client is **not crashed or broken** when the icon is missing — confirm via Activity Monitor before troubleshooting the client itself
- Reordering icons (Command + drag) only works while icons are visible; resolve visibility first
- macOS has no native built-in solution for notch icon truncation beyond removing icons

## Related Docs
- Apple Community discussion: https://discussions.apple.com/thread/253393969
- Twingate Component: Client | Platform: macOS