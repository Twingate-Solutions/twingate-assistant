# Admin Console Export

## Page Title
Admin Console Export (Audit Logs Report)

## Summary
Twingate allows administrators to export audit logs from the Admin Console Reports page. Exports are generated asynchronously in GZIP-compressed JSON format, with one JSON object per line representing each admin action. Timestamps in the UI display in local timezone, but exported data uses UTC.

## Key Information
- Exports available under **Settings → Reports**
- Output format: **GZIP-compressed JSON** (newline-delimited)
- Timestamps in export are **UTC** (UI display is local timezone)
- Export delivery: **email notification** when ready
- Typical completion time: few minutes; large exports may take several hours
- Each log entry captures: event time, actor, action taken, final state (with before-state if applicable)
- Detailed JSON schema available in Twingate docs

## Prerequisites
- Admin Console access with permissions to view Reports/Settings
- Email access to receive completion notification

## Step-by-Step: Generating an Export
1. Navigate to **Settings → Reports**
2. Click **Generate Audit Logs Report**
3. Select desired **time range** and **category**
4. Wait for email notification that export is ready
5. Return to **Reports page** to download the completed file

## Configuration Values
- **Time range**: User-selected during export creation
- **Category**: User-selected during export creation
- **Timestamp format in export**: UTC
- **File format**: `.gz` (GZIP)
- **Data format**: Newline-delimited JSON

## Gotchas
- **Safari users**: Safari's auto-unpack feature may cause the file to appear empty. Fix: go to **Safari → Preferences → General** and **uncheck** "Open 'Safe' files after downloading" before downloading
- UI time range selector shows local timezone, but exported timestamps are UTC — account for this when filtering or correlating logs
- Very large exports can take **hours**, not minutes — don't regenerate assuming failure

## Related Docs
- Twingate Audit Log JSON Schema (linked from export page)
- Settings/Reports page in Admin Console