---
source: https://www.twingate.com/docs/authentication
type: docs
fetched: 2026-11-13
source_version: e1275dd3582f38739f38433267c5898bae3afa0f40827c7a15c4f3811c9f1717
trust: official
---

# Page Title
Authentication (Twingate Security Policy Rule)

## Summary
The Authentication rule sets how often users must re-authenticate. It can be applied to Resource Policies or the Sign In Policy. Re-authentication behavior also depends on how the identity provider (IdP) handles repeat sign-ins.

## Key Information
- **Applies to:** Resource Policies and the Sign In Policy.
- **Not editable:** The Admin Console's own authentication policy cannot be changed.
- **Function:** Defines the re-authentication interval. Example: with a 6-hour rule, a user who hasn't authenticated in the past 6 hours is prompted when accessing the Resource.
- **Shared session window:** If a user authenticated within the time window, they are not prompted again, even under a different Security Policy.
  - Example: Sign In Policy is 7 days and Resource Policy is 6 hours. A user who signs in and then accesses the Resource right away is not prompted twice. They are prompted if they access the Resource more than 6 hours after sign-in.
- **IdP behavior:** Twingate does not control how the IdP handles authentication. Some IdPs may not ask for a password or other credentials again.

## Prerequisites
- Access to Twingate Security Policy configuration (Resource Policy or Sign In Policy).
- Admin access to your IdP if you need to force credential re-entry.

## Step-by-Step
The page gives no UI steps. General approach:
1. Choose the Resource Policy or Sign In Policy to edit.
2. Set the Authentication rule to the desired re-authentication frequency (for example, 6 hours or 7 days).
3. If true active re-authentication is required, configure your IdP to require a password on every authentication.

## Configuration Values
- Authentication frequency (time interval), for example 6 hours or 7 days. No env vars, CLI flags, or API parameters are listed on this page.

## Gotchas
- Re-authentication at Twingate does not guarantee the user re-enters credentials, since the IdP may silently reuse its own session.
- To force active re-authentication within each session period, require passwords at the IdP on every authentication.
- Authentication windows are shared across policies. A recent sign-in satisfies stricter Resource Policy rules until that rule's own interval elapses.
- The Admin Console authentication policy is fixed and cannot be modified.

## Related Docs
- Security Policies (Resource Policies and Sign In Policy)
- Identity provider configuration docs (for enforcing password prompts)