## Ephemeral Access

Time-bounded Group access to a Resource -- configure an expiration timestamp; when reached, the Group is automatically removed from the Resource.

**Concept:**
- Group X has access to Resource Y until 2026-06-01 17:00 UTC
- After that timestamp, Group X is removed from Resource Y -- no manual cleanup
- All users in the Group lose access at the same time
- Distinct from auto-lock (per-user inactivity-based) and JIT (per-request, per-window)

**Configurable Expiration Range:**
- From the next hour up to **one year** from the current date

### Configuration Locations

| Location | What It Does |
|---|---|
| **Resource page** -- adding a Group | Set expiration when granting Group access |
| **Resource page** -- options on existing Group assignment | Modify expiration on an already-granted Group |
| **Group page** -- per-Resource the Group has access to | Same operation, different navigation |

### Audit

- Expiration changes are logged in the **Access category of Audit Logs**
- Useful for compliance: verifiable record of when contractor access was granted and when it ended

### Common Use Cases

| Scenario | Pattern |
|---|---|
| **Project with defined end date** | Group expires at project end; access auto-revokes |
| **Contractor engagement** | Contractor Group expires at engagement end |
| **Break-glass access** | Add admin to break-glass Group with 4-hour expiry; Group auto-revokes |
| **Onboarding window** | New hire gets temporary access to legacy systems while migrating off |

### Decision Notes

- Use ephemeral when the **end date is known up front**
- Use **JIT (just-in-time)** when access is needed on demand but you don't know when (per /docs/jit-access-requests)
- Use **usage-based auto-lock** to catch forgotten access without an explicit end date (per /docs/usage-based-auto-lock)
- Combining ephemeral + auto-lock: ephemeral sets the hard end; auto-lock revokes earlier if unused

**Gotchas:**
- Expiration removes the **Group from the Resource** -- not the user from the Group. If the Group has access to other Resources, the user keeps those.
- Once the Group is removed, manually re-adding requires re-configuring everything -- consider using JIT workflows for repeated short-term access patterns
- The expiration timestamp is precise -- set it generously to avoid mid-meeting access loss

**Related Docs:**
- /docs/jit-access-requests -- Per-request time-bounded access
- /docs/usage-based-auto-lock -- Inactivity-based revocation
- /docs/security-policies -- Policy types overview
- /docs/audit-logs -- Audit Logs reference
- /docs/vendor-and-contractor-access-management -- Pattern using ephemeral for contractors
