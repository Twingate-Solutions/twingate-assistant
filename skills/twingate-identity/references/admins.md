## Admin Roles

Twingate has **four admin roles** with different write/read scopes across the Admin Console. The user who creates the network is the only admin by default.

### Roles

| Role | Write Capabilities | Read Capabilities |
|---|---|---|
| **Admin** | Entire Admin Console | Entire Admin Console |
| **DevOps** | Network tab only -- Resources, Connectors, Remote Networks, Group-to-Resource assignments, Access Requests | Entire Admin Console |
| **Support** | None -- read-only | Entire Admin Console |
| **Access Reviewer** | Access Requests page only -- approve/deny requests | Entire Admin Console |

### Assigning Roles

- User detail page (Users tab) -> click name
- **Manage** -> **Manage Role**
- Select desired role

### Admin Console Access

- URL: `https://<your-subdomain>.twingate.com`
- Authenticate with the configured IdP **or** supported social identity for the Twingate network
- DevOps / Support / Access Reviewer roles see a **role badge** next to the Twingate logo
- Hovering the badge shows what they can/can't do
- Attempts to edit out-of-scope settings are blocked with an error

### Decision Notes

- **Always have at least 2 Admin role users** (per /docs/security-policies-best-practices) -- avoids lockout from sudden departures
- **DevOps role** is right for engineers who manage Resources/Connectors but should not change billing/security settings
- **Access Reviewer** is right for compliance/security team members who need to approve JIT/auto-lock requests but shouldn't touch infrastructure
- **Support role** is the cleanest choice for read-only auditors and onboarding observers
- For finer delegation, use **Resource Approvers** (per /docs/resources-reviewing-access-requests) -- they can approve requests for specific Resources without any Admin Console access

### Gotchas

- Admins are not subject to MAR Sign-In Policy when accessing the Admin Console -- the **Admin Console Security Policy** governs that (see /docs/admin-console-security)
- Admin Console Security Policy enforces 1-hour re-auth (cannot be lengthened) and supports 2FA -- enforce 2FA always
- Role badges are not visible to Admins -- the unbadged UI is the full Admin role view
- Removing the only Admin from a tenant requires Twingate Support intervention -- always promote a second Admin first

### Related Docs

- /docs/admin-console-security -- Admin Console Sign-In Policy
- /docs/resources-reviewing-access-requests -- Resource Approvers (delegated approval without Admin role)
- /docs/security-policies-best-practices -- Why 2 Admins minimum
- /docs/users -- User management overview
