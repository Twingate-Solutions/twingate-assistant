# OneLogin Configuration

## Page Title
OneLogin Configuration for Twingate

## Summary
Twingate integrates with OneLogin for user authentication via OIDC and user/group synchronization via SCIM. Only users assigned to the OneLogin Twingate application can access Twingate resources. Configuration requires setup in both OneLogin Admin console and Twingate Admin console.

## Key Information
- Authentication: SP-Initiated SSO via OpenID Connect (OIDC)
- User/group sync: SCIM
- Plan requirements: Business or Enterprise (Twingate); OneLogin Unlimited Plan required for SCIM
- Users must initiate sessions from the Twingate Client app — portal-based launch is not supported

## Prerequisites
- Twingate Business or Enterprise plan
- OneLogin Unlimited Plan (for SCIM/user sync)
- Admin access to both OneLogin and Twingate Admin consoles

## Step-by-Step

### OneLogin Side
1. Go to **Applications > Add App**, search for "Twingate", select it
2. **Disable "Visible in portal"** toggle (users must authenticate from Twingate client, not OneLogin portal)
3. Click **Save**
4. Assign the Twingate application to OneLogin roles
   - Assigning to "Default" role enables quick testing
   - Recommended: create a dedicated role (e.g., "Admins") assigned to your account first to avoid lockout

### Twingate Side
1. Open the OneLogin integration setup in Twingate Admin console
2. Enter **OneLogin Subdomain** (found in OneLogin URL or Settings > Branding > Brand)
3. Copy **Client ID** and **Client Secret** from the **SSO tab** of the OneLogin Twingate app
4. Complete wizard by signing in with OneLogin to validate credentials

### Post-Setup
- Configure SCIM separately for user/group sync (see related docs)

## Configuration Values
| Field | Source |
|---|---|
| `OneLogin Subdomain` | OneLogin URL or Settings > Branding > Brand |
| `Client ID` | SSO tab of Twingate app in OneLogin |
| `Client Secret` | SSO tab of Twingate app in OneLogin |
| SCIM Base URL (placeholder) | `https://twingate.com` (temporary to bypass UI validation) |

## Gotchas
- **SCIM Base URL validation error**: OneLogin UI may show "SCIM Base URL cannot be blank" on Save — workaround: enter `https://twingate.com` in the Configuration tab temporarily; real SCIM setup is done separately
- **Role assignment risk**: If only "Default" role is assigned and later removed, you can lose admin access to Twingate — always assign a named admin role to yourself first
- **Portal visibility**: Hiding the app from the OneLogin portal is recommended since authentication only works when initiated from the Twingate client

## Related Docs
- SCIM for user & group sync (linked in docs)
- OneLogin Unlimited Plan documentation
- Twingate pricing page