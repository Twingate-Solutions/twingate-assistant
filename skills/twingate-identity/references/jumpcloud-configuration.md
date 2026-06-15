# JumpCloud Configuration

## Page Title
JumpCloud Configuration (Twingate IdP Integration)

## Summary
Twingate integrates with JumpCloud to handle user authentication via SAML and user/group synchronization via SCIM. Only users and groups associated with the Twingate app in JumpCloud can access Twingate resources. Requires Business or Enterprise plan.

## Key Information
- Authentication delegation: SAML
- User/group sync protocol: SCIM
- Plan requirement: Business & Enterprise only
- Sync is selective — only groups explicitly assigned to the Twingate app in JumpCloud are synced

## Prerequisites
- Twingate Business or Enterprise plan
- Admin access to JumpCloud admin console
- Admin access to Twingate Admin Console

## Step-by-Step Configuration

### Initial Setup
1. Create the Twingate application in JumpCloud admin console
2. In Twingate Admin Console, exchange SAML metadata:
   - Upload Twingate-provided `.xml` file to JumpCloud
   - Input JumpCloud-provided metadata URL into Twingate
3. Set the login URL within JumpCloud
4. Select initial group of JumpCloud users to sync to Twingate
5. Configure SCIM provisioning:
   - Copy Twingate-provided SCIM endpoint and token
   - Paste into **Identity Management** section of JumpCloud's Twingate application

### Selective Group Sync (Post-Setup)
1. JumpCloud admin portal → **User Authentication** → **SSO Applications**
2. Click Twingate application
3. Click **User Groups** tab
4. Check boxes next to groups to sync
5. Click **Save**

### Certificate Renewal
1. Twingate Admin Console → select **Renew Certificate**
2. Renew certificate in JumpCloud's Twingate application
3. Back in Twingate modal → select **Confirm Certificate Renewal**

## Configuration Values
| Item | Source | Destination |
|------|--------|-------------|
| SAML metadata `.xml` file | Twingate Admin Console | JumpCloud |
| JumpCloud metadata URL | JumpCloud | Twingate Admin Console |
| SCIM endpoint URL | Twingate Admin Console | JumpCloud Identity Management |
| SCIM token | Twingate Admin Console | JumpCloud Identity Management |

## Gotchas
- Groups not explicitly assigned to the Twingate app in JumpCloud will **not** sync — users in unassigned groups cannot use Twingate
- Use **"show bound User Groups"** checkbox on the User Groups page to audit currently synced groups
- Certificate renewal requires coordinated steps in both consoles — partial completion will break authentication

## Related Docs
- Twingate pricing page (for plan eligibility)
- General SAML/SCIM integration documentation
- Other IdP configuration guides (Okta, Azure AD, etc.)