# JumpCloud Configuration

## Page Title
JumpCloud Configuration (SAML + SCIM Integration)

## Summary
Twingate integrates with JumpCloud to synchronize user accounts (via SCIM) and delegate authentication (via SAML). Only users and groups assigned to the Twingate app in JumpCloud can access Twingate resources. Available on Business and Enterprise plans only.

## Key Information
- **Authentication**: SAML (delegated to JumpCloud)
- **Provisioning**: SCIM (user/group sync from JumpCloud)
- **Scope**: Only JumpCloud users/groups associated with the Twingate app gain access

## Prerequisites
- Twingate Business or Enterprise plan
- JumpCloud admin console access
- Twingate Admin Console access

## Step-by-Step Setup

1. **Create Twingate app in JumpCloud** admin console
2. **Exchange metadata** in Twingate Admin Console:
   - Upload Twingate-provided `.xml` file to JumpCloud
   - Enter JumpCloud-provided metadata URL into Twingate
   - Set login URL within JumpCloud
   - Select initial group of JumpCloud users to sync
3. **Configure SCIM provisioning** in JumpCloud:
   - Copy Twingate-provided SCIM endpoint and token
   - Paste into the **Identity Management** section of the JumpCloud Twingate application

## Selective Group Sync (Post-Setup)

**Path**: JumpCloud Admin Portal → User Authentication → SSO Applications → Twingate → User Groups tab

1. Check boxes next to groups to sync
2. Click **Save**
3. Groups and their members sync automatically to Twingate

- Use **"show bound User Groups"** checkbox to review already-selected groups

## Certificate Renewal

1. In Twingate Admin Console: select **"Renew Certificate"**
2. Renew certificate in JumpCloud Twingate application
3. In Twingate Admin Console modal: select **"Confirm Certificate Renewal"**

## Configuration Values
| Item | Source | Destination |
|------|--------|-------------|
| Twingate `.xml` metadata file | Twingate Admin Console | JumpCloud |
| JumpCloud metadata URL | JumpCloud | Twingate Admin Console |
| SCIM endpoint | Twingate Admin Console | JumpCloud Identity Management |
| SCIM token | Twingate Admin Console | JumpCloud Identity Management |
| Login URL | Twingate | JumpCloud app config |

## Gotchas
- Users/groups **not** assigned to the JumpCloud Twingate app cannot use Twingate at all
- Certificate renewal requires a **specific sequence** — initiate in Twingate first, renew in JumpCloud second, then confirm back in Twingate
- Plan gating: integration unavailable on Starter plan

## Related Docs
- Twingate pricing page (for plan eligibility)
- SCIM provisioning documentation
- SAML configuration guides