# OneLogin Configuration

## Page Title
OneLogin Configuration (Twingate SSO & SCIM Integration)

## Summary
Twingate integrates with OneLogin to delegate user authentication via OIDC and synchronize users/groups via SCIM. Only users assigned to the OneLogin Twingate application can access Twingate resources. Requires Business or Enterprise plan for OIDC; SCIM additionally requires OneLogin's Unlimited Plan.

## Key Information
- Authentication method: SP-Initiated SSO via OpenID Connect (OIDC)
- User/group sync method: SCIM
- Access control: Only OneLogin users assigned to the Twingate app can use Twingate
- Twingate app should be hidden from OneLogin portal ("Visible in portal" disabled) — users must initiate auth from Twingate Client, not OneLogin portal

## Prerequisites
- Twingate Business or Enterprise plan (OIDC)
- OneLogin Unlimited Plan (SCIM user sync)
- Admin access to both OneLogin Admin console and Twingate Admin console

## Step-by-Step

### OneLogin Side
1. Go to **Applications > Add App**, search for "Twingate", select it
2. Disable **"Visible in portal"** toggle → Save
3. Assign app to OneLogin roles (recommend creating a dedicated role rather than using Default role to avoid lockout)
4. If SCIM error appears on save ("SCIM Base URL cannot be blank"): navigate to **Configuration** tab, enter `https://twingate.com`, Save

### Twingate Side
5. Open Twingate Admin console, begin OneLogin integration activation
6. Enter **OneLogin Subdomain** (found in OneLogin URL or **Settings > Branding > Brand**)
7. Copy **Client ID** and **Client Secret** from the **SSO** tab of the Twingate app in OneLogin
8. Complete sign-in verification wizard to validate credentials
9. Configure SCIM separately (see Related Docs)

## Configuration Values

| Field | Source |
|-------|--------|
| `OneLogin Subdomain` | OneLogin Admin URL or Settings > Branding |
| `Client ID` | SSO tab of Twingate app in OneLogin |
| `Client Secret` | SSO tab of Twingate app in OneLogin |
| SCIM Base URL workaround | `https://twingate.com` (placeholder to bypass UI bug) |

## Gotchas
- **OneLogin UI bug**: Saving the app may throw "SCIM Base URL cannot be blank" — enter `https://twingate.com` as placeholder to bypass; real SCIM config done separately
- **Role assignment risk**: Assigning only to "Default" role works for testing but create a named admin role first to prevent lockout when restructuring roles later
- **No portal login**: Users cannot authenticate from the OneLogin portal — must start sessions from the Twingate Client app
- SCIM requires OneLogin Unlimited Plan (separate from Twingate plan requirement)

## Related Docs
- [SCIM user & group sync configuration](#) (linked as next step)
- [Twingate pricing page](https://www.twingate.com/pricing)
- [OneLogin SCIM documentation](https://onelogin.com) (external)