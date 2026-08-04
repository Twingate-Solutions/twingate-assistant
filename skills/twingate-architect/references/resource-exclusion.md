# Resource Exclusion (Bypass Twingate)

## Summary
Resource exclusions allow specific addresses to bypass Twingate's proxy infrastructure entirely, routing traffic directly via the local OS routing table. Designed for carving exceptions out of broader Resources (e.g., a public subdomain within a wildcard Resource). Excluded Resources generate no network events and are Connector-independent.

## Key Information
- **Routing Mode** setting per Resource: `Through Twingate` (default) or `Bypass Twingate`
- Bypassed traffic skips: Connectors, Relay, Security Policies, network event generation
- Bypassed traffic still subject to: DNS filtering, OS-level internet security
- Excluded Resources remain reachable even if all Connectors in a Remote Network are offline
- Changes to Routing Mode are captured in the audit log (who changed it, before/after values)
- Excluded Resources are **invisible** to Clients — don't appear in Resource list, no auth prompt

## Prerequisites / Version Requirements
Minimum Client versions:

| Component | Minimum Version |
|-----------|----------------|
| macOS | `2026.182` |
| iOS | `2026.182` |
| Android | `2026.181` |
| Linux | `2026.188` (latest channel) |
| Windows | not yet supported |

## Configuration

### Admin Console
1. Open Resource creation modal or edit existing Resource
2. Under **Routing Mode**, select **Bypass Twingate**
3. Enter specific FQDN or IP address
4. Save

### API (GraphQL)
```graphql
routingMode: BYPASS_TWINGATE  # in createResource or updateResource mutation
# Default: THROUGH_TWINGATE
```

### REST API
```json
"routing_mode": "bypass_twingate"
// Default: "through_twingate"
```

## Configuration Values
| Context | Field | Values | Default |
|---------|-------|--------|---------|
| GraphQL | `routingMode` | `BYPASS_TWINGATE`, `THROUGH_TWINGATE` | `THROUGH_TWINGATE` |
| REST | `routing_mode` | `bypass_twingate`, `through_twingate` | `through_twingate` |

## Gotchas
- **No wildcards or CIDR ranges** — only specific FQDNs or IP addresses accepted; blocked at UI and API level (prevents routing loops)
- **No port restrictions** — port section hidden when Bypass selected; cannot be combined
- **Identity Firewall Resources cannot be bypassed** — blocked at UI and API level
- **Aliases inherit bypass** — an alias on an excluded Resource also bypasses Twingate
- **No Security Policies or JIT/usage-based access** — hidden in UI for excluded Resources (Ephemeral Access still configurable)
- **Older Clients silently ignore exclusions** — Clients below minimum version will route excluded Resources normally (through Twingate)
- Remote Network association is retained for organizational purposes only

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
