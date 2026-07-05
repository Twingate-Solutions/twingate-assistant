# Audit Logs

## Summary
Twingate provides audit log activity tracking for account events including create, delete, edit, and connect operations. Logs can be manually exported via Admin Console or automatically synced to AWS S3 in JSON format.

## Key Information
- **Event types tracked:** create, delete, edit, connect
- **Export format:** JSON
- **Export methods:** Manual (Admin Console) or automated (AWS S3 sync)
- **Schema reference:** Separate audit logs schema page available

## Covered Categories
- Access
- API Keys
- Devices
- Device Integrations
- Device Security
- Secure DNS (DNS-over-HTTPS + DNS filtering)
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

### Automated Export (AWS S3)
- Syncs JSON files to an AWS S3 bucket
- Requires separate S3 integration configuration

## Gotchas
- Export is JSON only — no native CSV or syslog format mentioned
- Two distinct export paths (Admin Console vs S3) require separate configuration
- S3 sync setup documented separately

## Related Docs
- Audit Logs Schema page (JSON field definitions)
- AWS S3 bucket sync configuration
- Admin Console documentation