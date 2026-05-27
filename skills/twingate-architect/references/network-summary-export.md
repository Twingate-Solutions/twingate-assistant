# Network Summary Export

## Page Title
Network Summary Export

## Summary
Twingate allows admins to export aggregated summaries of Remote Network activity via the Admin Console Reports page. Reports are generated asynchronously in gzip-compressed JSON (NDJSON) format and can be filtered by date range and Remote Network. Data includes connection counts, bytes transferred, relay vs. P2P percentages, and top accessed addresses.

## Key Information
- Export type: **Summary** (aggregated per Resource, not per-event)
- Output format: **gzip-compressed NDJSON** (one JSON object per line)
- Timestamps in export are **UTC**; time range selection uses **local timezone**
- Time range filtering is based on **connection end time**, not start time
- Report generated in background; notification sent via email when ready
- Default Remote Network filter: **all**

## Prerequisites
- Admin Console access
- Navigate to: **Settings → Reports → Network Events tab**

## Step-by-Step

1. Go to **Settings → Reports → Network Events**
2. Click **Generate Network Events Report**
3. Set **Report Type** to `Summary`
4. Select date/time range and Remote Network(s)
5. Wait for email notification or refresh the page
6. Return to Reports page to download

## Export Fields

| Field | Description |
|---|---|
| `resource_id` | Resource identifier |
| `resource_address` | Resource address |
| `remote_network` | Associated Remote Network name |
| `remote_network_id` | Associated Remote Network ID |
| `total_connections` | Total connection count |
| `success_connections` | Successful connections |
| `failed_connections` | Total failed connections |
| `failed_connections_dns` | DNS-related failures |
| `failed_connections_other` | Other failures |
| `total_bytes` | Total bytes (sent + received) |
| `bytes_transferred` | Bytes sent |
| `bytes_received` | Bytes received |
| `protocol` | Protocols used |
| `percent_relay` | % connections via Twingate Relay |
| `percent_p2p` | % connections via peer-to-peer |
| `top_10_address_accessed` | Top 10 accessed addresses within Resource |

## Gotchas
- **File extension**: After decompression, manually add `.csv` to filename for spreadsheet compatibility
- **Large exports**: Millions of lines possible — spreadsheet editors may fail; use CLI tools instead
- **Safari bug**: If file appears empty, **disable** "Open 'Safe' files after downloading" in Safari → Preferences → General
- Timezone mismatch: selection UI is local time, but export timestamps are UTC

## Related Docs
- Network Events Export (detailed/per-event variant)
- Reports & Analytics (Admin Console)