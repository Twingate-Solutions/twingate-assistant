# OneLogin Configuration

## Page Title
OneLogin Configuration for Twingate

## Summary
Twingate integrates with OneLogin to synchronize user accounts and delegate authentication via OIDC and SCIM. Only users assigned to the OneLogin Twingate application can access Twingate resources. Setup requires configuration in both the OneLogin Admin console and Twingate Admin console.

## Key Information
- **Authentication**: SP-Initiated SSO via OpenID Connect (OIDC)
- **User/Group Sync**: SCIM protocol
- **Plan Requirements**: Business or Enterprise (OIDC); OneLogin Unlimited Plan required for SCIM
- Users can only authenticate from the Twingate Client app — not from the OneLogin portal

## Prerequisites
- Twingate Business or Enterprise plan
- OneLogin Unlimited Plan (for SCIM/user sync)
- Admin access to both OneLogin and Twingate Admin consoles

## Step-by-Step

### OneLogin Side
1. Go to **Applications > Add App**, search for and select **Twingate**
2. Disable **"Visible in portal"** toggle (users must authenticate via Twingate client, not OneLogin portal)
3. Click **Save**
4. Assign the Twingate app to OneLogin roles (recommend creating a dedicated role rather than using Default role)

### Twingate Side
5. Open Twingate Admin console and begin OneLogin integration activation
6. Enter **OneLogin Subdomain** (find at `Settings > Branding` in OneLogin, or from your OneLogin dashboard URL)
7. Copy **Client ID** and **Client Secret** from the **SSO** tab of the OneLogin Twingate application
8. Sign in with OneLogin to validate credentials
9. Configure SCIM separately (see related docs)

## Configuration Values
| Field | Source |
|-------|--------|
| `OneLogin Subdomain` | OneLogin Admin Dashboard URL or `Settings > Branding` |
| `Client ID` | SSO tab of OneLogin Twingate application |
| `Client Secret` | SSO tab of OneLogin Twingate application |
| SCIM Base URL (placeholder) | `https://twingate.com` (temporary, to bypass UI bug) |

## Gotchas
- **OneLogin UI bug**: When saving the app, OneLogin may throw "SCIM Base URL cannot be blank" error. Workaround: go to **Configuration** tab, enter `https://twingate.com`, and save. Real SCIM setup is done separately.
- **Role assignment risk**: Avoid relying solely on the Default role for access. Create a dedicated admin role first — removing Default role later without a fallback will lock you out of Twingate.
- **Portal visibility**: Twingate should be hidden from the OneLogin portal since authentication only works when initiated from the Twingate client app.

## Related Docs
- [SCIM User & Group Sync Configuration](#) (required follow-up step)
- [Twingate Pricing](https://www.twingate.com/pricing)
- [OneLogin SCIM documentation](https://onelogin.com)