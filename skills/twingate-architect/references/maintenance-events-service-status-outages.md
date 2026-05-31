# Monitoring Twingate Service Status & Maintenance Events

## Summary
Twingate exposes public read-only REST APIs (via Statuspage) to query real-time service health, incidents, and maintenance events. No authentication is required. All endpoints are also browsable at https://status.twingate.com/api/.

## Key Information
- Base URL: `https://status.twingate.com/api/v2/`
- All responses return JSON; no API key needed
- Postman collection available for all endpoints
- Page ID for Twingate: `d3m2m1y4ghc6`

## API Endpoints

| Purpose | Method | URL |
|---|---|---|
| Full summary (status + components + incidents + maintenance) | GET | `/v2/summary.json` |
| Overall status only | GET | `/v2/status.json` |
| All components | GET | `/v2/components.json` |
| Unresolved incidents | GET | `/v2/incidents/unresolved.json` |
| All past incidents | GET | `/v2/incidents.json` |
| Upcoming maintenance | GET | `/v2/scheduled-maintenances/upcoming.json` |
| Active maintenance | GET | `/v2/scheduled-maintenances/active.json` |
| Past maintenance | GET | `/v2/scheduled-maintenances.json` |

## Response Structure

**Summary response key fields:**
- `status.indicator` — overall health (`none`, `minor`, `major`, `critical`)
- `status.description` — human-readable e.g. `"All Systems Operational"`
- `components[].status` — per-component: `operational`, `degraded_performance`, `partial_outage`, `major_outage`, `under_maintenance`
- `components[].group` — `true` if this is a group container; child IDs listed in `components[]`
- `incidents[]` — active unresolved incidents
- `scheduled_maintenances[]` — active/upcoming maintenance

**Maintenance event fields:**
- `status`: `scheduled`, `in_progress`, `verifying`, `completed`
- `incident_updates[].affected_components` — lists `old_status` / `new_status` per component

## Monitored Components
- **Controller group**: Controller, User Authentication, Connection Authorization, IdP Synchronization
- **Admin Console group**: Admin Web Interface, Billing, Reports Export
- **Relay Infrastructure group**: Data Relays, Peer-to-Peer Infrastructure
- **Standalone**: Admin API, Analytics, Homepage (www/docs)

## Gotchas
- Admin Console availability is **independent** from Controller infrastructure — Admin Console outage does not affect end-user connectivity
- Component entries with `"group": true` are containers; actual status is on child components referenced by ID in the `components` array
- `summary.json` returns all data in one call — use it to minimize requests if polling

## Related Docs
- Live status page: https://status.twingate.com
- Statuspage API reference: https://status.twingate.com/api/