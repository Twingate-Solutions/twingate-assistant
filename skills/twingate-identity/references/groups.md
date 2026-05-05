## Groups

Groups are how users are authorized to access Resources. The core access-control concept in Twingate.

### Three Aspects of a Group

1. **Members** -- a set of Users (users may be in multiple Groups)
2. **Resources** -- the Resources that members are authorized to access
3. **Per-Resource access modifiers** (optional):
   - **Expiration time** (Ephemeral Access) -- Group access ends at a specified time; access is fully revoked
   - **Usage-based auto-lock** -- access locked per-user if not used within N days; unlocked via request workflow

### Authorization Logic

For a user to access a Resource, they must:
1. Be a member of a Group assigned to that Resource
2. Successfully satisfy the Resource's **Security Policy** (auth + MFA + device requirements)

Both conditions are required. Group membership grants the *opportunity*; the policy gates the *access*.

### Three Group Types

#### Built-in: Everyone Group

- Includes **all users** automatically
- Cannot be deleted; users cannot be removed
- Resources commonly assigned:
  - Company-wide dashboards / metrics
  - **Domain Controllers** for Windows AD environments
  - **IdP login domains** for SaaS App Gating

See /docs/security-policies-best-practices for the recommended Resource Policy on the Everyone Group (no auth + device trust).

#### Custom Groups

- Manually created and managed in the Admin Console
- Not modified by automation
- Manageable via Twingate Admin API

#### Synced Groups

- Automatically synchronized from the configured **IdP** via SCIM
- User membership is **read-only** in Twingate -- managed in the IdP
- Resources and Security Policies *can* be assigned to Synced Groups in Twingate

**IdP-Specific Sync Behavior:**

| IdP | Granular Sync Control |
|---|---|
| **Entra ID, Okta, OneLogin** | Native SCIM scoping -- choose which users/groups are synced |
| **Google Workspace** | No native SCIM scoping -- Twingate provides **Selective Sync** to limit which users / groups / OUs sync |

### Decision Notes

- **Use Synced Groups as much as possible** -- IdP is the source of truth for membership; Twingate inherits
- **Use Custom Groups for Twingate-specific buckets** -- e.g., a "Service Accounts" Group, a "Break-glass" Group, a Group for Resource Approvers
- Don't manually edit Synced Group memberships -- next sync overwrites
- For role-based access: model your IdP Groups around access patterns and let SCIM drive Twingate

### Gotchas

- A Resource accessible through multiple Groups inherits the Resource's Security Policy -- the **Group-level override** can change the policy for specific Groups (per /docs/security-policies)
- Group expiration (Ephemeral) revokes the Group from the Resource, not the user from the Group -- the user stays in the Group with access to other Resources
- Selective Sync for Google Workspace requires explicit configuration -- by default everything syncs, which can be overwhelming for large workspaces
- Synced Group names match the IdP exactly -- changing the name in the IdP renames the Twingate Group on next sync

### Related Docs

- /docs/users -- User management
- /docs/identity-providers -- IdP integration overview
- /docs/security-policies -- Group-on-Resource policy overrides
- /docs/security-policies-best-practices -- Everyone Group pattern
- /docs/ephemeral-access-to-resources -- Group expiration on Resources
- /docs/usage-based-auto-lock -- Per-user inactivity locking
- /docs/google-workspace-configuration -- Selective Sync
- /docs/scim-provisioning-api -- SCIM API reference
