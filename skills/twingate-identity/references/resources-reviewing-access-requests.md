# Reviewing Access Requests

## Summary
Access Requests arise from JIT access workflows or Usage-Based Auto Lock policies. Designated reviewers can approve or deny these requests via the Admin Console or direct email links. The review process is identical regardless of which workflow triggered the request.

## Key Information
- Requests visible on Admin Console Access Requests page; red dot on bell icon indicates pending requests
- Resolved requests displayed for last 90 days
- Resource Approvers can only see the Access Requests page — no other Admin Console access
- Email notifications always sent to Resource Approvers (non-configurable); Admin role notifications are configurable

## Who Can Review

| Role | Scope |
|------|-------|
| Admin, DevOps, Access Reviewer | All users and all resources |
| Resource Approvers | Only resources they are assigned to |

## Resource Approvers Setup
- Assigned per Resource via the Resource detail page in Admin Console
- Approvers are assigned as **Groups** (not individual users); all group members gain approval rights for that resource
- Recommended: create Groups tailored to specific delegation use cases
- Login URL for Resource Approvers: `https://<network>.twingate.com` (standard Admin Console URL)

## Step-by-Step: Assigning Resource Approvers
1. Navigate to the Resource detail page in Admin Console
2. Open the Resource Approvers assignment dialog
3. Add one or more Groups as approvers
4. Save — group members will receive email notifications for pending requests on that resource

## Step-by-Step: Reviewing a Request
1. **Via email**: Click the direct link in the notification email to log in and review
2. **Via Admin Console bell icon**: Click red dot → opens Access Requests page showing all open requests
3. **Via User page**: View open requests scoped to a specific user
4. **Via Resource page**: View all open requests across all users for that resource
5. Approve or deny the request from any of these entry points

## Gotchas
- Resource Approvers **always** receive email notifications — this cannot be disabled or reconfigured
- Resource Approvers have **zero** Admin Console access beyond the Access Requests page
- Assigning individuals as approvers requires putting them in a dedicated Group first
- Access Requests page shows resolved requests only for the last 90 days — older history not visible here

## Related Docs
- [JIT Access Workflow](https://www.twingate.com/docs/jit-access)
- [Usage-Based Auto Lock](https://www.twingate.com/docs/usage-based-auto-lock)
- [Admin Roles](https://www.twingate.com/docs/admin-roles)
- [Notifications Configuration](https://www.twingate.com/docs/notifications)