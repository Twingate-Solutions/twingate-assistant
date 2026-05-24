# Reviewing Access Requests

## Summary
Access Requests are generated via JIT access workflows or Usage-Based Auto Lock policies. Designated roles and Resource Approvers can review and approve these requests through the Admin Console or via email links.

## Key Information
- Resolved requests are visible for 90 days after resolution
- Resource Approvers receive **mandatory** email notifications; this cannot be configured/disabled
- Resource Approvers only see the Access Requests page — no other Admin Console access
- Requests can be reviewed from User pages, Resource pages, or the main Access Requests page
- Open requests trigger a red dot on the bell icon in the Admin Console

## Who Can Approve

| Role | Scope |
|------|-------|
| Admin | All users and resources |
| DevOps | All users and resources |
| Access Reviewer | All users and resources |
| Resource Approver | Only assigned resources |

## Prerequisites
- Admin Console access (for Admin roles)
- Resource Approver group assignment (for delegated approvals)
- Groups must be created before assigning as Resource Approvers

## Assigning Resource Approvers (Step-by-Step)
1. Navigate to the Resource page in Admin Console
2. Open the Resource Approvers dialog
3. Assign one or more Groups as Resource Approvers
4. All members of assigned Group(s) inherit approval rights for that resource only

## Configuration Notes
- Resource Approvers are assigned at the **Resource level**, not user level
- Assignment uses **Groups**, not individual users — design groups specifically for delegation use case
- Resource Approvers access the same Admin Console URL (e.g., `https://autoco.twingate.com`) but see only the Access Requests page

## Gotchas
- Resource Approver email notifications **cannot** be turned off — ensure assigned groups are appropriate recipients
- Resource Approvers have no other Admin Console visibility; design groups carefully to avoid unintended access delegation
- Standard admin notification preferences **do not apply** to Resource Approvers

## Related Docs
- JIT Access workflow
- Usage-Based Auto Lock policy
- Admin roles documentation
- Notifications configuration