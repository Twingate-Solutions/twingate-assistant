---
source: https://www.twingate.com/docs/admin-console-export
type: docs
fetched: 2026-08-14
source_version: 9a9783ca917de39463c1e0b9fb6f2b3dede453f8ea16f8183b788649cb8d5919
---

# Admin Console Export

## Page Title
Admin Console Export (Audit Logs Report)

## Summary
Twingate allows admins to export audit logs from the Admin Console Reports page. Exports are generated asynchronously, delivered via email notification, and output as GZIP-compressed JSON files.

## Key Information
- Exports accessible via: **Settings → Reports → Generate Audit Logs Report**
- Filter options: time range and category
- Time range UI displays in **local timezone**; exported timestamps are in **UTC**
- Output format: **GZIP-compressed JSON** (one JSON object per line)
- Each log entry contains: timestamp, actor, action, final state (with before-state if applicable)
- Full JSON schema available in Twingate documentation (linked from source page)

## Prerequisites
- Admin Console access with permissions to view Settings/Reports
- Email access to receive completion notification

## Step-by-Step

1. Navigate to **Settings → Reports**
2. Click **Generate Audit Logs Report**
3. Select desired **time range** and **category**
4. Wait for background processing (minutes to hours depending on size); completion notification sent via email
5. Return to **Reports page** to download completed report

## Configuration Values
- **Export format:** GZIP (`.gz`)
- **Data format:** JSON (newline-delimited)
- **Timestamp format:** UTC (in export file)

## Gotchas
- **Safari issue:** Safari's "Open Safe files after downloading" feature can cause GZIP files to appear empty. Fix: go to **Safari → Preferences → General** and **uncheck** "Open 'Safe' files after downloading"
- Large exports can take **several hours** — do not expect immediate availability
- UI time range selector shows local timezone, but **do not assume export timestamps match** — they are UTC
- Most standard compression tools (7-Zip, gunzip, etc.) can decompress GZIP output

## Related Docs
- Twingate Audit Log JSON Schema (linked from source page)
- Twingate Reports/Settings documentation