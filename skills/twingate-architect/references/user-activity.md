# User Activity - Twingate Documentation

## Page Title
User Activity Reports & Authentication Event Logging

## Summary
Twingate's Admin Console provides user activity reporting including authentication event logs, active user reports, and inactive user reports. Reports can be manually exported (JSON for auth events, CSV for user activity) or synced automatically to Amazon S3. Inactive users are automatically identified as accounts with no Resource access in the past 90 days.

## Key Information
- **Authentication events**: Track sign-in attempts, IDP errors, device posture mismatches, policy blocks, MFA setup/reset
- **Active Users Report**: Includes access timestamps, connection types, byte transfer stats, relay vs P2P percentages
- **Inactive Users Report**: Accounts with no Resource access in last 90 days
- **Export formats**: Authentication events → JSON (GZIP); User activity → CSV (GZIP)
- **Timestamps**: Selection UI uses local timezone; exported data timestamps are in UTC
- **S3 sync**: Available for authentication events (continuous/automated)

## Prerequisites
- Admin Console access
- Amazon S3 bucket configured (for automated sync only)

## Step-by-Step: Generating a Report
1. Go to **Settings → Reports → User Activity**
2. Click **Generate User Activity Report**
3. Select report type: **Authentication Events** or **User Activity**
4. Set time range (auth events window or active/inactive user window)
5. Report generates in background; email notification sent on completion
6. Return to Reports page to download
7. Optionally configure Amazon S3 sync for auth events

## Viewing Exports
- Files are GZIP compressed; use any standard decompression tool
- After decompression, add `.csv` extension to open in spreadsheet editors
- **Safari issue**: Disable "Open 'Safe' files after downloading" (Safari → Preferences → General) to prevent empty file issue

## Active User Report Columns
| Column | Description |
|--------|-------------|
| `user_email` | User's email address |
| `last_access_date` | Last Resource access timestamp |
| `total_connections` | All connections in period |
| `success_connections` / `failed_connections` | Connection outcomes |
| `failed_connections_dns` / `failed_connections_other` | Failure breakdown |
| `total_bytes`, `bytes_transferred`, `bytes_received` | Traffic stats |
| `percent_relay` / `percent_p2p` | Connection type distribution |
| `active_devices` | Active device count at report generation |
| `top_10_client_ips` | Top 10 source IPs |

## Authentication Event JSON Schema
Two event types:
- **`admin_login`**: Contains `version`, `time`, `action.type`, `user.email`, `user.id`, `policy.id`, `policy.name`
- **`reauth`** (Resource auth): Adds `device.id`, `device.name`, `resource.id`, `resource.name`

## Gotchas
- Large exports may take several hours
- Time range filter uses local timezone but exported timestamps are UTC — account for offset when filtering
- Safari auto-unpack can produce empty files; disable the feature before downloading
- Inactive threshold is fixed at 90 days (not configurable)
- S3 sync only available for authentication events, not user activity CSVs

## Related Docs
- Amazon S3 Sync setup
- Resource Policies
- Device Posture
- Admin Console Settings