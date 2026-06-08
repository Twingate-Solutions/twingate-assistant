# OneLogin Configuration – Twingate

## Summary
Twingate integrates with OneLogin for user authentication (OIDC) and user/group synchronization (SCIM). Only users assigned to the OneLogin Twingate application can access Twingate resources. Configuration requires setup in both OneLogin Admin and Twingate Admin consoles.

## Key Information
- **Authentication**: SP-Initiated SSO via OpenID Connect (OIDC)
- **Sync**: User and group synchronization via SCIM
- **Plans required**: Business or Enterprise (Twingate); SCIM requires OneLogin Unlimited Plan

## Prerequisites
- Twingate Business or Enterprise plan
- OneLogin Unlimited Plan (for SCIM/user sync)
- Admin access to both OneLogin and Twingate Admin consoles

## Step-by-Step

### OneLogin Side
1. Go to **Applications > Add App**, search for and select **Twingate**
2. **Disable "Visible in portal"** toggle (users must authenticate from Twingate client, not OneLogin portal)
3. Click **Save**
4. Assign the Twingate app to OneLogin roles (assign to a specific role you belong to, not just Default)

### Twingate Side
1. Open Twingate Admin console and start OneLogin integration activation
2. Enter **OneLogin Subdomain** (found in OneLogin URL or **Settings > Branding > Brand**)
3. Copy **Client ID** and **Client Secret** from the **SSO tab** of the OneLogin Twingate app
4. Follow the sign-in wizard to validate credentials and complete activation
5. Configure SCIM separately for user/group sync (see Related Docs)

## Configuration Values

| Field | Source |
|---|---|
| `OneLogin Subdomain` | OneLogin Admin URL or Settings > Branding > Brand |
| `Client ID` | OneLogin Twingate app > SSO tab |
| `Client Secret` | OneLogin Twingate app > SSO tab |
| SCIM Base URL (placeholder) | `https://twingate.com` (temporary to bypass UI bug) |

## Gotchas
- **SCIM Base URL error**: OneLogin may throw "SCIM Base URL cannot be blank" on save. Workaround: enter `https://twingate.com` in the Configuration tab temporarily, then save. Real SCIM URL is set up in the separate SCIM configuration step.
- **Role assignment risk**: If you assign the app only to the Default role and later remove it, you may lose Twingate access. Create a dedicated role (e.g., "Admins") for yourself first.
- **Portal visibility**: Keep Twingate hidden in the OneLogin portal—authentication only works when initiated from the Twingate client app, not via OneLogin portal click.

## Related Docs
- [SCIM user & group sync configuration](https://www.twingate.com/docs/scim) (required for full setup)
- [Twingate pricing](https://www.twingate.com/pricing)
- [OneLogin SCIM documentation](https://developers.onelogin.com/scim)