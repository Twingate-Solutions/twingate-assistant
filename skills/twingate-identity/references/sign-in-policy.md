---
source: https://www.twingate.com/docs/sign-in-policy
type: docs
fetched: 2026-11-13
source_version: 35c02b8416973427dfbd454f10fc971c72573e847b64a413b0a4a48685b01556
trust: official
---

# Sign In Policy

## Summary
The Sign In Policy defines baseline requirements every user must meet to sign in to the Twingate Client. It acts as the first gate: no Resources are visible or accessible until it is satisfied, regardless of how permissive individual Resource Policies are. It is configured in the Admin Console under **Policies > Sign In Policy** tab.

## Key Information
- Three configurable requirements: Device Security, Authentication Frequency, MFA.
- **Device Security**: device must meet either the Approved Operating System requirements or a Trusted Profile from Device Profiles. Changes to Device Profiles automatically apply to the Sign In Policy. Non-compliant devices are blocked from signing in entirely.
- **Authentication Frequency**: how often users must re-authenticate via the IdP. Intervals range from 7 to 31 days. The timer is a rolling window that resets whenever a Resource Policy re-authentication succeeds, so active users get extended sessions.
- **Session expiry**: user is signed out of the Client and prompted to authenticate via the IdP.
- **MFA**: optionally require Twingate native MFA at each sign-in; frequency is tied to the authentication frequency.
- **Sign In Policy vs. Resource Policies**:
  - Sign In Policy: evaluated at sign-in and when the session timer expires; controls Client access.
  - Resource Policies: evaluated per Resource access when that policy's auth timer has expired; provide per-Resource controls.
- A lenient Sign In Policy (e.g., 30 days) is reasonable, with stricter requirements enforced via Resource Policies.
- Sign-in sessions persist across Client restarts and device reboots. Resource Policy sessions do not.
- The Admin Console has a separate sign-in policy (**Settings > Admin Console Security**), independent of the Client Sign In Policy.

## Prerequisites
- Admin Console access.
- Device Profiles configured (for Trusted Profile-based Device Security).
- IdP integrated with Twingate.

## Step-by-Step
1. In the Admin Console, go to **Policies > Sign In Policy**.
2. Set Device Security (Approved OS requirements or Trusted Profile).
3. Choose the authentication frequency (7–31 days).
4. Optionally enable Twingate MFA.
5. Save.

## Configuration Values
- Authentication frequency: 7 days to 31 days.
- MFA: on/off.
- Device Security: Approved Operating System or Trusted Profile (managed in Device Profiles).

## Gotchas
- Enabling MFA in both the IdP and the Sign In Policy makes users complete MFA twice. Generally configure MFA in only one place.
- Devices failing Device Security are fully blocked from sign-in, not just from specific Resources.
- Sign In Policy settings do not govern Admin Console access.
- Sign-in sessions survive restarts; users stay signed in until expiry or an explicit sign-out.

## Related Docs
- Device Profiles
- How Sessions Work
- Multi-Factor Authentication
- Admin Console Security
- Resource Policies