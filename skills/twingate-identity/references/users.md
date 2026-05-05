## Users

How users are created, synchronized, billed, and authorized in Twingate.

### Two User Sources

| Source | Management | When to Use |
|---|---|---|
| **Social logins** (Google, Microsoft, GitHub, LinkedIn) | Manual via Admin Console -- invite, disable, delete | Small teams, trials, no enterprise IdP |
| **Enterprise IdP** (Okta, Entra ID, Google Workspace, JumpCloud, OneLogin, Keycloak) | SCIM-synced -- changes flow from IdP to Twingate | Production deployments |

When an IdP is connected, **users cannot be modified in the Twingate Admin Console** -- create/disable/delete in the IdP, sync handles the rest.

### Default Access -- "Everyone" Group

- New users are automatically added to the built-in **Everyone** Group
- Without further config, they have **no Resource access** -- the Everyone Group has no Resources by default
- Admins must either:
  - Add Resources to the Everyone Group (e.g., IdP login, AD/DC -- typical for the company-wide use case), or
  - Add the user to additional Groups that have Resource assignments

### Viewing User Access

User detail page provides two views:
- **List form**: tabular Group/Resource access
- **Access Graph**: visual mapping of Groups, Resources, paths, and policies
  - Filterable by Group, Remote Network, or Resource

### Billing

You are billed for:
- All synchronized users (active + disabled)
- All Service Accounts you create

Therefore: **delete unused users**, don't just disable them.

### Admin Roles

Three admin roles for Admin Console access (per /docs/admins):
- **Admin** -- full read/write
- **DevOps** -- read all + write Network tab only
- **Support** -- read-only

Plus the **Access Reviewer** role for approving JIT/auto-lock requests.

### Decision Notes

- **Always use a real IdP for production** -- SCIM-driven user lifecycle is critical for offboarding security
- For new tenants: start with social logins to evaluate, switch to IdP before scaling
- For mixed user populations (employees + contractors): use the IdP for employees, social logins for short-term contractors -- both sources work simultaneously
- **Offboard users by deleting**, not disabling, unless you expect a return -- saves billing

### Gotchas

- Users in IdP-synced Groups cannot be modified in Twingate -- changes there are reverted by the next sync
- The Everyone Group cannot be deleted, and users cannot be removed from it -- only IdP disable removes them
- Service Accounts are separate from human Users but billed alongside them
- Switching from social logins to an IdP doesn't automatically migrate users -- plan the cutover carefully

### Related Docs

- /docs/social-logins -- Social login flow
- /docs/identity-providers -- IdP integration
- /docs/groups -- Group concepts (Everyone, Custom, Synced)
- /docs/admins -- Admin role assignment
- /docs/offboarding-users -- Disable vs. delete + IdP-side offboarding
- /docs/scim-provisioning-api -- SCIM mechanics
