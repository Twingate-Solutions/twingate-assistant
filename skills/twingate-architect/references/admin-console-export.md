# Admin Console Export

## Page Title
Admin Console Export (Audit Logs Report)

## Summary
Twingate allows admins to export audit logs from the Admin Console as GZIP-compressed JSON files. Reports are generated asynchronously and delivered via email notification. Each log entry captures event timestamp, actor, action, and state changes.

## Key Information
- Exports are in **GZIP format** containing **JSON data**
- Timestamps in the UI display in **local timezone**; exported timestamps are in **UTC**
- Each line in the export = one admin action event
- Each event contains: timestamp, actor, action, final state (+ before state if applicable)
- Most exports complete in **minutes**; large exports may take **hours**
- Completed reports are downloadable from the Reports page
- JSON schema documentation available separately

## Prerequisites
- Admin access to Twingate Admin Console
- Email access to receive completion notification

## Step-by-Step

1. Navigate to **Settings → Reports**
2. Click **Generate Audit Logs Report**
3. Select **time range** and **category**
4. Wait for email notification (background processing)
5. Return to **Settings → Reports** to download the completed report

## Configuration Values
- **Time range**: User-selectable during export creation
- **Category**: User-selectable during export creation
- **Output format**: GZIP-compressed JSON (one JSON object per line)

## Gotchas
- **Safari issue**: If the file appears empty in Safari, disable the auto-unpack feature before downloading:
  - Safari → Preferences → General → uncheck **"Open 'Safe' files after downloading"**
- Time range selection UI shows **local timezone**, but exported timestamps are **UTC** — account for this when filtering by time
- No on-screen progress indicator; completion only communicated via **email**
- Very large date ranges can take **hours** — plan accordingly

## Related Docs
- Audit Logs JSON Schema (linked inline as "here")
- Twingate Reports/Settings page (Admin Console)