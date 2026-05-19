# Admin Console Export

## Page Title
Admin Console Export (Audit Logs Report)

## Summary
Twingate allows admins to export audit logs as JSON reports from the Admin Console Settings page. Reports are generated asynchronously and delivered via email when complete. Exports are GZIP-compressed JSON files with UTC timestamps.

## Key Information
- Exports available under **Settings → Reports**
- Time range selector uses local timezone display, but exported timestamps are in **UTC**
- Export format: **GZIP-compressed JSON** (one JSON object per line)
- Generation time: typically minutes; large exports may take hours
- Completed reports downloaded from the Reports page (not via email link)
- JSON schema documentation available (linked from docs page)

## Each Log Entry Contains
- Timestamp of event
- Actor (who performed the action)
- Action type
- Final state (includes before-state when applicable)

## Prerequisites
- Admin Console access
- Access to Settings → Reports page

## Step-by-Step: Generate Audit Log Export
1. Navigate to **Settings → Reports**
2. Click **Generate Audit Logs Report**
3. Select **time range** and **category**
4. Wait for background processing; email notification sent when ready
5. Return to **Reports page** to download

## Configuration Values
- **Time range**: configurable at export creation
- **Category**: configurable at export creation
- **Output format**: JSON (GZIP compressed)
- **Timestamp format**: UTC in export file

## Gotchas
- **Safari users**: Safari's auto-unpack feature may cause files to appear empty. Fix: Go to `Safari → Preferences → General` and **uncheck** "Open 'safe' files after downloading" before downloading
- Display timezone ≠ export timezone — UI shows local time but file contains UTC
- Large exports can take hours; don't expect immediate availability

## Related Docs
- Twingate JSON schema reference (linked inline on source page)
- Twingate Reports/Settings section of Admin Console