---
source: https://help.twingate.com/articles/1834259102-admin-console-network-events-report-is-blank-when-using-safari
type: help
fetched: 2026-10-28
source_version: 9eb8b861f2dd560f61ca71e34c6d2a8d7922917c124a7b55fe8ae0abc7c43035
trust: official
---

# Admin Console: Network Events Report is Blank

## Summary
When downloading a Network Events report in Safari on macOS, the file downloads without an extension, is uncompressed, and contains only CSV column headers with no data. All other browsers download the report correctly as a `.gzip` file with full event data.

## Key Information
- **Affected component:** Admin Console – Network Events Report
- **Affected platform:** macOS / Safari browser only
- **Symptom:** Downloaded file has no extension, contains only CSV header row, no event data
- **Expected behavior:** `.gzip` compressed file with complete event data

## Prerequisites
- Access to Twingate Admin Console
- Ability to use an alternative browser (Chrome, Firefox, Edge, etc.)

## Gotchas
- If a `.gzip` file downloaded from a **non-Safari** browser is also blank, the issue is unrelated to Safari — the report itself may not have finished generating; wait a few minutes and retry
- Safari silently strips the `.gzip` extension and decompresses the file incorrectly, resulting in a truncated output
- This is a **known, unresolved bug** — no fix currently exists on Twingate's side

## Resolution / Workarounds
1. **Use a non-Safari browser** (Chrome, Firefox, Edge) to download the Network Events report
2. If the report is blank in any browser, wait several minutes for report generation to complete, then retry the download

## Related Docs
- Twingate Admin Console – Network Analytics / Events reporting