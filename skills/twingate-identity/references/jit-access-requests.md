# JIT Access Requests

## Page Title
JIT Access Requests

## Summary
JIT Access Requests provide audited, temporary access workflows for Twingate Resources assigned to specific Groups. Users see locked Resources until access is approved (manually or automatically). Supports auto-approval with required reason or manual approval by Admins/Access Reviewers.

## Key Information
- Access Requests operate at **Resource level** (default) or **Group assignment level** (overrides Resource-level settings)
- Users see the Resource in the Client but cannot connect until access is granted
- Users trigger requests via navigating to the Resource address or **Authenticate** in the Client submenu
- Auto-approval: user approves immediately but must provide a reason
- Manual approval: Admin or Access Reviewer approves/denies; user notified by email
- Access tracking available via downloadable reports from Resource, Group, or User pages

## Prerequisites
- Resource must be configured with Access Requests enabled
- Approvers must have Admin or Access Reviewer role (for manual approval)
- Twingate Client installed on user device

## Configuration Values

### Access Period Options
| Option | Description |
|--------|-------------|
| Preset durations | Fixed time periods (e.g., 1 hour, 4 hours, 12 hours) |
| Custom Request | User specifies duration; max **7 days** |

### Approval Method Options
| Option | Behavior |
|--------|----------|
| Manual approval | Admin or Access Reviewer must explicitly approve each request |
| Auto-approval | User self-approves; reason for access required |

## Step-by-Step: Configure JIT on a Resource
1. Navigate to the Resource detail page
2. Enable Access Requests
3. Set **Access Period** (preset or Custom Request)
4. Set **Approval Method** (manual or auto-approval)
5. Optionally override settings per Group assignment on that Resource

## Gotchas
- Resource-level settings are **defaults only**; individual Group assignments can override them
- Custom Request allows users to choose duration up to 7 days — no finer-grained cap control
- Auto-approval still requires users to submit a reason; it is not silent/transparent access
- Users must actively trigger a request (navigate to address or use Client submenu) — no automatic prompt on first connection attempt beyond the locked state

## Related Docs
- [Reviewing Access Requests](https://www.twingate.com/docs/reviewing-access-requests) — approval workflow details and delegation
- [Usage-Based Access Reports](https://www.twingate.com/docs/usage-based-access) — report contents from Resource/Group/User pages