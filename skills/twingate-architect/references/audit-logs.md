# Audit Logs

## Summary
Twingate provides audit log activity tracking for account events including create, delete, edit, and connect operations. Logs can be manually exported via the Admin Console or automatically synced to an AWS S3 bucket in JSON format.

## Key Information
- **Event types tracked:** create, delete, edit, connect
- **Categories covered:**
  - Access, API Keys, Devices, Device Integrations, Device Security
  - Secure DNS (DNS-over-HTTPS and DNS filtering)
  - Network (Remote Networks, Connectors, Resources)
  - Policies, Service Accounts, Users & Groups
  - Machine Keys, Data Exports, MFA Configurations
- **Export format:** JSON
- **Export methods:** Manual (Admin Console) or automated sync to AWS S3

## Export Methods

### Manual Export
- Accessible via the Admin Console UI

### Automated Export
- Sync to AWS S3 bucket in JSON format
- See AWS S3 integration docs for setup

## Configuration Values
- Output format: JSON
- Destination options: Admin Console download, AWS S3 bucket

## Related Docs
- [Audit Logs Schema](https://www.twingate.com/docs/audit-logs-schema) — JSON field definitions
- AWS S3 bucket sync configuration
- Admin Console export guide

## Gotchas
- Only JSON format is supported; no CSV or syslog native export
- S3 sync requires separate configuration (not enabled by default)
- Schema details are on a separate page — reference before building log parsers or SIEM integrations