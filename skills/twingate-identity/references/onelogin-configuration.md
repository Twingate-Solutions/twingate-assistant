# OneLogin Configuration

## Page Title
OneLogin Configuration for Twingate

## Summary
Twingate integrates with OneLogin to handle user authentication via OIDC and user/group synchronization via SCIM. Only users assigned to the OneLogin Twingate application can access Twingate resources. Configuration requires setup in both the OneLogin Admin console and Twingate Admin console.

## Key Information
- Authentication: SP-Initiated SSO via OpenID Connect (OIDC)
- Sync: SCIM for user and group synchronization
- Twingate delegates authentication and user management entirely to OneLogin
- Users must be assigned to the OneLogin Twingate app to access Twingate

## Prerequisites
- Twingate Business or Enterprise plan (for OIDC)
- OneLogin Unlimited Plan (required for SCIM user sync)
- Admin access to both OneLogin and Twingate Admin consoles

## Step-by-Step

### OneLogin Side
1. Go to **Applications** → **Add App** → search for and select **Twingate**
2. Disable **"Visible in portal"** toggle (users must authenticate from Twingate client, not OneLogin portal)
3. Click **Save**
4. Assign the Twingate app to OneLogin roles
   - Recommended: Create a dedicated role (e.g., "Admins") rather than using Default role to avoid lockout
5. If SCIM error appears on save: go to **Configuration** tab, enter `https://twingate.com` as SCIM Base URL, save to bypass UI validation

### Twingate Side
6. In Twingate Admin console, activate OneLogin integration
7. Enter **OneLogin Subdomain** (found in OneLogin URL or **Settings > Branding > Brand**)
8. Enter **Client ID** and **Client Secret** from the **SSO** tab of the OneLogin Twingate app
9. Complete sign-in wizard to validate credentials
10. Configure SCIM separately for user/group sync (separate guide)

## Configuration Values
| Field | Source |
|-------|--------|
| OneLogin Subdomain | OneLogin URL or Settings > Branding > Brand |
| Client ID | SSO tab of OneLogin Twingate application |
| Client Secret | SSO tab of OneLogin Twingate application |
| SCIM Base URL (workaround) | `https://twingate.com` |

## Gotchas
- **Do not** make Twingate visible in OneLogin portal—authentication only works when initiated from the Twingate client app
- OneLogin UI bug: "SCIM Base URL cannot be blank" error on save; workaround is entering `https://twingate.com` in Configuration tab
- Using Default role for testing is fine, but set up a dedicated admin role before removing Default role to prevent losing Twingate access
- SCIM requires OneLogin Unlimited Plan—check plan before expecting sync to work

## Related Docs
- SCIM user & group sync configuration (separate guide)
- OneLogin SCIM documentation
- Twingate pricing page (plan requirements)