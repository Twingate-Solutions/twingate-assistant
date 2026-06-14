# User Activity Reports – Twingate

## Summary
Twingate Admin Console provides user activity reporting including authentication event logs, active user reports, and inactive user reports. Reports can be manually exported (CSV/JSON) or synced to Amazon S3. Authentication events help troubleshoot IDP errors, device posture failures, and policy blocks.

## Key Information
- **Authentication Events**: Exported as JSON (GZIP compressed); covers sign-in attempts, MFA events, policy blocks
- **Active Users Report**: Users who accessed Resources in selected time window; exported as CSV
- **Inactive Users Report**: Auto-identifies accounts with no Resource access in last **90 days**; exported as CSV
- All exports use **UTC timestamps**, but time range selection uses **local timezone**
- Export delivery is via **email notification**; most complete in minutes, large exports may take hours
- Authentication events can be **auto-synced to Amazon S3**

## Prerequisites
- Admin Console access
- Amazon S3 bucket configured (for automatic sync only)

## Step-by-Step: Generate Export
1. Go to **Settings → Reports → User Activity**
2. Click **Generate User Activity Report**
3. Select report type: **Authentication Events** or **User Activity**
4. Select time range (and active/inactive for User Activity reports)
5. Export runs in background; email sent when complete
6. Return to Reports page to download

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
| `active_devices` | Devices at report generation time |
| `num_of_client_ip` / `top_10_client_ips` | Client IP metrics |

### Authentication Event JSON Schema Fields
| Field | Description |
|-------|-------------|
| `version` | Schema version |
| `time` | Event timestamp (UTC) |
| `action.type` | Event type (e.g., `admin_login`, `reauth`) |
| `action.user.email` / `.id` | User identifier |
| `action.user.policy.id` / `.name` | Policy engaged |
| `action.user.device.id` / `.name` | Device (resource auth only) |
| `action.user.resource.id` / `.name` | Resource accessed (resource auth only) |

## Gotchas
- Export files are **GZIP compressed**; must decompress before use — add `.csv` extension after decompression
- **Safari**: Disable "Open 'safe' files after downloading" (Safari → Preferences → General) to prevent empty file issue
- Time range selector uses **local timezone** but exported timestamps are **UTC** — mismatches can cause confusion
- Inactive user threshold is fixed at **90 days** (not configurable)

## Related Docs
- Amazon S3 Sync setup (referenced in step 9)
- Resource Policies
- Device Posture configuration