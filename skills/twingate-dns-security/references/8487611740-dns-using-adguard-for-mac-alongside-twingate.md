---
source: https://help.twingate.com/articles/8487611740-dns-using-adguard-for-mac-alongside-twingate
type: help
fetched: 2026-11-01
source_version: 90cdc6ac338d2e0fb52b317645878b6c84c3b3426fd37527df5279f4ea9251ff
trust: official
---

# DNS: Using AdGuard for Mac alongside Twingate

## Summary
AdGuard for Mac can conflict with Twingate's transparent DNS proxy functionality, preventing Twingate DNS Resources from resolving. Changing AdGuard's filtering mode to "Automatic Proxy" resolves the conflict.

## Key Information
- Conflict occurs because both applications attempt to use the same system-level DNS/proxy functionality
- Only affects **AdGuard for Mac** (the installed OS application)
- AdGuard DNS and AdGuard Home (non-OS-installed) are **not** affected
- Full interoperability has not been fully verified — only briefly tested

## Prerequisites
- Twingate Client installed on macOS
- AdGuard for Mac installed
- Platform: macOS only (other platforms untested)

## Step-by-Step: Configure AdGuard to Allow Twingate DNS Proxy

1. Open the **AdGuard** application
2. Click the **Gear** icon
3. Click **Preferences**
4. Click the **Network** icon at the top of the Preferences window
5. Next to **Filtering Mode**, click **Change Mode**
6. Select **Automatic Proxy**
7. Click **Apply**

## Configuration Values
| Setting | Value |
|---|---|
| AdGuard Filtering Mode | `Automatic Proxy` |

## Gotchas
- Default AdGuard filtering mode blocks Twingate from acting as a transparent DNS proxy
- Symptom is silent — Twingate DNS Resources simply fail to resolve with no obvious error
- Other AdGuard products (AdGuard Home, AdGuard DNS) do not have this incompatibility
- Other OS platforms (Windows, Linux) are untested with this fix

## Related Docs
- Twingate DNS Resources configuration
- Twingate Client troubleshooting (macOS)