# Network Events Admin Console Export

## Page Title
Network Events Admin Console Export

## Summary
Twingate allows admins to export Network Events from the Admin Console Reports page as GZIP-compressed JSON files. Exports run in the background and can contain connection-level traffic data filtered by date range and Remote Network. The export schema is available separately.

## Key Information
- Exports are **GZIP-compressed**, **JSON format** (one event per line / JSONL)
- Timestamps in export are **UTC**, but the selection UI uses **local timezone**
- Time range is based on **connection end time**, not start time
- Remote Networks filter defaults to **all networks**
- Export runs asynchronously; notification sent via **email** when ready
- Processing time: seconds to minutes for small exports; **up to a few hours** for large ones

## Prerequisites
- Admin Console access with permissions to view Reports/Settings
- Access to Settings → Reports → Network Events tab

## Step-by-Step

1. Navigate to **Settings → Reports**
2. Click the **Network Events** tab
3. Click **Generate Network Events Report**
4. Set **Report Type** to `Events`
5. Select desired **date/time range** (local timezone)
6. Select **Remote Network(s)** (defaults to all)
7. Submit and wait for background processing
8. Return to Reports page to **download** when ready (or wait for email notification)

## Configuration Values
| Parameter | Notes |
|---|---|
| Report Type | Must be set to `Events` |
| Date/Time Range | Local timezone input; UTC output |
| Remote Networks | Optional filter; defaults to all |

## Viewing/Opening the Export
- Decompress with any GZIP tool
- **Rename file** by appending `.csv` extension for spreadsheet compatibility
- Large exports may contain **millions of rows**; spreadsheet editors may struggle
- **Safari users**: Disable "Open 'Safe' files after downloading" (Safari → Preferences → General) to prevent auto-unpack producing empty files

## Gotchas
- Time range filter uses **end time of connection**, not start — connections that started before the range but ended within it will be included
- Safari auto-unpack can produce an **empty-appearing file**; disable the feature before downloading
- Very large exports can take **several hours**
- File has no `.csv` extension by default — must be added manually after decompression

## Related Docs
- Network Events schema reference (linked as "detailed schema is available here" in source)
- Twingate Reports page documentation