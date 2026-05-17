# Audit Logs

## Summary
Twingate provides audit logging for account activity across security, network, and access categories. Logs can be manually exported via the Admin Console or automatically synced to an AWS S3 bucket in JSON format.

## Key Information
- **Event types captured**: create, delete, edit, connect
- **Categories logged**:
  - Access, API Keys, Devices, Device Integrations, Device Security
  - Secure DNS (DNS-over-HTTPS + DNS filtering)
  - Network (Remote Networks, Connectors, Resources)
  - Policies, Service Accounts, Users & Groups
  - Machine Keys, Data Exports, MFA Configurations
- **Export format**: JSON
- **Export methods**: Manual (Admin Console) or automated (AWS S3 sync)

## Export Methods

### Manual Export
- Access via Admin Console
- Download on-demand

### Automated Export
- Sync to AWS S3 bucket in JSON format
- See S3 bucket integration documentation for setup

## Configuration Values
- Output format: JSON
- Schema reference: Twingate audit logs schema page (separate doc)

## Gotchas
- No mention of retention period limits in this page — check schema docs for timestamp/retention details
- S3 sync requires separate configuration (not covered on this page)

## Related Docs
- Audit Logs Schema page (JSON field definitions)
- AWS S3 bucket sync configuration
- Admin Console export guide