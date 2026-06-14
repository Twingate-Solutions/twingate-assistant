# Exporting Network Traffic

## Summary
Twingate enables viewing and exporting network activity that flows through deployed Connectors. Only Connector-proxied traffic is captured; direct internet traffic is not visible. Multiple export methods are available depending on use case.

## Key Information
- **Scope**: Only traffic flowing through Connectors is logged — not general internet traffic
- **Four export methods**: Admin Console view, CSV export, AWS S3 JSON sync, real-time Connector logs
- **Log retention by plan**:
  - Starter: 24 hours
  - Teams: 7 days
  - Business: 30 days
  - Enterprise: 12 months

## Viewing in Admin Console
- Access logs via individual **User** or **Resource** pages
- Event details include: Resource IP, protocol, connection type, duration
- Filter by: Resource, user, date, other activity criteria

## Export Methods

| Method | Format | Reference |
|--------|--------|-----------|
| Admin Console view | UI | — |
| Manual CSV export | CSV | Admin Console |
| AWS S3 sync | JSON | Separate doc |
| Real-time Connector logging | — | Separate doc |

## Gotchas
- **Client IP not shown** — planned for future update
- **No access-denied events**: Zero trust model means clients only know about Resources they can access; denied access is indistinguishable from a Resource not existing
- Traffic must flow through a Connector to be logged — Twingate is not a full-tunnel VPN

## Related Docs
- Network Events Schema page
- AWS S3 sync documentation
- Real-time connection logging (Connector output)
- Pricing page (plan retention details)