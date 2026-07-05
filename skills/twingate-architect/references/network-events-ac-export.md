# Network Events Admin Console Export

## Page Title
Network Events Admin Console Export

## Summary
Twingate allows administrators to export Network Events from the Admin Console Reports page as GZIP-compressed JSON files. Exports run as background jobs and are delivered via email notification when complete. The export covers connection events filtered by date range and Remote Network(s).

## Key Information
- Export format: GZIP-compressed, newline-delimited JSON (one event per line)
- Timestamps in export are **UTC**, regardless of local timezone used during selection
- Time range filter uses **end time** of connection, not start time
- Remote Networks default to **all** if not specified
- Export duration: seconds to minutes typically; very large exports may take hours
- Completed exports are downloaded from the Reports page

## Prerequisites
- Admin Console access
- Access to Settings > Reports page
- Report Type must be set to **Events** (not another report type)

## Step-by-Step: Generating an Export
1. Navigate to **Settings → Reports**
2. Click **Network Events** tab
3. Click **Generate Network Events Report**
4. Set **Report Type** to `Events`
5. Select date/time range (uses local timezone for selection)
6. Select Remote Network(s) (defaults to all)
7. Wait for background processing; refresh page or await email notification
8. Return to Reports page to download completed export

## Viewing/Using the Export
1. Decompress the GZIP file using any standard compression tool
2. Rename the decompressed file with `.csv` extension for spreadsheet compatibility
3. Be aware: large time ranges may produce millions of rows, causing spreadsheet editor issues

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| Report Type | Must be set to `Events` |
| Date/Time Range | Local timezone input; UTC in output |
| Remote Networks | Optional filter; defaults to all |

## Gotchas
- **Safari users**: File may appear empty due to auto-unpack feature. Disable via Safari → Preferences → General → uncheck "Open 'Safe' files after downloading"
- **Timezone mismatch**: Selection UI uses local timezone but exported timestamps are in UTC
- **End time filtering**: Records are included based on when the connection *ended*, not when it started — connections spanning the boundary may be excluded/included unexpectedly
- **Large exports**: Millions of rows possible; spreadsheet editors may struggle — consider scripted processing
- **File extension**: Decompressed file has no `.csv` extension by default; must be manually renamed

## Related Docs
- Network Events export schema (linked as "detailed schema" in source — `/docs/network-events-schema` or similar)
- Twingate Reports page documentation