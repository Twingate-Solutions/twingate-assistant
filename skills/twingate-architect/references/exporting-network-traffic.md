# Exporting Network Traffic

## Summary
Twingate allows viewing and exporting network activity that flows through deployed Connectors. Only Connector-proxied traffic is visible; direct internet traffic is not captured. Multiple export methods are available depending on use case.

## Key Information
- Traffic visibility limited to Connector-routed traffic only (not general internet traffic)
- Four methods to access network traffic data
- Events viewable per User or per Resource in Admin Console
- Event details include: Resource IP, protocol, connection type, duration
- Client IP address not currently available
- No access-denied events (zero trust model: denied resources are invisible to clients)

## Export Methods
| Method | Format | Location |
|--------|--------|----------|
| View in Admin Console | UI | Admin Console (User/Resource pages) |
| Manual export | CSV | Admin Console |
| Sync to AWS S3 | JSON | AWS S3 bucket |
| Real-time connection logging | Direct output | Connector process |

## Log Retention by Plan
| Plan | Retention |
|------|-----------|
| Starter | 24 hours |
| Teams | 7 days |
| Business | 30 days |
| Enterprise | 12 months |

## Filtering Options
Filters available in Admin Console:
- Resource
- User
- Date
- Other activity criteria

## Gotchas
- **No client IP**: Not currently exposed in any export; planned for future update
- **No denied-access events**: Zero trust architecture makes denied resources indistinguishable from non-existent resources from the client perspective
- **Connector dependency**: Any Connector downtime creates gaps in traffic visibility
- Retention limits mean historical analysis is plan-dependent; ensure appropriate plan before incident investigation

## Related Docs
- Network Events Schema — field definitions for JSON/CSV exports
- AWS S3 sync configuration
- Real-time connection logging (Connector process output)
- Twingate pricing page (plan comparison)