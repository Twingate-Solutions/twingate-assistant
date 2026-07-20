# User Activity Reports

## Summary
Twingate's Admin Console provides user activity reporting including authentication event logs and active/inactive user reports. Reports can be manually exported as CSV/JSON files or automatically synced to Amazon S3. Authentication events help troubleshoot IDP errors, device posture mismatches, and policy blocks.

## Key Information
- **Authentication Events**: Track sign-in attempts (success/failure) to Twingate Client and Resource Policies; exported as JSON/GZIP
- **Active Users Report**: Users who accessed Resources in selected time window; exported as CSV/GZIP
- **Inactive Users Report**: Automatically identifies accounts with no Resource access in last **90 days**; exported as CSV/GZIP
- Timestamps in exports are **UTC**; time range selection uses **local timezone**
- Export delivery is async—email notification when ready; most complete in minutes, large exports may take hours
- S3 sync available for continuous authentication event streaming

## Prerequisites
- Admin Console access
- Amazon S3 bucket configured (optional, for auto-sync)

## Step-by-Step: Generate Export
1. Go to **Settings → Reports → User Activity**
2. Click **Generate User Activity Report**
3. Select report type: **Authentication Events** or **User Activity**
4. Select time range
5. For User Activity: choose **Active** or **Inactive** users
6. Wait for email notification
7. Return to Reports page to download

## Configuration Values
No CLI flags or env vars. Report types:
- `admin_login` — Admin Console sign-in event
- `reauth` — Resource authentication event

## Active User Report Columns
| Column | Description |
|--------|-------------|
| `user_email` | User email |
| `last_access_date` | Last Resource access timestamp |
| `total_connections` | All connections in period |
| `success_connections` | Successful connections |
| `failed_connections` | Total failed connections |
| `failed_connections_dns` | DNS-error failures |
| `failed_connections_other` | Non-DNS failures |
| `total_bytes` | Total bytes transferred |
| `bytes_transferred` | Bytes sent to Resources |
| `bytes_received` | Bytes received by user |
| `percent_relay` | % connections via relay |
| `percent_p2p` | % peer-to-peer connections |
| `active_devices` | Active device count at report time |
| `num_of_client_ip` | Unique IPs used |
| `top_10_client_ips` | Top 10 source IPs |

## Authentication Event JSON Schema Fields
- `version`, `time` (UTC), `action.type`, `action.user.email`, `action.user.id`
- `action.user.policy.id/name`
- Resource events also include: `action.user.device.id/name`, `action.user.resource.id/name`

## Gotchas
- Exports are GZIP compressed—must decompress before use; add `.csv` extension after decompression
- **Safari**: Disable "Open 'safe' files after downloading" (Safari → Preferences → General) to prevent empty file issue
- Inactive users threshold is fixed at **90 days**—not configurable
- Time range filter uses local timezone but export timestamps are UTC

## Related Docs
- Amazon S3 Sync setup (referenced but separate doc)
- Resource Policies documentation
- Device Posture documentation