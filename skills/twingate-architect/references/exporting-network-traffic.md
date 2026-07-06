# Exporting Network Traffic

## Page Title
Twingate Network Traffic Viewing and Exporting

## Summary
Twingate captures and exposes network activity flowing through deployed Connectors. Traffic not routed through Connectors (direct internet traffic) is not captured. Four export/viewing methods are available depending on use case.

## Key Information
- Only traffic through Connectors is captured — not general internet traffic
- Network events viewable per User or per Resource in Admin Console
- Event details include: Resource IP, protocol, connection type, duration
- Client IP address is **not currently available** (planned for future)
- Access denied events are **not captured** — zero trust model makes denied access indistinguishable from resource non-existence

## Log Retention by Plan
| Plan | Retention |
|------|-----------|
| Starter | 24 hours |
| Teams | 7 days |
| Business | 30 days |
| Enterprise | 12 months |

## Export Methods
1. **Admin Console** — View traffic inline on User or Resource pages; supports filtering
2. **CSV Export** — Manual export via Admin Console
3. **AWS S3 Sync** — JSON format, event streaming to S3 bucket
4. **Real-time Connection Logging** — Output directly from Connector process

## Filtering Options
Filters available in Admin Console:
- Resource
- User
- Date
- Other activity criteria

## Gotchas
- No access denied events logged — zero trust architecture prevents distinguishing denied access from non-existent resources
- Client IP not exposed in event data
- Short retention on lower tiers (Starter: 24h) limits forensic use
- Must have Connectors deployed — no Connectors = no traffic data

## Related Docs
- Network Events Schema (for JSON/CSV field definitions)
- AWS S3 Sync configuration
- Real-time connection logging (Connector process output)
- Twingate Pricing Page (plan comparison)