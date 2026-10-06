---
source: https://help.twingate.com/articles/1834259102-admin-console-network-events-report-is-blank-when-using-safari
type: help
fetched: 2026-10-04
source_version: 5e6fa06214abf242d0ca5e366a86d16a43cf327271670cbd074ee82dfd91c2e7
trust: official
---

# Admin Console: Network Events Report Blank in Safari

## Summary
Downloading Network Events reports via Safari on macOS produces a broken file containing only CSV column headers with no data. This is a known bug with no current fix; switching browsers is the only workaround.

## Key Information
- **Affected component:** Twingate Admin Console – Network Events Report
- **Affected platform:** macOS / Safari browser
- **Root cause:** Safari decompresses the `.gzip` response and strips the extension, resulting in an incomplete file with only the CSV header row
- **Other browsers (e.g., Chrome):** Return the correct `.gzip` file with full event data

## Symptoms
| Browser | File output |
|---------|-------------|
| Safari | No extension, CSV header only, no data rows |
| Chrome / Firefox / Edge | `.gzip` file, full event data present |

## Resolution
**No fix available.** Use any browser other than Safari to download Network Events reports.

## Workaround Steps
1. Open the Twingate Admin Console in Chrome, Firefox, or Edge.
2. Navigate to the Network Events report section.
3. Generate and download the report as normal.
4. The downloaded `.gzip` file will contain complete event data.

## Gotchas
- The Safari download appears to succeed (no error shown), making the issue easy to miss until you open the file and find it empty.
- The file lacks an extension in Safari, which may cause confusion about the file format.
- No ETA for a fix from Twingate.

## Related Docs
- Twingate Admin Console documentation
- Network Analytics / Events reporting