# Twingate Analytics

## Summary
Twingate provides analytics covering network traffic, admin audit logs, and user activity reports. Data is accessible via the Admin Console and exportable in CSV format. Network connection logs are also available in real-time via Connector configuration.

## Key Information
- Three distinct analytics areas: network traffic, audit logs, and usage/activity reports
- All data accessible through the Admin Console
- Audit logs retained for the **lifetime of the account**
- Network logs exportable in CSV format
- Real-time network logs available via advanced Connector configuration

## Analytics Types

### Network Traffic
- Logs all connections between Clients and Connectors
- Viewable on individual **User** and **Resource** detail pages in Admin Console
- Real-time output via advanced Connector configuration option
- Exportable as CSV

### Audit Logs
- Captures most Admin actions taken in the Admin Console
- Exportable from Admin Console
- Retained for lifetime of account

### Usage Reporting
- User activity report showing **last access time** per user
- Exportable from Admin Console

## Prerequisites
- Admin role required to access Admin Console analytics
- Advanced Connector configuration needed for real-time network log streaming

## Configuration Values
- Real-time network log output: configured via **advanced Connector configuration** (see Connector docs for specific env vars/flags)

## Gotchas
- Not all Admin actions are logged — documentation states "most actions" are captured, not all
- Real-time log streaming requires additional Connector setup beyond default configuration
- Usage report shows last access time only; granular per-session user activity may require network traffic logs

## Related Docs
- Analyzing network traffic (detailed guide)
- Advanced Connector configuration (for real-time log output)
- Audit Logs export guide
- User activity reports export guide
- Admins role documentation