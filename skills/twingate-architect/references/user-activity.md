# User Activity – Twingate Docs

## Page Title
User Activity (Reports)

## Summary
Twingate Admin Console provides user activity reporting covering authentication events, active users, and inactive users. Reports can be exported manually as CSV/JSON or synced automatically to Amazon S3. Admins use this to audit access, troubleshoot connection failures, and manage user counts.

## Key Information
- **Report types**: Authentication Events (JSON), Active Users (CSV), Inactive Users (CSV)
- **Inactive Users Report**: Auto-identifies accounts with no Resource access in last **90 days**
- **Export format**: GZIP-compressed; rename decompressed file with `.csv` extension to open in spreadsheet tools
- **Timestamps**: UI time range selection uses local timezone; exported timestamps are in **UTC**
- **Delivery**: Export runs in background; email notification when ready; download from Reports page
- **S3 sync**: Available for authentication events (automatic sync option)
- **Authentication event log format**: JSON with schema version, timestamp, action type, user/device/resource IDs

## Prerequisites
- Admin Console access
- Email configured to receive export-ready notifications
- Amazon S3 bucket configured (optional, for auto-sync)

## Step-by-Step
1. **Settings → Reports → User Activity**
2. Click **Generate User Activity Report**
3. Select report type: **Authentication Events** or **User Activity**
4. For Authentication Events: select time range
5. For User Activity: select **Active** or **Inactive** users + time range
6. Wait for email notification; return to Reports page to download
7. Optionally configure **Amazon S3 sync** for automatic authentication event delivery

## Configuration Values

**Active Users CSV Columns:**
| Column | Description |
|--------|-------------|
| `user_email` | User email |
| `last_access_date` | Last Resource access timestamp |
| `total_connections` | All connections in period |
| `success_connections` / `failed_connections` | Success/fail counts |
| `failed_connections_dns` / `failed_connections_other` | Failure breakdown |
| `total_bytes` / `bytes_transferred` / `bytes_received` | Bandwidth metrics |
| `percent_relay` / `percent_p2p` | Connection type breakdown |
| `active_devices` | Device count at report generation |
| `num_of_client_ip` / `top_10_client_ips` | Client IP usage |

**Authentication Event JSON Fields:**
- `version`, `time` (UTC), `action.type` (e.g., `admin_login`, `reauth`)
- `action.user`: `email`, `id`, `policy.id`, `policy.name`
- `action.user.device`: `id`, `name` (resource auth only)
- `action.user.resource`: `id`, `name` (resource auth only)

## Gotchas
- **Safari users**: Disable "Open safe files after downloading" (Safari → Preferences → General) to prevent empty file issue from auto-unpack
- Large exports can take **several hours**
- Inactive users threshold is fixed at **90 days** (not configurable)
- Active Users report `active_devices` count reflects time of report generation, not the selected time range

## Related Docs
- Amazon S3 sync configuration
- Resource Policies
- Device Posture
- Admin Console authentication settings