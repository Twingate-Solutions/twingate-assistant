# Exporting Network Traffic

## Summary
Twingate allows viewing and exporting network activity that flows through deployed Connectors. Only Connector-proxied traffic is captured; direct internet traffic is not visible. Multiple export formats and destinations are supported.

## Key Information
- Traffic visibility limited to traffic flowing through Connectors only
- Four methods to access network traffic data
- Events viewable per User or per Resource in Admin Console
- Filters available by Resource, user, date, or activity criteria
- Client IP address not currently captured in events

## Export Methods
| Method | Format | Location |
|--------|--------|----------|
| Admin Console view | UI | Admin Console (User/Resource pages) |
| Manual export | CSV | Admin Console download |
| S3 sync | JSON | AWS S3 bucket |
| Real-time logging | — | Connector process output |

## Log Retention by Plan
| Plan | Retention |
|------|-----------|
| Starter | 24 hours |
| Teams | 7 days |
| Business | 30 days |
| Enterprise | 12 months |

## Event Detail Fields
When clicking into a specific event:
- Resource IP address
- Protocol
- Connection type
- Duration

## Gotchas
- **No access denied events**: Zero trust architecture means clients only see Resources they have permission to access — denied access is indistinguishable from a Resource not existing
- **No client IP**: Client IP address is not currently included in exported events
- **Connector-only visibility**: Non-Connector traffic (direct internet) is never captured
- **Retention limits**: Short retention on lower tiers (24h on Starter) — configure S3 sync for long-term storage needs

## Related Docs
- Network Events Schema — field definitions for JSON/CSV exports
- AWS S3 sync configuration
- Real-time connection logging (Connector output)
- Twingate pricing page (plan comparison)