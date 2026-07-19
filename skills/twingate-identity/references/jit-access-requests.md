# JIT Access Requests

## Summary
JIT Access Requests provide temporary, audited access workflows for Twingate Resources. Users in configured Groups can see but not access locked Resources until approval is granted. Requests can be auto-approved or require manual Admin/Access Reviewer approval.

## Key Information
- Access Requests are configured at the **Resource level** (becomes default for all Group assignments) or overridden at individual **Group assignment level**
- Locked Resources are visible in the Client but inaccessible until approved
- Users trigger requests via navigating to the Resource address or selecting **Authenticate** from the Resource submenu
- Auto-approval requires users to supply a reason; manual approval requires Admin or Access Reviewer action
- Approved users receive email notification on approval or denial

## Prerequisites
- Admin or Access Reviewer role required to approve/manage requests
- Resource must have Access Requests enabled
- Users must be members of the configured Group assigned to the Resource

## Configuration Values

| Setting | Options |
|---|---|
| Access Period | Preset durations (unspecified in docs) or **Custom Request** |
| Custom Request max duration | 7 days |
| Approval Method | Manual approval or Auto-approval |

### Access Period Options
- Preset durations (e.g., 12 hours shown in example)
- `Custom Request` — user specifies duration up to 7 days

### Approval Method Options
- **Manual** — Admin or Access Reviewer must approve each request
- **Auto-approval** — user self-approves but must provide a reason

## Configuration Hierarchy
1. Set defaults at **Resource level**
2. Override per **Group assignment** as needed

## Tracking Access
- Download summary reports from the **Resource**, **Group**, or **User** page
- Report contents detailed in the usage-based access page

## Gotchas
- Custom Request allows **any duration up to 7 days** — no minimum enforced
- Auto-approval still requires a **stated reason** from the user (not fully frictionless)
- Resource-level settings are defaults only; Group assignments can override them independently
- Users see the Resource in Client regardless of lock status — visibility ≠ access

## Related Docs
- [Reviewing Access Requests](https://www.twingate.com/docs/reviewing-access-requests) — approval workflow and delegation details
- [Usage-Based Access](https://www.twingate.com/docs/usage-based-access) — report contents and access tracking