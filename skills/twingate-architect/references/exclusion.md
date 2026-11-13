---
source: https://www.twingate.com/docs/exclusion
type: docs
fetched: 2026-11-13
source_version: 99a370c60f8594611226ce5222bdf6504ef6aae6267a0c3f8ab21e1182e556f2
trust: official
---

# Resource Exclusion (Bypass Twingate)

## Summary
Resource Exclusion lets you set a Resource's Routing Mode to **Bypass Twingate**, so traffic to that address goes directly through the local OS routing table. It skips Connectors, Relays, and Security Policies. It is meant for carving exceptions out of a broader Resource (e.g., a public status page inside a wildcard Resource).

## Key Information
- Default Routing Mode is **Through Twingate** (proxied via Connectors, policies apply, network events generated).
- **Bypass Twingate**: no Connector, Relay, Security Policy, or network events. DNS filtering and OS-level internet security still apply.
- Excluded Resources are not Connector-dependent, so they stay reachable if all Connectors in a Remote Network are offline.
- Example: `*.corp.example.com` stays tunneled while `status.corp.example.com` bypasses.
- Excluded Resources are applied silently: they don't appear in the Client's Resource list or trigger auth prompts.

## Prerequisites
Minimum Client versions:
- macOS 2026.182
- Windows 2026.211
- Linux 2026.188
- iOS 2026.182
- Android 2026.181

## Step-by-Step (Admin Console)
1. Open the Resource creation modal or edit an existing Resource.
2. Under **Routing Mode**, select **Bypass Twingate**.
3. Enter a specific FQDN or IP address.
4. Save. The address becomes active on Clients at or above the minimum version.

## Configuration Values
- **GraphQL API**: `routingMode: BYPASS_TWINGATE` in `createResource` / `updateResource` mutations. Defaults to `THROUGH_TWINGATE`.
- **REST API**: `"routing_mode": "bypass_twingate"` in the Resource payload. Defaults to `"through_twingate"`.
- Server-side validation rejects wildcards, CIDR ranges, and ID-FW Resource types.

## Identifying Excluded Resources
- Add the **Routing Mode** column in the Resources data grid (hidden by default).
- A bypass icon appears inline in the Resource name regardless of column visibility.
- Filter by Routing Mode (Through Twingate / Bypass Twingate).

## Unchanged by Bypass
- Remote Network association (organizational only).
- Aliases (an alias on an excluded Resource also bypasses).
- DNS filtering and OS-level security.
- Audit logging: Routing Mode changes are logged with actor and before/after values.

## Gotchas
- Only a specific FQDN or IP is allowed; wildcards and CIDR are blocked in the UI and API (prevents routing loops).
- No port restrictions (port section is hidden).
- No network events for excluded traffic, so no visibility in traffic logs.
- Security Policies and JIT / usage-based access options are hidden; Ephemeral Access can still be configured.
- Identity Firewall Resources cannot be set to Bypass (blocked in UI and API).
- Clients below the minimum version won't honor the exclusion.

## Related Docs
- Resources and Routing Mode settings
- Remote Networks and Connectors
- Security Policies
- Identity Firewall
- Audit logs