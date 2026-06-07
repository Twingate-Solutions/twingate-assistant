# Network Events Admin Console Export

## Page Title
Network Events Admin Console Export

## Summary
Twingate allows administrators to export Network Events from the Admin Console Reports page as GZIP-compressed JSON files. Exports run in the background and are filterable by date/time range and Remote Network. The exported data can be opened as CSV in spreadsheet editors after decompression.

## Key Information
- Export format: GZIP-compressed JSON (one event per line / JSONL format)
- Timestamps in export are **UTC**, regardless of local timezone used during selection
- Time range filtering uses **end time** of connection, not start time
- Remote Networks filter defaults to **all networks**
- Export completion time: seconds to minutes for most; hours for very large exports
- Notification sent via email when export is ready

## Prerequisites
- Admin Console access with permissions to view Reports/Settings
- Access to the **Reports** page under **Settings**

## Step-by-Step

1. Navigate to **Settings → Reports**
2. Click the **Network Events** tab
3. Click **Generate Network Events Report**
4. Set **Report Type** to `Events`
5. Select date/time range and Remote Network(s)
6. Wait for background processing (email notification sent on completion)
7. Return to **Reports** page to download the file

## Configuration Values
- **Report Type**: `Events`
- **Time range**: local timezone (converted to UTC in output)
- **Remote Networks**: defaults to all if not specified

## Gotchas
- **Safari users**: Disable auto-unpack to avoid empty file appearance — uncheck *Open "Safe" files after downloading* in Safari → Preferences → General
- **Large exports**: May contain millions of lines; opening directly in spreadsheet editors (Excel, Sheets) may cause performance issues or failures
- **File rename required**: After decompressing GZIP, manually add `.csv` extension to open in spreadsheet editors
- **Timezone mismatch**: Selection UI uses local timezone, but exported timestamps are UTC
- **Connection timing**: Events are indexed by connection **end time** — connections spanning the boundary may appear in unexpected ranges

## Related Docs
- [Network Events Schema](https://www.twingate.com/docs/network-events-schema) (linked as "detailed schema" in source)
- Reports page (Settings → Reports)