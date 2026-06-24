# Twingate Service Status & Maintenance Events API

## Summary
Twingate exposes public read-only REST APIs (via Statuspage) to monitor service health, incidents, and maintenance windows in real time. No authentication required. All endpoints return JSON.

## Key Information
- Base URL: `https://status.twingate.com/api/v2/`
- Full API reference also at: `https://status.twingate.com/api/`
- Postman collection available for all endpoints
- All timestamps in UTC (`Etc/UTC`)
- Page ID: `d3m2m1y4ghc6`

## Prerequisites
- No API key or authentication required
- HTTP GET requests only

## API Endpoints

| Purpose | Endpoint |
|---|---|
| Full summary (status + components + incidents + maintenance) | `GET /api/v2/summary.json` |
| Unresolved incidents | `GET /api/v2/incidents/unresolved.json` |
| Upcoming maintenance | `GET /api/v2/scheduled-maintenances/upcoming.json` |
| Active maintenance | `GET /api/v2/scheduled-maintenances/active.json` |
| Past maintenance events | `GET /api/v2/scheduled-maintenances.json` |

## Response Structure

**Summary response includes:**
- `status.indicator` — overall status (`none` = all operational)
- `status.description` — human-readable overall status
- `components[]` — per-component status objects
- `incidents[]` — active incidents
- `scheduled_maintenances[]` — active/upcoming maintenance

**Component fields:**
- `id`, `name`, `status` (`operational`, `under_maintenance`, `degraded_performance`, etc.)
- `group` (bool) — whether it's a group container
- `group_id` — parent group if nested
- `only_show_if_degraded` — display hint

**Maintenance event fields:**
- `status`: `scheduled`, `in_progress`, `completed`
- `impact`: `maintenance`
- `incident_updates[]` — timeline with `affected_components` showing `old_status`/`new_status`

## Monitored Components
- **Controller group**: Controller, User Authentication, Connection Authorization, IdP Synchronization
- **Relay Infrastructure**: Data Relays, Peer-to-Peer Infrastructure
- **Admin Console**: Admin Web Interface, Billing, Reports Export
- **Standalone**: Admin API, Analytics
- **Homepage**: www.twingate.com, docs.twingate.com

## Gotchas
- Admin Console outages do **not** impact end-user connectivity — Controller and Relay infrastructure are independent
- `summary.json` is the most efficient single call to get all status data at once
- Components with `group: true` are containers; actual status lives in child components referenced by `components[]` array of IDs
- Past maintenance returned by `/scheduled-maintenances.json` (not a `/past` endpoint)

## Related Docs
- Live status page: https://status.twingate.com
- API index: https://status.twingate.com/api/