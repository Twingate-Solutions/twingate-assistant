---
source: https://www.twingate.com/docs/usage-based-auto-lock
type: docs
fetched: 2026-11-13
source_version: c9a026aee155eff0e0adfbfb0cae946211e3d5faaf33359f472b164b19c45ff1
trust: official
---

# Usage-based Auto-lock

## Summary
Usage-based auto-lock removes a user's access to a Twingate Resource if they haven't accessed it within a configured duration, helping enforce least privilege. Locked users regain access through manual approval by an approver or by giving a reason under automatic approval. It can be configured from Resource or Group pages in the Admin Console.

## Key Information
- Admin Console durations: 1, 7, 30, 60, or 90 days. Other durations are available via the API.
- Locking is evaluated **per user**, even when the duration is set on a Group.
- Groups inherit the Resource-level auto-lock configuration by default, but can override it.
- Changes to auto-lock settings are logged in the **Access** category of the audit logs.
- Regaining access depends on the approval method:
  - **Manual:** an approver must approve the user's request (see Reviewing Access Requests).
  - **Automatic:** the user gives a reason and access is restored immediately. The reason is still recorded in analytics and on the resolved requests page.
- Locked-out users see a block page where they submit a request with a reason.
- Users receive an email when a request is approved or denied.
- Admins can manually unlock a Resource for a user on the user's detail page.

## Prerequisites
- Admin Console access.
- For notifications: Admin, Viewer, DevOps, Helpdesk, or Access Reviewer role (email toggles apply to these roles).
- Approvers designated for manual approval.

## Step-by-Step
**From a Resource page**
1. Set the auto-lock duration on the Resource (applies to all users with access).
2. When adding a Group to the Resource, optionally specify a Group-specific duration.
3. To change an existing Group, click its options button and set the duration and approval method.

**From a Group page**
1. Open the Group's detail page.
2. Set the auto-lock duration and approval method for specific Resources.

**Unlock a user:** open the user's detail page and unlock the Resource.

**Track access:** download an access summary from the Resource, Group, or User page.

## Configuration Values
- **Notifications:** Settings > Notifications (email toggles per user, plus webhooks).
- **Access summary report contents:** Groups with access and the policy used, expiration dates, auto-lock duration, and per-user lock status and last admin unlock.
- **Webhook payload fields:** `timestamp`, `tenant`, `version` ("1"), `type` ("ACCESS_REQUEST"), `request_id`, `request_url`, `user_name`, `user_url`, `resource_name`, `resource_url`, `requested_at`, `reason`, `approval_mode` ("MANUAL"), `request_type` ("AutoLock"), `request_duration_seconds` (e.g., 2592000 = 30 days).

## Gotchas
- Non-standard durations can only be set through the API, not the Admin Console.
- A Group-level duration does not lock everyone at once; each user's last access is evaluated individually.
- Group settings override inherited Resource-level settings, so check both when debugging unexpected locks.
- Under automatic approval, users still must supply a reason.

## Related Docs
- Reviewing Access Requests
- Settings > Notifications (webhooks and email)
- Audit logs (Access category)