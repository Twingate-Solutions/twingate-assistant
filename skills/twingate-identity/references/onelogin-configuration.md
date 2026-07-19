# OneLogin Configuration

## Page Title
OneLogin Configuration (Twingate SSO & SCIM Integration)

## Summary
Twingate integrates with OneLogin to delegate authentication via OIDC and synchronize users/groups via SCIM. Only users assigned to the OneLogin Twingate application can access Twingate resources. Configuration requires setup in both the OneLogin Admin console and the Twingate Admin console.

## Key Information
- Supports SP-Initiated SSO via OpenID Connect (OIDC)
- Supports SCIM for user and group synchronization
- Only assigned OneLogin users can authenticate with Twingate
- Users should start sessions from the Twingate Client app, not the OneLogin portal

## Prerequisites
- Twingate Business or Enterprise plan (for OIDC)
- OneLogin Unlimited Plan (required for SCIM user sync)
- Admin access to both OneLogin and Twingate Admin consoles

## Step-by-Step

### OneLogin Admin Console
1. Go to **Applications > Add App**, search for "Twingate", select it
2. **Disable "Visible in portal"** toggle — users must authenticate from the Twingate client, not the portal
3. Click **Save**
4. Assign the Twingate application to OneLogin roles (see Gotchas)

### Twingate Admin Console
1. Navigate to the OneLogin integration activation screen
2. Enter **OneLogin Subdomain** (find in OneLogin URL or **Settings > Branding > Brand**)
3. Copy **Client ID** and **Client Secret** from the **SSO tab** of the Twingate OneLogin app
4. Complete the wizard by signing in with OneLogin to validate credentials
5. Configure SCIM separately for user/group sync (see related docs)

## Configuration Values
| Field | Source |
|-------|--------|
| `OneLogin Subdomain` | OneLogin URL or Settings > Branding > Brand |
| `Client ID` | SSO tab of OneLogin Twingate app |
| `Client Secret` | SSO tab of OneLogin Twingate app |
| SCIM Base URL (placeholder) | `https://twingate.com` (temporary, to bypass UI validation) |

## Gotchas
- **"SCIM Base URL cannot be blank" error**: Known OneLogin UI bug. Workaround: enter `https://twingate.com` in the Configuration tab and save to bypass validation. Real SCIM URL configured separately.
- **Role assignment risk**: Assigning only the Default role is easy for testing but hard to recover from if removed. Create a dedicated admin role (e.g., "Admins") and assign it alongside Default role to prevent losing access.
- **Portal visibility**: Twingate should be hidden from the OneLogin portal — authentication only works when initiated from the Twingate client app.

## Related Docs
- SCIM user & group sync configuration (linked from page)
- Twingate pricing page (plan requirements)
- OneLogin SCIM documentation (Unlimited Plan requirements)