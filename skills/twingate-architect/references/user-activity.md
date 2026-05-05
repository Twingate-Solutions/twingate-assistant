# User Activity Reporting

## Summary
Twingate's Admin Console provides user activity and authentication event reporting for security auditing and troubleshooting. Reports can be exported as CSV/JSON files manually or synced automatically to Amazon S3. Inactive users (no resource access in 90 days) are automatically identified.

## Key Information
- **Authentication Events**: Track sign-in attempts (success/failure), IDP errors, device posture mismatches, policy blocks, MFA setup/reset — exported as JSON (GZIP)
- **Active Users Report**: Users who accessed resources in selected time range — exported as CSV (GZIP)
- **Inactive Users Report**: Accounts with no resource access in last 90 days — exported as CSV
- Exports complete in background; email notification sent when ready
- Timestamps in export are UTC; time range selection uses local timezone
- S3 sync available for continuous authentication event streaming

## Prerequisites
- Admin Console access
- Amazon S3 bucket configured (optional, for automated sync)

## Step-by-Step: Generate Export
1. Navigate to **Settings → Reports → User Activity**
2. Click **Generate User Activity Report**
3. Select report type: **Authentication Events** or **User Activity**
4. Select time range (authentication events) or report type + time range (active/inactive users)
5. Wait for background processing (minutes to hours for large exports)
6. Download from Reports page when email notification received
7. Optionally configure Amazon S3 sync for automated delivery

## Active User Report Columns
| Column | Description |
|--------|-------------|
| `user_email` | User email address |
| `last_access_date` | Last resource access timestamp |
| `total_connections` | All connections in period |
| `success_connections` | Successful connections |
| `failed_connections` | Total failed connections |
| `failed_connections_dns` | DNS-error failures |
| `failed_connections_other` | Non-DNS failures |
| `total_bytes` / `bytes_transferred` / `bytes_received` | Bandwidth metrics |
| `percent_relay` / `percent_p2p` | Connection type breakdown |
| `active_devices` | Device count at report generation |
| `num_of_client_ip` / `top_10_client_ips` | Client IP metrics |

## Authentication Event JSON Schemas
**Admin Console sign-in**: `action.type = "admin_login"` — includes user email, ID, policy ID/name

**Resource authentication**: `action.type = "reauth"` — includes user, policy, device (ID/name), resource (ID/name)

Both schemas include `version` and `time` (UTC) fields.

## Gotchas
- Export files are GZIP compressed; must decompress before use — rename to `.csv` after decompression
- **Safari users**: Disable "Open 'Safe' files after downloading" (Safari → Preferences → General) to prevent empty file issue from auto-unpack
- Time range filter uses local timezone but export timestamps are UTC — potential confusion when correlating
- Inactive user threshold is fixed at 90 days (not configurable)
- Active device count reflects report generation time, not the selected time period

## Related Docs
- Amazon S3 Sync configuration
- Device Posture policies
- Resource Policies