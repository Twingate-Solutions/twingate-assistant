# Network Summary Export

## Page Title
Network Summary Export

## Summary
Twingate allows admins to export aggregated summaries of Remote Network activity from the Admin Console Reports page. Reports are generated asynchronously in gzip-compressed JSON format and can be filtered by date range and Remote Network. Output includes connection counts, byte transfer stats, and routing breakdowns per Resource.

## Key Information
- Report type: **Summary** (aggregated per Resource, not per-event)
- Output format: gzip-compressed JSON (one event per line)
- Timestamps in export are **UTC**; time range selection uses **local timezone**
- Time range filtering uses **connection end time**, not start time
- Default Remote Network filter: **all**
- Generation is async — wait for email notification or refresh page to check status

## Prerequisites
- Admin Console access
- Navigate to: **Settings → Reports → Network Events tab**

## Step-by-Step
1. Go to **Settings → Reports**
2. Click **Network Events** tab
3. Click **Generate Network Events Report**
4. Set **Report Type** to `Summary`
5. Select date/time range and Remote Network(s)
6. Wait for email notification or refresh Reports page
7. Download completed report from Reports page

## Export Fields (CSV Columns)
| Field | Description |
|---|---|
| `resource_id` | Resource ID |
| `resource_address` | Resource address |
| `remote_network` | Associated Remote Network name |
| `remote_network_id` | Remote Network ID |
| `total_connections` | Total connection count |
| `success_connections` | Successful connections |
| `failed_connections` | Total failed connections |
| `failed_connections_dns` | DNS-related failures |
| `failed_connections_other` | Other failures |
| `total_bytes` | Total bytes transferred + received |
| `bytes_transferred` | Bytes sent |
| `bytes_received` | Bytes received |
| `protocol` | Protocols used |
| `percent_relay` | % routed through Twingate Relay |
| `percent_p2p` | % routed peer-to-peer |
| `top_10_address_accessed` | Top 10 addresses within Resource |

## Gotchas
- File extension must be manually added (`.csv`) after decompression — file is not automatically named with extension
- Large time ranges or high-activity environments may produce millions of rows — may crash spreadsheet editors
- **Safari**: If file appears empty, **uncheck** "Open 'Safe' files after downloading" (Safari → Preferences → General) to disable auto-unpack interference
- Underlying format is JSON (newline-delimited), not native CSV despite `.csv` rename convention

## Related Docs
- Network Events Export (detailed/raw event export, distinct from Summary)
- Twingate Reports/Admin Console documentation