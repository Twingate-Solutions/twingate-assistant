---
source: https://www.twingate.com/docs/user-activity
type: docs
fetched: 2026-08-14
source_version: 808dfcb59632a32ebbaff724e66a2873ee0c68714f5d9ddedd6f2640b6628534
---

# User Activity Reporting

## Page Title
User Activity

## Summary
Twingate Admin Console provides user activity reporting including authentication event logs, active user reports, and inactive user reports. Reports can be exported manually as CSV/JSON (GZIP) or synced automatically to Amazon S3. Inactive users are automatically flagged after 90 days without Resource access.

## Key Information
- **Authentication Events**: Track sign-in attempts (success/fail), IDP errors, device posture mismatches, policy blocks, MFA setup/resets
- **Active Users Report**: CSV with connection stats, bytes transferred, relay vs P2P percentages, client IPs
- **Inactive Users Report**: Automatically identifies accounts with no Resource access in last 90 days
- Export formats: JSON (authentication events), CSV (user activity) — both GZIP compressed
- Timestamps in exports are UTC; time range selection uses local timezone
- Large exports may take several hours; completion notification sent via email
- S3 sync available for continuous authentication event streaming

## Prerequisites
- Admin Console access
- Amazon S3 bucket configured (for automatic sync only)

## Step-by-Step: Generating a Report
1. Navigate to **Settings → Reports → User Activity**
2. Click **Generate User Activity Report**
3. Select report type: **Authentication Events** or **User Activity**
4. Select time range (Authentication Events) or report subtype (Active/Inactive Users) + time range
5. Wait for email notification when export is ready
6. Return to Reports page to download
7. Optionally configure Amazon S3 sync for automatic authentication event export

## Viewing Exports
- Files are GZIP compressed — decompress with any standard tool
- After decompression, add `.csv` extension to open in spreadsheet editors
- **Safari gotcha**: Disable "Open 'Safe' files after downloading" (Safari → Preferences → General) to prevent empty file issue

## Active User Report Columns
| Column | Description |
|--------|-------------|
| `user_email` | User email |
| `last_access_date` | Last Resource access timestamp |
| `total_connections` | Total connections in period |
| `success_connections` / `failed_connections` | Connection outcomes |
| `failed_connections_dns` / `failed_connections_other` | Failure breakdown |
| `total_bytes` / `bytes_transferred` / `bytes_received` | Bandwidth metrics |
| `percent_relay` / `percent_p2p` | Connection type distribution |
| `active_devices` | Device count at report generation time |
| `num_of_client_ip` / `top_10_client_ips` | Client IP usage |

## Authentication Event JSON Schema
Two event types with key fields:
- **`admin_login`**: `version`, `time`, `action.type`, `action.user.email`, `action.user.id`, `action.user.policy.{id,name}`
- **`reauth`**: Same as above plus `action.user.device.{id,name}` and `action.user.resource.{id,name}`

## Gotchas
- Time range selection uses **local timezone** but exported timestamps are **UTC**
- Safari auto-unzip can corrupt downloads — disable the safe file setting
- Inactive threshold is fixed at **90 days** (not configurable)
- Active device count reflects time of report generation, not the selected period

## Related Docs
- Amazon S3 Sync configuration
- Resource Policies
- Device Posture