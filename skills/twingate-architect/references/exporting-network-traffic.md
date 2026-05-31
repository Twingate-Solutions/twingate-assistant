# Exporting Network Traffic

## Summary
Twingate enables viewing and exporting network activity that flows through deployed Connectors. Only Connector-proxied traffic is captured; direct internet traffic is not visible. Multiple export methods are available depending on use case.

## Key Information
- Only traffic flowing through **Connectors** is captured (not general internet traffic)
- Four methods to access network traffic data
- Events viewable per User or per Resource in Admin Console
- Detailed event data includes: Resource IP, protocol, connection type, duration
- Client IP address is **not currently available** (planned for future)

## Export Methods
| Method | Format | Location |
|--------|--------|----------|
| Admin Console view | UI | Admin Console (User/Resource pages) |
| Manual export | CSV | Admin Console |
| AWS S3 sync | JSON | AWS S3 bucket |
| Real-time connection logging | Raw logs | Connector process output |

## Log Retention by Plan
| Plan | Retention |
|------|-----------|
| Starter | 24 hours |
| Teams | 7 days |
| Business | 30 days |
| Enterprise | 12 months |

## Filtering Options
Filter network events by:
- Resource
- User
- Date
- Other activity criteria

## Gotchas
- **Access denied events are not logged**: Zero trust architecture means clients only see Resources they have permission to access — denied access is indistinguishable from a Resource not existing
- **Client IP not exposed**: Currently unavailable in all export formats
- **Retention limits**: Starter plan only retains 24 hours of logs — insufficient for most audit/compliance needs
- Only Connector traffic is captured; Twingate is not a full-tunnel VPN

## Related Docs
- Network Events Schema (event field definitions for CSV/JSON formats)
- AWS S3 sync configuration
- Real-time connection logging (Connector-level)
- Pricing page (plan comparison for retention limits)