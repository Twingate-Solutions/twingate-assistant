---
source: https://www.twingate.com/docs/jit-access-requests
type: docs
fetched: 2026-11-13
source_version: f767531dff4561d33b671e2ac6b46a98428d78b5d8d2531f1bff4a06415939c0
trust: official
---

# JIT Access Requests

## Summary
JIT Access Requests provide an audited, just-in-time workflow that grants temporary access to sensitive Resources. They can be enabled for all or specific Groups assigned to a Resource, and requests are either auto-approved or need explicit approver sign-off.

## Key Information
- Users in a Group with Access Requests enabled still see the Resource in the Client, but it is locked until access is approved.
- Users request access by navigating to the Resource address or selecting **Authenticate** from the Resource's submenu in the Client. This opens an access request page in the browser.
- **Auto-approval:** access is available immediately after the user submits the request. The user must supply a reason.
- **Manual approval:** an approver must approve each request. The user gets an email when the request is approved or denied.
- Configuration can be set at the Resource level (the default for all Group assignments) or per Group assignment (overrides the Resource-level setting).

## Prerequisites
- A Resource with one or more Groups assigned.
- Admin access to configure the Resource or Group assignments.
- For manual approval, approvers need to be able to review requests (see Reviewing Access Requests).

## Step-by-Step (Configuration)
1. Open the Resource in the Admin Console (or a specific Group assignment on it).
2. Enable Access Requests.
3. Select an **Access Period**: a preset duration, or **Custom Request**.
4. Select an **Approval Method**: manual or auto-approval.
5. Save. Group-level settings override the Resource-level defaults.

## Configuration Values
- **Access period:** preset durations (e.g., 12 hours), or **Custom Request**, where the user chooses a duration of up to 7 days when submitting.
- **Approval method:** manual approval or auto-approval (user self-approves with a reason).
- **Scope:** Resource-level default vs. Group-assignment override.

## Gotchas
- Group-level configuration overrides the Resource-level one, so check the assignment when behavior differs from expectations.
- Custom requests are capped at 7 days.
- With auto-approval, users self-approve, so the audit trail depends on the reason they provide.
- With manual approval, users are notified by email only after a decision is made.
- The Resource appears in the Client but is not usable until approved, which can confuse users.

## Tracking Access
Download a summary of configuration details and current user access status from the Resource, Group, or User page. Report contents are described on the Usage-based Auto-lock page.

## Related Docs
- Reviewing Access Requests (reviewing and delegating requests)
- Usage-based Auto-lock (report contents)