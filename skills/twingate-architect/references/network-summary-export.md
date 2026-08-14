---
source: https://www.twingate.com/docs/network-summary-export
type: docs
fetched: 2026-08-14
source_version: fa42303de2fe8905f0c025ef2090f91c00efd7c1f4b9bab65ef28031c14f7d6b
---

# Network Summary Export

## Page Title
Network Summary Export

## Summary
Twingate allows admins to export aggregated summaries of Remote Network activity via the Admin Console Reports page. Reports are generated asynchronously and delivered as gzip-compressed JSON/CSV files. Data covers connection counts, bytes transferred, protocol usage, and relay vs. P2P breakdown per Resource.

## Key Information
- Report type: **Summary** (aggregated per Resource, not per-event)
- Output format: **gzip-compressed JSON** (one event per line); rename to `.csv` after decompression for spreadsheet use
- Timestamps in export are **UTC**; time range selection uses **local timezone**
- Time range filtering uses **connection end time**, not start time
- Reports generated in background; download via Reports page or email notification
- Large time ranges may produce millions of lines — spreadsheet editors may struggle

## Prerequisites
- Admin Console access
- Navigate to: **Settings → Reports → Network Events tab**

## Step-by-Step
1. Go to **Settings → Reports → Network Events**
2. Click **Generate Network Events Report**
3. Set **Report Type** to `Summary`
4. Select date/time range and Remote Network(s) (defaults to all)
5. Wait for background generation; refresh page or await email
6. Download from Reports page
7. Decompress gzip file; rename with `.csv` extension to open in spreadsheet editor

## Export Fields

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
| `total_bytes` | Total bytes (transferred + received) |
| `bytes_transferred` | Bytes sent |
| `bytes_received` | Bytes received |
| `protocol` | Protocols used |
| `percent_relay` | % of connections via Twingate Relay |
| `percent_p2p` | % of connections via peer-to-peer |
| `top_10_address_accessed` | Top 10 addresses accessed within Resource |

## Gotchas
- **Safari users**: If file appears empty, disable "Open 'Safe' files after downloading" (Safari → Preferences → General) before downloading
- Time range is based on **end time** of connection — connections that started before the range but ended within it will be included
- Very large exports may cause spreadsheet editor crashes; use CLI tools (`zcat`, `jq`) for large datasets
- File has no `.csv` extension by default — must be added manually after decompression

## Related Docs
- Network Events Export (detailed per-event export)
- Reports page (Settings)