# User Activity Reporting

## Summary
Twingate's Admin Console provides user activity reporting including authentication event logs and active/inactive user reports. Reports can be exported manually as JSON/CSV or synced automatically to Amazon S3.

## Key Information
- **Authentication Events**: Track sign-in attempts (success/failure), IDP errors, device posture mismatches, policy blocks, MFA setup/reset actions
- **Active Users Report**: Users who accessed Resources in the selected time range; includes connection stats, bytes transferred, IP info
- **Inactive Users Report**: Automatically flags accounts with no Resource access in last 90 days
- Export formats: Authentication events → JSON (GZIP); User activity → CSV (GZIP)
- Timestamps in exports are UTC; time range selection uses local timezone
- Export delivery is async via email; most complete in minutes, large exports may take hours
- Continuous sync available via Amazon S3 for authentication events

## Prerequisites
- Admin Console access
- Amazon S3 bucket configured (for automated sync only)

## Step-by-Step: Generating a Report
1. Navigate to **Settings → Reports → User Activity**
2. Click **Generate User Activity Report**
3. Select report type: **Authentication Events** or **User Activity**
4. Select time range (and active/inactive for User Activity)
5. Wait for email notification when complete
6. Return to Reports page to download
7. Optionally configure S3 sync for ongoing authentication event exports

## Viewing Exports
- Files are GZIP compressed; decompress with any standard tool
- After decompression, add `.csv` extension to open in spreadsheet editors
- **Safari gotcha**: Disable "Open 'safe' files after downloading" (Safari → Preferences → General) to prevent automatic unpacking issues

## Active User Report Columns
| Column | Description |
|--------|-------------|
| `user_email` | User email |
| `last_access_date` | Last Resource access timestamp |
| `total_connections` | All connections in period |
| `success_connections` / `failed_connections` | Connection outcomes |
| `failed_connections_dns` / `failed_connections_other` | Failure categorization |
| `total_bytes` / `bytes_transferred` / `bytes_received` | Traffic metrics |
| `percent_relay` / `percent_p2p` | Connection type breakdown |
| `active_devices` | Device count at report generation |
| `top_10_client_ips` | Top source IPs |

## Authentication Event JSON Schema
Two event types:
- **`admin_login`**: Contains `version`, `time`, `action.type`, `user.email`, `user.id`, `policy.id/name`
- **`reauth`** (Resource auth): Same as above plus `device.id/name` and `resource.id/name`

## Gotchas
- Time range filter uses **local timezone** but export timestamps are **UTC**
- Inactive users threshold is fixed at **90 days** (not configurable)
- `active_devices` reflects count **at time of report generation**, not during the period
- Large exports can take **hours**; download link only available via Reports page after email notification

## Related Docs
- Amazon S3 Sync configuration
- Resource Policies
- Device Posture