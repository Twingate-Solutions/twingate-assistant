# Exporting Network Traffic

## Summary
Twingate enables viewing and exporting network activity that flows through deployed Connectors. Only Connector-proxied traffic is captured; direct internet traffic is not visible. Multiple export methods are available depending on use case.

## Key Information
- Only traffic flowing through deployed Connectors is captured
- Four methods to access network traffic data
- Log retention varies by plan tier
- Client IP address is not currently captured (planned for future)
- Access denied events are not logged (zero-trust architecture limitation)

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

## Viewing in Admin Console
- Navigate to individual **User** or **Resource** page
- View recent network traffic events
- Click specific events for details: Resource IP, protocol, connection type, duration
- Filter by: Resource, user, date, activity criteria

## Gotchas
- **No client IP**: Currently unavailable, planned for future release
- **No access denied events**: Zero-trust model means clients only see Resources they have permission to access; denied access is indistinguishable from a Resource not existing
- **Connector-only scope**: Non-Connector traffic (direct internet) is never captured regardless of plan
- Retention limits are minimums — check pricing page for current plan details

## Related Docs
- Network Events Schema (for JSON/CSV field definitions)
- AWS S3 sync configuration
- Real-time connection logging (Connector)
- Twingate pricing page (plan comparison)