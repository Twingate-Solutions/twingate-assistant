# Monitoring Twingate Service Status & Maintenance Events

## Summary
Twingate exposes public REST APIs (via Statuspage) for real-time monitoring of service health, incidents, and scheduled maintenance. All endpoints are unauthenticated GET requests returning JSON. The same data is browsable at https://status.twingate.com/api/.

## Key Information
- Base URL: `https://status.twingate.com/api/v2/`
- No authentication required
- All timestamps in UTC (ISO 8601)
- Postman collection available in official docs

## API Endpoints

| Purpose | Endpoint |
|---|---|
| Full summary (status + components + incidents + maintenance) | `GET /summary.json` |
| Overall status only | `GET /status.json` |
| Unresolved incidents | `GET /incidents/unresolved.json` |
| Past incidents | `GET /incidents.json` |
| Upcoming maintenance | `GET /scheduled-maintenances/upcoming.json` |
| Active maintenance | `GET /scheduled-maintenances/active.json` |
| Past maintenance | `GET /scheduled-maintenances.json` |

## Response Structure

**`/summary.json`** returns:
- `status.indicator` — `none` | `minor` | `major` | `critical`
- `status.description` — human-readable string
- `components[]` — per-component status objects
- `incidents[]` — active incidents
- `scheduled_maintenances[]` — active/upcoming maintenance

**Component fields:**
- `id`, `name`, `status` (`operational`, `under_maintenance`, `degraded_performance`, `partial_outage`, `major_outage`)
- `group` (bool) — parent group component
- `group_id` — parent group ID if child component

**Maintenance event fields:**
- `status`: `scheduled` | `in_progress` | `completed`
- `impact`: `maintenance`
- `incident_updates[]` — history with `affected_components[]` showing `old_status`/`new_status`

## Monitored Components
- **Controller group**: Controller, User Authentication, Connection Authorization, IdP Synchronization
- **Relay Infrastructure group**: Data Relays, Peer-to-Peer Infrastructure
- **Admin Console group**: Admin Web Interface, Billing, Reports Export
- **Standalone**: Admin API, Analytics, Homepage (www.twingate.com, docs.twingate.com)

## Gotchas
- Admin Console availability is **independent** from Controller — Admin Console outage does not block end-user connections
- Component groups have `"group": true` with a `components[]` array of child IDs; children have `"group": false` with a `group_id` pointing to parent
- `/summary.json` includes both active incidents and active/upcoming maintenance inline — use it to avoid multiple calls
- `/scheduled-maintenances.json` returns **all** maintenance events (past + active), not just past

## Related Docs
- Status page UI: https://status.twingate.com
- API index: https://status.twingate.com/api/