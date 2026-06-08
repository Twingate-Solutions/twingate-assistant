# Network Summary Export

## Page Title
Network Summary Export

## Summary
Twingate allows admins to export aggregated summaries of Remote Network activity from the Admin Console's Reports page. Reports are generated asynchronously and delivered as gzip-compressed JSON files. Each summary provides connection statistics, byte transfer data, and routing information per resource.

## Key Information
- Export format: gzip-compressed, newline-delimited JSON (one event per line)
- Timestamps in export are **UTC**; time range selection uses **local timezone**
- Time range filter uses **end time** of connection (not start time)
- Remote Networks default to "all" if not specified
- Reports generate in background; notification sent via email when ready
- Large exports may contain millions of lines — not ideal for spreadsheet editors

## Prerequisites
- Admin Console access
- Navigate to: **Settings → Reports → Network Events tab**

## Step-by-Step
1. Go to **Settings → Reports → Network Events**
2. Click **Generate Network Events Report**
3. Set **Report Type** to **Summary**
4. Select date/time range and Remote Network(s)
5. Wait for background generation (refresh page or check email)
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
| `failed_connections_other` | Non-DNS failures |
| `total_bytes` | Total bytes transferred + received |
| `bytes_transferred` | Bytes sent |
| `bytes_received` | Bytes received |
| `protocol` | Protocols used |
| `percent_relay` | % connections via Twingate Relay |
| `percent_p2p` | % connections via peer-to-peer |
| `top_10_address_accessed` | Top 10 addresses within resource |

## Gotchas
- **Safari users**: If file appears empty, **disable** "Open 'Safe' files after downloading" (Safari → Preferences → General) before downloading
- After decompression, manually add `.csv` extension to open in spreadsheet editors
- Spreadsheet editors may struggle with very large exports — use CLI tools for large datasets
- Time zone mismatch: selection UI is local time, but exported timestamps are UTC

## Related Docs
- Network Events Export (raw event-level export, as opposed to summary)
- Reports page documentation