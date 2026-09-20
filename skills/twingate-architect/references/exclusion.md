---
source: https://www.twingate.com/docs/exclusion
type: docs
fetched: 2026-09-20
source_version: 122f1ac589d6311880e371b3cbfd8602d430564afc065b47de4e46a70a6db9ca
---

# Resource Exclusion (Bypass Twingate)

## Summary
Resource exclusions allow specific addresses to bypass Twingate infrastructure entirely, routing traffic directly to the OS routing table. Designed for carving exceptions from broader Resources (e.g., excluding a public status page from a wildcard Resource) without restructuring topology. Excluded Resources remain reachable even when all Connectors are offline.

## Key Information
- **Routing Mode** setting per Resource: `Through Twingate` (default) or `Bypass Twingate`
- Bypassed traffic: no Connector/Relay, no Security Policy evaluation, no network events generated
- DNS filtering and OS-level internet security still apply
- Excluded Resources still belong to a Remote Network (organizational only)
- Aliases on excluded Resources also bypass Twingate
- Changes to Routing Mode are captured in audit log; traffic itself generates no network events
- Excluded Resources are **invisible** to Clients (not shown in Resource list, no auth prompt)

## Prerequisites
Minimum Client versions required:
| Platform | Version |
|----------|---------|
| macOS | 2026.182 |
| Windows | 2026.211 |
| Linux | 2026.188 |
| iOS | 2026.182 |
| Android | 2026.181 |

## Configuration

### Admin Console
1. Open Resource creation modal or edit existing Resource
2. Under **Routing Mode**, select **Bypass Twingate**
3. Enter specific FQDN or IP address
4. Save

### API (GraphQL)
```graphql
# createResource or updateResource mutation
routingMode: BYPASS_TWINGATE   # defaults to THROUGH_TWINGATE if omitted
```

### REST API
```json
{
  "routing_mode": "bypass_twingate"
}
// Defaults to "through_twingate" if omitted
```

## Configuration Values
| Context | Field | Values |
|---------|-------|--------|
| GraphQL | `routingMode` | `BYPASS_TWINGATE`, `THROUGH_TWINGATE` |
| REST | `routing_mode` | `"bypass_twingate"`, `"through_twingate"` |

## Gotchas
- **No wildcards or CIDR ranges** — must be a specific FQDN or IP address; blocked at UI and API level (prevents routing loops)
- **No port restrictions** — port section hidden when Bypass is selected
- **Identity Firewall Resources cannot be bypassed** — blocked at UI and API level
- **No Security Policies or JIT/usage-based access** — hidden in UI for excluded Resources (Ephemeral Access still configurable)
- **Older Clients silently ignore** exclusions — clients below minimum version won't apply bypass behavior
- **Routing Mode column hidden by default** — must manually add via "add column" menu in Resources grid

## Identifying Excluded Resources
- Add **Routing Mode** column via "add column" menu in Resources data grid
- Bypass icon appears inline in Resource name cell regardless of column visibility
- Filter by Routing Mode to manage sets separately

## Related Docs
- Routing Mode (general)
- Security Policies
- Identity Firewall
- Ephemeral Access
- Audit Logging