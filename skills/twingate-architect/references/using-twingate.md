# Using Twingate

## Summary
Covers how to connect the Twingate Client to a network, access Resources, manage multiple accounts, and handle Resource authentication/re-authentication. Includes tips on split tunneling behavior and network switching.

## Key Information
- Initial connection requires your network URL subdomain (e.g., `autoco` from `autoco.twingate.com`) and login via SSO/social provider
- Split tunneling is default behavior — non-Resource traffic bypasses Twingate; no performance impact from leaving Client connected
- Client auto-reconnects on network changes; may trigger browser auth window automatically
- Only one account can be active at a time; accounts are fully isolated from each other
- Resources with additional auth requirements show a **lock icon** in the Client
- Authorization expiry is determined by the Resource's Security Policy (not visible in Client UI)

## Multiple Account Support
| Platform | Minimum Version |
|----------|----------------|
| macOS | 2025.227 |
| Windows | 2025.232 |
| iOS | 2025.227 |

## Resource Authentication
- **Trigger automatically**: Visit the Resource — Twingate sends a notification to click and complete auth in browser
- **Trigger manually**: Find Resource in Client → open menu → select **Authenticate**
- **Renew before expiry**: Find Resource in Client → open menu → select **Renew Session**

## Proactive Reauthentication Notifications (Early Access)
- Notifies before authorization expires; click notification to renew without finding Resource manually
- Supported on macOS/Windows/Linux/iOS/Android version **2025.72+**
- Must be enabled by Twingate team — requires contacting support

## Gotchas
- Security Policy applied to a Resource is **not visible** in the Client — users won't know why additional auth is triggered
- Switching accounts requires manually toggling the active account; Resources from inactive accounts are inaccessible until you switch
- "Log Out" removes the account entirely; the disconnect toggle only suspends the active session
- If auto-reconnect doesn't trigger browser auth, manually click **Connect to…** in the Client

## Related Docs
- Twingate Client installation
- Security Policy configuration
- MFA setup