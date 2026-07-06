# Using Twingate (Client Usage Guide)

## Summary
Covers how to connect to a Twingate network, access Resources, manage multiple accounts, and handle Resource authentication. Explains session management including expiration and proactive reauthentication.

## Key Information
- Network URL format: `<network-name>` from `<network-name>.twingate.com` (e.g., `autoco`)
- Authentication via social login (Google, GitHub) or SSO (Okta, Entra ID)
- Split tunneling is default — non-Resource traffic bypasses Twingate; leave Client connected
- Client auto-reconnects on network switches; may prompt browser re-auth via IdP
- Resources with additional auth requirements show a **lock icon** in the Client
- Security Policy applied to a Resource is not visible to end users in the Client

## Multiple Accounts Support

| Platform | Minimum Version |
|----------|----------------|
| macOS    | 2025.227        |
| Windows  | 2025.232        |
| iOS      | 2025.227        |

- Only **one account active at a time**; accounts are fully isolated from each other
- Add account: select **Add Another Account**
- Remove account: authenticate into account → More → **Log Out**
- Disconnect (without removing): toggle icon next to account

## Resource Authentication
- Resources may require step-up auth based on their Security Policy (e.g., MFA)
- **Trigger auth automatically**: visit the Resource → click Twingate notification → complete browser auth
- **Trigger auth manually**: Client → find Resource → open menu → **Authenticate**
- Authorization expires per Security Policy; must re-authenticate after expiration
- **Proactive renewal**: Client → Resource menu → **Renew Session**

## Proactive Reauthentication Notifications (Early Access)

| Platform | Minimum Version |
|----------|----------------|
| macOS    | 2025.72         |
| Windows  | 2025.72         |
| Linux    | 2025.72         |
| iOS      | 2025.72         |
| Android  | 2025.72         |

- Notifies before authorization expires; click notification to renew without manual navigation
- Must be **enabled by Twingate team** — contact support to activate

## Gotchas
- Only the **active account's Resources** are accessible; switch accounts to reach others
- Disconnecting the Client forces re-authentication when reconnecting — prefer leaving it connected
- If auto-reconnect doesn't trigger browser auth, manually click **Connect to…** in Client
- Auth expiration is policy-driven and not surfaced in the Client UI — users must track or use proactive notifications

## Related Docs
- [Twingate Client Installation](#) (prerequisite)
- [Security Policy](https://www.twingate.com/docs/security-policies)
- [MFA Configuration](https://www.twingate.com/docs/mfa)