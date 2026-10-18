---
source: https://help.twingate.com/articles/1834259102-admin-console-network-events-report-is-blank-when-using-safari
type: help
fetched: 2026-10-18
source_version: f480d26b2b49a7043e23ace2aa1f9509ab8c0af379e53d07d8ebe0234d6180cb
trust: official
---

# Admin Console: Network Events Report is Blank

## Summary
When downloading a Network Events report from the Twingate Admin Console using Safari on macOS, the downloaded file contains only CSV column headers with no event data. This is a known Safari-specific bug with no current fix; use a non-Safari browser as a workaround.

## Key Information
- **Affected component:** Admin Console – Network Events Report
- **Affected platform:** macOS / Safari browser
- **Safari behavior:** Downloads file with no extension, contains only the CSV header row, no data
- **Non-Safari behavior:** Downloads a properly formatted `.gzip` file containing all event data
- **If non-Safari browsers also return blank `.gzip` files:** The report itself may not have finished generating — wait and retry

## Prerequisites
- Access to Twingate Admin Console
- A Network Events report queued for download

## Resolution / Workaround
1. **Do not use Safari** for downloading Network Events reports
2. Use an alternative browser (Chrome, Firefox, Edge, etc.)
3. If the report is blank in all browsers, wait several minutes for report generation to complete, then retry the download

## Gotchas
- The Safari download appears to succeed (no error shown), making it easy to assume the report is empty rather than browser-caused
- Blank output in non-Safari browsers is a **different issue** (report not yet generated), not the same Safari bug
- No permanent fix is available as of this writing

## Related Docs
- Twingate Admin Console documentation
- Network Analytics / Events reporting