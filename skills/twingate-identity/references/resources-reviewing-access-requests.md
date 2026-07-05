# Reviewing Access Requests

## Summary
Access Requests are submitted by users via JIT access or Usage-Based Auto Lock workflows and require review/approval by authorized roles. Both workflows use the same review process. Reviewers can approve or deny requests from the Admin Console or directly via email notification links.

## Key Information
- Resolved requests are visible for **90 days** after resolution
- Resource Approvers receive **mandatory email notifications** (cannot be disabled)
- Admin role notifications are configurable; Resource Approver notifications are not
- Resource Approvers only see the Access Requests page—no other Admin Console access
- Resource Approvers are assigned at the **Resource level** via Groups

## Who Can Review Requests

| Role | Scope |
|------|-------|
| Admin | All users, all resources |
| DevOps | All users, all resources |
| Access Reviewer | All users, all resources |
| Resource Approver | Any user, assigned resources only |

## Prerequisites
- Resource Approvers must be members of a Group assigned to the specific Resource
- Resource Approver assignment done via Resource detail page in Admin Console
- Resource Approvers log in at the standard Admin Console URL (e.g., `https://autoco.twingate.com`)

## Step-by-Step: Assigning Resource Approvers
1. Navigate to the Resource detail page in Admin Console
2. Open the Resource Approvers dialog
3. Assign one or more Groups as approvers
4. All members of assigned Groups gain review rights for that Resource

## Step-by-Step: Reviewing Access Requests
1. Watch for red dot on bell notification icon (Admin Console, top right)
2. Select notification to open **Access Requests page**
3. Alternatively, click link in email notification to go directly to the request
4. Review request and approve or deny
5. Can also review from the **User detail page** or **Resource detail page**

## Gotchas
- Resource Approvers **cannot configure** notification preferences—emails are always sent
- Assign purpose-built Groups for Resource Approver delegation (avoid assigning broad Groups)
- Resource Approvers have **zero Admin Console access** beyond the Access Requests page
- Open requests appear with a red dot indicator; missing this requires checking User/Resource pages directly
- Both JIT and Usage-Based Auto Lock requests use the **identical** review flow

## Related Docs
- JIT Access workflow
- Usage-Based Auto Lock policy
- Admin roles documentation
- Notifications configuration