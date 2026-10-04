---
source: https://help.twingate.com/articles/8487611740-dns-using-adguard-for-mac-alongside-twingate
type: help
fetched: 2026-10-04
source_version: 1d0fc9401b2759880a9dd2038ac56a5db3a5c639356ba4ad5575f0e539be1bfe
trust: official
---

# DNS: Using AdGuard for Mac alongside Twingate

## Summary
AdGuard for Mac can conflict with Twingate's transparent DNS proxy functionality, preventing Twingate DNS Resources from resolving. Switching AdGuard's filtering mode to "Automatic Proxy" resolves the conflict.

## Key Information
- Conflict occurs because both AdGuard (app) and Twingate compete for system-level DNS proxy functionality
- Only affects **AdGuard for Mac** (OS-installed application)
- **Not affected**: AdGuard DNS, AdGuard Home (non-OS-installed products) — no incompatibility with those
- Full interoperability has not been fully verified; fix is partially tested
- Other platforms (Windows, etc.) untested

## Prerequisites
- Twingate Client installed on macOS
- AdGuard for Mac installed
- Admin access to AdGuard preferences

## Symptom
Twingate DNS Resources fail to resolve while AdGuard client is active.

## Step-by-Step Fix

1. Open the **AdGuard** application
2. Click the **Gear** icon
3. Click **Preferences**
4. Click the **Network** icon at the top of the preferences window
5. Next to **Filtering Mode**, click **Change Mode**
6. Select **Automatic Proxy**
7. Click **Apply**

## Configuration Values

| Setting | Location | Required Value |
|---|---|---|
| Filtering Mode | AdGuard → Preferences → Network | `Automatic Proxy` |

## Gotchas
- Default AdGuard filtering mode blocks Twingate's DNS proxy operation — must be changed manually after AdGuard installation
- Non-app AdGuard products (AdGuard DNS servers, AdGuard Home) do **not** have this issue
- Only macOS tested; other OS variants of AdGuard app are untested and may behave differently
- This is a workaround, not a fully verified interoperability solution

## Related Docs
- Twingate DNS Resources configuration
- Twingate Client troubleshooting (macOS)