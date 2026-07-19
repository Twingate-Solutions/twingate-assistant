# Twingate Analytics

## Summary
Twingate provides analytics covering network traffic, admin audit logs, and user activity reports. Data is accessible via the Admin Console and exportable in CSV format. Network connection logs are also available in real-time via advanced Connector configuration.

## Key Information
- **Three report types**: Network traffic logs, audit logs, and usage/activity reports
- Network logs are viewable per User and per Resource in the Admin Console
- Audit logs cover most Admin Console actions and are retained for the lifetime of the account
- User activity report shows last access time for every user
- All reports are exportable in CSV format

## Report Types

| Report | Location | Export | Real-time |
|--------|----------|--------|-----------|
| Network Traffic | User/Resource detail pages | CSV | Via Connector config |
| Audit Logs | Admin Console | CSV | No |
| User Activity | Admin Console | CSV | No |

## Prerequisites
- Admin role required to access Admin Console reports
- Advanced Connector configuration needed for real-time network log streaming

## Access Points
- **Network traffic**: Admin Console → individual User or Resource detail pages
- **Audit logs**: Admin Console → export option
- **User activity**: Admin Console → export option

## Gotchas
- Audit logs only cover *most* admin actions, not necessarily all actions
- Real-time network log output requires additional Connector configuration (advanced option), not enabled by default
- Network logs record connections between Clients and Connectors only

## Related Docs
- Analyzing network traffic (detailed guide)
- Advanced Connector configuration (for real-time log output)
- Audit log export guide
- User activity report export guide