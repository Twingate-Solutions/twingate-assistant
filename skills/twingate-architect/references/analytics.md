# Twingate Analytics

## Page Title
Analytics

## Summary
Twingate provides reporting tools for monitoring network traffic, admin actions, and user activity. Data is accessible via the Admin Console and exportable in CSV format. Three main analytics categories exist: network traffic logs, audit logs, and usage reports.

## Key Information
- **Network Traffic Logs**: Logged for all Client-to-Connector connections
- **Audit Logs**: Tracks most Admin Console actions; retained for account lifetime
- **Usage Reports**: Shows last access time per user

## Data Access Methods

### Network Traffic
- View per-user and per-Resource in Admin Console detail pages
- Stream in real-time via advanced Connector configuration
- Export as CSV from Admin Console

### Audit Logs
- Exportable from Admin Console
- Covers most admin actions taken in the Admin Console

### Usage Reports
- Export from Admin Console
- Contains last-access timestamp per user

## Prerequisites
- Admin role required to access Admin Console
- Connector must be deployed and active for network traffic logging
- Advanced Connector configuration needed for real-time log streaming

## Gotchas
- Not all admin actions may be logged ("most actions" implies some exceptions)
- Real-time log streaming requires additional Connector configuration beyond defaults
- Network traffic logs are tied to individual User/Resource pages — no single unified traffic view mentioned on this page

## Related Docs
- Analyzing Network Traffic (detailed guide)
- Advanced Connector Configuration (for real-time log output)
- Audit Logs export guide
- User Activity Reports export guide
- Admin role documentation