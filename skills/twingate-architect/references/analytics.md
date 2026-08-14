---
source: https://www.twingate.com/docs/analytics
type: docs
fetched: 2026-08-14
source_version: 59ae4a450836ccbf31d48a20505653e760e479387277aa73c4ae90220577b1b9
---

# Analytics

## Page Title
Analytics Overview

## Summary
Twingate provides analytics covering network traffic, admin audit logs, and user activity reports. Data is accessible via the Admin Console and exportable in CSV format. This page serves as an index to the three main analytics features.

## Key Information
- **Three analytics categories**: Network Traffic, Audit Logs, Usage Reporting
- Network connection logs are available per User and per Resource in Admin Console
- Audit logs cover most Admin Console actions and are retained for the lifetime of the account
- User activity reports show last access time per user
- All reports are exportable in CSV format

## Analytics Features

### Network Traffic Logs
- Logged for all Client-to-Connector connections
- Viewable in Admin Console under individual User and Resource detail pages
- Available as real-time output via advanced Connector configuration
- Exportable in CSV from Admin Console

### Audit Logs
- Captures most actions performed by Admins in the Admin Console
- Exportable in CSV format
- Retained for the lifetime of the account

### Usage Reporting
- User activity report showing last access time per user
- Exportable from Admin Console

## Prerequisites
- Admin role required to access Admin Console analytics
- Twingate account with active Connectors (for network traffic logs)

## Configuration Values
- Real-time network traffic logs require **advanced Connector configuration** (see Connector docs)

## Gotchas
- Not all Admin actions may be captured in audit logs ("most actions" — not explicitly "all")
- Real-time log streaming is an advanced Connector option, not enabled by default
- No mention of log retention limits for network traffic logs (audit logs are lifetime)

## Related Docs
- [Analyzing Network Traffic](https://www.twingate.com/docs/network-traffic) — detailed network log analysis
- [Advanced Connector Configuration](https://www.twingate.com/docs/connector-advanced) — real-time log output setup
- [Audit Logs Export](https://www.twingate.com/docs/audit-logs) — how to export admin audit logs
- [User Activity Reports](https://www.twingate.com/docs/user-activity) — export usage reports