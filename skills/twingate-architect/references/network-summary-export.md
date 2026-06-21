# Network Summary Export

## Page Title
Network Summary Export

## Summary
Twingate allows admins to export summarized Remote Network activity reports from the Admin Console. Reports are generated asynchronously in gzip-compressed JSON format and contain per-resource connection statistics for a selected time range and network scope.

## Key Information
- Reports are generated in the background; download via Admin Console or email notification
- Timestamps in the export are **UTC**, but the time range selector uses **local timezone**
- Time range filtering uses **connection end time**, not start time
- Remote Networks default to "all" if not specified
- Export format: gzip-compressed, newline-delimited JSON (one event per line)
- Add `.csv` extension after decompression to open in spreadsheet editors

## Prerequisites
- Admin Console access
- Access to Settings > Reports > Network Events tab

## Step-by-Step

1. Navigate to **Settings → Reports**
2. Click **Network Events** tab
3. Click **Generate Network Events Report**
4. Set **Report Type** to `Summary`
5. Select date/time range and target Remote Network(s)
6. Wait for background generation; refresh page or await email notification
7. Return to Reports page to download
8. Decompress gzip file; rename with `.csv` extension before opening

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
| `top_10_address_accessed` | Top 10 addresses within resource |

## Gotchas
- Large time ranges or high-activity environments may produce millions of rows — spreadsheet editors may fail to open
- Safari may show file as empty if "Open safe files after downloading" is enabled; **disable** that setting in Safari → Preferences → General
- File has no `.csv` extension by default — must be added manually after decompression
- Time range filter is based on connection **end time**, which may exclude long-running connections that started before the range

## Related Docs
- Network Events (detailed export, non-summary variant)
- Twingate Reports/Settings documentation