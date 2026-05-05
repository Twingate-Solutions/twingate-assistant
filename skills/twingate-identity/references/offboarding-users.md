## Offboarding Users

Best practices for revoking Twingate access when a user leaves the org or no longer needs access. Two scenarios depending on the IdP model.

### Scenario 1: Social Logins (No IdP)

Direct in-Twingate offboarding via Admin Console:

1. **Team page** -> Users tab
2. Locate the user
3. **Disable** or **Delete**:

| Action | Effect | Billing |
|---|---|---|
| **Disable** | User cannot log in; account info retained | Still counted as billable user |
| **Delete** | Account permanently removed | No longer billable |

**Use Disable** when there's a chance the user might return; **Delete** when offboarding is permanent.

### Scenario 2: Enterprise IdP (SCIM-Synced)

Twingate users are managed in the IdP -- changes flow into Twingate via SCIM:

**Full org offboarding:**
- Disable / delete the user in the IdP (Okta, Entra ID, JumpCloud, OneLogin, Google Workspace)
- Wait for SCIM sync to propagate to Twingate

**Twingate-only revocation (user stays in the org):**
- Remove the user from any IdP Groups that are synced to Twingate
- Synced changes will revoke Group memberships -> Resource access

**Sync Delay -- Belt-and-Suspenders Approach:**

SCIM sync isn't always instantaneous. To guarantee immediate revocation:

- Log in to Twingate Admin Console
- **Devices** section -> locate the user's device(s)
- **Block** the device
- Blocked devices cannot access any Resources, regardless of IdP sync status
- Device stays blocked until explicitly unblocked

### Decision Notes

- **Always block devices** for terminated users -- don't rely on SCIM sync alone for security-critical departures
- For high-trust users (admins, finance): combine IdP disable + Twingate device block + 2FA reset
- For routine departures: IdP disable is usually sufficient; SCIM sync windows are typically minutes
- Audit the **Audit Logs** for the user's last activity timestamps to verify revocation was effective

### Gotchas

- **Disabled users are still billed** in Twingate -- delete them once you're confident they won't return
- SCIM sync delay varies by IdP and config -- Okta typically syncs within 5-10 minutes; some IdPs are slower
- Removing a user from a synced IdP Group only revokes that Group's access -- if they're in multiple synced Groups, remove from all
- "Everyone" Group cannot have users removed -- IdP-disable is the only way to remove someone from Everyone
- Service Accounts (machine identities) are managed separately -- disable/delete via the Service Accounts UI or API

### Related Docs

- /docs/social-logins -- Social login user management
- /docs/identity-providers -- IdP / SCIM overview
- /docs/users -- User management
- /docs/devices, /docs/managing-devices -- Device blocking
- /docs/audit-logs -- Auditing offboarding actions
- /docs/scim-provisioning-api -- SCIM mechanics
