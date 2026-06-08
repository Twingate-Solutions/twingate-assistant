# Reviewing Access Requests

## Summary
Covers how to approve or deny Access Requests from JIT access workflows or Usage-Based Auto Lock policies. Both Admin roles and delegated Resource Approvers can review requests. The review process is identical regardless of which workflow triggered the request.

## Key Information
- Access Requests originate from two workflows: JIT access or Usage-Based Auto Lock
- Resolved requests are visible for 90 days on the Access Requests page
- Red dot on bell icon in Admin Console indicates pending requests
- Resource Approvers only see the Access Requests page — no other Admin Console access
- Email notifications to Resource Approvers always fire and cannot be configured/disabled

## Who Can Review

**Admin roles (all users and resources):**
- Admin
- DevOps
- Access Reviewer

**Resource Approvers (assigned resources only):**
- One or more Groups assigned per Resource
- All Group members can review requests for assigned Resources only
- Useful for delegating access review without granting full admin access

## Prerequisites
- Admin Console access for Admin roles
- Resource Approver assignment via Resource detail page (for delegated approvers)
- Groups must be pre-configured to assign as Resource Approvers

## Step-by-Step: Assigning Resource Approvers
1. Navigate to the Resource detail page in Admin Console
2. Open the Resource Approvers dialog
3. Assign one or more Groups as Resource Approvers
4. Members of assigned Groups can now review requests for that Resource

## Step-by-Step: Reviewing Access Requests
1. Watch for red dot on bell icon (Admin Console, upper right) — indicates open requests
2. Click the notification to open the Access Requests page
3. Alternatively, review from the User detail page or Resource detail page
4. Approve or deny the request

**Resource Approvers:** Log in via standard Admin Console URL (e.g., `https://<network>.twingate.com`) — will land directly on Access Requests page. Typically use the direct link from email notification.

## Gotchas
- Resource Approvers **cannot** configure their notification preferences — they always receive email for pending requests
- Resource Approvers have **zero** Admin Console visibility beyond the Access Requests page
- Assign purpose-built Groups as Resource Approvers rather than reusing existing groups
- The Access Requests page is the only entry point for Resource Approvers; plan onboarding accordingly

## Related Docs
- [JIT Access Workflow](https://www.twingate.com/docs/jit-access)
- [Usage-Based Auto Lock](https://www.twingate.com/docs/usage-based-auto-lock)
- [Admin Roles](https://www.twingate.com/docs/admin-roles)
- [Notifications Configuration](https://www.twingate.com/docs/notifications)