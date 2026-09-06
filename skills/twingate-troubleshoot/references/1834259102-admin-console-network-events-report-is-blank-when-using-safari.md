---
source: https://help.twingate.com/articles/1834259102-admin-console-network-events-report-is-blank-when-using-safari
type: help
fetched: 2026-09-06
source_version: 384c005abbd06af04adca144308d90ccdf48d2c9a93dacc9d6e0d238e006e648
---

# Admin Console: Network Events Report Blank in Safari

## Summary
Downloading Network Events reports via Safari on macOS results in a broken file containing only CSV column headers with no data. This is a known bug with no current fix — use a different browser.

## Key Information
- Safari downloads the report as an uncompressed file with no extension
- File contains only the CSV header row, no event data
- Other browsers (e.g., Chrome) download correctly as a `.gzip` compressed file with full data
- Issue is specific to Safari on macOS

## Prerequisites
- Access to Twingate Admin Console
- Network Events report generation permissions

## Symptoms
| Browser | Result |
|---------|--------|
| Safari | No file extension, CSV headers only, no data |
| Chrome | `.gzip` file, full event data |

## Resolution
**No fix currently available.**

**Workaround:** Use any browser other than Safari (Chrome, Firefox, Edge) to download Network Events reports.

## Gotchas
- The downloaded file in Safari is not obviously broken — it opens as a valid CSV but appears empty because only headers are present
- Do not attempt to decompress or reprocess the Safari-downloaded file; the data was never included

## Affected Components
- **Component:** Admin Console
- **Platform:** macOS
- **Browser:** Safari only

## Related Docs
- Twingate Network Events / Analytics reporting documentation