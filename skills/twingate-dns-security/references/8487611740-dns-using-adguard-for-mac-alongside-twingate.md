---
source: https://help.twingate.com/articles/8487611740-dns-using-adguard-for-mac-alongside-twingate
type: help
fetched: 2026-09-06
source_version: b574b66b112e4dab96a78e9bf550537ea073f55a25da7c9404b4a05b4927f7ca
---

# DNS: Using AdGuard for Mac alongside Twingate

## Summary
AdGuard for Mac can conflict with Twingate's transparent DNS proxy functionality, preventing Twingate DNS Resources from resolving. Changing AdGuard's filtering mode to "Automatic Proxy" resolves the conflict. Only the macOS installed AdGuard Ad Blocker application is affected.

## Key Information
- **Affected component**: Twingate Client on macOS
- **Root cause**: AdGuard and Twingate both attempt to use the same system-level DNS proxy functionality
- **Scope**: Only AdGuard for Mac (installed application); AdGuard DNS and AdGuard Home are **not** affected
- **Interoperability status**: Briefly tested only — full interoperability not verified

## Prerequisites
- AdGuard for Mac installed and active
- Twingate Client installed on macOS
- Admin access to modify AdGuard preferences

## Symptoms
- Twingate DNS Resources fail to resolve when AdGuard client is running
- Connections to DNS-based Twingate Resources are broken

## Step-by-Step Resolution

1. Open the **AdGuard** application
2. Click the **Gear** icon
3. Click **Preferences**
4. Click the **Network** icon at the top of the Preferences window
5. Next to **Filtering Mode**, click **Change Mode**
6. Select **Automatic Proxy**
7. Click **Apply**

## Configuration Values
| Setting | Location | Value |
|---|---|---|
| Filtering Mode | AdGuard → Preferences → Network | `Automatic Proxy` |

## Gotchas
- Other platforms (Windows, Linux, etc.) are untested — this fix is macOS-specific
- Other AdGuard product variants (AdGuard DNS, AdGuard Home) do not have this conflict
- Full interoperability is **not guaranteed** — this is a partial workaround, not a fully validated solution
- If AdGuard filtering mode is already set to Automatic Proxy and issues persist, further troubleshooting beyond this article is required

## Related Docs
- Twingate Client documentation
- Twingate DNS Resources configuration