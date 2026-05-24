# Twingate Service Status & Maintenance Events API

## Summary
Twingate exposes public read-only REST APIs via `status.twingate.com/api/v2` to retrieve real-time service health, incidents, and maintenance windows. No authentication required. All responses are JSON.

## Key Information
- Base URL: `https://status.twingate.com/api/v2/`
- Interactive API reference: `https://status.twingate.com/api/`
- Postman collection available for all endpoints
- All timestamps in UTC (ISO 8601)
- Page ID for Twingate: `d3m2m1y4ghc6`

## API Endpoints

| Purpose | Method | Endpoint |
|---|---|---|
| Full summary (status + components + incidents + maintenance) | GET | `/summary.json` |
| Overall status only | GET | `/status.json` |
| Unresolved incidents | GET | `/incidents/unresolved.json` |
| Past incidents | GET | `/incidents.json` |
| Upcoming maintenance | GET | `/scheduled-maintenances/upcoming.json` |
| Active maintenance | GET | `/scheduled-maintenances/active.json` |
| Past maintenance | GET | `/scheduled-maintenances.json` |

## Key Response Fields

**Status object** (`/summary.json` → `status`):
- `indicator`: `"none"` | `"minor"` | `"major"` | `"critical"`
- `description`: Human-readable string (e.g., `"All Systems Operational"`)

**Component object**:
- `status`: `"operational"` | `"degraded_performance"` | `"partial_outage"` | `"major_outage"` | `"under_maintenance"`
- `group`: boolean — if `true`, component is a group container with child IDs in `components[]`
- `group_id`: parent group ID if component is a child

**Monitored components include**:
- Controller (User Authentication, Connection Authorization, IdP Synchronization)
- Relay Infrastructure (Data Relays, Peer-to-Peer Infrastructure)
- Admin Console (Admin Web Interface, Billing, Reports Export)
- Admin API, Analytics, Homepage, docs.twingate.com

**Maintenance/Incident object**:
- `status`: `"scheduled"` | `"in_progress"` | `"verifying"` | `"completed"`
- `incident_updates[]`: array of timestamped status updates with `affected_components`
- Each affected component shows `old_status` → `new_status`

## Gotchas
- Admin Console downtime does **not** impact end-user connectivity — the Controller handles auth/access independently
- Component groups (`"group": true`) contain child component IDs in `components[]` array, not full objects — children appear separately in the top-level `components` array
- `/summary.json` returns everything in one call; use it to minimize requests if polling
- `/scheduled-maintenances.json` returns **all** maintenance events (past + active + upcoming), not just past

## Related Docs
- Status page UI: https://status.twingate.com
- API index: https://status.twingate.com/api/
- Twingate Admin API docs (separate): your Twingate network GraphQL API