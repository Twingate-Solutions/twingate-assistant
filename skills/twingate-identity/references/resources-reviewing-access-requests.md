# Reviewing Access Requests

## Summary
Access Requests are reviewed when users submit JIT access requests or when resources are locked via Usage-Based Auto Lock policies. Admins and designated Resource Approvers can approve or deny requests through the Admin Console or directly via email notification links.

## Key Information
- Access Requests page shows all open requests plus resolved requests from the last 90 days
- Red dot on bell notification icon in Admin Console indicates pending requests
- Resource Approvers only see the Access Requests page — no other Admin Console access
- Email notifications to Resource Approvers always fire and cannot be configured/disabled
- Requests can be reviewed from the Access Requests page, User detail page, or Resource detail page

## Who Can Review Requests

| Role | Scope |
|------|-------|
| Admin | All users, all resources |
| DevOps | All users, all resources |
| Access Reviewer | All users, all resources |
| Resource Approver | All users, assigned resources only |

## Prerequisites
- Admin Console access to assign Resource Approvers
- Resource Approvers must be organized into Groups before assignment

## Step-by-Step: Assigning Resource Approvers

1. Navigate to the Resource detail page in the Admin Console
2. Open the Resource Approvers assignment dialog
3. Select one or more Groups to assign as approvers
4. Save — all members of assigned Group(s) can now review requests for that resource

## Step-by-Step: Reviewing an Access Request

1. Click bell notification icon (red dot indicates pending requests) **or** follow link in email notification
2. On the Access Requests page, review open requests
3. Alternatively, review from the specific User's detail page or Resource detail page
4. Approve or deny the request

## Configuration Values
- Resource Approver login URL: `https://<network-name>.twingate.com` (standard Admin Console URL)
- Resolved request retention on Access Requests page: **90 days**

## Gotchas
- Resource Approvers **always** receive email notifications — this cannot be disabled or configured, unlike Admin role notifications
- Resource Approvers log in via the normal Admin Console URL but are restricted to only the Access Requests page
- Assign purpose-built Groups as Resource Approvers rather than reusing existing broad Groups
- The review workflow is identical whether triggered by JIT or Usage-Based Auto Lock

## Related Docs
- JIT Access workflow
- Usage-Based Auto Lock policy
- Admin roles documentation
- Notifications configuration