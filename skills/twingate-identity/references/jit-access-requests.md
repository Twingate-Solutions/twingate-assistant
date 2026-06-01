# JIT Access Requests

## Summary
JIT Access Requests provide temporary, audited access workflows for Twingate Resources. Access can require explicit Admin/Access Reviewer approval or be auto-approved with a mandatory reason. Settings are configurable at the Resource level (as defaults) or overridden per Group assignment.

## Key Information
- Users in JIT-enabled Groups see Resources in the Client but cannot access them until approved (locked state)
- Users trigger requests via navigating to the Resource address or selecting **Authenticate** from the Resource submenu
- Auto-approval grants immediate access after submission; manual approval sends email notification on decision
- Resource-level settings serve as defaults; individual Group assignments can override them

## Configuration Values

| Setting | Options |
|---|---|
| Access Period | Preset durations or **Custom Request** (user-specified, max 7 days) |
| Approval Method | Manual (Admin or Access Reviewer) or Auto-approval (self-approved, reason required) |

## Configuration Steps
1. Navigate to the Resource detail page
2. Enable Access Requests at the Resource level to set defaults for all Group assignments
3. Set **Access Period** (preset or Custom Request)
4. Set **Approval Method** (manual or auto-approval)
5. Optionally override settings on individual Group assignments within the Resource

## Gotchas
- Auto-approval still requires users to supply a reason — not fully frictionless
- Custom Request access periods are user-defined but capped at **7 days maximum**
- Resource-level config is only a default; Group-level overrides take precedence for specific assignments
- Users must be in an assigned Group to see the Resource at all; JIT restricts access within that Group

## Tracking Access
- Download usage summaries from the Resource, Group, or User page
- Report contents detailed in the **usage-based access** documentation

## Related Docs
- [Reviewing Access Requests](https://www.twingate.com/docs/reviewing-access-requests) — approval workflow and delegation details
- [Usage-Based Access](https://www.twingate.com/docs/usage-based-access) — report contents and tracking