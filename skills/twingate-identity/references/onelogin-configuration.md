---
source: https://www.twingate.com/docs/onelogin-configuration
type: docs
fetched: 2026-08-14
source_version: 8786ef1d8ee0af0bfbbac3296cd64f84d0f44d5e6e2f229de922c1216342890c
---

# OneLogin Configuration

## Page Title
OneLogin Configuration for Twingate

## Summary
Twingate integrates with OneLogin for user authentication via OIDC and user/group synchronization via SCIM. Only users assigned to the OneLogin Twingate application can access Twingate resources. Configuration requires setup in both OneLogin Admin console and Twingate Admin console.

## Key Information
- Authentication: SP-Initiated SSO via OpenID Connect (OIDC)
- User/group sync: SCIM protocol
- Integration delegates authentication and directory sync entirely to OneLogin
- Users must start sessions from the Twingate Client app (not OneLogin portal)

## Prerequisites
- Twingate Business or Enterprise plan (for OIDC)
- OneLogin Unlimited Plan (required for SCIM/user sync)
- Admin access to both OneLogin and Twingate Admin consoles

## Step-by-Step

### OneLogin Side
1. Go to **Applications > Add App**, search for "Twingate", select the app
2. **Disable "Visible in portal"** toggle (users must authenticate from Twingate client, not portal)
3. Click **Save**
4. Assign app access via OneLogin roles (recommend creating a dedicated role rather than using Default role)
5. If "SCIM Base URL cannot be blank" error appears: navigate to **Configuration** tab, enter `https://twingate.com`, click Save

### Twingate Side
1. Open Twingate Admin console and begin OneLogin integration activation
2. Enter **OneLogin Subdomain** (found in OneLogin URL or **Settings > Branding > Brand**)
3. Enter **Client ID** and **Client Secret** from the **SSO tab** of the OneLogin Twingate application
4. Complete sign-in wizard to validate credentials
5. Configure SCIM separately (see Related Docs)

## Configuration Values

| Field | Source |
|-------|--------|
| OneLogin Subdomain | OneLogin URL or Settings > Branding > Brand |
| Client ID | OneLogin Twingate app > SSO tab |
| Client Secret | OneLogin Twingate app > SSO tab |
| SCIM Base URL (placeholder) | `https://twingate.com` (temporary fix for UI bug) |

## Gotchas
- **Portal visibility**: Must disable "Visible in portal" — authentication only works when initiated from Twingate client app
- **SCIM UI bug**: OneLogin may throw "SCIM Base URL cannot be blank" error on save; workaround is entering `https://twingate.com` in Configuration tab temporarily
- **Role management**: Avoid assigning only to Default role — create a dedicated admin role first to prevent lockout if Default role is later removed
- **SCIM requires OneLogin Unlimited Plan** — standard OneLogin plans do not support SCIM

## Related Docs
- SCIM user & group sync configuration (linked from page)
- OneLogin SCIM documentation (for plan requirements)
- Twingate pricing page (for plan comparison)