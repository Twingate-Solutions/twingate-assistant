## JumpCloud Configuration

How to integrate JumpCloud with Twingate -- SAML user authentication + SCIM user/group sync.

**Plan Requirement:**
- **Business or Enterprise** Twingate plans only

### What's Delegated to JumpCloud

- **User authentication** via SAML
- **User and group synchronization** via SCIM

Only users and groups associated with the Twingate app in JumpCloud can use Twingate.

### Three-Step Setup

**Step 1: Create the Twingate Application in JumpCloud Admin Console**

**Step 2: Complete & Validate Configuration in Twingate Admin Console**
- Exchange SAML metadata:
  - Twingate provides a `.xml` metadata file
  - JumpCloud provides a metadata URL
- Set the Login URL within JumpCloud
- Select an initial group of JumpCloud users to sync to Twingate

**Step 3: Set Up SCIM in JumpCloud's Twingate Application**
- Copy the **SCIM endpoint** and **SCIM token** from Twingate
- Paste into the **Identity Management** section of the Twingate app in JumpCloud

### Selective Group Sync (Post-Setup)

After initial integration, change which JumpCloud groups sync to Twingate:

1. JumpCloud admin portal -> **User Authentication > SSO Applications**
2. Open the Twingate application
3. **User Groups** tab
4. Check boxes next to groups you want to sync
5. **Save**

Once saved, the selected groups + their members sync automatically to Twingate.

**Tip**: Use the **show bound User Groups** checkbox on the User Groups page to see what's currently synced.

### Renewing JumpCloud SAML Certificates

When a SAML certificate is approaching expiry:

1. Twingate Admin Console -> **Renew Certificate**
2. Renew the certificate in the Twingate application within JumpCloud
3. Back in Twingate -> **Confirm Certificate Renewal** in the modal

This dual-renewal flow ensures continuity -- old cert remains valid until the new one is confirmed.

### Decision Notes

- JumpCloud is the right IdP if your team already uses it for device + identity management; for IdP-only environments, Okta or Entra ID may be more flexible
- For SaaS app gating: see /docs/saas-app-gating-with-jumpcloud (uses JumpCloud Conditional Lists)
- Use Selective Group Sync to keep Twingate's user list scoped -- syncing all JumpCloud groups can clutter the Admin Console

### Gotchas

- SAML cert renewals can break sign-in if not done in lockstep -- always follow the dual-renewal flow
- SCIM token in JumpCloud is sensitive -- rotate periodically; treat as a credential
- Users not in the Twingate app's assigned groups cannot sign in -- check JumpCloud group membership if users report sign-in failures

### Related Docs

- /docs/identity-providers -- IdP overview
- /docs/saas-app-gating-with-jumpcloud -- SaaS app gating with JumpCloud
- /docs/scim-provisioning-api -- SCIM mechanics
- /docs/groups -- Synced Groups behavior
