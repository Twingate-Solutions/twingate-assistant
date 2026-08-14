---
source: https://www.twingate.com/docs/network-events-ac-export
type: docs
fetched: 2026-08-14
source_version: de74e2c479e6d7cb5760441c999c197080136e09cdb6b69878db5865d3547101
---

# Network Events Admin Console Export

## Page Title
Network Events Admin Console Export

## Summary
Twingate allows administrators to export Network Events from the Admin Console Reports page as GZIP-compressed JSON files. Exports run as background jobs and are delivered via email notification or manual page refresh. Files can be large and require decompression before use.

## Key Information
- Exports are in **GZIP format**, containing **JSON** (one event per line / JSONL format)
- Timestamps in the export are **UTC**, but the date/time range selector uses **local timezone**
- Time range filtering uses the **end time** of connections, not start time
- Remote Networks filter defaults to **all networks**
- Export schema documented separately (linked as "here" on source page)
- Large exports may take **a few hours**; typical exports complete in seconds to minutes

## Prerequisites
- Admin Console access with permissions to view Reports
- Access to Settings > Reports page

## Step-by-Step

1. Navigate to **Settings → Reports**
2. Click the **Network Events** tab
3. Click **Generate Network Events Report**
4. Set **Report Type** to `Events`
5. Select desired **date & time range** and **Remote Network(s)**
6. Wait for background processing; refresh page or await **email notification**
7. Return to Reports page to **download** the completed report

## Configuration Values
| Parameter | Options/Notes |
|-----------|---------------|
| Report Type | Must be set to `Events` |
| Date/Time Range | Local timezone input; UTC in output |
| Remote Networks | Single or multiple; defaults to all |

## Gotchas
- **Safari users**: If file appears empty, disable auto-unpack via Safari → Preferences → General → uncheck "Open 'Safe' files after downloading"
- **Large datasets**: Millions of rows can cause spreadsheet editors to crash or fail to open
- **File rename required**: After decompression, manually add `.csv` extension for spreadsheet compatibility (even though underlying format is JSON/JSONL — note the doc recommends `.csv` but data is JSON)
- **Timezone mismatch**: Input range is local time; exported timestamps are UTC — account for offset when filtering
- **Connection timing**: Filter applies to connection *end time*, not start time — connections that started before the range but ended within it will be included

## Related Docs
- Network Events export schema (referenced inline as "here" — check Twingate docs for schema detail page)
- Reports page documentation