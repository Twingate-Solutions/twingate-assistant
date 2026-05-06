# Admin Console Export

## Page Title
Admin Console Export (Audit Logs Report)

## Summary
Twingate allows administrators to export audit logs from the Admin Console Reports page. Exports are generated asynchronously in GZIP-compressed JSON format, with one JSON object per line representing each admin action.

## Key Information
- Exports are delivered via email notification when complete
- Most exports complete in minutes; large exports may take hours
- Timestamps in the UI are shown in local timezone; export timestamps are in **UTC**
- Export format: **GZIP-compressed JSON** (newline-delimited)
- Each JSON line contains: event timestamp, actor, action type, final state (with before-state if applicable)
- Full JSON schema available in Twingate documentation

## Prerequisites
- Access to Admin Console with Settings permissions
- Access to Reports page under Settings

## Step-by-Step: Generating an Audit Log Export

1. Navigate to **Settings → Reports**
2. Click **Generate Audit Logs Report**
3. Select **time range** and **category** for the export
4. Wait for email notification that the export is ready (background process)
5. Return to **Settings → Reports** to download the completed report

## Configuration Values
- **Time range**: User-selected at generation time
- **Category**: User-selected at generation time
- **Timezone**: UI displays local time; export data is UTC

## Gotchas
- **Safari issue**: Safari's "Open safe files after downloading" feature may cause the GZIP file to appear empty. Fix: Go to **Safari → Preferences → General** and **uncheck** "Open 'safe' files after downloading" before downloading
- UI time range selector shows local timezone, but exported timestamps are UTC — account for this when filtering or analyzing logs
- Very large exports can take several hours; do not expect immediate availability

## Related Docs
- Twingate JSON Schema for audit log exports (linked as "here" in source page)
- Twingate Settings / Reports page