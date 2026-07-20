# Network Traffic Export - Twingate

## Page Title
Exporting Network Traffic

## Summary
Twingate captures and exports network activity that flows through deployed Connectors (not all user traffic). Multiple export methods are available ranging from Admin Console viewing to real-time Connector logging. Traffic visibility is scoped only to Connector-proxied traffic.

## Key Information
- Only traffic routed through Connectors is captured — direct internet traffic is invisible to Twingate
- Four export methods available (see Step-by-Step)
- Events viewable per User or per Resource in Admin Console
- Client IP addresses are **not** currently shown
- Access denied events are **not** logged (by design — zero trust model hides non-permitted resources entirely)

## Prerequisites
- Deployed Connectors on your network
- Admin Console access
- Appropriate plan tier for required retention period

## Export Methods (Step-by-Step)

1. **View in Admin Console** — Navigate to individual User or Resource page to see recent traffic; click events for details (Resource IP, protocol, connection type, duration)
2. **Manual CSV Export** — Export via Admin Console UI
3. **AWS S3 Sync** — Sync network events in JSON format to an S3 bucket
4. **Real-time Connection Logging** — Output directly from the Connector process

## Configuration Values
- Event schema reference: [Network Events Schema page](https://www.twingate.com/docs/network-events-schema)
- Export formats: CSV (manual), JSON (S3 sync)

## Retention Periods by Plan

| Plan | Retention |
|------|-----------|
| Starter | 24 hours |
| Teams | 7 days |
| Business | 30 days |
| Enterprise | 12 months |

## Gotchas
- **No access denied events**: Zero trust design means clients only know about permitted Resources; denied access is indistinguishable from resource non-existence
- **No client IP**: Currently not captured in event data (planned for future update)
- **Connector scope**: Events only reflect traffic through your deployed Connectors — split-tunnel traffic to internet bypasses this entirely
- Retention limits mean historical investigations are plan-dependent

## Filtering
Admin Console supports filtering by: Resource, User, Date, Activity criteria

## Related Docs
- Network Events Schema
- AWS S3 Sync setup
- Real-time Connection Logging
- Connector deployment
- Twingate Pricing (plan comparison)