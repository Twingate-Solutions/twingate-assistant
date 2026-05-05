## Keycloak Configuration

Twingate integrates with Keycloak for **OIDC-based user authentication only**. No SCIM user/group sync.

**Plan Requirement:**
- **Business or Enterprise** Twingate plans only

### What's Delegated to Keycloak

- **User authentication** via OIDC
- **No** user/group sync (unlike Okta, Entra ID, etc.)

This means:
- Users authenticate via Keycloak
- Twingate Users / Groups are managed manually (or via the Admin API)
- No automatic provisioning/deprovisioning -- you must disable users in Twingate when offboarding from Keycloak

### Setup

The Keycloak Twingate integration is **not self-service** -- contact Twingate Support to enable it.

### Decision Notes

- **Use Keycloak only if it's your existing IdP** -- you'll lack the SCIM lifecycle automation that Okta/Entra ID/JumpCloud/Google Workspace provide
- For new IdP rollouts, prefer one of the SCIM-supported IdPs unless Keycloak is a non-negotiable constraint
- Manual user lifecycle in Twingate means **higher operational risk** -- a Keycloak-disabled user can still log in to Twingate until you also disable them in Twingate

### Gotchas

- No SCIM sync = manual user/group management
- Offboarding requires action in **both** Keycloak and Twingate -- automate this externally if possible (custom script via Twingate Admin API)
- Setup is gated through Twingate Support -- expect a longer onboarding cycle than self-service IdPs

### Related Docs

- /docs/identity-providers -- IdP overview (compare integration options)
- /docs/users, /docs/groups -- Manual user/group management
- /docs/api-overview -- Twingate Admin API for automation
