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
- **Export formats:** JSON only
- **Export methods:** Manual (Admin Console) or automated sync (AWS S3)

## Export Methods

### Manual Export
- Access via Admin Console
- Download as JSON file on-demand

### Automated Export
- Sync to AWS S3 bucket in JSON format
- Requires separate S3 integration configuration

## Configuration Values
- Output format: JSON
- Destination options: Admin Console download, AWS S3 bucket

## Related Docs
- [Audit Logs Schema](https://www.twingate.com/docs/audit-logs-schema) — JSON field definitions and structure
- AWS S3 bucket sync configuration (linked from Admin Console)

## Gotchas
- Only JSON format is supported; no CSV or syslog output natively
- S3 sync requires additional setup beyond basic audit log access
- Use cases limited to troubleshooting and investigation per documentation