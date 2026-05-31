# Using Twingate Client

## Summary
Covers day-to-day usage of the Twingate Client after installation, including connecting to a network, switching accounts, accessing Resources, and handling Resource authentication/re-authentication.

## Key Information
- Initial connection requires your network subdomain (e.g., `autoco` from `autoco.twingate.com`) and login via SSO/social provider
- Twingate uses **split tunneling**: only traffic destined for internal Resources is routed through Twingate; all other traffic is unaffected
- Client automatically reconnects if network is interrupted; may open browser for re-authentication
- Resources with stricter Security Policies show a **lock icon** and require additional auth steps before access

## Multiple Accounts
Supported on:
- macOS ≥ 2025.227, Windows ≥ 2025.232, iOS ≥ 2025.227

Behavior:
- Only **one account active at a time**; accounts are fully isolated from each other
- Add account: select **Add Another Account**
- Remove account: authenticate into account → **More > Log Out**
- Disconnect without logout: toggle icon next to authenticated account

## Resource Authentication
- Resources may require MFA or additional auth based on their assigned **Security Policy**
- Two ways to authenticate for a locked Resource:
  1. Visit the Resource normally → click Twingate notification → complete browser auth
  2. Find Resource in Client → open menu → select **Authenticate**
- Authorization expires per Security Policy; re-authentication required after expiry

## Proactive Reauthentication
- **Renew Session**: Resource menu → **Renew Session** (manual, all versions)
- **Proactive notifications** (early access, requires opt-in via Twingate team):
  - Supported: macOS/Windows/Linux/iOS/Android ≥ 2025.72
  - Notifies before authorization expires; click notification to renew without finding Resource manually

## Gotchas
- Security Policy assigned to a Resource is **not visible** in the Client
- Switching accounts is required to access Resources from a different account — no cross-account Resource visibility
- Proactive reauthentication notifications are **early access**; must contact Twingate to enable
- No need to disconnect Client between sessions — leaving it running avoids unnecessary re-authentication

## Related Docs
- Twingate Client Installation
- Security Policy configuration
- MFA setup