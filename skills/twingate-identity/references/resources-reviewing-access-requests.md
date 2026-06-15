# Reviewing Access Requests

## Summary
Access Requests arise from JIT access workflows or Usage-Based Auto Lock policies. Authorized reviewers can approve or deny requests via the Admin Console or email notification links. The review process is identical regardless of which workflow triggered the request.

## Key Information
- Requests are visible on the **Access Requests page**, individual **User pages**, and individual **Resource pages**
- Resolved requests are visible for the last **90 days**
- Red dot on the bell icon in Admin Console indicates pending requests
- Resource Approvers **only** see the Access Requests page — no other Admin Console access
- Resource Approvers always receive email notifications; this is **not configurable**
- Email notifications contain direct links to review specific requests

## Who Can Review Requests

| Role | Scope |
|------|-------|
| Admin | All users, all resources |
| DevOps | All users, all resources |
| Access Reviewer | All users, all resources |
| Resource Approver | All users, assigned resources only |

## Prerequisites
- Admin Console access (for Admin/DevOps/Access Reviewer roles)
- Group membership in an assigned Resource Approver group (for Resource Approvers)

## Assigning Resource Approvers
1. Navigate to the **Resource** page in Admin Console
2. Open the Resource Approvers dialog
3. Assign one or more **Groups** as approvers
4. All members of assigned groups gain review rights for that resource only

## Configuration Notes
- Resource Approvers are assigned at the **Resource level**, not the user level
- Assign Groups specifically tailored to delegation use cases
- Resource Approvers log in via the standard Admin Console URL (e.g., `https://autoco.twingate.com`) but only see Access Requests

## Gotchas
- Resource Approvers **cannot** have email notifications disabled — always notified
- Resource Approvers have **zero** Admin Console visibility beyond the Access Requests page
- Groups (not individual users) are assigned as Resource Approvers; all group members inherit the role
- Notification settings available to Admin roles are **not available** for Resource Approvers

## Related Docs
- JIT Access Workflows
- Usage-Based Auto Lock
- Admin Roles
- Notifications Configuration