# Audit Logs

## Summary
Twingate provides audit logging for account activity across multiple categories. Logs can be manually exported via the Admin Console or automatically synced to an AWS S3 bucket in JSON format.

## Key Information
- **Export formats**: JSON only
- **Export methods**: Manual (Admin Console) or automated (AWS S3 sync)
- **Event types captured**: create, delete, edit, connect

## Logged Categories
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

### Automated S3 Sync
- Syncs JSON files to an AWS S3 bucket
- Requires separate S3 integration configuration

## Related Docs
- Audit Logs Schema — JSON structure reference
- AWS S3 bucket sync configuration
- Admin Console export guide

## Gotchas
- Only JSON format is supported; no CSV or syslog native export
- For schema details needed for parsing/integration, consult the audit logs schema page separately