# Network Events Admin Console Export

## Page Title
Network Events Admin Console Export

## Summary
Twingate allows administrators to export Network Events from the Admin Console Reports page as GZIP-compressed JSON files. Exports run as background jobs with email notification on completion. The output contains one JSON object per line (JSONL format).

## Key Information
- Export format: GZIP-compressed JSONL (one JSON event per line)
- Timestamps in export are **UTC**, regardless of local timezone used during selection
- Time range filter uses **connection end time**, not start time
- Remote Networks default to all if not specified
- Export duration: seconds to minutes typically; large exports may take hours
- Detailed schema available via linked documentation (separate page)

## Prerequisites
- Admin Console access with permissions to view Reports/Settings
- Access to the **Reports** page under **Settings**

## Step-by-Step

1. Navigate to **Settings → Reports**
2. Click the **Network Events** tab
3. Click **Generate Network Events Report**
4. Set **Report Type** to `Events`
5. Select date/time range (local timezone) and target Remote Network(s)
6. Wait for background processing — refresh page or await email notification
7. Return to Reports page to download completed export

## Configuration Values
| Parameter | Options/Notes |
|-----------|---------------|
| Report Type | Must be set to `Events` |
| Date/Time Range | Local timezone input; UTC in output |
| Remote Networks | Defaults to all; can filter to specific networks |
| Time filter basis | Connection **end time** |

## Gotchas
- **Safari users**: Automatic unpacking may result in an apparently empty file. Disable via *Safari → Preferences → General → uncheck "Open 'Safe' files after downloading"*
- After decompression, **manually add `.csv` extension** to the file for spreadsheet compatibility
- Very large exports (millions of lines) may crash or hang spreadsheet editors — consider programmatic processing
- Local timezone is used for **input selection only**; actual exported timestamps are always UTC
- Export is asynchronous — the page must be refreshed or email awaited before download is available

## Related Docs
- Network Events schema (linked inline as "here" on the source page)
- Reports page documentation (implied)