## Audit Logs

Overview of Twingate audit log capabilities. Covers what event categories are logged and the two available export methods: manual Admin Console download or continuous AWS S3 sync.

**Logged Event Categories:**
- Access
- API Keys
- Devices & Device Integrations
- Device Security
- Secure DNS (DNS-over-HTTPS, DNS filtering)
- Network (Remote Networks, Connectors, Resources)
- Policies
- Service Accounts
- Users & Groups
- Machine Keys
- Data Exports
- MFA Configurations

**Key Information:**
- Captures create, delete, edit, and connect events across all categories
- Export via Admin Console (manual, GZIP JSON) or continuous sync to AWS S3 (JSON)

**Related Docs:**
- /docs/audit-logs-schema -- JSON schema for audit log events
- /docs/admin-console-export -- Manual export via Admin Console
- /docs/syncing-data-to-s3 -- Continuous S3 sync configuration
