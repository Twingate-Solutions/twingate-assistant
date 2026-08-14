---
source: https://www.twingate.com/docs/exporting-network-traffic
type: docs
fetched: 2026-08-14
source_version: bada7980d631d6f1053ecbadadabb79ce310d4a4bcf0570122066f46aebf07d6
---

# Network Traffic Export - Twingate

## Page Title
Exporting Network Traffic

## Summary
Twingate captures and exports network activity that flows through deployed Connectors. Multiple export methods are available for troubleshooting and audit purposes. Only Connector-proxied traffic is visible; direct internet traffic is not captured.

## Key Information
- Traffic visibility limited to flows through deployed Connectors only
- Four export/viewing methods available
- Event schema details on separate network events schema page
- Client IP address not currently captured (planned for future)
- Access denied events not logged (zero-trust design limitation)

## Export Methods
| Method | Format | Location |
|--------|--------|----------|
| Admin Console view | UI | User or Resource page |
| Manual export | CSV | Admin Console download |
| S3 sync | JSON | AWS S3 bucket |
| Real-time connection logging | Raw logs | Connector process output |

## Log Retention by Plan
| Plan | Retention |
|------|-----------|
| Starter | 24 hours |
| Teams | 7 days |
| Business | 30 days |
| Enterprise | 12 months |

## Admin Console Filtering
Filter network events by:
- Resource
- User
- Date
- Other activity criteria

## Event Detail Fields (per event)
- Resource IP address
- Protocol
- Connection type
- Duration

## Gotchas
- **No access denied events**: Zero-trust model makes denied access indistinguishable from non-existent resources; clients only see Resources they have permission to access
- **No client IP**: Source IP of connecting client is not currently recorded
- **Connector-only visibility**: Non-Twingate internet traffic is invisible — this is not a full network monitor
- **Retention limits**: Short retention on lower tiers (24 hours on Starter) limits historical investigation capability

## Prerequisites
- Connectors must be deployed on target networks for any traffic to appear
- Admin Console access required for CSV export and UI viewing
- AWS S3 bucket required for JSON sync method

## Related Docs
- Network Events Schema page (for JSON/CSV field definitions)
- Twingate Pricing page (plan comparison)
- Connector deployment documentation
- AWS S3 sync configuration