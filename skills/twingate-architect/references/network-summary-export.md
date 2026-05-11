# Network Summary Export

## Page Title
Network Summary Export

## Summary
Twingate allows admins to export aggregated summaries of Remote Network activity from the Admin Console's Reports page. Reports are generated asynchronously in gzip-compressed JSON format and can be filtered by date range and Remote Network. Each line in the export represents a resource-level summary of connection statistics.

## Key Information
- Reports are generated in the background; download via Reports page or email notification
- Export format: gzip-compressed, newline-delimited JSON (`.json.gz`)
- Time range uses **local timezone** for selection, but export timestamps are in **UTC**
- Time filtering is based on **connection end time**, not start time
- Remote Networks default to "all" if not specified
- Large exports may contain millions of lines — avoid opening directly in spreadsheet editors

## Prerequisites
- Admin Console access
- Navigate to: **Settings → Reports → Network Events tab**

## Step-by-Step

1. Go to **Settings → Reports → Network Events**
2. Click **Generate Network Events Report**
3. Set **Report Type** to `Summary`
4. Select date/time range and target Remote Network(s)
5. Wait for background generation (refresh page or await email)
6. Return to Reports page to download

## Export Fields

| Field | Description |
|---|---|
| `resource_id` | Resource identifier |
| `resource_address` | Resource address |
| `remote_network` | Associated Remote Network name |
| `remote_network_id` | Remote Network identifier |
| `total_connections` | All connection attempts |
| `success_connections` | Successful connections |
| `failed_connections` | Total failed connections |
| `failed_connections_dns` | DNS-related failures |
| `failed_connections_other` | Non-DNS failures |
| `total_bytes` | Total bytes transferred + received |
| `bytes_transferred` | Bytes sent |
| `bytes_received` | Bytes received |
| `protocol` | Protocols used |
| `percent_relay` | % routed via Twingate Relay |
| `percent_p2p` | % routed peer-to-peer |
| `top_10_address_accessed` | Top 10 addresses accessed within resource |

## Gotchas
- **Safari users**: If file appears empty, disable "Open 'safe' files after downloading" (Safari → Preferences → General) before downloading
- After decompression, **manually add `.csv` extension** to open in spreadsheet editors
- File is JSON format despite `.csv` rename suggestion — each line is a JSON object
- Millions of rows possible for large environments; use programmatic tools (e.g., `jq`, pandas) instead of Excel/Sheets

## Related Docs
- Network Events Export (detailed/raw event logs)
- Twingate Reports/Analytics documentation