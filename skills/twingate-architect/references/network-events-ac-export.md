# Network Events Admin Console Export

## Page Title
Network Events Admin Console Export

## Summary
Twingate allows administrators to export Network Events from the Admin Console Reports page as GZIP-compressed JSON files. Exports run in the background and cover a user-specified date range and Remote Network scope. Files contain one JSON object per line and may be very large depending on activity volume.

## Key Information
- Export format: GZIP-compressed, newline-delimited JSON (one event per line)
- Timestamps in export are **UTC**, but the time range selector uses **local timezone**
- Time range is based on connection **end time**, not start time
- Remote Networks default to **all** if none selected
- Export runs asynchronously; notification sent via email when ready
- Export duration: seconds to minutes typically; large exports may take hours

## Prerequisites
- Admin Console access
- Access to Settings > Reports page
- Report Type must be set to **Events** (not another report type)

## Step-by-Step

1. Navigate to **Settings → Reports**
2. Click the **Network Events** tab
3. Click **Generate Network Events Report**
4. Set **Report Type** to `Events`
5. Select desired **date & time range** (uses local timezone)
6. Select **Remote Network(s)** (defaults to all)
7. Wait for background processing; refresh page or await email notification
8. Return to Reports page to **download** the completed report

## Configuration Values
| Parameter | Options/Notes |
|---|---|
| Report Type | Must be set to `Events` |
| Date/Time Range | Local timezone input; UTC output |
| Remote Networks | Multi-select; defaults to all |

## File Handling
- Decompress with any standard GZIP/compression tool
- After decompression, **rename file with `.csv` extension** for spreadsheet compatibility
- Very large exports (millions of lines) may not open well in spreadsheet editors — use a text processor or data pipeline instead

## Gotchas
- **Safari users**: Disable auto-unpack to prevent empty file issue — uncheck *Open "Safe" files after downloading* in Safari → Preferences → General
- Time range filter uses connection **end time** — connections that started before the range but ended within it will be included
- Exported timestamps are UTC regardless of local timezone used during selection
- File has no `.csv` extension by default; must be manually added after decompression

## Related Docs
- [Network Events Schema](#) (linked as "detailed schema is available here" — internal link)
- Network Events tab under Settings → Reports