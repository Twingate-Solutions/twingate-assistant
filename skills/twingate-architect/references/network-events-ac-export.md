# Network Events Admin Console Export

## Page Title
Network Events Admin Console Export

## Summary
Twingate allows administrators to export network traffic event data from the Admin Console Reports page. Exports are generated asynchronously in GZIP-compressed JSON (NDJSON) format and can be filtered by date range and Remote Network.

## Key Information
- Exports are in **GZIP format**, containing **NDJSON** (one JSON object per line)
- Timestamps in the export are **UTC**, but the selection UI uses **local timezone**
- Time range filtering is based on **connection end time**, not start time
- Export completes in background; notification sent via email when ready
- Export size can contain **millions of lines** depending on time range and activity

## Prerequisites
- Admin Console access with permissions to view Reports/Settings
- Access to the **Reports** page under Settings

## Step-by-Step

1. Navigate to **Settings → Reports**
2. Click the **Network Events** tab
3. Click **Generate Network Events Report**
4. Set **Report Type** to `Events`
5. Select desired **date & time range** and **Remote Network(s)** (defaults to all)
6. Wait for background processing; refresh page or await email notification
7. Return to **Reports** page to download completed export

## Configuration Values
| Parameter | Details |
|-----------|---------|
| Report Type | Must be set to `Events` |
| Date/Time Range | Local timezone input; UTC in output |
| Remote Networks | Defaults to all networks |

## Gotchas
- **Safari auto-unpack issue**: If file appears empty in Safari, disable "Open 'Safe' files after downloading" via Safari → Preferences → General
- **File extension**: After decompression, manually add `.csv` extension to open in spreadsheet editors
- **Large exports**: May take **hours** for very large datasets; millions of rows can crash spreadsheet editors — use CLI tools or data pipelines instead
- **Time zone mismatch**: UI selection is local time, but exported timestamps are UTC — account for this when filtering
- **Connection timing**: Filter range uses connection **end time**, so connections that started before the range but ended within it will be included

## Related Docs
- [Network Events Schema](https://www.twingate.com/docs/) (linked as "detailed schema" in source)
- Network Events SIEM/streaming export (separate from this Admin Console export)