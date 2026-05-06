# Using Twingate (Client Guide)

## Summary
Covers how to connect the Twingate Client to a network, access Resources, and manage authentication. Includes multi-account support details and session management for Resource authorization.

## Key Information
- Network URL format: `<network-name>` from `<network-name>.twingate.com` (e.g., `autoco`)
- Authentication via social login (Google, GitHub) or SSO (Okta, Entra ID)
- Split tunneling is default behavior — non-Resource traffic passes through normally
- Only one account can be active at a time even when multiple accounts are logged in
- Resources with additional auth requirements show a **lock icon** in the Client
- Security Policy applied to a Resource is not visible in the Client UI

## Prerequisites
- Twingate Client installed on device
- Network URL from your organization
- Valid identity provider credentials

## Multi-Account Support (Minimum Versions)
| Platform | Min Version |
|----------|-------------|
| macOS    | 2025.227    |
| Windows  | 2025.232    |
| iOS      | 2025.227    |

## Proactive Reauthentication Notifications (Minimum Versions)
All platforms (macOS, Windows, Linux, iOS, Android): **2025.72** — Early access; must be enabled by Twingate team.

## Step-by-Step: Resource Authentication
1. Access Resource normally (browser, SSH, RDP, etc.)
2. If additional auth required → Twingate notification appears → click to open browser
3. **Manual method**: Find Resource in Client → open menu → select **Authenticate**
4. To renew proactively: Resource menu → **Renew Session**

## Step-by-Step: Adding/Removing Accounts
- **Add account**: Select **Add Another Account** in Client
- **Remove account**: Authenticate into account → More submenu → **Log Out**
- **Disconnect without removing**: Toggle icon next to authenticated account

## Gotchas
- Each account is isolated — switching accounts required to access Resources from another account
- Resource authorization expires per Security Policy; expiration time is policy-defined and not shown in Client
- Client may auto-open browser to re-authenticate after network interruption
- Leaving Client connected is recommended — no performance penalty due to split tunneling
- Proactive reauthentication notifications are **early access** and require Twingate team enablement

## Related Docs
- [Install Twingate Client](#) (client installation)
- [Security Policy](https://www.twingate.com/docs/security-policies)
- [MFA configuration](https://www.twingate.com/docs/mfa)