---
source: https://help.twingate.com/articles/1834259102-admin-console-network-events-report-is-blank-when-using-safari
type: help
fetched: 2026-08-06
source_version: 153b213803b448c6b7e5fdd6ca0c33139a8679684a46261355f6aed53765acfe
---

# Admin Console: Network Events Report Blank in Safari

## Summary
Downloading Network Events reports via Safari on macOS produces a broken file containing only CSV column headers with no data. This is a known bug with no current fix — use a different browser.

## Key Information
- Safari downloads the report as an uncompressed file with no extension
- File contains only the CSV header row, no event data
- Chrome and other browsers download correctly as a `.gzip` file with full data
- Issue is specific to Safari on macOS

## Affected Components
- **Component:** Admin Console
- **Platform:** macOS
- **Browser:** Safari

## Symptoms
- Downloaded report has no file extension
- File opens but contains only the header line (no rows)
- Same report downloaded in Chrome returns a proper `.gzip` with all events

## Resolution
**No fix available.** Use any browser other than Safari to download Network Events reports.

## Gotchas
- No workaround exists within Safari itself
- Don't assume the report is empty — the data is there, Safari just fails to handle the gzip response correctly

## Related Docs
- Network Events / Analytics reporting in Twingate Admin Console