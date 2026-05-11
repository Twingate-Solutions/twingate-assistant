# Twingate Service Status & Maintenance Events API

## Summary
Twingate exposes public read-only REST APIs via `status.twingate.com` to retrieve real-time service health, incidents, and maintenance events. All endpoints return JSON and require no authentication. The same data is browsable at https://status.twingate.com/api/.

## Key Information
- **Base URL:** `https://status.twingate.com/api/v2/`
- No authentication required
- All timestamps in UTC (ISO 8601)
- Postman collection available for all endpoints
- Page ID for Twingate: `d3m2m1y4ghc6`

## API Endpoints

| Purpose | Method | Endpoint |
|---|---|---|
| Full summary (status + components + incidents + maintenance) | GET | `/summary.json` |
| Unresolved incidents | GET | `/incidents/unresolved.json` |
| Past incidents | GET | `/incidents.json` |
| Upcoming maintenance | GET | `/scheduled-maintenances/upcoming.json` |
| Active maintenance | GET | `/scheduled-maintenances/active.json` |
| Past maintenance | GET | `/scheduled-maintenances.json` |

## Response Structure

**Summary response top-level keys:**
- `page` — metadata (id, name, url, timezone, updated_at)
- `components` — array of service components with individual statuses
- `incidents` — array of active incidents
- `scheduled_maintenances` — array of maintenance events
- `status` — overall status (`indicator`, `description`)

**Component fields:** `id`, `name`, `status`, `group`, `group_id`, `showcase`, `only_show_if_degraded`

**Overall status indicators:** `none` = All Systems Operational

**Component status values:** `operational`, `under_maintenance`, `degraded_performance`, `partial_outage`, `major_outage`

## Monitored Components
- **Controller group:** Controller, User Authentication, Connection Authorization, IdP Synchronization
- **Admin Console group:** Admin Web Interface, Billing, Reports Export
- **Relay Infrastructure group:** Data Relays, Peer-to-Peer Infrastructure
- **Standalone:** Admin API, Analytics, Homepage (www.twingate.com, docs.twingate.com)

## Maintenance Event Fields
- `id`, `name`, `status` (e.g., `completed`, `in_progress`, `scheduled`)
- `impact`: `maintenance`
- `incident_updates[]`: array of status updates with `affected_components` showing `old_status` → `new_status`
- `scheduled_for`, `scheduled_until`: maintenance window times

## Gotchas
- Admin Console downtime does **not** impact end-user connectivity — Controller handles auth/authorization independently
- Components with `"group": true` are containers; actual status is on child components (identified by `group_id`)
- Components with `"only_show_if_degraded": true` are hidden when healthy
- The `/summary.json` endpoint duplicates incident and maintenance data, so you can use it as a single call for full status

## Related Docs
- Status page UI: https://status.twingate.com
- API index: https://status.twingate.com/api/
- Twingate Admin API: separate from this status API