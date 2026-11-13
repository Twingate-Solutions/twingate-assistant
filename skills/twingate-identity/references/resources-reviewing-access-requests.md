---
source: https://www.twingate.com/docs/resources-reviewing-access-requests
type: docs
fetched: 2026-11-13
source_version: db89b62bedc6438040b0976a4645717c64e400499b8ed30b6b2f8dadea942edc
trust: official
---

# Reviewing Access Requests

## Summary
Access Requests are created when users request access through a JIT workflow or when a Resource is locked by a Usage-based Auto-lock policy. Review works the same way for both. Approvers can be Admin roles or Groups delegated per Resource (Resource Approvers).

## Key Information
- **Roles that can review all Users and Resources:** Admin, DevOps, Access Reviewer.
- **Resource Approvers:** One or more Groups assigned to a Resource. Members can approve requests only for the Resources they are assigned to, for any User.
- Resource Approvers have no Admin Console access beyond the Access Requests page. They sign in via the normal Admin Console URL (e.g., `https://autoco.twingate.com`) and see only that page.
- **Notifications:** Resource Approvers always receive an email when a request is pending, and this cannot be configured. Admin role notifications are configurable. Emails link directly to the open request.
- **Access Requests page:** Admins see a red dot on the bell icon (upper right of the Admin Console) when requests are open. The page lists all open requests across all Resources, plus requests resolved in the last 90 days.
- Admins can also review open requests from a User's detail page (that User's requests) or a Resource's detail page (all open requests for all Users).

## Prerequisites
- Admin Console access with an Admin, DevOps, or Access Reviewer role, or membership in a Group assigned as Resource Approver for the Resource.
- A JIT access workflow or Usage-based Auto-lock policy generating requests.

## Step-by-Step

**Assign Resource Approvers**
1. Open the Resource's detail page in the Admin Console.
2. Open the Resource Approvers dialog from the entry point on that page.
3. Add or remove the Groups that should review requests, then save.

**Review a request**
1. Click the bell icon, use the email link, or open the User or Resource page.
2. Open the pending request on the Access Requests page.
3. Approve or deny it.

## Configuration Values
No env vars, CLI flags, or API params are documented on this page. Configuration is done in the Admin Console UI only.

## Gotchas
- Resource Approver email notifications can't be turned off or tuned, so use Groups tailored to the delegation use case to avoid noisy alerts.
- Resolved requests only appear for 90 days.
- Resource Approvers can't see the rest of the Admin Console, so don't rely on them for other administrative tasks.
- Approver scope is per Resource, so assign Groups on each Resource that needs delegated review.

## Related Docs
- JIT access workflow documentation
- Usage-based Auto-lock policy documentation
- Admin roles documentation
- Notifications settings documentation