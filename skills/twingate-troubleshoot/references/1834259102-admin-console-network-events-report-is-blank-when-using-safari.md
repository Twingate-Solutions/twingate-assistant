---
source: https://help.twingate.com/articles/1834259102-admin-console-network-events-report-is-blank-when-using-safari
type: help
fetched: 2026-11-08
source_version: fa475007a0040ee0624eb589830b83c27c6ceef98bd64086d1c8e1e729113203
trust: official
---

# Admin Console: Network Events Report is Blank

## Summary
When downloading a Network Events report from the Twingate Admin Console using Safari on macOS, the downloaded file contains only CSV column headers with no data. This is a known Safari-specific bug with no current fix; use a different browser as a workaround.

## Key Information
- **Affected component:** Admin Console – Network Events Report
- **Affected platform:** macOS / Safari browser
- **Symptom:** Downloaded file has no extension and contains only the CSV header row, no event data
- **Expected format:** `.gzip` file with full event data (works correctly in non-Safari browsers)
- **Secondary issue:** If a `.gzip` file from a non-Safari browser is also blank, the report may not have finished generating yet

## Prerequisites
- Access to Twingate Admin Console
- A Network Events report generated for download

## Gotchas
- Safari strips the `.gzip` extension and decompresses (or mishandles) the file, resulting in an empty-looking CSV
- Do not mistake a Safari-caused blank file for a report generation failure — verify with another browser first
- If non-Safari browsers also return a blank `.gzip`, the issue is server-side report generation, not the browser

## Resolution / Workaround
1. **Use a non-Safari browser** (Chrome, Firefox, Edge, etc.) to download the Network Events report
2. If the report is still blank in a non-Safari browser, **wait a few minutes** and retry — the report may still be generating

> ⚠️ No permanent fix exists at this time. This is a known limitation with Safari's handling of gzip-compressed downloads from the Admin Console.

## Related Docs
- Twingate Admin Console – Network Analytics
- Twingate Help Center: [source article](https://help.twingate.com/articles/1834259102-admin-console-network-events-report-is-blank-when-using-safari)