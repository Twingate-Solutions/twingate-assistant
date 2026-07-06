# JIT Access Requests

## Summary
JIT Access Requests provide temporary, audited access workflows for Twingate Resources. Access can be auto-approved or require manual approval from an Admin or Access Reviewer. Users see locked Resources until access is granted.

## Key Information
- Configured at the Resource level (becomes default for all Group assignments) or overridden at individual Group assignment level
- Two approval methods: **manual** (Admin/Access Reviewer approves) or **auto-approval** (user self-approves but must provide reason)
- Access periods: preset durations or **Custom Request** (user-specified, max 7 days)
- Users see the Resource in the Client but cannot connect until approved
- Users trigger requests via navigating to Resource address or selecting **Authenticate** from the Resource submenu in the Client
- If auto-approved: immediate access after submission
- If manual: user receives email notification on approval/denial

## Configuration Values

| Setting | Options |
|---|---|
| Access Period | Preset durations or Custom Request (up to 7 days) |
| Approval Method | Manual approval or Auto-approval |

## Prerequisites
- Resource must have Access Requests enabled for the relevant Group assignment
- Approvers must have Admin or Access Reviewer role (for manual approval)

## Step-by-Step: Configuring JIT Access

1. Navigate to the Resource detail page
2. Configure Access Requests at the Resource level (sets default for all Group assignments)
3. Optionally override settings on individual Group assignments
4. Select **Access Period** (preset or Custom Request)
5. Select **Approval Method** (manual or auto-approval)

## Tracking Access
- Download usage summary from the Resource, Group, or User page
- See usage-based access page for full report details

## Gotchas
- Custom Request duration is capped at **7 days** maximum
- Resource-level settings are defaults only — Group-level assignments can override them
- Auto-approval still requires users to supply a reason for access
- Users can see locked Resources in the Client but cannot connect without approval

## Related Docs
- [Reviewing Access Requests](https://www.twingate.com/docs/reviewing-access-requests)
- [Usage-Based Access Reports](https://www.twingate.com/docs/usage-based-access)