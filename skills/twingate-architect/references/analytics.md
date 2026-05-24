# Twingate Analytics

## Summary
Twingate provides analytics covering network traffic, admin audit logs, and user activity reports. Data is accessible via the Admin Console and exportable in CSV format. Network connection logs are also available in real-time via advanced Connector configuration.

## Key Information
- Three distinct analytics areas: network traffic, audit logs, and usage/activity reports
- Network logs displayed on individual User and Resource detail pages in Admin Console
- Audit logs cover most Admin Console actions and are retained for the lifetime of the account
- All major report types are exportable in CSV format

## Analytics Categories

### Network Traffic
- Logs all connections between Clients and Connectors
- Viewable per-user and per-resource in Admin Console
- Real-time output available via advanced Connector configuration
- Exportable as CSV

### Audit Logs
- Captures most admin actions taken in the Admin Console
- Retained for the lifetime of the account
- Exportable from Admin Console

### Usage Reporting
- User activity report showing last access time per user
- Exportable from Admin Console

## Prerequisites
- Admin role required to access Admin Console analytics
- Advanced Connector configuration needed for real-time log streaming

## Configuration Values
- Real-time log output: configured via advanced Connector settings (see Connector advanced configuration docs)

## Gotchas
- Not all admin actions may be logged ("most actions" language implies some exceptions)
- Real-time network logs require additional Connector configuration — not enabled by default
- No mention of log retention limits for network traffic logs (only audit logs specify lifetime retention)

## Related Docs
- Analyzing network traffic (detailed guide)
- Advanced Connector configuration (real-time log streaming)
- Audit Logs export guide
- User activity reports export guide