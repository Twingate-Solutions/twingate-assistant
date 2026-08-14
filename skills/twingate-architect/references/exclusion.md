---
source: https://www.twingate.com/docs/exclusion
type: docs
fetched: 2026-08-14
source_version: bfb71764bf7f5e40d3b3c94e4fd216a9809863187ec9c3f80508d705155e8a58
---

# Resource Exclusion (Bypass Twingate)

## Summary
Resource exclusions allow specific addresses within a Resource to bypass Twingate's Connector and Relay infrastructure entirely, routing traffic directly to the local OS routing table. This is useful for carving exceptions out of broader wildcard Resources (e.g., excluding a public status page from a `*.corp.example.com` Resource). Bypassed Resources remain reachable even when all Connectors are offline.

## Key Information
- **Routing Mode** field on each Resource: `Through Twingate` (default) or `Bypass Twingate`
- Bypassed traffic: no Connector/Relay, no Security Policy evaluation, no network events generated
- DNS filtering and OS-level internet security still apply
- Excluded Resources remain in their Remote Network for organizational purposes
- Aliases on excluded Resources also bypass Twingate
- Routing Mode changes are captured in audit logs; traffic itself is not logged
- Excluded Resources are invisible to Clients (no Resource list entry, no auth prompt)

## Prerequisites
Minimum Client versions:
- macOS: 2026.182
- iOS: 2026.182
- Android: 2026.181
- Linux: 2026.188 (in `latest` channel)
- Windows: not yet supported

## Step-by-Step (Admin Console)
1. Open Resource creation modal or edit an existing Resource
2. Under **Routing Mode**, select **Bypass Twingate**
3. Enter a specific FQDN or IP address
4. Save — takes effect immediately on supported Clients

## Configuration Values

**GraphQL API:**
```graphql
createResource / updateResource {
  routingMode: BYPASS_TWINGATE  # default: THROUGH_TWINGATE
}
```

**REST API:**
```json
{
  "routing_mode": "bypass_twingate"  // default: "through_twingate"
}
```

## Gotchas
- **Wildcards and CIDR ranges are blocked** — only specific FQDNs or IPs accepted (enforced at UI and API level to prevent routing loops)
- **No port restrictions** — port section is hidden when Bypass is selected
- **Identity Firewall Resources cannot be bypassed** — blocked at UI and API level (per-user identity evaluation is incompatible)
- **Security Policies and JIT/usage-based access** are hidden in UI for excluded Resources (Ephemeral Access still configurable)
- **No network events** generated — excluded traffic never reaches Twingate infrastructure
- Older Clients below minimum versions will not receive bypass behavior (silently ignored)

## Identifying Excluded Resources
- Add **Routing Mode** column via "add column" menu in Resources data grid (hidden by default)
- Bypass icon appears inline in Resource name cell
- Filter Resources by Routing Mode (`Through Twingate` / `Bypass Twingate`)

## Related Docs
- Routing Mode (Resource settings)
- Identity Firewall
- Security Policies
- Ephemeral Access / JIT Access
- Audit Logging