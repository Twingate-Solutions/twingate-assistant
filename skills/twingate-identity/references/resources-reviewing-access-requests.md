# Reviewing Access Requests

## Summary
Access Requests occur during JIT access workflows or when a Resource is locked via Usage-Based Auto Lock policy. Designated admins and Resource Approvers can review and approve requests through the Admin Console or via email links. All review workflows use the same process regardless of request origin.

## Key Information
- Access Requests page shows all open requests plus resolved requests from the last 90 days
- Red dot on bell notification icon in Admin Console indicates pending requests
- Resource Approvers only see the Access Requests page — no other Admin Console access
- Email notifications to Resource Approvers always fire and cannot be configured/disabled
- Admin role notifications can be configured; Resource Approver notifications cannot

## Who Can Approve Requests

**Full Admin roles (all Users and Resources):**
- Admins
- DevOps
- Access Reviewer

**Resource Approvers:**
- Members of assigned Groups
- Can only approve requests for Resources they are explicitly assigned to
- No Admin Console access beyond Access Requests page

## Assigning Resource Approvers

**Steps:**
1. Navigate to the Resource page in Admin Console
2. Open the Resource Approvers dialog
3. Assign one or more Groups as approvers

**Behavior:**
- All members of assigned Group(s) can review requests for that Resource
- Resource Approvers can still log in via the standard Admin Console URL (e.g., `https://autoco.twingate.com`)
- Assign purpose-specific Groups to keep delegation scoped appropriately

## Reviewing Access Requests

**Access methods:**
1. **Bell icon** — Red dot indicates open requests; click to navigate to Access Requests page
2. **Email link** — Direct link in notification email to log in and review specific request
3. **User page** — Admins can review open requests per user
4. **Resource page** — Admins can see all open requests across all users for a Resource

## Gotchas
- Resource Approvers **always** receive email notifications — no way to suppress or configure this
- Recommend creating Groups specifically tailored to the delegation use case rather than reusing existing broad Groups
- Resource Approvers logging into the Admin Console URL will only land on the Access Requests page — no other navigation available
- Resolved requests are only visible for 90 days

## Related Docs
- JIT Access workflow
- Usage-Based Auto Lock policy
- Admin roles reference
- Notifications configuration