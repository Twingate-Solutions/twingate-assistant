# Network Summary Export

## Page Title
Network Summary Export

## Summary
Twingate allows admins to export aggregated summaries of Remote Network activity via the Admin Console Reports page. Reports are generated asynchronously in gzip-compressed JSON format and contain per-resource connection statistics for a selected date range and network scope.

## Key Information
- Export type: **Summary** (aggregated stats per resource, not raw events)
- Output format: gzip-compressed JSON (one event per line / JSONL)
- Timestamps in export are **UTC**; time range selection uses **local timezone**
- Time range filtering uses connection **end time**, not start time
- Reports generated in background; notification sent via email when ready
- File must be renamed with `.csv` extension after decompression to open in spreadsheet editors

## Prerequisites
- Admin Console access
- Navigate to: **Settings → Reports → Network Events tab**

## Step-by-Step

1. Go to **Settings → Reports → Network Events**
2. Click **Generate Network Events Report**
3. Set **Report Type** to `Summary`
4. Select date/time range and Remote Network(s) (defaults to all networks)
5. Wait for background generation; refresh page or await email notification
6. Return to Reports page to download completed report
7. Decompress the `.gz` file and rename with `.csv` extension

## Export Fields

| Field | Description |
|---|---|
| `resource_id` | Resource identifier |
| `resource_address` | Resource address |
| `remote_network` | Associated Remote Network name |
| `remote_network_id` | Remote Network identifier |
| `total_connections` | Total connection count |
| `success_connections` | Successful connections |
| `failed_connections` | Total failed connections |
| `failed_connections_dns` | DNS-related failures |
| `failed_connections_other` | Non-DNS failures |
| `total_bytes` | Total bytes transferred + received |
| `bytes_transferred` | Bytes sent |
| `bytes_received` | Bytes received |
| `protocol` | Protocols used |
| `percent_relay` | % connections via Twingate Relay |
| `percent_p2p` | % peer-to-peer connections |
| `top_10_address_accessed` | Top 10 addresses within the resource |

## Gotchas
- **Safari users**: If file appears empty, **disable** "Open 'Safe' files after downloading" (Safari → Preferences → General) before downloading
- Large time ranges or high-activity environments may produce millions of rows — avoid opening directly in spreadsheet editors
- Time zone mismatch: selection UI is local time, but exported timestamps are UTC
- Remote Network filter defaults to "all" if not specified

## Related Docs
- Network Events (raw/detailed export — separate report type)
- Twingate Reports page (Admin Console)