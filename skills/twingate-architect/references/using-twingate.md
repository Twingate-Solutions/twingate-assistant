# Using Twingate (Client Usage Guide)

## Summary
Covers how to connect to a Twingate network, access Resources, manage multiple accounts, and handle Resource authentication/re-authentication via the Twingate Client. Includes tips on split tunneling behavior and network switching.

## Key Information
- Network URL format: just the subdomain (e.g., `autoco` from `autoco.twingate.com`)
- Login via social (Google, GitHub) or SSO (Okta, Entra ID)
- Split tunneling is default — non-Resource traffic bypasses Twingate; no performance impact from leaving Client running
- Client auto-reconnects on network switch; may open browser for re-auth

## Multiple Account Support
| Platform | Min Version |
|----------|-------------|
| macOS    | 2025.227    |
| Windows  | 2025.232    |
| iOS      | 2025.227    |

- Only **one account active at a time**; accounts are fully isolated
- Add account: "Add Another Account"
- Remove account: authenticate → More → "Log Out"
- Disconnect (without removing): toggle icon next to account

## Resource Authentication
- Resources may require additional auth based on their **Security Policy** (e.g., MFA)
- Lock icon in Client = additional auth required
- Security Policy name is **not visible** in the Client

**Two ways to authenticate:**
1. Visit Resource normally → Twingate sends notification → click to open browser
2. Find Resource in Client → open menu → select **Authenticate**

## Authorization Expiration & Renewal
- Access expires per Security Policy settings
- **Proactive renew:** Resource menu → **Renew Session**
- **Proactive reauthentication notifications** (early access — must be enabled by Twingate team):

| Platform | Min Version |
|----------|-------------|
| macOS/Windows/Linux/iOS/Android | 2025.72 |

## Step-by-Step: Initial Connection
1. Install Twingate Client
2. Enter network subdomain (e.g., `autoco`)
3. Authenticate via identity provider
4. Access Resources normally (browser, SSH, RDP, etc.)

## Gotchas
- Do **not** quit Client unnecessarily — forces re-authentication on restart
- Switching accounts requires manual selection; Resources of inactive accounts are inaccessible
- Proactive reauthentication notifications require explicit enablement by Twingate support
- If auto-reconnect after network change doesn't open auth browser, manually click **Connect to…** in Client

## Related Docs
- Twingate Client installation
- Security Policy configuration
- MFA setup