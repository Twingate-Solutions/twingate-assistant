# Using Twingate Client

## Summary
Covers end-user operation of the Twingate Client after installation, including connecting to a network, accessing resources, handling resource-level authentication, and managing multiple accounts.

## Key Information
- Network URL format: just the subdomain portion (e.g., `autoco` from `autoco.twingate.com`)
- Auth via social login (Google, GitHub) or SSO (Okta, Entra ID)
- Split tunneling is default behavior — non-Resource traffic bypasses Twingate
- Client auto-reconnects on network changes; may trigger browser re-auth
- Only one account can be active at a time even with multiple accounts logged in

## Prerequisites
- Twingate Client installed
- Network subdomain provided by admin
- Identity provider credentials

## Multiple Accounts Support
Minimum client versions required:
| Platform | Version |
|----------|---------|
| macOS | 2025.227 |
| Windows | 2025.232 |
| iOS | 2025.227 |

- Add account: select **Add Another Account**
- Remove account: authenticate into account → **More** → **Log Out**
- Disconnect without removing: toggle icon next to account name

## Resource Authentication
- Resources with Security Policy requiring MFA show a **lock icon**
- Two ways to authenticate:
  1. Visit the resource normally → click Twingate notification → complete browser auth
  2. Find resource in Client → open menu → select **Authenticate**
- Authorization expires per Security Policy; re-auth required after expiration
- Proactive renew: Resource menu → **Renew Session**

## Proactive Reauthentication Notifications (Early Access)
Minimum versions: macOS/Windows/Linux/iOS/Android **2025.72**
- Notifies before authorization expires
- Click notification to reauthenticate without finding resource manually
- Must be enabled by Twingate support team

## Gotchas
- Security Policy assigned to a Resource is **not visible** in the Client
- Multiple accounts are fully isolated — Resources from Account A are invisible when Account B is active
- Leaving Client connected is intentional and recommended; disconnecting causes unnecessary re-auth
- Proactive reauthentication notifications require explicit enablement by Twingate team

## Related Docs
- Twingate Client Installation
- Security Policy configuration
- MFA setup