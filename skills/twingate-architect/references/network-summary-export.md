# Network Summary Export

## Page Title
Network Summary Export

## Summary
Twingate allows admins to export aggregated summaries of Remote Network activity via the Admin Console Reports page. Reports are generated asynchronously in gzip-compressed JSON/CSV format and delivered via email notification when ready.

## Key Information
- Export type: **Summary** (aggregated per-resource stats, not raw event logs)
- Output format: gzip-compressed JSON (one event per line); rename to `.csv` after decompression
- Timestamps in export are **UTC**; time range selection uses **local timezone**
- Time range filtering is based on **connection end time**, not start time
- Remote Networks default to "all" if not specified
- Large exports may contain millions of lines — avoid opening directly in spreadsheet editors

## Prerequisites
- Admin Console access
- Access to Settings → Reports → Network Events tab

## Step-by-Step

1. Navigate to **Settings → Reports**
2. Click **Network Events** tab
3. Click **Generate Network Events Report**
4. Set **Report Type** to `Summary`
5. Select date/time range and Remote Network(s)
6. Wait for background generation; refresh page or await email notification
7. Return to Reports page to download when ready
8. Decompress gzip file; rename with `.csv` extension to open in spreadsheet editor

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
| `percent_relay` | % of connections via Twingate Relay |
| `percent_p2p` | % of peer-to-peer connections |
| `top_10_address_accessed` | Top 10 addresses accessed within resource |

## Gotchas
- **Safari users**: If downloaded file appears empty, **disable** "Open 'safe' files after downloading" (Safari → Preferences → General) — Safari auto-unpacks gzip but may corrupt the file display
- Time range is local timezone on input but **UTC in output** — account for offset when cross-referencing
- Very large exports can crash spreadsheet editors; use CLI tools (`jq`, `awk`) for large datasets
- File has no `.csv` extension by default — must rename manually after decompression

## Related Docs
- Network Events (raw event export — distinct from Summary)
- Twingate Reports / Admin Console Settings