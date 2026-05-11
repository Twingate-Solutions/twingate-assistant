# JIT Access Requests

## Summary
JIT Access Requests enable an audited, just-in-time access workflow for Groups assigned to a Resource. Resources appear locked to users until access is approved, supporting either auto-approval or explicit admin/reviewer approval. Primary use case is temporary access to sensitive Resources.

## Key Information
- Configured at **Resource level** (becomes default for all Group assignments) or **per Group assignment** (overrides Resource default)
- Resource appears visible but **locked** in Client until access is granted
- Users trigger requests by accessing the Resource address or selecting "Authenticate" from Client submenu
- Access request page loads in browser
- Auto-approval requires user to supply a reason; manual approval notifies user via email when approved/denied
- Maximum custom access period: **7 days**

## Configuration Options

| Option | Values |
|--------|--------|
| Access Period | Preset durations (e.g., 12 hours) or "Custom Request" (user specifies, up to 7 days) |
| Approval Method | Auto-Approval (self-approved, reason required) or Manual (Admin or Access Reviewer must approve) |

## Prerequisites
- Resource must exist with Group assignments configured
- For manual approval: Admin or Access Reviewer role required to approve requests

## Configuration Steps
1. Navigate to the Resource detail page
2. Enable Access Requests at the Resource level (sets default for all Group assignments)
3. Select access period: preset duration or "Custom Request"
4. Select approval method: Auto-Approval or manual approval required
5. Optionally override settings per individual Group assignment

## Tracking Access
- Download access summary from Resource, Group, or User page
- Full details on usage-based access page

## Gotchas
- Resource is **visible** to users in Client even when locked — they just cannot connect until approved
- Resource-level config is **inherited** by all Group assignments unless explicitly overridden per assignment
- Auto-approval still requires the user to submit a reason
- Custom Request periods capped at 7 days maximum

## Related Docs
- [Reviewing Access Requests](#) — details on approving/denying and delegating review
- [Usage-Based Access](#) — tracking configuration details and current access status