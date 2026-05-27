# Admin Console Export

## Page Title
Admin Console Export (Audit Logs Report)

## Summary
Twingate allows administrators to export audit logs from the Admin Console Reports page. Exports are generated asynchronously, delivered via email notification, and provided in GZIP-compressed JSON format.

## Key Information
- Exports available under **Settings → Reports**
- Time range UI displays in **local timezone**; exported timestamps are in **UTC**
- Output format: **GZIP-compressed JSON** (one JSON object per line)
- Each log entry contains: timestamp, actor, action type, final state (with before-state where applicable)
- Most exports complete in minutes; large exports may take several hours
- Completed reports must be manually downloaded from the Reports page after email notification

## Prerequisites
- Admin Console access
- Access to Settings → Reports page
- Email access to receive completion notification

## Step-by-Step

1. Navigate to **Settings → Reports** in Admin Console
2. Click **Generate Audit Logs Report**
3. Select **time range** and **category**
4. Wait for email notification (background job; minutes to hours)
5. Return to **Reports page** to download completed export

## Configuration Values
- **Export format:** GZIP (`.gz`)
- **Data format:** JSON (newline-delimited)
- **Timestamp format in export:** UTC
- **Categories:** Selectable at generation time (specific categories not enumerated)

## Gotchas
- **Safari auto-unpack issue:** Safari may unpack GZIP automatically and display file as empty. Fix: Go to **Safari → Preferences → General** and **uncheck** "Open 'Safe' files after downloading" before downloading
- Time range selector shows local timezone but export timestamps are UTC — avoid confusion when filtering/parsing
- No in-page progress indicator; must wait for email then return to Reports page to download
- Very large exports can take **hours**, not minutes

## Related Docs
- [Audit Log JSON Schema](https://www.twingate.com/docs/admin-console-export) (linked as "here" in source — verify exact URL)
- Twingate Reports/Settings documentation