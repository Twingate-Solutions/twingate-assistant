# OneLogin Configuration

## Page Title
OneLogin Configuration for Twingate

## Summary
Twingate integrates with OneLogin to handle user authentication via OIDC and user/group synchronization via SCIM. Only users assigned to the OneLogin Twingate application can access Twingate resources. Configuration requires setup in both the OneLogin Admin console and the Twingate Admin console.

## Key Information
- Authentication method: SP-Initiated SSO via OpenID Connect (OIDC)
- User/group sync: SCIM
- Integration is **Business and Enterprise plans only**
- SCIM requires OneLogin's **Unlimited Plan**
- Users can only authenticate from the Twingate Client app, not from the OneLogin portal

## Prerequisites
- Twingate Business or Enterprise plan
- OneLogin Unlimited Plan (for SCIM/user sync)
- Admin access to both OneLogin and Twingate consoles

## Step-by-Step

### OneLogin Side
1. Go to **Applications** → **Add App** → search for and select **Twingate**
2. Disable **"Visible in portal"** toggle (users must authenticate via Twingate client, not OneLogin portal)
3. Click **Save**
4. Assign the Twingate app to OneLogin roles
5. If SCIM error appears on save ("SCIM Base URL cannot be blank"), navigate to **Configuration** tab, enter `https://twingate.com`, and save to bypass validation

### Twingate Side
1. Open the OneLogin integration screen in Twingate Admin console
2. Enter **OneLogin Subdomain** (found in OneLogin URL or **Settings > Branding > Brand**)
3. Copy **Client ID** and **Client Secret** from the **SSO** tab of the OneLogin Twingate app
4. Sign in with OneLogin to validate credentials
5. Complete the activation wizard
6. Configure SCIM separately for user/group sync

## Configuration Values
| Field | Source |
|-------|--------|
| `OneLogin Subdomain` | OneLogin URL or Settings > Branding > Brand |
| `Client ID` | SSO tab of OneLogin Twingate app |
| `Client Secret` | SSO tab of OneLogin Twingate app |
| SCIM Base URL workaround | Enter `https://twingate.com` temporarily |

## Gotchas
- **"SCIM Base URL cannot be blank" error** is a known OneLogin UI bug — enter `https://twingate.com` as a workaround to save
- **Do not assign only the Default role** in production — create a dedicated role (e.g., "Admins") to prevent losing admin access if role assignments change
- **Disable "Visible in portal"** — users cannot initiate auth from OneLogin portal; only from Twingate client
- SCIM configuration is a **separate step** not covered on this page

## Related Docs
- SCIM user/group sync configuration (linked as follow-up step)
- OneLogin Unlimited Plan documentation (for SCIM requirements)
- Twingate pricing page (plan eligibility)