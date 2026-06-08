# JIT Access Requests

## Summary
JIT Access Requests provide temporary, audited access workflows for Twingate Resources. Access can be auto-approved or require manual approval from an Admin or Access Reviewer. Users see locked Resources and must explicitly request access through the Client.

## Key Information
- Configured at **Resource level** (becomes default for all Group assignments) or overridden at **individual Group assignment level**
- Two approval modes: **manual** (Admin/Access Reviewer approves) or **auto-approval** (user self-approves but must supply a reason)
- Access periods: preset durations or **Custom Request** (user-specified, max 7 days)
- Users see the Resource in the Client but cannot connect until approved — Resource state shows as "locked"
- Users trigger request via navigating to Resource address or selecting **Authenticate** from the Resource submenu in the Client
- Manual approval: user receives email notification on approval/denial
- Auto-approval: immediate access after request submission

## Prerequisites
- Admin or Access Reviewer role required to approve manual requests
- Access Requests must be enabled on the Resource or Group assignment

## Configuration
### Resource-Level Settings
| Setting | Options |
|---|---|
| Access Period | Preset durations (e.g., 1hr, 4hr, 12hr, 24hr) or Custom Request (up to 7 days) |
| Approval Method | Manual approval or Auto-approval |

### Override Behavior
- Resource-level config = default for all Group assignments
- Individual Group assignments can override Resource-level settings

## Step-by-Step: Enable JIT on a Resource
1. Navigate to the Resource detail page
2. Configure Access Request settings (access period + approval method)
3. Optionally override settings on specific Group assignments within the Resource

## Step-by-Step: User Request Flow
1. User sees locked Resource in Client
2. User navigates to Resource address **or** selects **Authenticate** from submenu
3. Browser opens access request page
4. User submits request (with reason if auto-approval; optional reason for manual)
5. Auto-approval: immediate access granted; Manual: wait for email notification

## Tracking Access
- Download usage summary from the **Resource**, **Group**, or **User** page
- Report contents documented in the [usage-based access page](https://www.twingate.com/docs/usage-based-access)

## Gotchas
- Custom Request duration is capped at **7 days** maximum
- Auto-approval still requires users to supply a reason — it is not frictionless
- Group-level overrides take precedence over Resource-level defaults; verify Group assignments if behavior is unexpected
- Access Requests apply per Group assignment — a user in multiple Groups may have different access rules for the same Resource

## Related Docs
- [Reviewing Access Requests](https://www.twingate.com/docs/reviewing-access-requests)
- [Usage-Based Access Reports](https://www.twingate.com/docs/usage-based-access)
- Access Reviewers role documentation