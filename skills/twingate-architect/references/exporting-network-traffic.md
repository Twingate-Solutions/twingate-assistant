# Exporting Network Traffic

## Summary
Twingate enables viewing and exporting network activity flowing through deployed Connectors. Only traffic routed through Connectors is captured; direct internet traffic is not visible. Multiple export methods are available depending on use case.

## Key Information
- Traffic visibility limited to Connector-routed traffic only (not a full VPN traffic capture)
- Four export/viewing methods available
- Event schema documented separately on network events schema page
- Client IP addresses not currently available in event data
- Access denied events not logged (zero trust architecture limitation—clients only see permitted Resources)

## Export Methods
| Method | Format | Location |
|--------|--------|----------|
| Admin Console view | UI | User or Resource page |
| Manual export | CSV | Admin Console |
| AWS S3 sync | JSON | S3 bucket |
| Real-time connection logging | Direct output | Connector process |

## Log Retention by Plan
| Plan | Retention |
|------|-----------|
| Starter | 24 hours |
| Teams | 7 days |
| Business | 30 days |
| Enterprise | 12 months |

## Filtering Options
Available filter criteria in Admin Console:
- Resource
- User
- Date
- Other activity criteria

## Event Detail Fields
When clicking into a specific event:
- Resource IP address
- Protocol
- Connection type
- Duration

## Gotchas
- **No client IP**: Currently unavailable; planned for future update
- **No access denied events**: Zero trust model makes denied access indistinguishable from non-existent Resources at the client level
- **Connector dependency**: Only traffic routed through Connectors appears; ensure Connectors are deployed on target networks before relying on this for audit/compliance
- **Retention limits**: Starter plan's 24-hour retention is unsuitable for audit or forensic use cases

## Related Docs
- Network Events Schema page
- AWS S3 sync documentation
- Real-time connection logging documentation
- Twingate pricing page (plan comparison)