# JumpCloud Configuration

## Page Title
JumpCloud Configuration (SAML + SCIM Integration with Twingate)

## Summary
Twingate integrates with JumpCloud for user authentication via SAML and user/group synchronization via SCIM. Only users and groups associated with the Twingate app in JumpCloud can access Twingate resources. Requires Business or Enterprise plan.

## Key Information
- **Authentication**: SAML delegated to JumpCloud
- **Provisioning**: SCIM protocol for user/group sync
- **Scope**: Only JumpCloud users/groups assigned to the Twingate app gain access
- **Selective sync**: Can control which groups sync post-setup

## Prerequisites
- Twingate Business or Enterprise plan
- JumpCloud admin console access
- Twingate Admin Console access

## Step-by-Step Configuration

### Initial Setup
1. Create the Twingate application in JumpCloud admin console
2. Exchange metadata between systems:
   - Upload Twingate-provided `.xml` file into JumpCloud
   - Enter JumpCloud-provided metadata URL into Twingate Admin Console
3. Set the login URL within JumpCloud
4. Select an initial group of JumpCloud users to sync to Twingate
5. Configure SCIM provisioning:
   - Copy Twingate-provided SCIM endpoint and token
   - Paste into **Identity Management** section of JumpCloud's Twingate application

### Selective Group Sync (Post-Setup)
1. JumpCloud admin portal → **User Authentication** → **SSO Applications**
2. Click the Twingate application
3. Click **User Groups** tab
4. Check boxes next to groups to sync
5. Click **Save**
   - Groups and their members sync automatically to Twingate
   - Use **show bound User Groups** checkbox to verify current selections

### Certificate Renewal
1. Twingate Admin Console → select **Renew Certificate**
2. Renew certificate in JumpCloud's Twingate application
3. Return to Twingate Admin Console modal → select **Confirm Certificate Renewal**

## Configuration Values
| Item | Source | Destination |
|------|--------|-------------|
| Twingate metadata `.xml` | Twingate Admin Console | JumpCloud app config |
| JumpCloud metadata URL | JumpCloud | Twingate Admin Console |
| SCIM endpoint | Twingate Admin Console | JumpCloud Identity Management |
| SCIM token | Twingate Admin Console | JumpCloud Identity Management |

## Gotchas
- Users/groups **not** assigned to the Twingate app in JumpCloud cannot access any resources—no exceptions
- Certificate renewal requires completing steps in **both** consoles in sequence; partial completion leaves integration broken
- Initial group selection happens during setup; changes require returning to the JumpCloud **User Groups** tab

## Related Docs
- Twingate pricing page (for plan eligibility)
- General SAML/SCIM integration documentation
- Twingate Admin Console identity provider setup