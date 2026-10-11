---
source: https://help.twingate.com/articles/1834259102-admin-console-network-events-report-is-blank-when-using-safari
type: help
fetched: 2026-10-11
source_version: e9b864c0b11e0f0008590221fdab008dec49954d7464dc19c9bebd71b901ae27
trust: official
---

# Admin Console: Network Events Report is Blank

## Summary
When downloading a Network Events report from the Twingate Admin Console using Safari on macOS, the downloaded file contains only CSV column headers with no data. This is a known Safari-specific bug with no current fix.

## Key Information
- **Affected component:** Admin Console – Network Events Report
- **Affected platform:** macOS / Safari browser
- **Symptom:** Downloaded file has no extension, contains only the CSV header row, no event data
- **Expected behavior:** Other browsers download a properly formatted `.gzip` file with full event data
- **Separate issue:** If `.gzip` files from non-Safari browsers are also blank, the report may not have finished generating yet

## Prerequisites
- Access to Twingate Admin Console
- A Network Events report triggered for download

## Gotchas
- Safari strips the `.gzip` format and delivers an incomplete file — this is not a permissions or data issue
- Do not mistake a blank report in Safari for a legitimate "no events" result
- A blank `.gzip` from Chrome/Firefox/Edge is a different problem (report generation failure), not the same Safari bug

## Resolution / Workarounds
1. **Use a non-Safari browser** (Chrome, Firefox, Edge) to download the Network Events report
2. **If non-Safari downloads are also blank:** wait several minutes and retry — the report may still be generating

## Configuration Values
None applicable.

## Related Docs
- Twingate Admin Console – Network Analytics / Network Events reporting