# Network Events Admin Console Export

## Page Title
Network Events Admin Console Export

## Summary
Twingate allows administrators to export Network Events from the Admin Console Reports page as GZIP-compressed JSON files. Exports run as background jobs with email notification on completion. Files contain one JSON object per line with UTC timestamps.

## Key Information
- Export format: GZIP-compressed, newline-delimited JSON (one event per line)
- Timestamps in export are **UTC**, regardless of local timezone used for selection
- Time range filter uses **end time** of connection, not start time
- Remote Networks default to "all" if not specified
- Export duration: seconds to minutes typically; large exports may take hours
- File has no `.csv` extension by default — must be renamed manually

## Prerequisites
- Admin Console access with permissions to view Reports/Settings
- Report Type must be set to **Events** (not another type)

## Step-by-Step

1. Go to **Settings → Reports**
2. Click **Network Events** tab
3. Click **Generate Network Events Report**
4. Set **Report Type** to `Events`
5. Select date/time range (uses local timezone for selection)
6. Select Remote Network(s) (defaults to all)
7. Wait for background processing; optionally wait for email notification
8. Return to Reports page to download completed export

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| Report Type | Must be set to `Events` |
| Date/Time Range | Local timezone input; UTC in output |
| Remote Networks | Optional filter; defaults to all |

## Gotchas
- **Safari auto-unpack issue**: If the file appears empty in Safari, disable "Open 'Safe' files after downloading" in Safari → Preferences → General before downloading
- **Spreadsheet limits**: Large time ranges may produce millions of rows, causing spreadsheet editors to fail or hang — consider scripted processing instead
- **File extension**: Export has no `.csv` extension; manually append `.csv` after decompression for spreadsheet compatibility
- **Timezone mismatch**: Selection UI uses local time but exported timestamps are UTC — account for this when correlating with other logs
- **Connection timing**: Filter captures events by connection *end time*, so connections that started before the range but ended within it will be included

## Related Docs
- [Network Events Schema](https://www.twingate.com/docs/network-events-schema) (linked as "detailed schema" in source)
- Reports page (Settings → Reports in Admin Console)