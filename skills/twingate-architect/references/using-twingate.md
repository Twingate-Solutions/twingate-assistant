# Using Twingate

## Summary
Covers end-user operation of the Twingate Client after installation, including connecting to a network, accessing Resources, handling Resource-level authentication requirements, and managing sessions. Also covers multi-account support and reauthentication workflows.

## Key Information
- Network URL format: just the subdomain (e.g., `autoco` from `autoco.twingate.com`)
- Login via social providers (Google, GitHub) or SSO (Okta, Entra ID)
- Twingate uses **split tunneling** — only Resource-destined traffic is routed through Twingate; no performance impact on other traffic
- Client auto-reconnects on network switches; may open browser for IdP re-authentication
- Resources with additional auth requirements show a **lock icon** in the Client
- Security Policy applied to a Resource is not visible in the Client UI

## Multi-Account Support
Minimum Client versions required:
| Platform | Version |
|----------|---------|
| macOS | 2025.227 |
| Windows | 2025.232 |
| iOS | 2025.227 |

- Only **one account active at a time**; accounts have no visibility into each other
- Add account: "Add Another Account"
- Remove account: authenticate → More submenu → "Log Out"
- Disconnect (without logging out): toggle icon next to account

## Resource Authentication
- Resources may require MFA or step-up auth based on their Security Policy
- **Trigger auth**: visit the Resource normally → click Twingate notification → complete browser auth
- **Manual auth**: find Resource in Client → open menu → select **Authenticate**
- **Renew session proactively**: Resource menu → **Renew Session**

## Proactive Reauthentication Notifications (Early Access)
Minimum Client versions required:
| Platform | Version |
|----------|---------|
| macOS/Windows/Linux/iOS/Android | 2025.72 |

- Notifies before authorization expires; click notification to reauthenticate without interruption
- Must be **enabled by Twingate team** — contact support to activate

## Gotchas
- Switching accounts is required before accessing Resources on another account — no cross-account Resource visibility
- Authorization expires per Security Policy; expiration timing is not shown in the Client
- Proactive reauthentication notifications are early access and off by default — requires manual enablement by Twingate
- Do not disconnect the Client unnecessarily; leaving it connected avoids forced reauthentication

## Related Docs
- Twingate Client installation
- Security Policies
- MFA configuration