## Network Events Admin Console Export

Exports per-connection network event logs from the Admin Console as a GZIP-compressed CSV. Each connection is one row; timestamps are UTC even though the selection UI shows local time.

**Key Information:**
- Export path: Settings → Reports → Network Events tab → Generate Network Events Report → Report Type: Events
- Filter by date range and Remote Network(s) (defaults to all)
- Time range uses local timezone for selection; exported timestamps are UTC
- Time filter uses connection **end time**, not start time
- Export runs in background; email notification sent when ready

**Step-by-Step:**
1. Settings → Reports → Network Events tab
2. Click Generate Network Events Report
3. Set Report Type = Events
4. Select date/time range and Remote Network(s)
5. Download from Reports page once complete (or via email link)

**Gotchas:**
- Large exports (millions of rows) may crash spreadsheet editors -- narrow the time range or filter by Remote Network
- After decompressing the GZIP, add `.csv` to the filename manually for spreadsheet apps to open it
- Safari: disable "Open 'safe' files after downloading" to avoid empty file on auto-unpack

**Related Docs:**
- /docs/detailed-network-event-schema -- Full CSV and JSON field reference
- /docs/network-summary-export -- Aggregate per-Resource summary export
- /docs/syncing-data-to-s3 -- Continuous S3 export
