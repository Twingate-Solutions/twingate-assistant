# Monitoring Twingate Service Status & Maintenance Events

## Summary
Twingate exposes public read-only REST APIs (via Statuspage) to query real-time service health, incidents, and scheduled maintenance windows. No authentication is required. All endpoints return JSON.

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
| Overall status only | included in `summary.json` → `status` field |
| Per-component status | included in `summary.json` → `components` array |
| Unresolved incidents | `GET /api/v2/incidents/unresolved.json` |
| Past incidents | `GET /api/v2/incidents.json` *(implied)* |
| Upcoming maintenance | `GET /api/v2/scheduled-maintenances/upcoming.json` |
| Active maintenance | `GET /api/v2/scheduled-maintenances/active.json` |
| Past maintenance | `GET /api/v2/scheduled-maintenances.json` |

## Key Response Fields

**Status object** (`summary.json → status`):
- `indicator`: `"none"` | `"minor"` | `"major"` | `"critical"`
- `description`: human-readable string (e.g., `"All Systems Operational"`)

**Component object**:
- `id`, `name`, `status` (`"operational"` | `"degraded_performance"` | `"partial_outage"` | `"major_outage"` | `"under_maintenance"`)
- `group`: boolean — if `true`, component is a group container with child `components` array (IDs only)
- `group_id`: parent group ID if component belongs to a group

**Monitored components include**:
- Controller (User Authentication, Connection Authorization, IdP Synchronization)
- Relay Infrastructure (Data Relays, Peer-to-Peer Infrastructure)
- Admin Console (Admin Web Interface, Billing, Reports Export)
- Admin API, Analytics, Homepage, docs.twingate.com

**Maintenance object**:
- `status`: `"scheduled"` | `"in_progress"` | `"completed"`
- `incident_updates[].affected_components[].old_status` / `new_status`: tracks state transitions

## Gotchas
- Component groups (`"group": true`) contain only child component IDs in the `components` array — fetch individual component status from the flat `components` list
- `summary.json` includes `incidents` and `scheduled_maintenances` arrays, but these may be empty; use dedicated endpoints for reliability
- Admin Console availability is **independent** of Controller — Admin Console outage does not affect end-user connectivity
- `scheduled-maintenances.json` (no qualifier) returns **past** events, not all events

## Related Docs
- Status page UI: https://status.twingate.com
- API index: https://status.twingate.com/api/