# Monitoring Twingate Service Status & Maintenance Events

## Summary
Twingate exposes public read-only REST APIs (via Statuspage) to query real-time service health, incidents, and maintenance windows. All endpoints are unauthenticated GET requests returning JSON. Full API index available at `https://status.twingate.com/api/`.

## Key Information
- All APIs are under `https://status.twingate.com/api/v2/`
- No authentication required
- Returns standard Statuspage.io JSON format
- Page ID: `d3m2m1y4ghc6`
- Postman collection available in official docs

## API Endpoints

| Purpose | Method | URL |
|---|---|---|
| Full summary (status + components + incidents + maintenance) | GET | `https://status.twingate.com/api/v2/summary.json` |
| Unresolved incidents | GET | `https://status.twingate.com/api/v2/incidents/unresolved.json` |
| Past incidents | GET | `https://status.twingate.com/api/v2/incidents.json` |
| Upcoming maintenance | GET | `https://status.twingate.com/api/v2/scheduled-maintenances/upcoming.json` |
| Active maintenance | GET | `https://status.twingate.com/api/v2/scheduled-maintenances/active.json` |
| Past maintenance | GET | `https://status.twingate.com/api/v2/scheduled-maintenances.json` |

## Response Structure (summary.json)
- `status.indicator` — overall status (`none`, `minor`, `major`, `critical`)
- `status.description` — human-readable overall status
- `components[]` — per-component status; `group: true` indicates a component group with child IDs in `components[]`
- `incidents[]` — active incidents
- `scheduled_maintenances[]` — active/upcoming maintenance

## Monitored Components
| Component | Group |
|---|---|
| Controller, User Authentication, Connection Authorization, IdP Synchronization | Controller |
| Data Relays, Peer-to-Peer Infrastructure | Relay Infrastructure |
| Admin Web Interface, Billing, Reports Export | Admin Console |
| Admin API, Analytics | (standalone) |
| www.twingate.com, docs.twingate.com | Homepage |

## Component Status Values
- `operational`
- `under_maintenance`
- `degraded_performance`
- `partial_outage`
- `major_outage`

## Gotchas
- Admin Console availability is **independent** from Controller; Admin Console downtime does not affect end-user connectivity
- Component entries with `"group": true` contain child component IDs in their `components[]` array, not status details—look up children separately
- `scheduled-maintenances.json` returns **all** (past + active + upcoming); use specific `/active` or `/upcoming` endpoints to filter
- `incident_updates[].affected_components[].code` maps to `components[].id` in the summary response

## Related Docs
- Statuspage API reference: `https://status.twingate.com/api/`
- Twingate status page: `https://status.twingate.com`