# Audit Logs

## Summary
Twingate provides audit log export functionality for account activity tracking. Logs cover create, delete, edit, and connect events across major platform categories. Export is available manually via Admin Console or automatically synced to AWS S3.

## Key Information
- **Format:** JSON
- **Export methods:** Manual (Admin Console) or automated sync to AWS S3
- **Schema reference:** Separate audit logs schema page available

## Covered Event Categories
- Access
- API Keys
- Devices & Device Integrations
- Device Security
- Secure DNS (DNS-over-HTTPS and DNS filtering)
- Network (Remote Networks, Connectors, Resources)
- Policies
- Service Accounts
- Users & Groups
- Machine Keys
- Data Exports
- MFA Configurations

## Event Types Captured
- Create
- Delete
- Edit
- Connect

## Export Options

### Manual Export
- Access via Admin Console
- One-time JSON download

### Automated Export
- Sync to AWS S3 bucket
- JSON file format
- Requires S3 bucket configuration (see related docs)

## Gotchas
- Only JSON format is supported; no native CSV or syslog export
- AWS S3 sync requires separate configuration steps
- Schema details are on a separate documentation page—verify field names before building integrations

## Related Docs
- Audit Logs Schema page (JSON field definitions)
- AWS S3 bucket sync configuration
- Admin Console guide