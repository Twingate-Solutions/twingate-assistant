# Using Twingate Client

## Summary
Guide for end users on connecting to Twingate, accessing resources, and managing authentication. Covers multi-account support, resource-level security policies, and session management.

## Key Information
- Network URL format: subdomain only (e.g., `autoco` from `autoco.twingate.com`)
- Login via social providers (Google, GitHub) or SSO (Okta, Entra ID)
- Split tunneling is default behavior — non-Resource traffic bypasses Twingate
- Client auto-reconnects on network switch/interruption
- Only one account can be active at a time (multi-account supported)

## Multi-Account Support
Minimum client versions required:
| Platform | Version |
|----------|---------|
| macOS | 2025.227 |
| Windows | 2025.232 |
| iOS | 2025.227 |

- Add accounts via "Add Another Account"
- Remove: authenticate into account → More → "Log Out"
- Disconnect without removing: toggle icon next to account

## Resource Authentication
- Resources with stricter Security Policies than user's baseline show a **lock icon**
- Two ways to authenticate:
  1. Visit the resource normally → click Twingate notification → complete browser auth
  2. Find resource in Client → open menu → select **Authenticate**
- Security Policy name is not visible in Client
- Authorization expires per Security Policy settings

## Proactive Reauthentication
- **Renew Session**: Resource menu → "Renew Session" (manual)
- **Proactive notifications** (early access, requires opt-in via Twingate team):
  - Notifies before authorization expires
  - Minimum versions: macOS/Windows/Linux/iOS/Android **2025.72**

## Gotchas
- Each authenticated account is isolated — Resources from Account A are inaccessible while Account B is active; must switch accounts explicitly
- Switching networks may open browser window for re-authentication; if not automatic, manually click **Connect to…**
- Authorization expiration is Resource-specific based on applied Security Policy — expiry time is not shown in Client
- Proactive reauthentication notifications require manual enablement by Twingate support team

## Tips
- Leave Client connected — split tunneling means no performance impact on non-Resource traffic
- No need to disconnect/reconnect between sessions; avoids forced reauthentication

## Related Docs
- [Installing the Twingate Client](https://www.twingate.com/docs/install-client)
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [MFA Configuration](https://www.twingate.com/docs/mfa)