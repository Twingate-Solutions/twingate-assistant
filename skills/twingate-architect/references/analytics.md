# Twingate Analytics

## Summary
Twingate provides analytics covering network traffic logs, admin audit logs, and user activity reports. Data is accessible via the Admin Console and exportable in CSV format. Network logs are also available in real-time via advanced Connector configuration.

## Key Information
- **Three report types**: Network traffic logs, audit logs, user activity reports
- Network connections between Clients and Connectors are all logged
- Audit logs cover most Admin Console actions and are retained for the lifetime of the account
- User activity report shows last access time per user
- CSV export available for all report types

## Data Access Methods
| Report Type | View In Console | Real-Time Stream | CSV Export |
|---|---|---|---|
| Network Traffic | User & Resource detail pages | Yes (Connector config) | Yes |
| Audit Logs | Admin Console | No | Yes |
| User Activity | Admin Console | No | Yes |

## Prerequisites
- Admin role required to access Admin Console reports
- Advanced Connector configuration needed for real-time network log streaming

## Configuration
- Real-time network log output requires **advanced Connector configuration** (separate from standard setup)

## Gotchas
- Not all Admin Console actions are logged in audit logs — documentation states "most actions" not all
- Real-time log streaming is an **advanced** Connector option, not enabled by default
- Audit logs are exportable for the **lifetime of the account** — no documented retention limit mentioned for network logs specifically

## Related Docs
- Analyzing network traffic (detailed)
- Advanced Connector configuration (for real-time log streaming)
- Audit Logs export guide
- User activity reports export guide