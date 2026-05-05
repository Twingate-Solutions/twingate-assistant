## Identity Providers Overview

The hub doc for IdP integration in Twingate. Lists supported IdPs and the multi-IdP / migration patterns.

### Supported IdPs

**All Plans:**
- Google Workspace
- Social logins (Google, Microsoft, GitHub, LinkedIn) -- not strictly an IdP, but functions as one for small teams

**Business & Enterprise Plans:**
- Entra ID (formerly Azure AD)
- Okta
- OneLogin
- JumpCloud
- Keycloak

Each has its own configuration guide. Choose based on what your org already uses.

### Multi-IdP Support

Twingate accounts can have **multiple IdPs connected simultaneously**:

**Common patterns:**
- **Migration**: Old IdP + new IdP active in parallel during cutover; users gradually move from old to new
- **Mixed populations**: Employees on Okta + contractors on social logins
- **Subsidiaries**: Parent company on Entra ID + acquired company on their existing Okta
- **Multiple instances of same IdP**: Two separate Okta tenants synced into one Twingate account

**Naming**: rename connected IdPs in Twingate for easier source tracking. **Teams page** has a Source filter so you can see which IdP a user came from.

### Changing the Identity Provider

Settings -> Identity Provider -> options menu on the configured IdP -> Disconnect.

**On disconnect**:
- All users and synced groups from that IdP are removed
- If disconnecting would leave the account with **no admin**, Twingate requires you to provide a new admin email (a social login user)
- Re-authenticate via the new admin email after disconnect, then set up the new IdP

**Mixing social with IdP**: when first connecting an IdP with social logins already enabled, Twingate prompts whether to keep or remove the social users. Recommend **removing them** for a cleaner transition.

### Twingate Universal 2FA

- Use **Twingate native 2FA** instead of (or alongside, but not duplicating) the IdP's 2FA
- Native 2FA gives precise per-Resource control -- enforce 2FA only on sensitive Resources rather than all sign-ins
- See /docs/two-factor-authentication

### Decision Notes

- For new deployments: pick one IdP early; multiple IdPs add operational complexity
- During migration (e.g., Okta -> Entra ID): connect the new IdP, dual-run for a defined window, then disconnect the old one
- For contractors: layering social logins on top of an enterprise IdP avoids creating IdP accounts for transient users
- Always verify a user with admin role is in **multiple connected sources** before disconnecting any IdP -- otherwise lockout risk

### Gotchas

- Disconnect is destructive -- syncs are wiped, users from that IdP are removed
- The "social logins removal on first IdP connect" prompt is easy to miss -- choose deliberately
- Multi-IdP user collisions: if the same email exists in two IdPs, Twingate may create two separate users. Match emails carefully across IdPs.

### Related Docs

- /docs/entra-id-configuration, /docs/google-workspace-configuration, /docs/okta-configuration, /docs/onelogin-configuration, /docs/jumpcloud-configuration, /docs/keycloak-configuration -- Per-IdP guides
- /docs/social-logins -- Social login fallback
- /docs/offboarding-users -- IdP offboarding
- /docs/two-factor-authentication -- Native 2FA
