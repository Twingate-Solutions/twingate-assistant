# User Activity Reports

## Summary
Twingate Admin Console provides user activity reporting including authentication event logs and active/inactive user reports. Reports can be manually exported as CSV/JSON or automatically synced to Amazon S3. Authentication events help troubleshoot connection failures, IDP errors, device posture mismatches, and policy blocks.

## Key Information
- **Authentication Events**: Track sign-in attempts (success/fail) to Twingate Client and Resource Policies; exported as JSON (GZIP)
- **Active Users Report**: Users who accessed Resources in selected time range; exported as CSV (GZIP)
- **Inactive Users Report**: Automatically identifies accounts with no Resource access in last **90 days**
- Timestamps in exports are **UTC**; time range selection uses **local timezone**
- Export delivered via email; most complete in minutes, large exports up to hours
- S3 sync available for continuous authentication event streaming

## Prerequisites
- Admin Console access
- Amazon S3 bucket configured (for automated sync only)

## Step-by-Step: Generate Export
1. Navigate to **Settings → Reports → User Activity**
2. Click **Generate User Activity Report**
3. Select report type: **Authentication Events** or **User Activity**
4. Select time range
5. For User Activity, select **Active** or **Inactive** users
6. Wait for email notification, then return to Reports page to download
7. Optionally configure Amazon S3 sync for authentication events

## Viewing Exports
- Format: **GZIP compressed**; decompress with any standard tool
- Add `.csv` extension after decompression for spreadsheet compatibility
- **Safari issue**: Disable "Open safe files after downloading" (Safari → Preferences → General) to prevent empty file behavior

## Active User Report Columns
| Column | Description |
|--------|-------------|
| `user_email` | User email |
| `last_access_date` | Last Resource access timestamp |
| `total_connections` | All connections in period |
| `success_connections` / `failed_connections` | By outcome |
| `failed_connections_dns` / `failed_connections_other` | Failure breakdown |
| `total_bytes` / `bytes_transferred` / `bytes_received` | Data transfer stats |
| `percent_relay` / `percent_p2p` | Connection type distribution |
| `active_devices` | Device count at report generation |
| `top_10_client_ips` | Top source IPs |

## Authentication Event JSON Schema
Two event types:
- **`admin_login`**: Contains `version`, `time`, `action.type`, `user.email`, `user.id`, `policy.id`, `policy.name`
- **`reauth`**: Same as above plus `device.id`, `device.name`, `resource.id`, `resource.name`

## Gotchas
- Inactive users threshold is fixed at **90 days** (not configurable)
- Export timestamps are UTC regardless of local timezone used for selection
- Large exports can take **hours**—plan accordingly for time-sensitive audits
- Safari auto-unzip can corrupt GZIP files; disable the setting before downloading

## Related Docs
- Amazon S3 Sync configuration
- Resource Policies
- Device Posture
- Admin Console Settings