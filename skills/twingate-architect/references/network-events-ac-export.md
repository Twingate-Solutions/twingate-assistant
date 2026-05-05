# Network Events Admin Console Export

## Page Title
Network Events Admin Console Export

## Summary
Twingate allows administrators to export Network Events from the Admin Console Reports page as GZIP-compressed JSON files. Exports run in the background and can be downloaded once complete, with an email notification sent when ready.

## Key Information
- Exports are in **GZIP format**, containing **JSON** (one event per line / JSONL format)
- Timestamps in the export are **UTC**, but the selection UI uses **local timezone**
- Time range filtering uses **connection end time**, not start time
- Remote Networks default to **all** if not specified
- Export duration: typically seconds to minutes; large exports may take hours
- Schema reference available separately (linked as "here" in source)

## Prerequisites
- Admin Console access with permissions to view Reports
- Access to Settings > Reports page

## Step-by-Step

1. Navigate to **Settings → Reports**
2. Click the **Network Events** tab
3. Click **Generate Network Events Report**
4. Set **Report Type** to `Events`
5. Select desired **date & time range** and **Remote Network(s)**
6. Wait for background processing; refresh page or await email notification
7. Return to Reports page to **download** the completed export

## Configuration Values
| Parameter | Options/Notes |
|-----------|---------------|
| Report Type | Must be set to `Events` |
| Date/Time Range | Local timezone input; UTC in output |
| Remote Networks | Multi-select; defaults to all |

## Viewing the Export

1. Decompress the GZIP file using any standard compression tool
2. Rename the decompressed file with `.csv` extension for spreadsheet compatibility
3. Be aware: large time ranges may produce millions of rows, causing spreadsheet performance issues

## Gotchas
- **Safari users**: If file appears empty, disable "Open 'safe' files after downloading" in Safari → Preferences → General (auto-unpack interferes with download)
- **Timezone mismatch**: UI selection is local time, but exported timestamps are UTC
- **Filter basis**: Range filters on connection *end time*, not start time — connections that started before the range but ended within it will be included
- **Large exports**: May take hours; millions of rows can crash spreadsheet editors — consider programmatic processing for large datasets
- File is JSONL (newline-delimited JSON), not a traditional CSV despite the recommended `.csv` rename

## Related Docs
- Network Events schema (referenced but URL not provided in source)
- Reports page documentation