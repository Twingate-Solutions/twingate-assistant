---
source: https://help.twingate.com/articles/8487611740-dns-using-adguard-for-mac-alongside-twingate
type: help
fetched: 2026-08-06
source_version: 005c8b25d92d5b9f5d6e6293778ddf25e49e9c45fc778fda0435dfa05c33d06b
---

# DNS: Using AdGuard for Mac alongside Twingate

## Summary
AdGuard for Mac can conflict with Twingate's transparent DNS proxy functionality, preventing Twingate DNS Resources from resolving. Changing AdGuard's filtering mode to "Automatic Proxy" resolves the conflict. Only the macOS AdGuard Ad Blocker application is affected; AdGuard DNS and AdGuard Home are not impacted.

## Key Information
- **Affected component**: Twingate Client on macOS
- **Conflict cause**: AdGuard and Twingate both attempt to use the same system-level DNS proxy functionality
- **Scope**: Only AdGuard for Mac (OS-installed app); AdGuard DNS and AdGuard Home products are **not** affected
- **Interoperability status**: Briefly tested only — full interoperability not verified

## Prerequisites
- AdGuard for Mac installed and active
- Twingate Client installed on macOS
- Admin access to AdGuard preferences

## Symptom
Twingate DNS Resources fail to resolve while AdGuard client is active.

## Step-by-Step Resolution

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
- Other AdGuard OS installations (non-Mac) are untested — solution may not apply
- Upstream DNS server configurations resolving queries to the device are **not** affected by this incompatibility
- Full interoperability is not guaranteed even after applying this fix

## Related Docs
- Twingate DNS Resources configuration
- Twingate Client transparent proxy behavior