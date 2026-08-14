---
source: https://www.twingate.com/docs/jit-access-requests
type: docs
fetched: 2026-08-14
source_version: 1d45840a1c2a5c8997cd969ac1f0012963b8aab29148bca5b4439dd98e64702f
---

# JIT Access Requests

## Summary
JIT Access Requests provide just-in-time, audited access workflows for Twingate Resources, granting temporary access either automatically or via manual approval. Users see locked Resources in the Client until access is approved. Configuration can be set at the Resource level (as default) or overridden per Group assignment.

## Key Information
- Users see the Resource in the Client but cannot connect until access is approved
- Users trigger a request via navigating to the Resource address or selecting **Authenticate** from the Client submenu
- Auto-approval requires users to supply a reason; manual approval requires an Admin or Access Reviewer
- Access period options: preset durations or **Custom Request** (user-specified, max 7 days)
- Configuration hierarchy: Resource-level settings are defaults; individual Group assignments can override

## Prerequisites
- Resource must exist in Twingate
- Users must be assigned to a Group that has the Resource assigned
- For manual approval: Admin or Access Reviewer role required to approve requests

## Configuration

### Access Period Options
| Option | Details |
|--------|---------|
| Preset durations | Fixed time periods (e.g., 12 hours) |
| Custom Request | User-specified duration, up to 7 days max |

### Approval Method Options
| Method | Behavior |
|--------|----------|
| Auto-approval | User approves immediately; reason required |
| Manual approval | Admin or Access Reviewer must explicitly approve/deny |

## Step-by-Step: Configuring JIT on a Resource
1. Navigate to the Resource detail page
2. Configure Access Request settings at the Resource level (becomes default for all Group assignments)
3. Select **Access Period** (preset or Custom Request)
4. Select **Approval Method** (manual or auto-approval)
5. Optionally override settings on individual Group assignments

## User Workflow
1. User attempts to connect or selects **Authenticate** from the Resource submenu in the Client
2. Browser opens the access request page
3. User submits request (with reason if auto-approval, or awaits review if manual)
4. If auto-approved: immediate access granted
5. If manual: user receives email notification on approval or denial

## Tracking & Reporting
- Download access summary from the **Resource**, **Group**, or **User** page
- Report contents detailed on the usage-based access page

## Gotchas
- Custom Request duration is capped at **7 days**; users cannot request longer periods
- Resource-level config is only a default — Group-level overrides take precedence
- Auto-approval still requires a reason from the user (not fully frictionless)
- Manual approval requires a designated Admin or Access Reviewer — ensure these roles are assigned before enabling

## Related Docs
- [Reviewing Access Requests](https://www.twingate.com/docs/reviewing-access-requests)
- [Usage-Based Access Report](https://www.twingate.com/docs/usage-based-access)