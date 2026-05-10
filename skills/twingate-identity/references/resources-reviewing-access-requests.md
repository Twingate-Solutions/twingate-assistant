# Reviewing Access Requests

## Summary
Access Requests are generated via JIT access workflows or Usage-Based Auto Lock policies. Authorized reviewers approve or deny these requests through the Admin Console or direct email links. The review process is identical regardless of request origin.

## Key Information
- Resolved requests are visible for 90 days after resolution
- Resource Approvers have **no Admin Console access** except the Access Requests page
- Resource Approvers always receive email notifications (not configurable)
- Admin roles receive configurable notifications; Resource Approvers do not
- Open requests trigger a red dot on the bell icon in Admin Console

## Who Can Review Requests

| Role | Scope |
|------|-------|
| Admin | All users, all resources |
| DevOps | All users, all resources |
| Access Reviewer | All users, all resources |
| Resource Approver | Any user, assigned resources only |

## Configuring Resource Approvers

**Prerequisites:** Admin Console access

**Steps:**
1. Navigate to the Resource page in Admin Console
2. Open the Resource Approvers dialog
3. Assign one or more Groups as Resource Approvers

**Behavior:**
- All members of assigned Group(s) can review requests for that resource
- Resource Approvers log in via standard URL (e.g., `https://autoco.twingate.com`)
- They see only the Access Requests page upon login

## Reviewing Requests

**Access methods:**
- Bell icon (red dot indicates pending requests) → Access Requests page
- Direct link in email notification
- User page in Admin Console (shows open requests per user)
- Resource page in Admin Console (shows all open requests for all users)

## Gotchas
- Resource Approver notifications cannot be disabled or reconfigured — always email
- Assign purpose-specific Groups as Resource Approvers to avoid over-delegation
- Resource Approvers cannot access any other Admin Console functionality
- Email notifications contain direct login links — typical workflow doesn't require navigating the console manually

## Related Docs
- JIT Access Workflow
- Usage-Based Auto Lock Policy
- Admin Roles
- Notifications Configuration