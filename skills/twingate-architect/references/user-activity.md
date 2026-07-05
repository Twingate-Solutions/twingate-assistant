# User Activity Reports

## Page Title
User Activity (Twingate Admin Console Reporting)

## Summary
Twingate provides user activity and authentication event reporting via the Admin Console. Admins can export authentication events as JSON (manual or S3 sync) and user activity reports as CSV. Reports help troubleshoot connection issues, audit MFA events, and manage inactive accounts.

## Key Information
- **Authentication Events**: Tracks sign-in attempts (success/failure), IDP errors, device posture mismatches, policy blocks, MFA setup/resets
- **Active Users Report**: Includes connections, bytes transferred, relay vs P2P breakdown, client IPs
- **Inactive Users Report**: Auto-identifies accounts with no Resource access in last **90 days**
- Export formats: Authentication events → **JSON (GZIP)**; User activity → **CSV (GZIP)**
- Timestamps in exports are **UTC**; time range selection uses **local timezone**
- Large exports may take **a few hours**; completion notification sent via **email**
- Authentication events can be synced automatically to **Amazon S3**

## Prerequisites
- Admin Console access
- Amazon S3 bucket configured (for automatic sync only)

## Step-by-Step: Generate Export
1. Go to **Settings → Reports → User Activity**
2. Click **Generate User Activity Report**
3. Select report type: **Authentication Events** or **User Activity**
4. For Authentication Events: select time range
5. For User Activity: select **Active** or **Inactive** users + time range
6. Wait for email notification (minutes to hours)
7. Return to Reports page to download
8. Optionally configure **Amazon S3 sync** for ongoing authentication event export

## Configuration Values

### Active Users Report CSV Columns
| Column | Description |
|--------|-------------|
| `user_email` | User email |
| `last_access_date` | Last Resource access timestamp |
| `total_connections` | All connections in period |
| `success_connections` | Successful connections |
| `failed_connections` | All failed connections |
| `failed_connections_dns` | DNS-related failures |
| `failed_connections_other` | Non-DNS failures |
| `total_bytes` | Total bytes transferred |
| `bytes_transferred` | Bytes sent to Resources |
| `bytes_received` | Bytes received by user |
| `percent_relay` | % connections via relay |
| `percent_p2p` | % peer-to-peer connections |
| `active_devices` | Active devices at report time |
| `num_of_client_ip` | Unique client IPs used |
| `top_10_client_ips` | Top 10 client IPs |

### Authentication Event JSON Fields
- `version`, `time` (UTC), `action.type` (e.g., `admin_login`, `reauth`)
- `action.user`: `email`, `id`, `policy.id`, `policy.name`
- Resource auth additionally includes: `device.id`, `device.name`, `resource.id`, `resource.name`

## Gotchas
- Exports are **GZIP compressed** — rename decompressed file with `.csv` extension for spreadsheet compatibility
- **Safari users**: Disable "Open safe files after downloading" (Safari → Preferences → General) to prevent empty file issues
- Inactive users threshold is fixed at **90 days** — not configurable
- Time range UI uses local timezone but export timestamps are UTC

## Related Docs
- Amazon S3 Sync setup
- Resource Policies
- Device Posture