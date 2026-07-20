<!-- triage: unassigned URL: https://www.twingate.com/docs/exclusion -->

# Resource Exclusion (Bypass Twingate)

## Summary
Resources can be set to "Bypass Twingate" routing mode, sending traffic directly to the OS routing table instead of through Connectors/Relays. This allows carving exceptions from broader Resources (e.g., excluding a public status page from a wildcard domain Resource) without topology restructuring.

## Key Information
- Default routing mode is `Through Twingate`; alternative is `Bypass Twingate`
- Bypassed Resources: no Connector/Relay involved, no Security Policy evaluation, no network events generated
- Bypassed Resources remain reachable even if all Connectors in a Remote Network are offline
- DNS filtering and OS-level internet security still apply
- Audit log captures all Routing Mode changes (who, before/after values)
- Bypassed Resources are invisible to end users — don't appear in Client Resource list, no auth prompt triggered

## Prerequisites
Minimum Client versions required:
- macOS: 2026.182
- iOS: 2026.182
- Android: 2026.181
- Linux: 2026.188 (in `latest` channel)
- Windows: not yet supported

## Step-by-Step (Admin Console)
1. Open Resource creation modal or edit existing Resource
2. Under **Routing Mode**, select **Bypass Twingate**
3. Enter specific FQDN or IP address (wildcards/CIDR blocked)
4. Save — active immediately on qualifying Clients

## Configuration Values

| Context | Field | Value |
|---|---|---|
| GraphQL API | `routingMode` | `BYPASS_TWINGATE` / `THROUGH_TWINGATE` (default) |
| REST API | `routing_mode` | `"bypass_twingate"` / `"through_twingate"` (default) |

Apply to `createResource` or `updateResource` mutations/payloads.

## Gotchas
- **Wildcards and CIDR ranges are blocked** — must use specific FQDN or IP; enforced at both UI and API level
- **Port restrictions unavailable** — port section hidden when Bypass is selected
- **Identity Firewall (ID-FW) Resources cannot be bypassed** — blocked at UI and API level
- **No network events generated** — bypassed traffic never reaches Twingate infrastructure; Security Policies and JIT/usage-based access options hidden in UI
- **Ephemeral Access** can still be configured for bypassed Resources
- **Remote Network association persists** — bypassed Resources still belong to a Remote Network (organizational only)
- **Aliases inherit bypass** — an alias on a bypassed Resource also bypasses Twingate
- Older Clients (below minimum versions) will not apply exclusions silently

## Identifying Excluded Resources
- Add **Routing Mode** column via "add column" menu in Resources data grid (hidden by default)
- Bypass icon appears inline in Resource name cell
- Filter by Routing Mode to manage sets separately

## Related Docs
- Routing Mode settings
- Security Policies
- Identity Firewall
- Ephemeral Access
- Audit Logging