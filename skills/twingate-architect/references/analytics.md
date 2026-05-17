# Twingate Analytics

## Summary
Twingate provides analytics covering network traffic, admin audit logs, and user activity reports. Data is accessible via the Admin Console and exportable in CSV format. Some network logging also supports real-time output via Connector configuration.

## Key Information
- **Three report types**: Network traffic logs, audit logs, and usage/activity reports
- Network connections between Clients and Connectors are all logged
- Audit logs cover most Admin Console actions and are retained for the lifetime of the account
- User activity report shows last access time per user
- All reports are exportable in CSV format from the Admin Console

## Report Types

| Report | Location | Export | Real-time |
|--------|----------|--------|-----------|
| Network Traffic | User & Resource detail pages in Admin Console | CSV | Yes (via Connector config) |
| Audit Logs | Admin Console | CSV | No |
| User Activity | Admin Console | CSV | No |

## Prerequisites
- Admin role required to access Admin Console reports
- Advanced Connector configuration needed for real-time network log output

## Access Paths
1. **Network Traffic**: Admin Console → individual User or Resource detail pages
2. **Audit Logs**: Admin Console → export function
3. **User Activity**: Admin Console → export function

## Gotchas
- Real-time network log streaming requires additional Connector configuration (not enabled by default)
- Not all Admin Console actions are logged — audit logs cover "most" actions, not all
- Audit log retention is account lifetime, but confirm this meets compliance requirements before relying on it

## Related Docs
- Analyzing network traffic (detailed guide)
- Advanced Connector configuration (for real-time log output)
- Audit Logs export guide
- User activity report export guide