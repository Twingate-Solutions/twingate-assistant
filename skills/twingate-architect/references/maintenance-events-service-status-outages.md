## Twingate Service Status & Maintenance Events API

Twingate exposes a public REST API at `https://status.twingate.com/api/v2/` for programmatically querying service status, incidents, and scheduled maintenance events. All data is also available at `https://status.twingate.com`. A Postman collection is provided for all endpoints.

**Key Information**
- Base URL: `https://status.twingate.com/api/v2/`
- All requests are unauthenticated GET requests returning JSON
- Components tracked: Admin Web Interface, Billing, Controller, User Authentication, Connection Authorization, IdP Synchronization, Data Relays, Peer-to-Peer Infrastructure, Analytics, Reports Export, Admin API, docs.twingate.com, www.twingate.com
- Status values: `operational`, `degraded_performance`, `partial_outage`, `major_outage`, `under_maintenance`
- Top-level status indicator: `"none"` = All Systems Operational

**API Endpoints**

| Endpoint | Purpose |
|---|---|
| `GET /v2/summary.json` | Summary of all component statuses + active incidents + upcoming maintenance |
| `GET /v2/incidents/unresolved.json` | List of currently unresolved incidents |
| `GET /v2/incidents.json` | List of past incidents |
| `GET /v2/scheduled-maintenances/upcoming.json` | Upcoming scheduled maintenance events |
| `GET /v2/scheduled-maintenances/active.json` | Currently active maintenance event |
| `GET /v2/scheduled-maintenances.json` | List of past maintenance events |

**Gotchas**
- The Admin Console (admin web interface) is independent from the Controller infrastructure -- Admin Console downtime does NOT affect end-user connections to Resources
- Use `summary.json` for a single call covering status + incidents + upcoming maintenance; use individual endpoints for polling specific categories

**Related Docs**
- /docs/service-reliability
- /docs/api-overview
