# JumpCloud Configuration

## Page Title
JumpCloud Configuration (SAML + SCIM Integration)

## Summary
Twingate integrates with JumpCloud to synchronize user accounts (via SCIM) and delegate authentication (via SAML). Only users and groups assigned to the Twingate app in JumpCloud can access Twingate resources. Available on Business and Enterprise plans only.

## Key Information
- **Authentication**: SAML (delegated to JumpCloud)
- **Provisioning**: SCIM (user/group sync)
- **Scope**: Only JumpCloud users/groups associated with the Twingate app gain access

## Prerequisites
- Twingate Business or Enterprise plan
- JumpCloud admin console access
- Twingate Admin Console access

## Step-by-Step Setup

1. **Create Twingate app in JumpCloud** admin console
2. **Exchange metadata** in Twingate Admin Console:
   - Upload Twingate-provided `.xml` file to JumpCloud
   - Input JumpCloud-provided metadata URL into Twingate
   - Set login URL within JumpCloud
   - Select initial group of JumpCloud users to sync
3. **Configure SCIM provisioning**:
   - Copy Twingate-provided SCIM endpoint and token
   - Paste into **Identity Management** section of JumpCloud's Twingate application

## Selective Group Sync (Post-Setup)

1. JumpCloud admin portal → **User Authentication** → **SSO Applications**
2. Click the Twingate application
3. Go to **User Groups** tab
4. Check boxes next to groups to sync
5. Click **Save**

- Groups and their members sync automatically after save
- Use **"show bound User Groups"** checkbox to audit currently synced groups

## Certificate Renewal

1. Twingate Admin Console → select **"Renew Certificate"**
2. Renew the certificate inside JumpCloud's Twingate application
3. Return to Twingate Admin Console modal → select **"Confirm Certificate Renewal"**

> Order matters: initiate renewal in Twingate first, renew in JumpCloud second, confirm in Twingate last.

## Configuration Values

| Item | Source | Destination |
|------|--------|-------------|
| Twingate `.xml` metadata file | Twingate Admin Console | JumpCloud |
| JumpCloud metadata URL | JumpCloud | Twingate Admin Console |
| SCIM endpoint URL | Twingate Admin Console | JumpCloud Identity Management |
| SCIM token | Twingate Admin Console | JumpCloud Identity Management |

## Gotchas
- Users/groups **not** assigned to the JumpCloud Twingate app cannot access Twingate, regardless of other JumpCloud settings
- Certificate renewal sequence must follow the specific order above to avoid breaking authentication
- Plan gating: integration unavailable on Starter/free plans

## Related Docs
- Twingate pricing page (for plan eligibility)
- General SAML/SCIM identity provider configuration docs
- Twingate Admin Console documentation