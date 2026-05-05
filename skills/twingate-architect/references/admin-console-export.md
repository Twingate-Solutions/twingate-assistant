## Admin Console Export (Audit Logs)

Generates and downloads audit log reports from Settings > Reports in the Admin Console. Reports are exported in GZIP-compressed JSON format with one line per admin action.

**Key Information:**
- Navigate to Settings → Reports → Generate Audit Logs Report
- Select time range and category before generating
- Export runs in background; email notification sent when complete
- Time range shown in local timezone; exported event timestamps are in UTC

**Output Format:**
- GZIP-compressed JSON (`.json.gz`)
- One JSON line per event, containing: timestamp, actor, action, final state (and before-state if applicable)
- Full JSON schema available in the detailed audit logs schema documentation

**Gotchas:**
- Large exports can take up to a few hours (most complete within minutes)
- Safari: if the file appears empty, disable "Open 'safe' files after downloading" in Safari → Preferences → General to prevent auto-unpack issues
- Use any standard GZIP decompression tool (`gunzip`, 7-Zip, macOS Archive Utility)

**Related Docs:**
- /docs/audit-logs -- Audit log overview
- /docs/audit-logs-schema -- Detailed JSON schema for audit log events
- /docs/network-overview -- Real-time network metrics dashboard
