---
source: https://www.twingate.com/docs/how-sessions-work
type: docs
fetched: 2026-11-13
source_version: 3b40d993064236310d437ca2e05e8d07d37dab2d8e1487ec2ad3bc37e39c5e12
trust: official
---

# How Sessions Work

## Summary
Twingate controls re-authentication frequency with two independent timers: the Sign In Policy session and per-Resource Policy sessions. When a timer expires, Twingate checks a stored copy of the user's IdP session to decide whether re-authentication can be completed silently or requires a redirect to the IdP. Understanding the interaction helps balance security with user friction.

## Key Information
- **Sign In Policy session**: when it expires, the user is signed out of the Twingate Client and must sign in again. It is the baseline gate for all of Twingate.
- **Resource Policy session**: each Resource Policy has its own timer. When it expires, the user must re-authenticate before accessing Resources under that policy.
- **Stored IdP session**: Twingate keeps a copy from the user's last successful sign-in. It is not configurable in Twingate.
  - If still valid: a Twingate-hosted page opens briefly and completes re-auth with no IdP redirect. The user acts only if the Resource Policy requires MFA.
  - If expired: the user is redirected to the IdP, and after success all Twingate timers reset.
- **IdP session lifetime control**:
  - Enterprise IdPs (Okta, Entra ID, Google Workspace, JumpCloud, OneLogin): configurable on the IdP side.
  - Social IdPs (Google, Microsoft, LinkedIn, GitHub): set by the provider and not modifiable.
- **Rolling window**: each successful Resource Policy re-auth resets the Sign In Policy timer to its full duration. Users who stop accessing Resources eventually hit Sign In expiry.
- Other SSO-linked apps manage their own sessions, and Twingate does not influence them.

## Prerequisites
- Admin access to the Twingate Admin Console (or API).
- For enterprise IdPs, access to IdP session settings and SCIM provisioning.

## Example Flow (default Sign In 30 days, Resource Policy 8 hours)
1. The user signs in once and gets a 30-day Sign In session and an 8-hour Resource session.
2. At 8 hours, Twingate checks the stored IdP session. If it is valid, re-auth is automatic. Otherwise the user is redirected to the IdP.
3. Regular Resource access keeps rolling the Sign In timer forward.

## Offboarding (revoke within ~5 minutes)
1. Block the user's devices in Twingate (Admin Console or API). This applies to all IdP types and is enforced within 5 minutes for active connections.
2. Enterprise IdPs: suspend the user in the IdP and revoke active sessions. The SCIM sync to Twingate can take up to an hour.
3. Social logins: disable the user in Twingate. Sessions are revoked in about 5 minutes on average.

Do steps 1 and 2 together for enterprise IdPs, as each covers for a delay in the other.

## Policy Design Recommendations
- **Sign In Policy**: long interval, up to 30 days.
- **Long-lived connections (RDP/SSH)**: 12–16 hours.
- **Short-lived connections (internal web apps)**: 12–16 hours, or shorter for sensitive ones.
- **Business-critical Resources**: shorter than once per day, based on your risk tolerance.
- **Device-only policies**: for Resources that need access without user interaction (system services, monitoring endpoints). They enforce device requirements but skip authentication.

## Gotchas
- Device-only policies do not reset the Sign In Policy timer.
- Social IdPs do not support SCIM, so use device blocking and user disabling.
- Prefer deactivating over deleting users in enterprise IdPs, since this preserves audit logs. The effect on Twingate access is the same.
- A shorter IdP session lifetime causes more IdP redirects. Use Twingate policy timers as the primary control.

## Related Docs
- Device-only Resource Policies
- How to Offboard Users
- Sign In Policy and Resource Policy configuration