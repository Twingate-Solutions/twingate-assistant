---
source: https://www.twingate.com/docs/audit-logs
type: docs
fetched: 2026-08-14
source_version: e8f2cc6e7bfbe8054992d2c2671d6f4ce1fbd4ec4a3f5ef91509b564b6c8bdc8
---

# Audit Logs

## Summary
Twingate provides audit log activity tracking for account events including create, delete, edit, and connect operations. Logs can be manually exported via the Admin Console or automatically synced to an AWS S3 bucket in JSON format.

## Key Information
- **Export formats**: JSON only
- **Export methods**: Manual (Admin Console) or automated (AWS S3 sync)
- **Event types tracked**: create, delete, edit, connect

## Covered Categories
- Access
- API Keys
- Devices
- Device Integrations
- Device Security
- Secure DNS (DNS-over-HTTPS and DNS filtering)
- Network (Remote Networks, Connectors, Resources)
- Policies
- Service Accounts
- Users & Groups
- Machine Keys
- Data Exports
- MFA Configurations

## Export Methods

### Manual Export
- Access via Admin Console
- Downloads JSON report on demand

### Automated Export
- Sync to AWS S3 bucket in JSON format
- See AWS S3 integration docs for configuration

## Related Docs
- [Audit Logs Schema](https://www.twingate.com/docs/audit-logs-schema) — JSON field definitions
- AWS S3 bucket sync configuration
- Admin Console export instructions

## Gotchas
- Only JSON format is supported; no CSV or syslog native export
- Schema details are on a separate page — required reading for parsing log data programmatically