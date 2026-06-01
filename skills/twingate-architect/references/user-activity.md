# User Activity Reports – Twingate

## Summary
Twingate's Admin Console provides user activity reporting including authentication event logs and active/inactive user reports. Reports can be exported manually as CSV/JSON (GZIP) or synced automatically to an S3 bucket. Authentication events help troubleshoot connection failures; user reports help manage license counts and adoption.

## Key Information
- **Authentication Events**: Track sign-in attempts (success/failure) for Client and Resource Policies; includes IDP errors, device posture mismatches, policy blocks, MFA actions
- **Active Users Report**: Users who accessed Resources in the selected time window
- **Inactive Users Report**: Users with no Resource access in the last 90 days (auto-identified)
- Export formats: Authentication events → **JSON (GZIP)**; User activity → **CSV (GZIP)**
- Timestamps in exports are **UTC**; time range selection uses **local timezone**
- Large exports may take several hours; completion notification sent via **email**
- S3 sync available for continuous authentication event delivery

## Prerequisites
- Admin Console access
- Amazon S3 bucket configured (for automatic sync only)

## Step-by-Step: Generate Export
1. **Settings → Reports → User Activity**
2. Click **Generate User Activity Report**
3. Select report type: **Authentication Events** or **User Activity**
4. For Authentication Events: select time range
5. For User Activity: select **Active** or **Inactive** users + time range
6. Wait for email notification (minutes to hours)
7. Return to Reports page to download
8. (Optional) Configure Amazon S3 sync for automatic authentication event delivery

## Viewing Exports
- Files are **GZIP compressed** — decompress with any standard tool
- After decompression, add **`.csv`** extension to open in spreadsheet editors
- **Safari issue**: Disable "Open 'Safe' files after downloading" (Safari → Preferences → General) to prevent auto-unpack corruption

## Active User Report Columns
| Column | Description |
|--------|-------------|
| `user_email` | User email |
| `last_access_date` | Last Resource access timestamp |
| `total_connections` | All connections in period |
| `success_connections` / `failed_connections` | By outcome |
| `failed_connections_dns` / `failed_connections_other` | Failure breakdown |
| `total_bytes` / `bytes_transferred` / `bytes_received` | Data transfer |
| `percent_relay` / `percent_p2p` | Connection type distribution |
| `active_devices` | Devices at report generation time |
| `num_of_client_ip` / `top_10_client_ips` | Client IP usage |

## Authentication Event JSON Schema Fields
| Field | Description |
|-------|-------------|
| `version` | Schema version |
| `time` | Event timestamp (UTC) |
| `action.type` | Event type (e.g., `admin_login`, `reauth`) |
| `action.user.email` / `.id` | User identifier |
| `action.user.policy.id` / `.name` | Policy engaged |
| `action.user.device.id` / `.name` | Device (Resource auth only) |
| `action.user.resource.id` / `.name` | Resource accessed (Resource auth only) |

## Gotchas
- Time range selector uses local timezone but export timestamps are UTC — account for offset when filtering
- Inactive Users Report threshold is fixed at **90 days** (not configurable)
- Safari's auto-unpack can corrupt GZIP files; disable the setting before downloading

## Related Docs
- Amazon S3 Sync configuration
- Resource Policies
- Device Posture