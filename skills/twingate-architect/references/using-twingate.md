## Using Twingate (End User Guide)

Guide for end users on connecting to Twingate, accessing Resources, handling per-Resource authentication, and understanding split tunneling. Covers multi-account support and proactive reauthentication.

**Key Information:**
- Network name: enter subdomain only (e.g., `autoco` from `autoco.twingate.com`)
- Authentication via social login (Google, GitHub) or SSO (Okta, Entra)
- Only Resource-bound traffic is intercepted (split tunneling) -- regular internet is unaffected
- Client reconnects automatically on network switches; may open browser for re-authentication
- Resources requiring additional auth show a lock icon in the Client

**Multi-Account Support** (macOS 2025.227+, Windows 2025.232+, iOS 2025.227+):
- Multiple accounts can be authenticated simultaneously; only one active at a time
- "Add Another Account" to add; "Log Out" under More to remove; toggle icon to switch active account
- Resources from an inactive account are inaccessible until that account is selected

**Resource Authentication:**
- Resources with stricter Security Policies than the base session prompt for additional auth
- Trigger manually: Client → Resource menu → Authenticate
- Proactive reauthentication: Client → Resource menu → Renew Session

**Proactive Reauthentication Notifications** (all platforms v2025.72+, early access):
- Client notifies before Resource authorization expires -- click to reauthenticate without interruption
- Contact Twingate to enable for your account

**Gotchas:**
- Security Policy applied to a Resource is not visible in the Client -- users may be surprised by unexpected auth prompts
- Quitting the Client requires reauthentication on next launch; leaving it running preserves the session

**Related Docs:**
- /docs/clients -- Client installation
- /docs/security-policies -- Security Policy configuration
- /docs/endpoint-requirements -- Firewall requirements
