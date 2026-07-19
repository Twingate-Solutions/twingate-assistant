# Admin Console Export

## Page Title
Admin Console Export (Audit Logs Report)

## Summary
Twingate allows admins to export audit logs from the Admin Console Reports page. Exports are generated asynchronously, delivered via email notification, and provided in GZIP-compressed JSON format with UTC timestamps.

## Key Information
- Exports are in **GZIP + JSON** format (one JSON object per line)
- Timestamps in the export are **UTC** (UI displays in local timezone)
- Each log entry contains: event time, actor, action, final state (with before-state if applicable)
- Large exports may take **a few hours**; most complete in minutes
- Completed reports are downloaded from the Reports page (not via email link)
- A detailed JSON schema is available in Twingate docs

## Prerequisites
- Admin access to Twingate Admin Console
- Access to **Settings > Reports** page
- Email access to receive completion notification

## Step-by-Step

1. Navigate to **Settings > Reports** in Admin Console
2. Click **Generate Audit Logs Report**
3. Select **time range** and **category** for the export
4. Wait for background processing — completion email will be sent
5. Return to **Settings > Reports** to download the completed report

## Configuration Values
| Parameter | Details |
|-----------|---------|
| Time Range | Selectable; UI shows local timezone, export uses UTC |
| Category | Selectable filter at generation time |
| Output Format | GZIP-compressed JSON (`.gz`) |
| Timestamp Format | UTC |

## Gotchas
- **Safari users**: Safari's auto-unpack feature may cause files to appear empty. Fix: Go to `Safari > Preferences > General` → uncheck **"Open 'Safe' files after downloading"** before decompressing manually
- Time range selection displays in **local timezone** but exported timestamps are **UTC** — account for this when filtering/parsing
- No direct download link in the email — must return to the Reports page to download
- Very large datasets can take **hours** — plan accordingly for time-sensitive audits

## Related Docs
- Twingate Audit Log JSON Schema (linked inline as "here" on the source page)
- Twingate Reports/Settings documentation