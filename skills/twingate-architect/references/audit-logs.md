# Audit Logs

## Summary
Twingate provides audit log export functionality for account activity tracking. Logs capture create, delete, edit, and connect events across major platform categories. Export is available via Admin Console (manual) or automated sync to AWS S3.

## Key Information
- **Format:** JSON
- **Export methods:** Manual via Admin Console, or automated sync to AWS S3
- **Schema documentation:** Available on separate audit logs schema page

## Covered Event Categories
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

## Event Types Captured
- `create`
- `delete`
- `edit`
- `connect`

## Export Methods

### Manual Export
- Accessed via Admin Console
- One-time JSON download

### Automated Export
- Sync to AWS S3 bucket
- Output format: JSON file

## Gotchas
- No mention of retention period or log volume limits
- S3 sync requires separate configuration (see S3 integration docs)
- Schema details are on a separate page — reference before building integrations

## Related Docs
- Audit Logs Schema page (for JSON field definitions)
- AWS S3 bucket sync configuration
- Admin Console documentation