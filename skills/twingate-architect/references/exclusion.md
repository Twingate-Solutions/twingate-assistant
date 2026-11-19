---
source: https://www.twingate.com/docs/exclusion
type: docs
fetched: 2026-11-19
source_version: 642538e3fab2bbc592326dc4f934c35b33ca0ae597670bea09a631e630f3f00c
trust: official
---

# Resource Exclusion (Bypass Twingate)

## Summary
Resource exclusion lets you set a specific FQDN or IP address within a Resource to bypass Twingate. Traffic goes directly to the local OS routing table, skipping Connectors, Relays, and Security Policies. It is intended for carving exceptions out of a broader Resource (e.g., a public status page inside a `*.corp.example.com` wildcard).

## Key Information
- Each Resource has a **Routing Mode**: `Through Twingate` (default) or `Bypass Twingate`.
- Bypass means no Connector or Relay, no Security Policy evaluation, and no network events.
- DNS filtering and OS-level internet security still apply.
- Excluded Resources don't depend on Connectors, so they stay reachable if all Connectors in a Remote Network are offline.
- Excluded Resources still belong to a Remote Network (organizational only).
- An alias on an excluded Resource also bypasses Twingate.
- Changes to Routing Mode are recorded in the audit log (who, before/after values).
- Excluded Resources are applied silently: they don't appear in the Client's Resource list or trigger auth prompts.

## Prerequisites
Minimum Client versions:
- macOS 2026.182
- Windows 2026.211
- Linux 2026.188
- iOS 2026.182
- Android 2026.181

## Step-by-Step (Admin Console)
1. Open the Resource creation modal, or edit an existing Resource.
2. Under **Routing Mode**, select **Bypass Twingate**.
3. Enter a specific FQDN or IP address.
4. Save. The address becomes active on Clients at or above the minimum version.

## Configuration Values
- **GraphQL API:** `routingMode: BYPASS_TWINGATE` in `createResource` / `updateResource`. Defaults to `THROUGH_TWINGATE`.
- **REST API:** `"routing_mode": "bypass_twingate"` in the Resource payload. Defaults to `"through_twingate"`.
- Server-side validation rejects wildcards, CIDR ranges, and PAM Resource types.

## Identifying Excluded Resources
- Add the **Routing Mode** column in the Resources data grid (hidden by default).
- A bypass icon always appears in the Resource name cell.
- Filter by Routing Mode to manage each set.

## Gotchas
- Only a specific FQDN or IP is allowed. Wildcards and CIDR are blocked in UI and API to prevent routing loops.
- Port restrictions are unavailable (port section is hidden).
- Security Policies and JIT/usage-based access options are hidden for excluded Resources. Ephemeral Access can still be configured.
- No network events are generated, so there is no traffic visibility for these addresses.
- Privileged Access Management Resources cannot be set to Bypass (PAM requires per-user identity evaluation).
- Clients below the minimum version won't honor the exclusion.

## Related Docs
- Resources and Routing Mode settings
- Remote Networks and Connectors
- Security Policies
- Privileged Access Management
- Audit logs
- Twingate GraphQL and REST API references