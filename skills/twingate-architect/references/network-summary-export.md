# Network Summary Export

## Page Title
Network Summary Export

## Summary
Twingate allows admins to export summarized Remote Network activity reports from the Admin Console. Reports are generated asynchronously in gzip-compressed JSON format and contain per-resource connection statistics for a specified time range and network selection.

## Key Information
- Reports are generated in the background; download via Admin Console or email notification
- Timestamps in the export are **UTC**, but the time range selection uses **local timezone**
- Time range is based on **connection end time**, not start time
- Default Remote Networks selection is "all"
- Output format: **gzip-compressed, newline-delimited JSON** (not CSV natively)
- Large datasets may contain millions of lines — avoid opening directly in spreadsheet editors

## Prerequisites
- Admin Console access
- Access to Reports page under Settings

## Step-by-Step

1. Go to **Settings → Reports**
2. Click **Network Events** tab
3. Click **Generate Network Events Report**
4. Set **Report Type** to `Summary`
5. Select date/time range and Remote Network(s)
6. Wait for background generation (refresh page or await email)
7. Return to Reports page to download

## Export Fields

| Field | Description |
|---|---|
| `resource_id` | Resource ID |
| `resource_address` | Resource address |
| `remote_network` | Associated Remote Network name |
| `remote_network_id` | Remote Network ID |
| `total_connections` | Total connection count |
| `success_connections` | Successful connections |
| `failed_connections` | Failed connections total |
| `failed_connections_dns` | DNS-related failures |
| `failed_connections_other` | Other failures |
| `total_bytes` | Total bytes transferred + received |
| `bytes_transferred` | Bytes sent |
| `bytes_received` | Bytes received |
| `protocol` | Protocols used |
| `percent_relay` | % routed through Twingate Relay |
| `percent_p2p` | % routed peer-to-peer |
| `top_10_address_accessed` | Top 10 accessed addresses within Resource |

## Gotchas
- File has **no `.csv` extension** after decompression — rename manually before opening in spreadsheet software
- **Safari users**: if file appears empty, **uncheck** "Open 'Safe' files after downloading" in Safari → Preferences → General
- Large exports may crash or hang spreadsheet editors — use CLI tools or data processing pipelines instead
- Timezone mismatch: selection UI uses local time, export timestamps are UTC

## Related Docs
- Network Events (detailed/raw export variant)
- Twingate Reports page (Admin Console)