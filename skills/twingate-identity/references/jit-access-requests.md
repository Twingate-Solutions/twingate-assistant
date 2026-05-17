# JIT Access Requests

## Summary
JIT Access Requests enable audited, just-in-time access workflows for Groups assigned to Resources. Resources appear locked to users until access is approved, supporting both auto-approval and manual approval flows. Designed for sensitive Resources requiring temporary, time-limited access.

## Key Information
- Access Requests can be configured at the **Resource level** (becomes default for all Group assignments) or overridden per **individual Group assignment**
- Resource state is **locked by default** until access is approved or auto-approved
- Users trigger requests by accessing the Resource address directly or via "Authenticate" in the Client submenu
- Auto-approval requires users to supply a reason; manual approval notifies users via email on approve/deny
- Maximum access period: **7 days**
- Preset time periods available (e.g., 12-hour), or **Custom Request** lets users specify duration at request time

## Prerequisites
- Admin or Access Reviewer role required to approve requests
- Resource must have Access Requests feature enabled
- Users must be members of a Group assigned to the Resource

## Configuration Options

### Access Period
| Option | Behavior |
|--------|----------|
| Preset (e.g., 1hr, 12hr, 24hr) | All requests granted for fixed duration |
| Custom Request | User specifies duration at request time (max 7 days) |

### Approval Method
| Option | Behavior |
|--------|----------|
| Auto Approval | User self-approves; reason required |
| Requires Approval | Admin or Access Reviewer must approve; user notified via email |

## Configuration Steps
1. Navigate to the **Resource detail page**
2. Enable Access Requests at the Resource level (sets default for all Group assignments)
3. Select **access period** (preset or custom)
4. Select **approval method** (auto or manual)
5. Optionally override configuration on individual **Group assignment** level

## Tracking Access
- Download access summary from **Resource**, **Group**, or **User** pages
- Summary includes configuration details and current user access status
- Full details on usage-based access page

## Gotchas
- Resource-level config is **inherited** by all Group assignments unless individually overridden — changing the default affects all non-overridden assignments
- Custom Request period is user-specified at request time, not admin-controlled
- Auto-approval still requires a reason from the user — it is not frictionless
- Users **see** the Resource in the Client even when locked; they just cannot connect until approved

## Related Docs
- [Reviewing Access Requests](https://www.twingate.com/docs/reviewing-access-requests) — approving/denying and delegating to Access Reviewers
- [Usage-Based Access](https://www.twingate.com/docs/usage-based-access) — tracking and downloading access summaries