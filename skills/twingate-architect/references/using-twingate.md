---
source: https://www.twingate.com/docs/using-twingate
type: docs
fetched: 2026-08-14
source_version: ce59a6a8ed90cfb6e888dd262b0c2f789326172ef1eaae70660d676be61f7bd2
---

# Using Twingate

## Summary
Covers end-user operation of the Twingate Client after installation, including connecting to a network, accessing resources, handling resource-level authentication, and managing multiple accounts.

## Key Information
- Network URL format: use only the subdomain portion (e.g., `autoco` from `autoco.twingate.com`)
- Login via social providers (Google, GitHub) or SSO (Okta, Entra ID)
- Twingate uses **split tunneling** — only traffic to internal Resources routes through Twingate; leave Client connected permanently
- Client auto-reconnects on network changes; may open browser for re-authentication
- Resources with additional auth requirements show a **lock icon** in the Client

## Multiple Accounts Support
Minimum client versions required:
| Platform | Version |
|----------|---------|
| macOS | 2025.227 |
| Windows | 2025.232 |
| iOS | 2025.227 |

- Only **one account active at a time**; accounts are fully isolated
- Add account: select **Add Another Account**
- Remove account: authenticate into account → More → **Log Out**
- Disconnect (keep credentials): toggle icon next to account

## Resource Authentication
- Security Policy may require MFA per-resource regardless of global settings
- Two ways to authenticate a locked Resource:
  1. **Passive**: Visit the resource normally → click Twingate notification → complete browser auth
  2. **Manual**: Client → find Resource → open menu → **Authenticate**
- Authorization expires per Security Policy; re-authentication required on expiry

## Proactive Reauthentication
- **Renew before expiry**: Client → Resource → menu → **Renew Session**
- **Proactive notifications** (early access, all platforms v2025.72+): Client notifies before expiry; click notification to renew
  - Must be enabled by Twingate team — contact support to enable

## Gotchas
- Security Policy assigned to a Resource is **not visible** in the Client
- Switching accounts required to access Resources from a different account — no cross-account resource visibility
- Quitting the Client may force full reauthentication; prefer leaving it running
- If auto-reconnect doesn't trigger after network change, manually click **Connect to…** in Client

## Prerequisites
- Twingate Client installed
- Network subdomain from administrator
- Valid identity provider credentials

## Related Docs
- Twingate Client installation
- Security Policy configuration
- MFA setup