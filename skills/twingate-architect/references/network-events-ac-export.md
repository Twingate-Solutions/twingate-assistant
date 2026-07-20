# Network Events Admin Console Export

## Page Title
Network Events Admin Console Export

## Summary
Twingate allows exporting Network Events from the Admin Console as GZIP-compressed JSON files. Exports run in the background and are delivered via email notification or manual page refresh. Each event is represented as a single JSON line (JSONL format).

## Key Information
- Exports are in **GZIP format**, containing **JSONL** (one JSON object per line)
- Timestamps in export are **UTC**, but the selection UI uses **local timezone**
- Time range filtering is based on **connection end time**, not start time
- Remote Networks default to **all** if not specified
- Export duration: seconds to minutes typically; large exports may take hours
- Detailed schema available separately (linked from source page)

## Prerequisites
- Admin Console access with permissions to view Reports/Settings
- Report Type must be set to **Events** (not another report type)

## Step-by-Step: Generating an Export
1. Navigate to **Settings → Reports**
2. Click the **Network Events** tab
3. Click **Generate Network Events Report**
4. Set **Report Type** to `Events`
5. Select **date & time range** (uses local timezone)
6. Select **Remote Network(s)** (defaults to all)
7. Wait for background processing; refresh page or await email notification
8. Return to Reports page to download completed export

## Viewing/Using the Export
1. Decompress the GZIP file using any standard compression tool
2. Rename the decompressed file to add `.csv` extension for spreadsheet editors
3. Be aware: large time ranges may produce millions of rows, potentially causing spreadsheet performance issues

## Configuration Values
| Parameter | Options/Notes |
|-----------|---------------|
| Report Type | Must be set to `Events` |
| Date/Time Range | Local timezone input; UTC in output |
| Remote Networks | One or more; defaults to all |

## Gotchas
- **Safari auto-unpack issue**: If file appears empty in Safari, disable "Open 'Safe' files after downloading" under Safari → Preferences → General before re-downloading
- **Timezone mismatch**: UI selection is local time, but exported timestamps are UTC — account for this when filtering
- **End-time filtering**: Connections that *started* outside the range but *ended* within it will be included; connections that started within but ended outside will not
- **Large exports**: May take hours and could crash spreadsheet editors — consider processing programmatically

## Related Docs
- Network Events schema (linked from source as "here")
- Twingate Reports documentation