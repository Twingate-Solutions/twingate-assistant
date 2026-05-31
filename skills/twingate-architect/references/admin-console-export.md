# Admin Console Export

## Page Title
Admin Console Export (Audit Logs Report)

## Summary
Twingate allows administrators to export audit logs from the Admin Console Reports page. Exports are generated asynchronously in GZIP-compressed JSON format, with one JSON object per line per admin action. Timestamps in the UI are local timezone, but export timestamps are UTC.

## Key Information
- Export format: GZIP-compressed, newline-delimited JSON
- Timestamps in export: UTC
- Timestamps in UI selection: Local timezone
- Delivery: Email notification when ready; download from Reports page
- Processing time: Minutes for small exports; hours for very large exports
- Each JSON line contains: event time, actor, action, final state, and before-state (if applicable)
- Full JSON schema available in Twingate docs (linked from source page)

## Prerequisites
- Admin Console access
- Access to Settings > Reports page

## Step-by-Step

1. Navigate to **Settings → Reports**
2. Click **Generate Audit Logs Report**
3. Select **time range** and **category**
4. Wait for email notification that export is ready
5. Return to **Reports page** to download

## Configuration Values
- **Time range**: Selectable during export generation (UI displays local timezone; export outputs UTC)
- **Category**: Selectable filter during export generation

## Gotchas
- **Safari users**: Safari may auto-unpack the GZIP and show an empty file. Fix: Go to `Safari > Preferences > General` and **uncheck** "Open 'Safe' files after downloading" before downloading
- UI time range selector shows local timezone, but exported timestamps are in UTC — account for this when filtering or correlating logs
- Large exports can take several hours; do not expect immediate availability

## Related Docs
- Twingate JSON schema reference (linked from source page as "here")
- Twingate Reports/Settings section of Admin Console