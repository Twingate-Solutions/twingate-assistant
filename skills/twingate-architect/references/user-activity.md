## User Activity Report

Twingate's user activity and authentication event reporting, accessible under Settings → Reports → User Activity. Exports are either active/inactive user CSVs or authentication event JSON (gzip-compressed).

**Report Types:**
- **Authentication Events** -- JSON export for a selected time range; also supports continuous S3 sync
- **Active Users** -- users who accessed Resources in the selected window
- **Inactive Users** -- accounts with no Resource access in the last 90 days (auto-identified)

**Step-by-Step Export:**
1. Settings → Reports → User Activity
2. Click Generate User Activity Report
3. Select Authentication Events or User Activity
4. For auth events: select time range; for user activity: select active/inactive and time range
5. Export completes in background; email notification sent
6. Download from Reports page; rename decompressed file with `.csv` extension

**Active User CSV Columns:**
- `user_email`, `last_access_date`, `total_connections`, `success_connections`, `failed_connections`
- `failed_connections_dns`, `failed_connections_other`, `total_bytes`, `bytes_transferred`, `bytes_received`
- `percent_relay`, `percent_p2p`, `active_devices`, `num_of_client_ip`, `top_10_client_ips`

**Authentication Event JSON Schemas:**
- Admin Console sign-in: `action.type = "admin_login"`, includes user email/id and policy id/name
- Resource authentication: `action.type = "reauth"`, adds device (id/name) and resource (id/name) fields
- All events: `version`, `time` (UTC), `action` root object

**Gotchas:**
- Time range selection uses local timezone; exported timestamps are UTC
- Safari auto-unpack may produce empty file -- disable "Open safe files after downloading"
- Auth event S3 sync must be configured separately; CSVs are manual-export only

**Related Docs:**
- /docs/syncing-data-to-s3 -- S3 sync for authentication events
- /docs/analytics -- Analytics overview
