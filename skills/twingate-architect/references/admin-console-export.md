# Admin Console Export

## Page Title
Admin Console Export (Audit Logs Report)

## Summary
Twingate allows admins to export audit logs as JSON reports via the Settings > Reports page. Reports are generated asynchronously and delivered via email notification. Exports are compressed in GZIP format with UTC timestamps.

## Key Information
- Export format: **GZIP-compressed JSON** (one JSON line per admin action)
- Timestamps in export are **UTC** (UI displays in local timezone)
- Each log entry contains: event time, actor, action taken, final state (with before-state if applicable)
- Generation time: minutes for small exports, up to **a few hours** for large ones
- Completed reports are downloaded from the Reports page (not via email link)
- JSON schema documentation available separately

## Prerequisites
- Admin access to Twingate Admin Console
- Access to Settings > Reports page

## Step-by-Step

1. Navigate to **Settings → Reports**
2. Click **Generate Audit Logs Report**
3. Select **time range** and **category**
4. Wait for email notification that report is ready
5. Return to **Settings → Reports** to download

## Configuration Values
- **Time range**: Selectable during generation (displayed in local timezone, exported in UTC)
- **Category**: Selectable filter during generation (specific categories not enumerated in docs)

## Gotchas
- **Safari issue**: Safari's auto-unpack feature can cause GZIP files to appear empty. Fix: Go to **Safari → Preferences → General** and **uncheck** "Open 'safe' files after downloading" before downloading
- Time range selection UI shows local timezone, but exported timestamps are **UTC** — account for this when filtering/correlating logs
- Report download requires returning to the Reports page; it is not directly downloadable from the email
- Large exports can take **hours** — plan accordingly for time-sensitive audits

## Related Docs
- Twingate JSON schema for audit log export (linked inline, URL not provided)
- Twingate Reports/Settings documentation