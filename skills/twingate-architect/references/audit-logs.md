# Audit Logs

## Summary
Twingate audit logs track account activity across multiple categories including access, devices, network, and users. Logs can be manually exported via the Admin Console or automatically synced to an AWS S3 bucket in JSON format.

## Key Information
- **Event types captured**: create, delete, edit, and connect events
- **Categories covered**:
  - Access, API Keys, Devices, Device Integrations, Device Security
  - Secure DNS (DNS-over-HTTPS and DNS filtering)
  - Network (Remote Networks, Connectors, Resources)
  - Policies, Service Accounts, Users & Groups
  - Machine Keys, Data Exports, MFA Configurations
- **Output format**: JSON
- **Export methods**: Manual (Admin Console) or automated sync to AWS S3

## Prerequisites
- Admin Console access
- For S3 sync: AWS S3 bucket configured with appropriate permissions

## Export Methods

### Manual Export
- Access via Admin Console
- Download JSON report on demand

### Automated S3 Sync
- Syncs logs in JSON format to an AWS S3 bucket
- Requires separate S3 bucket configuration (see related docs)

## Related Docs
- [Audit Logs Schema](https://www.twingate.com/docs/audit-log-schema) — JSON field definitions
- [AWS S3 Bucket Sync](https://www.twingate.com/docs/audit-logs-s3) — S3 integration setup

## Gotchas
- Use cases limited to troubleshooting and investigation; no real-time streaming mentioned
- JSON schema details are on a separate page — review before building integrations against the log format