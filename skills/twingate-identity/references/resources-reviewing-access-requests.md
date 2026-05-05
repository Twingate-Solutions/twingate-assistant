## Reviewing Access Requests

How approvers handle incoming Access Requests (from JIT or Usage-Based Auto-Lock). Same review flow regardless of which workflow generated the request.

### Who Can Approve

| Role | Scope |
|---|---|
| **Admin** (Twingate role) | All Users, all Resources |
| **DevOps** (Twingate role) | All Users, all Resources |
| **Access Reviewer** (Twingate role) | All Users, all Resources |
| **Resource Approver** (Group assigned per-Resource) | Only the Resources their Group is assigned to |

### Resource Approvers

The mechanism for **delegating approval** to non-admin users -- e.g., the engineering manager approves access requests for the staging cluster, without giving them full Twingate Admin access.

**How to Assign:**
- Resource detail page in the Admin Console
- Add one or more **Groups** as Resource Approvers for the Resource
- All members of assigned Groups become approvers for that Resource

**Resource Approver Permissions:**
- Can approve/deny Access Requests for their assigned Resources
- **Cannot** access the Admin Console outside of the Access Requests page
- Sign in via the standard Admin Console URL (`https://<tenant>.twingate.com`) -- they only see Access Requests

**Notifications:**
- Resource Approvers **always** receive an email notification on a pending request
- Notification settings cannot be customized per Resource Approver -- this is by design
- Tip: assign **purpose-built Groups** as Resource Approvers (e.g., "Infra-Approvers"), not large ad-hoc Groups

### How Approvers See Requests

**Admin / DevOps / Access Reviewer:**
- Red dot on the bell icon in the Admin Console when there are open requests
- Click -> Access Requests page (all open + last 90 days resolved)
- Can also review on the User detail page (User's open requests) or Resource detail page (Resource's open requests)

**Resource Approver:**
- Email notification with a direct link to the request
- Login at the Admin Console URL takes them straight to the Access Requests page (only page they see)

### Notification Configuration (for Admin Roles)

- **Settings -> Access Requests** -- choose which Admin roles get email notifications:
  - Admins
  - DevOps
  - Access Reviewers
- Disable email and use a **webhook** for incoming requests (custom Slack/PagerDuty integration)
- Webhook payload includes: `request_id`, `user_name`, `resource_name`, `reason`, `approval_mode`, `request_type` (JIT or AutoLock), `request_duration_seconds`, `request_url` -- see /docs/usage-based-auto-lock for the example payload schema

### Decision Notes

- Use Resource Approvers heavily for **shifting approval to subject-matter experts** (engineering managers, team leads) -- reduces admin bottleneck
- Webhook integration is the right answer for **high-volume environments** -- email approval doesn't scale
- For sensitive break-glass Resources: require Admin approval, not Resource Approver, and configure webhook to PagerDuty for explicit on-call signoff

**Gotchas:**
- Resource Approvers' email notifications cannot be silenced -- if they're noisy, change the Group assigned as approvers
- Resource Approvers see only Access Requests -- they cannot see the rest of the Twingate config; that's by design but may surprise users new to the role
- Approvals expire if not acted on -- request a review SLA in your runbook

**Related Docs:**
- /docs/jit-access-requests -- JIT workflow that generates requests
- /docs/usage-based-auto-lock -- Auto-lock workflow that also generates requests + webhook payload schema
- /docs/admins -- Admin role definitions
