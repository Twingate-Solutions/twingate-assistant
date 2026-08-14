---
source: https://www.twingate.com/docs/jumpcloud-configuration
type: docs
fetched: 2026-08-14
source_version: a28dbaac7cee7a0e828915bc92913a150d2d4595e33ef8c7a78aa8354450ded8
---

# JumpCloud Configuration

## Page Title
JumpCloud Configuration (Twingate Identity Provider Integration)

## Summary
Twingate integrates with JumpCloud to synchronize user accounts via SCIM and delegate authentication via SAML. Only users and groups associated with the Twingate app in JumpCloud can access Twingate resources. Requires Business or Enterprise plan.

## Key Information
- **Authentication method**: SAML (delegated to JumpCloud)
- **User/group sync method**: SCIM protocol
- **Scope**: Only JumpCloud users/groups assigned to the Twingate app can use Twingate

## Prerequisites
- Twingate Business or Enterprise plan
- JumpCloud admin console access
- Twingate Admin Console access

## Step-by-Step

### Initial Setup
1. Create the Twingate application in the JumpCloud admin console
2. In Twingate Admin Console, exchange metadata:
   - Upload Twingate-provided `.xml` file to JumpCloud
   - Input JumpCloud-provided metadata URL into Twingate
3. Set the login URL within JumpCloud
4. Select an initial group of JumpCloud users to sync to Twingate
5. Configure SCIM provisioning:
   - Copy Twingate-provided SCIM endpoint and token
   - Paste into the **Identity Management** section of JumpCloud's Twingate application

### Selective Group Sync (Post-Setup)
1. JumpCloud admin portal → **User Authentication** → **SSO Applications**
2. Click the Twingate application
3. Click **User Groups** tab
4. Check boxes next to groups to sync
5. Click **Save** — groups and their members sync automatically

### Certificate Renewal
1. Twingate Admin Console → select **Renew Certificate**
2. Renew certificate in JumpCloud's Twingate application
3. Return to Twingate Admin Console modal → select **Confirm Certificate Renewal**

## Configuration Values
| Item | Source | Destination |
|------|--------|-------------|
| Metadata `.xml` file | Twingate Admin Console | JumpCloud |
| Metadata URL | JumpCloud | Twingate Admin Console |
| SCIM endpoint | Twingate Admin Console | JumpCloud Identity Management |
| SCIM token | Twingate Admin Console | JumpCloud Identity Management |
| Login URL | Twingate Admin Console | JumpCloud |

## Gotchas
- Groups must be explicitly assigned in JumpCloud — unassigned groups/users cannot access Twingate
- To verify currently synced groups: check **show bound User Groups** box on the User Groups page in JumpCloud
- Certificate renewal requires confirming in **both** JumpCloud and Twingate Admin Console (order matters: initiate in Twingate → renew in JumpCloud → confirm in Twingate)

## Related Docs
- Twingate pricing page (for plan eligibility)
- General SAML/SCIM integration documentation
- Twingate Admin Console identity provider settings