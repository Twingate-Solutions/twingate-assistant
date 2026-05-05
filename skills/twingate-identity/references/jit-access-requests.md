## JIT Access Requests

Just-in-Time access requests gate Resource access behind an explicit request workflow. Useful for sensitive Resources where the goal is **zero standing access** -- users see they have access in the Client, but the Resource is locked until the request is approved (or auto-approved with a reason).

**Key Concepts:**
- Configurable per-Resource or per-Group-on-Resource
- Group-level config overrides the Resource default
- Two approval modes: **Auto Approval** (user provides reason) or **Required Approval** (admin/Resource Approver decides)
- Access is granted for a configurable time window after approval

### User Experience

- Users see the Resource in their Client with a **locked state**
- To request access:
  - Try to access the Resource address, **or**
  - Select **Authenticate** from the Resource's submenu in the Client
- Browser opens an Access Request page
- User enters reason (and custom duration if "Custom Request" is enabled)
- **Auto Approval**: immediate access after submitting (reason is logged)
- **Required Approval**: user receives email when approved/denied

### Configuration

**Per-Resource (default for all Group assignments):**
- Resource detail page -> enable Access Requests
- Set the access period (preset durations OR Custom Request -- up to 7 days)
- Set the approval method (Auto Approval / Required Approval)

**Per-Group-on-Resource (override):**
- Override the Resource default for specific Groups
- Useful pattern: Resource defaults to "Required Approval, 2-hour", but a trusted Group gets "Auto Approval, 12-hour"

**Available Time Periods:**
- Presets: e.g., 1 hour, 4 hours, 12 hours, 24 hours (per Admin Console)
- **Custom Request**: user picks at request time, max 7 days
- Longer durations possible via API

### Approval Workflow

Approvers come from these sources (see /docs/resources-reviewing-access-requests):
- Twingate **Admin / DevOps / Access Reviewer** roles can approve any request
- **Resource Approvers** (Groups assigned per-Resource) can approve requests for their assigned Resources -- and only those

Approvers are notified via email; they review on the Access Requests page in the Admin Console.

### Tracking & Audit

- Audit Logs (Access category) capture all configuration changes and request decisions
- Per-Resource, per-Group, or per-User CSV export shows current access status
- Resolved requests are visible for 90 days

### Decision Notes

- Use JIT for **production infrastructure**, **break-glass scenarios**, and **vendor/contractor access** to sensitive Resources
- For most users + low-risk Resources: standard Group assignment (no JIT) is simpler
- Auto Approval with a reason gives an audit trail without blocking users -- a middle path between "always granted" and "always requires approval"
- Combine with **Usage-Based Auto-Lock** -- users get JIT access for a window, then auto-lock kicks in if they don't use it

**Gotchas:**
- Custom Request max is 7 days at the Admin Console -- API can set longer if needed
- The Resource appears in the Client even when locked -- users see what they could potentially access (this is intentional UX, not a bug)
- Auto Approval still requires the user to enter a reason -- without a reason the Client cannot proceed

**Related Docs:**
- /docs/resources-reviewing-access-requests -- Approval workflow + Resource Approvers
- /docs/usage-based-auto-lock -- Companion: lock based on inactivity instead of time-bounded access
- /docs/ephemeral-access-to-resources -- Companion: time-bounded Group-on-Resource (no per-request workflow)
- /docs/security-policies -- Policy types overview
