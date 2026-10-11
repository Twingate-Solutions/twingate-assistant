---
source: https://www.twingate.com/docs/2026-10-admin-role-changes
type: docs
fetched: 2026-10-11
source_version: 6935a731e2319ba1542823b49003cf96b719203b3b69b7940d1fe785ff9ce3c9
trust: official
---

<!-- triage: unassigned -->

# Admin Role Changes (October 2026)

## Page Title
Admin Role Changes – Support and DevOps Role Updates (Week of October 19, 2026)

## Summary
Twingate is updating the Support and DevOps admin roles to restrict access to sensitive data (DNS filtering logs, Billing). The Support role is being renamed to "Viewer" with reduced permissions. These changes take effect the week of October 19, 2026.

## Key Information

- **Affected roles:** Support (→ Viewer) and DevOps only; all other admin roles unchanged
- **Support → Viewer rename:**
  - Loses access to: Secure DNS page, Client Configuration page (Internet Security tab), Billing settings page
  - Retains: read-only permissions for the rest of the Admin Console
- **DevOps change:** Loses access to Billing settings page only; no other permission changes
- **Internet Security role** (already available): grants read+write on Internet Security tab; read-only elsewhere except Billing
- **API/Terraform:** Continue using `SUPPORT` as the identifier for the Viewer role — no config changes needed

## Prerequisites
- Admin Console access with a role that can manage user roles (e.g., full Admin)
- Internet Security role available now for assignment

## Step-by-Step: Assign the Internet Security Role

1. In the Admin Console, go to **Team > Users**
2. Select the target user
3. Click **Manage Role**
4. Select **Internet Security**
5. Click **Confirm Changes**

## Configuration Values

| Context | Value | Notes |
|---|---|---|
| API / Terraform | `SUPPORT` | Identifier retained for the renamed Viewer role |
| New role identifier | `INTERNET_SECURITY` | Assumed; check API docs for exact enum |

## Gotchas

- **Internet Security role has no read-only option** — it grants full read+write on that tab; assign only to users who need to manage those settings
- **Support tasks** (MFA reset, device verification) should use the **Helpdesk** role, not Viewer
- **Existing API/Terraform configs referencing `SUPPORT` do not need updating** after the rename
- Changes are automatic during the week of October 19, 2026 — no migration action required for the rename itself

## Related Docs
- [Admin Roles overview](https://www.twingate.com/docs/admin-roles)
- Helpdesk role documentation
- Internet Security role documentation
- Twingate Support: contact for questions about these changes