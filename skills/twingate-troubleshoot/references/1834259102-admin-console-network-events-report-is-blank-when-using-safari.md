---
source: https://help.twingate.com/articles/1834259102-admin-console-network-events-report-is-blank-when-using-safari
type: help
fetched: 2026-10-25
source_version: b124818b105817f69d410d58570fffb09ff876a3b8ff7e72ee591b4082e884b5
trust: official
---

# Admin Console: Network Events Report is Blank

## Summary
When downloading a Network Events report from the Twingate Admin Console using Safari on macOS, the downloaded file contains only CSV column headers with no data. This is a known Safari-specific bug with no current fix; using a non-Safari browser is the workaround.

## Key Information
- **Affected component:** Admin Console – Network Events Report
- **Affected platform:** macOS / Safari browser
- **Symptom:** Downloaded file has no file extension and contains only the CSV header row, no event data
- **Expected behavior:** Non-Safari browsers download a `.gzip` file containing full event data
- **Secondary issue:** If `.gzip` files from non-Safari browsers are also blank, the report may not have finished generating yet

## Prerequisites
- Access to Twingate Admin Console
- A Network Events report triggered for download

## Gotchas
- Safari silently decompresses gzip responses and then drops the data, resulting in a header-only file — there is no error message indicating failure
- A blank `.gzip` from Chrome or Firefox is a **separate issue** (report not yet generated), not the same Safari bug
- No resolution exists at this time within the Admin Console or Safari settings

## Resolution / Workaround
1. **Use a non-Safari browser** (Chrome, Firefox, Edge, etc.) to download the Network Events report
2. If the report is still blank in a non-Safari browser, wait a few minutes and retry — the report may still be generating

## Related Docs
- Twingate Admin Console – Network Analytics
- Twingate Help Center: [https://help.twingate.com](https://help.twingate.com)