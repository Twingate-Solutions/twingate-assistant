# User Activity Reporting

## Page Title
User Activity

## Summary
Twingate Admin Console provides user activity reporting including authentication event logs and active/inactive user reports. Admins can export data manually as CSV/JSON or sync to Amazon S3. Reports help troubleshoot connection issues and manage user lifecycle.

## Key Information
- **Authentication Events**: Tracks sign-in attempts (success/failure), IDP errors, device posture mismatches, policy blocks, MFA setup/reset
- **Active Users Report**: Users who accessed Resources in the selected time window
- **Inactive Users Report**: Automatically flags accounts with no Resource access in **90+ days**
- Export formats: **JSON** (authentication events), **CSV** (user activity), delivered via **GZIP**
- Timestamps in exports are **UTC**; time range selection uses **local timezone**
- Large exports may take several hours; completion notification sent via email
- Authentication events can be synced to **Amazon S3** automatically

## Prerequisites
- Admin Console access
- Amazon S3 bucket configured (for automated sync only)

## Step-by-Step: Generate Export
1. Settings → **Reports** → **User Activity**
2. Click **Generate User Activity Report**
3. Select report type: **Authentication Events** or **User Activity**
4. For Authentication Events: select time range
5. For User Activity: select **Active** or **Inactive** users + time range
6. Wait for email notification (minutes to hours)
7. Return to Reports page to download
8. Optionally configure **Amazon S3 sync** for ongoing authentication event delivery

## Configuration Values

### Active User Report CSV Columns
| Column | Description |
|--------|-------------|
| `user_email` | User email |
| `last_access_date` | Last Resource access timestamp |
| `total_connections` | All connections in period |
| `success_connections` | Successful connections |
| `failed_connections` | Total failed connections |
| `failed_connections_dns` | DNS-related failures |
| `failed_connections_other` | Non-DNS failures |
| `total_bytes` / `bytes_transferred` / `bytes_received` | Bandwidth metrics |
| `percent_relay` / `percent_p2p` | Connection type breakdown |
| `active_devices` | Device count at report generation time |
| `num_of_client_ip` / `top_10_client_ips` | Client IP metrics |

### Authentication Event JSON Schema Fields
- `version`, `time` (UTC), `action.type` (e.g., `admin_login`, `reauth`)
- `action.user`: `email`, `id`, `policy.id`, `policy.name`
- Resource auth adds: `device.id`, `device.name`, `resource.id`, `resource.name`

## Gotchas
- **Safari users**: Disable "Open safe files after downloading" to prevent auto-unpack issues with GZIP
- After decompressing GZIP, **manually add `.csv` extension** to open in spreadsheet editors
- Inactive Users Report threshold is fixed at **90 days** — not configurable
- Time range input is local timezone but export timestamps are UTC — watch for offset confusion

## Related Docs
- Amazon S3 Sync configuration
- Resource Policies
- Device Posture
- Admin Console Settings