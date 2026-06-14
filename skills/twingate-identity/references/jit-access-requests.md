# JIT Access Requests

## Summary
JIT Access Requests provide temporary, audited access workflows for Twingate Resources. Access can be auto-approved or require manual approval from an Admin or Access Reviewer. Resources remain locked to users until access is granted through the request workflow.

## Key Information
- Users see locked Resources in the Client and must request access via the Resource address or **Authenticate** submenu option
- Requests open a browser-based access request page
- Auto-approval requires users to supply a reason; manual approval requires Admin or Access Reviewer action
- Users receive email notifications on approval or denial
- Configuration can be set at Resource level (becomes default for all Group assignments) or overridden per Group assignment

## Configuration Values

**Access Period Options:**
- Preset durations (specific values not listed in docs)
- `Custom Request` — user specifies duration, maximum 7 days

**Approval Method Options:**
- `Manual Approval` — Admin or Access Reviewer must approve each request
- `Auto-Approval` — user self-approves but must provide reason

## Configuration Scope
| Level | Behavior |
|-------|----------|
| Resource level | Default for all Group assignments |
| Group assignment level | Overrides Resource-level settings |

## Step-by-Step: Configure JIT on a Resource
1. Navigate to the Resource detail page
2. Configure Access Requests settings (access period + approval method)
3. Optionally override settings on specific Group assignments

## Tracking Access
- Download usage summary from Resource, Group, or User page
- See **usage-based access page** for report contents

## Gotchas
- Users can **see** the Resource in the Client but **cannot connect** until approved — visibility without access is expected behavior
- Custom Request durations are user-specified but capped at 7 days
- Resource-level settings are defaults only; per-Group overrides take precedence
- Auto-approval still requires a reason from the user — it is not frictionless

## Related Docs
- [Reviewing Access Requests](#) — covers delegating and reviewing request details
- [Usage-Based Access](#) — covers downloadable report contents