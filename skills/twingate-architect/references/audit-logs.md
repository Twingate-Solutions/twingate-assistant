# Audit Logs

## Summary
Twingate provides audit log export functionality for account activity tracking. Logs capture create, delete, edit, and connect events across major resource categories. Export is available manually via Admin Console or automated sync to AWS S3.

## Key Information
- **Format:** JSON
- **Export methods:** Admin Console (manual) or AWS S3 bucket (automated sync)
- **Schema reference:** Separate audit logs schema page available

## Covered Event Categories
- Access
- API Keys
- Devices & Device Integrations
- Device Security
- Secure DNS (DNS-over-HTTPS + DNS filtering)
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

## Export Options

### Manual Export
- Via Admin Console UI

### Automated Export
- Sync to AWS S3 bucket in JSON format

## Gotchas
- No mention of retention limits or log rotation on this page — check schema page for field details
- S3 sync requires separate configuration (not detailed on this page)

## Related Docs
- Audit Logs Schema page (for JSON field definitions)
- AWS S3 bucket integration documentation