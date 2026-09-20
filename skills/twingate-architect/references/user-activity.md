---
source: https://www.twingate.com/docs/user-activity
type: docs
fetched: 2026-09-20
source_version: 409588710643d990cbf14248b41a1395828cab9b5fcd715f710891c669e2b585
---

# User Activity Reporting

## Page Title
User Activity

## Summary
Twingate Admin Console provides user activity reporting including authentication event logs and active/inactive user reports. Reports can be exported manually as JSON/CSV or synced automatically to Amazon S3. Authentication events support time-range filtering; inactive users report always covers the last 90 days.

## Key Information
- **Two report types**: Authentication Events (JSON/GZIP) and User Activity (CSV/GZIP)
- **User Activity subtypes**: Active Users (with time range) or Inactive Users (fixed 90-day window)
- **Export format**: GZIP compressed; rename decompressed file with `.csv` or treat as JSON
- Timestamps in exports are **UTC**; time range selection uses **local timezone**
- Export completed via email notification; download from Reports page
- Large exports may take several hours
- Authentication events can be synced to **Amazon S3** automatically

## Prerequisites
- Admin Console access
- Amazon S3 bucket configured (for automated sync only)

## Step-by-Step: Generate Export
1. Navigate to **Settings → Reports → User Activity**
2. Click **Generate User Activity Report**
3. Select report type: **Authentication Events** or **User Activity**
4. For Authentication Events: select time range
5. For User Activity: select **Active Users** (+ time range) or **Inactive Users** (no time range needed)
6. Wait for email notification; return to Reports page to download
7. Optional: configure Amazon S3 sync for automated authentication event delivery

## Configuration Values

### Active Users Report Columns
| Column | Description |
|--------|-------------|
| `user_email` | User email |
| `last_access_date` | Last Resource access timestamp |
| `total_connections` | Total connections in period |
| `success_connections` / `failed_connections` | Connection outcomes |
| `failed_connections_dns` / `failed_connections_other` | Failure breakdown |
| `total_bytes` / `bytes_transferred` / `bytes_received` | Bandwidth metrics |
| `percent_relay` / `percent_p2p` | Connection type breakdown |
| `active_devices` | Active device count at report generation |
| `num_of_client_ip` / `top_10_client_ips` | Client IP data |

### Authentication Event JSON Schema Fields
| Field | Description |
|-------|-------------|
| `version` | Schema version (e.g., `"1"`) |
| `time` | Event timestamp (UTC ISO 8601) |
| `action.type` | e.g., `admin_login`, `reauth` |
| `action.user.id` / `.email` | User identifier |
| `action.policy.id` / `.name` | Policy applied |
| `action.device.id` / `.name` | Device (resource auth only) |
| `action.resource.id` / `.name` | Resource accessed (resource auth only) |

## Gotchas
- **Safari**: Disable "Open 'Safe' files after downloading" to prevent auto-unpack producing empty files
- **Inactive Users**: Fixed 90-day lookback — no custom time range available
- **File extension**: Decompressed files need `.csv` manually appended for spreadsheet editors
- Export timestamps are UTC regardless of local timezone used for range selection

## Related Docs
- Amazon S3 Sync setup (referenced but separate doc)
- Resource Policies
- Device Posture configuration