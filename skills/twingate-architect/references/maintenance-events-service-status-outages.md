# Twingate Service Status & Maintenance Events API

## Summary
Twingate exposes public REST APIs via `status.twingate.com/api/v2` to retrieve real-time service status, incidents, and maintenance events. No authentication required. All endpoints return JSON.

## Key Information
- **Base URL:** `https://status.twingate.com/api/v2/`
- **Status page UI:** `https://status.twingate.com`
- **API index:** `https://status.twingate.com/api/`
- **Postman Collection** available for all endpoints
- All timestamps in UTC (ISO 8601)
- No API key or authentication needed

## API Endpoints

| Purpose | Method | URL |
|---|---|---|
| Full summary (status + components + incidents + maintenance) | GET | `/v2/summary.json` |
| Unresolved incidents | GET | `/v2/incidents/unresolved.json` |
| Past incidents | GET | `/v2/incidents.json` |
| Upcoming maintenance | GET | `/v2/scheduled-maintenances/upcoming.json` |
| Active maintenance | GET | `/v2/scheduled-maintenances/active.json` |
| Past maintenance | GET | `/v2/scheduled-maintenances.json` |

## Monitored Components
- **Controller group:** Controller, User Authentication, Connection Authorization, IdP Synchronization
- **Relay Infrastructure group:** Data Relays, Peer-to-Peer Infrastructure
- **Admin Console group:** Admin Web Interface, Billing, Reports Export
- **Standalone:** Admin API, Analytics, www.twingate.com, docs.twingate.com

## Response Schema Notes

**Status indicator values:** `none` | `minor` | `major` | `critical`

**Component status values:** `operational` | `degraded_performance` | `partial_outage` | `major_outage` | `under_maintenance`

**Maintenance status values:** `scheduled` | `in_progress` | `completed`

**Summary response top-level keys:**
```json
{ "page": {}, "components": [], "incidents": [], "scheduled_maintenances": [], "status": {"indicator": "none", "description": "All Systems Operational"} }
```

**Component object key fields:**
- `id`, `name`, `status`, `group` (bool), `group_id`, `components` (array of child IDs if group)

**Maintenance object key fields:**
- `id`, `name`, `status`, `impact`, `scheduled_for`, `scheduled_until`, `incident_updates[]`
- `incident_updates[].affected_components[].old_status` / `new_status`

## Gotchas
- Admin Console outages **do not affect** end-user connectivity — Controller is the critical path component
- Component groups (`"group": true`) contain child component IDs in `components[]` array; check children for granular status
- `summary.json` returns everything in one call — prefer this over multiple requests for dashboard polling
- Past maintenance endpoint (`/scheduled-maintenances.json`) returns **all** maintenance records, not just active/upcoming

## Related Docs
- Twingate status page: https://status.twingate.com
- API self-documentation: https://status.twingate.com/api/