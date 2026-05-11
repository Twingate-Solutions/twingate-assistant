# Exporting Network Traffic

## Summary
Twingate provides multiple methods to view and export network activity flowing through deployed Connectors. Only traffic routed through Connectors is captured; direct internet traffic is not visible. Useful for troubleshooting and security investigation.

## Key Information
- Four export/viewing methods available:
  - Admin Console UI (per-user or per-resource view)
  - Manual CSV export via Admin Console
  - JSON sync to AWS S3 bucket
  - Real-time connection logging from Connector process
- Event details include: Resource IP, protocol, connection type, duration
- Filters available: Resource, user, date, other activity criteria
- Schema documentation available on the network events schema page

## Prerequisites
- Active Connector(s) deployed on target network
- Appropriate admin access to Admin Console

## Log Retention by Plan
| Plan | Retention |
|------|-----------|
| Starter | 24 hours |
| Teams | 7 days |
| Business | 30 days |
| Enterprise | 12 months |

## Gotchas
- **Client IP not shown** — currently unavailable, planned for future update
- **No access-denied events** — Zero trust architecture means denied access is indistinguishable from a Resource not existing; clients only see Resources they have permission to access
- **Connector-only visibility** — Non-tunneled traffic (direct internet) is never captured regardless of configuration
- Short retention on lower tiers (24 hours on Starter) limits investigative window significantly

## Related Docs
- Network Events Schema
- AWS S3 Sync configuration
- Real-time connection logging (Connector)
- Twingate pricing page (plan comparisons)