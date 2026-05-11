# Audit Logs

## Summary
Twingate provides audit log functionality for tracking account activity across all major resource categories. Logs capture create, delete, edit, and connect events and can be exported manually or synced automatically to AWS S3 in JSON format.

## Key Information
- **Event types captured**: create, delete, edit, connect
- **Categories covered**:
  - Access, API Keys, Devices, Device Integrations, Device Security
  - Secure DNS (DNS-over-HTTPS + DNS filtering)
  - Network (Remote Networks, Connectors, Resources)
  - Policies, Service Accounts, Users & Groups
  - Machine Keys, Data Exports, MFA Configurations
- **Export format**: JSON
- **Export methods**: Manual via Admin Console OR automated sync to AWS S3

## Prerequisites
- Twingate account with Admin Console access
- For S3 sync: AWS S3 bucket configured (see S3 integration docs)

## Export Methods

### Manual Export
1. Log into Admin Console
2. Navigate to Audit Logs section
3. Export JSON report directly

### Automated S3 Sync
- Configure AWS S3 bucket integration
- Logs sync automatically in JSON format
- See separate S3 bucket documentation for setup steps

## Configuration Values
- **Output format**: JSON (fixed, no alternatives)
- **Delivery options**: Admin Console download | AWS S3 sync

## Gotchas
- JSON schema details are on a separate schema page — review before building parsers or SIEM integrations
- No mention of retention limits, log streaming (e.g., SIEM direct push), or filtering options on this page

## Related Docs
- Audit Logs Schema page (JSON field definitions)
- AWS S3 bucket sync configuration
- Admin Console documentation