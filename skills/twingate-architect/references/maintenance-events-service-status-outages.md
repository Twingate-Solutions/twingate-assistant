# Monitoring Twingate Service Status & Maintenance Events

## Summary
Twingate exposes public REST APIs (via Statuspage) to retrieve real-time service status, incidents, and maintenance events. All endpoints are unauthenticated GET requests returning JSON. The same data is available at https://status.twingate.com/api/.

## Key Information
- Base URL: `https://status.twingate.com/api/v2/`
- No authentication required
- All responses include a `page` metadata object plus the relevant data array
- Postman collection available for all endpoints
- Page ID: `d3m2m1y4ghc6`

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

## Component Groups
- **Controller** (`qjtcw45cbnzc`): Controller, User Authentication, Connection Authorization, IdP Synchronization
- **Admin Console** (`ybbtjt0tpv20`): Admin Web Interface, Billing, Reports Export
- **Relay Infrastructure** (`nh6xcxh41s05`): Data Relays, Peer-to-Peer Infrastructure
- **Homepage** (`3h4fm0kpyqtw`): www.twingate.com, docs.twingate.com
- **Standalone**: Admin API, Analytics

## Response Fields

**Status indicator values:** `none`, `minor`, `major`, `critical`

**Component status values:** `operational`, `degraded_performance`, `partial_outage`, `major_outage`, `under_maintenance`

**Maintenance status values:** `scheduled`, `in_progress`, `verifying`, `completed`

**Summary response top-level keys:**
- `page` — metadata
- `components` — array of all components with individual status
- `incidents` — unresolved incidents
- `scheduled_maintenances` — active/upcoming maintenance
- `status` — overall indicator + description string

## Gotchas
- Admin Console outages do **not** impact end-user connectivity — it is independent from Controller infrastructure
- Components with `"group": true` are parent containers; their `components` array contains child component IDs
- `only_show_if_degraded: true` components are hidden in UI when operational but still appear in API responses
- The `/summary.json` endpoint combines all other endpoints into a single call — use it to minimize requests

## Related Docs
- Twingate Status page UI: https://status.twingate.com
- Statuspage API reference: https://status.twingate.com/api/