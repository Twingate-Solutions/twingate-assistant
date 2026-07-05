# OneLogin Configuration – Twingate Integration

## Summary
Twingate integrates with OneLogin for SSO via OIDC and user/group synchronization via SCIM. Only users assigned to the OneLogin Twingate application can access Twingate resources. Setup requires configuration in both OneLogin Admin and Twingate Admin consoles.

## Key Information
- Authentication: SP-Initiated SSO via OpenID Connect (OIDC)
- User/group sync: SCIM
- SCIM requires OneLogin **Unlimited Plan**
- OIDC integration requires Twingate **Business or Enterprise plan**

## Prerequisites
- Twingate Business or Enterprise plan
- OneLogin Unlimited Plan (for SCIM/user sync)
- Admin access to both OneLogin and Twingate Admin consoles

## Step-by-Step

### OneLogin Side
1. Go to **Applications > Add App**, search for and select **Twingate**
2. Disable **"Visible in portal"** toggle (users must authenticate from Twingate Client, not OneLogin portal)
3. Click **Save**
4. Assign Twingate app to OneLogin roles (controls who can use Twingate)
5. If SCIM error appears on save: navigate to **Configuration tab**, enter `https://twingate.com` as SCIM Base URL, save to dismiss validation error

### Twingate Side
1. Open OneLogin integration setup in Twingate Admin console
2. Enter **OneLogin Subdomain** (found in OneLogin URL or **Settings > Branding > Brand**)
3. Copy **Client ID** and **Client Secret** from the **SSO tab** of the Twingate app in OneLogin
4. Sign in with OneLogin to validate credentials
5. Complete SCIM configuration separately (see Related Docs)

## Configuration Values

| Field | Source |
|---|---|
| `OneLogin Subdomain` | OneLogin URL or Settings > Branding > Brand |
| `Client ID` | OneLogin Twingate app > SSO tab |
| `Client Secret` | OneLogin Twingate app > SSO tab |
| SCIM Base URL (placeholder) | `https://twingate.com` |

## Gotchas
- **"SCIM Base URL cannot be blank" error**: Known OneLogin UI bug. Workaround: enter `https://twingate.com` in Configuration tab to clear validation; actual SCIM URL configured separately
- **Hide app from OneLogin portal**: Users cannot initiate auth from OneLogin portal—only from the Twingate Client app. Disable "Visible in portal" to avoid confusion
- **Role assignment risk**: Avoid assigning only the Default role initially. Create a dedicated admin role first so you don't lose access if Default role is later removed from the app

## Related Docs
- [SCIM user & group sync configuration](#) (linked as next step in guide)
- OneLogin SCIM plan requirements: OneLogin documentation
- Twingate pricing page (for plan eligibility)