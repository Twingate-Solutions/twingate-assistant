# Monitoring Twingate Service Status & Maintenance Events

## Summary
Twingate exposes public REST APIs (via Statuspage) for real-time monitoring of service health, incidents, and maintenance events. All endpoints are unauthenticated GET requests returning JSON. A Postman collection is available for quick testing.

## Key Information
- Base URL: `https://status.twingate.com/api/v2/`
- No authentication required
- All timestamps in UTC (ISO 8601)
- Status page UI: `https://status.twingate.com`
- Full API reference: `https://status.twingate.com/api/`

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
- **Controller group**: Controller, User Authentication, Connection Authorization, IdP Synchronization
- **Relay Infrastructure group**: Data Relays, Peer-to-Peer Infrastructure
- **Admin Console group**: Admin Web Interface, Billing, Reports Export
- **Homepage group**: www.twingate.com, docs.twingate.com
- **Standalone**: Admin API, Analytics

## Response Structure

**Summary response key fields:**
```json
{
  "status": { "indicator": "none|minor|major|critical", "description": "string" },
  "components": [{ "id", "name", "status", "group", "group_id", "components" }],
  "incidents": [],
  "scheduled_maintenances": []
}
```

**Component status values:** `operational`, `degraded_performance`, `partial_outage`, `major_outage`, `under_maintenance`

**Maintenance event fields:** `id`, `name`, `status` (`scheduled|in_progress|completed`), `impact`, `started_at`, `resolved_at`, `incident_updates[].affected_components`

## Gotchas
- Admin Console downtime does **not** affect end-user connectivity — Controller infrastructure is independent
- Components with `group: true` are containers; check child component IDs in the `components` array for actual status
- `showcase: false` components are still returned but hidden from the public status page UI
- The summary endpoint returns all data in one call — prefer it over multiple endpoint calls if you need a full picture

## Related Docs
- [Twingate Status Page](https://status.twingate.com)
- [Statuspage API Reference](https://status.twingate.com/api/)
- [Postman Collection](https://www.twingate.com/docs/maintenance-events-service-status-outages) (linked from doc page)