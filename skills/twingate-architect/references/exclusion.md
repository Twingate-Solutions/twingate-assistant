---
source: https://www.twingate.com/docs/exclusion
type: docs
fetched: 2026-08-06
source_version: b4d18c0552a9b24f61453a16fe26489460288f026a84d8c2126df5445d07dab3
---

# Resource Exclusion (Bypass Twingate)

## Summary
Allows specific addresses within a Resource to bypass Twingate's Connector and Relay infrastructure entirely, routing traffic directly via the local OS routing table. Useful for carving exceptions from broad wildcard Resources without restructuring topology. Excluded Resources remain reachable even when all Connectors are offline.

## Key Information
- **Routing Mode** per Resource: `Through Twingate` (default) or `Bypass Twingate`
- Bypass traffic: no Connector, no Relay, no Security Policy evaluation, no network events generated
- DNS filtering and OS-level internet security still apply
- Excluded Resources remain reachable when all Connectors are offline
- Audit log captures all Routing Mode changes (actor, before/after values)
- Excluded Resources do **not** appear in the Client's Resource list or trigger auth prompts

## Prerequisites
Minimum Client versions:
- macOS: `2026.182`
- iOS: `2026.182`
- Android: `2026.181`
- Linux: `2026.188` (currently in `latest` channel)
- Windows: not yet supported

## Configuration

### Admin Console
1. Open Resource creation modal or edit existing Resource
2. Under **Routing Mode**, select **Bypass Twingate**
3. Enter a specific FQDN or IP address
4. Save

### API (GraphQL)
```graphql
createResource / updateResource mutation:
  routingMode: BYPASS_TWINGATE   # defaults to THROUGH_TWINGATE if omitted
```

### REST API
```json
{
  "routing_mode": "bypass_twingate"   // defaults to "through_twingate" if omitted
}
```

## Configuration Values
| Parameter | Values | Default |
|-----------|--------|---------|
| `routingMode` (GraphQL) | `BYPASS_TWINGATE` / `THROUGH_TWINGATE` | `THROUGH_TWINGATE` |
| `routing_mode` (REST) | `bypass_twingate` / `through_twingate` | `through_twingate` |

## Gotchas
- **No wildcards or CIDR ranges** — only specific FQDNs or IPs accepted; blocked at both UI and API level (prevents routing loops)
- **No port restrictions** — port section hidden when Bypass selected
- **Identity Firewall Resources cannot be bypassed** — blocked at UI and API level
- **Aliases inherit bypass** — an alias on a bypassed Resource also bypasses Twingate
- **No network events generated** — bypassed traffic never reaches Twingate infrastructure; Security Policies and JIT/usage-based access options hidden in UI
- **Ephemeral Access** can still be configured on excluded Resources
- Older Clients silently ignore excluded Resources (no fallback routing through Twingate)

## Identifying Excluded Resources
- Add **Routing Mode** column via "add column" menu in Resources data grid (hidden by default)
- Bypass icon appears inline in Resource name cell
- Filter by Routing Mode to manage sets separately

## Related Docs
- Routing Mode configuration
- Security Policies
- Identity Firewall
- Ephemeral / JIT Access
- Audit Logging