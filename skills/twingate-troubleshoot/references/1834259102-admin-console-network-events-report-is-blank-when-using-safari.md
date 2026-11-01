---
source: https://help.twingate.com/articles/1834259102-admin-console-network-events-report-is-blank-when-using-safari
type: help
fetched: 2026-11-01
source_version: b00c7ab7ffade4cd2ead5c7ccca766ce67495539d6ea9f3fe26cdf53a8ebd958
trust: official
---

# Admin Console: Network Events Report is Blank

## Summary
When downloading a Network Events report from the Twingate Admin Console using Safari on macOS, the downloaded file contains only CSV column headers with no data. This is a known Safari-specific bug with no current fix; using an alternative browser is the recommended workaround.

## Key Information
- **Affected component:** Admin Console – Network Events Report
- **Affected platform:** macOS / Safari browser
- **Symptom:** Downloaded file has no extension and contains only the CSV header row
- **Expected behavior:** File downloads as `.gzip` format containing full event data
- **Other browsers:** Return a properly compressed `.gzip` file with data

## Gotchas
- If a `.gzip` file downloaded via a non-Safari browser is also blank, the report may not have finished generating — this is a separate issue from the Safari bug
- Do not confuse "headers-only" Safari output with a generation failure; the two have different causes

## Resolution / Workaround
1. **Switch browsers** — use Chrome, Firefox, or any non-Safari browser to download the Network Events report
2. **If non-Safari download is also blank** — wait several minutes and retry; the report may still be generating

## Current Status
No fix available as of last update. Safari workaround is the only resolution.

## Related Docs
- Twingate Admin Console – Network Analytics / Events reporting