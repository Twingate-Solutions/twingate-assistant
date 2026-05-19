# Exporting Network Traffic

## Summary
Twingate enables viewing and exporting network activity flowing through deployed Connectors. Only traffic routed through Connectors is captured — direct internet traffic is not visible. Multiple export methods are available depending on use case.

## Key Information
- Network activity is **only captured for traffic through Connectors**, not general internet traffic
- Events viewable per User or per Resource in Admin Console
- Event details include: Resource IP, protocol, connection type, duration
- Client IP address is **not currently available** (planned for future)
- Access denied events are **not logged** — zero trust architecture means clients only see Resources they have permission to access

## Export Methods
| Method | Format | Details |
|--------|--------|---------|
| Admin Console view | UI | Filter by Resource, user, date, activity |
| Manual CSV export | CSV | Via Admin Console |
| AWS S3 sync | JSON | Real-time network events stream |
| Connector real-time logging | Raw | Output directly from Connector process |

## Log Retention by Plan
| Plan | Retention |
|------|-----------|
| Starter | 24 hours |
| Teams | 7 days |
| Business | 30 days |
| Enterprise | 12 months |

## Filtering Options (Admin Console)
- Resource
- User
- Date
- Activity criteria

## Gotchas
- **No access denied events**: Zero trust design prevents distinguishing "denied" from "resource doesn't exist" — clients only see permitted Resources
- **No client IP**: Currently unavailable in event data
- **Connector dependency**: Traffic not routed through a Connector will never appear in logs regardless of plan
- Retention limits are **minimums** — check pricing page for full plan details

## Related Docs
- Network Events Schema (event field definitions for CSV/JSON formats)
- AWS S3 sync configuration
- Real-time connection logging (Connector-level)
- Pricing page (plan comparison)