# JIT Access Requests

## Summary
JIT Access Requests provide an audited, just-in-time access workflow for Groups assigned to Resources. Resources appear locked to users until access is approved, supporting either auto-approval or explicit Admin/Access Reviewer approval. Designed for sensitive Resources requiring temporary, time-limited access.

## Key Information
- Access Requests can be configured at **Resource level** (becomes default/inherited) or **per Group assignment** (overrides Resource default)
- Resource appears in Client as locked until access is granted
- Users trigger request by accessing the Resource address or selecting "Authenticate" from Client submenu
- Request loads an access request page in the browser
- Auto-approval requires user to supply a reason; manual approval notifies user via email when approved/denied
- Maximum access period: **7 days**

## Configuration Options

### Access Period
| Option | Description |
|--------|-------------|
| Preset durations | Fixed time period (e.g., 12 hours) applied to all requests |
| Custom Request | User specifies duration at request time (up to 7 days) |

### Approval Method
| Option | Description |
|--------|-------------|
| Approval Required | Admin or Access Reviewer must explicitly approve |
| Auto Approval | User self-approves but must provide reason |

## Prerequisites
- Resource must exist with Group assignments configured
- For manual approval: Admin or Access Reviewer role required to approve/deny requests
- Users must be members of the Group assigned to the Resource

## Configuration Steps
1. Navigate to Resource detail page
2. Configure Access Requests at Resource level (sets default for all Group assignments)
3. Select access period (preset duration or "Custom Request")
4. Select approval method (Auto Approval or Approval Required)
5. Optionally override configuration per individual Group assignment

## Tracking Access
- Download summary from Resource, Group, or User page for configuration details and current user access status
- See **usage-based access** page for full details

## Gotchas
- Resource-level config is **inherited** by all Group assignments; individual assignments must be explicitly overridden if different behavior needed
- Auto-approval still requires user to submit a reason — it is not fully frictionless
- Custom Request option shifts duration control to the user at request time, not the admin

## Related Docs
- [Reviewing Access Requests](https://www.twingate.com/docs/reviewing-access-requests) — approving/denying and delegating requests
- [Usage-Based Access](https://www.twingate.com/docs/usage-based-access) — tracking access status and downloading summaries