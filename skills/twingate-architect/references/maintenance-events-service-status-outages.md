---
source: https://www.twingate.com/docs/maintenance-events-service-status-outages
type: docs
fetched: 2026-08-14
source_version: 023102376d57abf09bc5f8fc4179ab62be4602b27c02a512e86da8fc1af5fcc8
---

# Twingate Service Status & Maintenance Events API

## Summary
Twingate exposes public read-only REST APIs via `status.twingate.com/api/v2` to retrieve real-time service health, incidents, and maintenance events. No authentication required. All endpoints return JSON.

## Key Information
- Base URL: `https://status.twingate.com/api/v2/`
- Full API reference also at: `https://status.twingate.com/api/`
- Postman collection available for all endpoints
- All timestamps in UTC (ISO 8601)
- No API key required

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/summary.json` | GET | Full summary: status, components, incidents, maintenances |
| `/incidents/unresolved.json` | GET | Active/unresolved incidents only |
| `/scheduled-maintenances/upcoming.json` | GET | Future scheduled maintenances |
| `/scheduled-maintenances/active.json` | GET | Currently active maintenance windows |
| `/scheduled-maintenances.json` | GET | All maintenances including past/completed |

## Monitored Components
- **Controller group**: Controller, User Authentication, Connection Authorization, IdP Synchronization
- **Relay Infrastructure group**: Data Relays, Peer-to-Peer Infrastructure
- **Admin Console group**: Admin Web Interface, Billing, Reports Export
- **Standalone**: Admin API, Analytics, Homepage (www.twingate.com, docs.twingate.com)

## Response Structure

**Status indicators**: `none`, `minor`, `major`, `critical`  
**Component statuses**: `operational`, `degraded_performance`, `partial_outage`, `major_outage`, `under_maintenance`  
**Maintenance statuses**: `scheduled`, `in_progress`, `completed`

Key fields in component objects:
- `id`, `name`, `status`, `group` (bool), `group_id`, `components` (child IDs if group)
- `only_show_if_degraded` — hidden from UI when operational

Key fields in maintenance/incident objects:
- `impact`, `started_at`, `resolved_at`, `incident_updates[]` with `affected_components[]`
- Each affected component shows `old_status` → `new_status`

## Gotchas
- Admin Console outages do **not** impact end-user connectivity — it's independent from Controller infrastructure
- Component groups (`"group": true`) contain child component IDs in `components[]` array; individual child components reference parent via `group_id`
- `/scheduled-maintenances.json` returns **all** maintenances (past + active + upcoming), not just past ones despite the docs implying "past only"
- Empty arrays (`[]`) returned when no incidents/maintenances exist — not null

## Related Docs
- Live status page: https://status.twingate.com
- API index: https://status.twingate.com/api/