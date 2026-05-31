# Network Summary Export

## Page Title
Network Summary Export

## Summary
Twingate allows admins to export aggregated summaries of Remote Network connection activity via the Admin Console Reports page. Reports are generated asynchronously in gzip-compressed JSON (NDJSON) format and can be filtered by date range and Remote Network. Output includes connection counts, byte transfer metrics, and routing statistics per Resource.

## Key Information
- Reports are generated in the background; notification sent via email when ready
- Export format: gzip-compressed NDJSON (one JSON object per line)
- Timestamps in export are **UTC**, but date range selection uses **local timezone**
- Time range filtering is based on **connection end time**, not start time
- Default Remote Network filter: all networks

## Prerequisites
- Admin Console access
- Access to Settings > Reports page

## Step-by-Step

1. Navigate to **Settings → Reports**
2. Click **Network Events** tab
3. Click **Generate Network Events Report**
4. Set **Report Type** to **Summary**
5. Select date/time range and Remote Network(s)
6. Wait for background generation (refresh page or await email)
7. Return to Reports page to download

## Export Fields

| Field | Description |
|-------|-------------|
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
| `percent_relay` | % routed through Twingate Relay |
| `percent_p2p` | % routed peer-to-peer |
| `top_10_address_accessed` | Top 10 addresses accessed within Resource |

## Gotchas
- Large time ranges or high-activity environments may produce millions of lines — may crash spreadsheet editors
- Add `.csv` extension manually after decompression for spreadsheet compatibility
- **Safari users**: if file appears empty, **uncheck** "Open 'safe' files after downloading" in Safari > Preferences > General
- Time zone mismatch: selection UI uses local time, exported timestamps are UTC

## Related Docs
- Network Events Export (detailed/raw event export)
- Twingate Reports/Settings documentation