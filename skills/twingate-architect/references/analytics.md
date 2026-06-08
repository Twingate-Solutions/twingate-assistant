# Twingate Analytics

## Summary
Twingate provides analytics covering network traffic, admin audit logs, and user activity reports. Data is accessible via the Admin Console and exportable in CSV format. Network connection logs are also available in real-time via advanced Connector configuration.

## Key Information
- **Three report types**: Network traffic logs, audit logs, and usage/activity reports
- **Network logs** appear on individual User and Resource detail pages in Admin Console
- **Audit logs** capture most Admin Console actions; retained for lifetime of account
- **User activity report** shows last access time per user
- All reports exportable in CSV format from Admin Console
- Network logs also streamable in real-time via Connector configuration

## Prerequisites
- Admin role required to access Admin Console
- Advanced Connector configuration needed for real-time log streaming

## Data Access Methods

| Report Type | Admin Console | Export | Real-Time Stream |
|-------------|--------------|--------|-----------------|
| Network Traffic | ✓ (User/Resource pages) | ✓ CSV | ✓ (Connector config) |
| Audit Logs | ✓ | ✓ CSV | ✗ |
| User Activity | ✗ | ✓ CSV | ✗ |

## Configuration Values
- Real-time network log output: configured via **advanced Connector configuration** (see separate Connector docs)

## Gotchas
- Audit logs cover "most" Admin actions — not explicitly all actions
- Real-time log streaming requires additional Connector-level configuration, not enabled by default
- User activity report only shows last access time, not full session history

## Related Docs
- Analyzing network traffic (detailed guide)
- Advanced Connector configuration (real-time log output)
- Audit Logs export guide
- User activity reports export guide