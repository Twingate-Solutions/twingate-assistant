---
source: https://www.twingate.com/docs/resource-policies
type: docs
fetched: 2026-11-13
source_version: 54fd9d8939d1ae44331b79dda5f353ed2083d35fbb0d1986f6ef48ed967de27a
trust: official
---

# Resource Policies

## Summary
Resource Policies define the authentication, device security, and location requirements users must meet to access a specific Twingate Resource. They are managed in the Admin Console under Policies > Resource Policies tab and assigned per Resource, with optional per-Group overrides.

## Key Information
- Each policy has a name and up to three optional requirement types: Authentication, Device, Location.
- A **Default Policy** exists on every network, is auto-assigned to new Resources, and can be edited but not deleted.
- **Authentication requirements**
  - Authentication frequency: 1 hour to 31 days. On expiry, Twingate checks the stored IdP session; if valid, the user continues uninterrupted, otherwise they are redirected to the IdP.
  - MFA: toggles Twingate's native MFA, enforced at the chosen frequency.
  - Authentication can be disabled entirely to create a device-only policy.
  - Rolling window: any successful authentication resets the timer across all Resources.
- **Device security modes**
  - Any Device (default): meets Approved OS requirements or a Trusted Profile.
  - Only Trusted Devices: must meet a Trusted Profile (Approved OS alone is insufficient).
  - Custom: select specific Trusted Profiles and Approved OS configurations.
- **Location requirements** (Enterprise plan only): allowlist or denylist of countries. Cuba, Iran, North Korea, and Syria are always blocked and cannot be overridden.

## Prerequisites
- Admin Console access.
- Device Profiles configured (via "Manage Device Security") if using Trusted Devices or Custom modes.
- Enterprise plan for geoblocking.

## Steps
**Create a policy:** Policies > Resource Policies tab > Create > name it > set Authentication, Device, and/or Location requirements.

**Assign to a Resource:** Open the Resource detail page > select a policy. It applies to all Groups with access by default.

**Override for a Group:** On the Resource detail page, change the policy on that Group's assignment. To revert to inheriting, reset the override for that Group.

## Policy Disambiguation (multiple applicable policies)
1. Each of the user's Groups contributes its override, or the Resource-level policy if it has no override.
2. If the user already has a session satisfying one applicable policy, that policy is used.
3. Otherwise Twingate selects the easiest policy to satisfy given the user's current state (e.g., no MFA over MFA, or device requirements already met).
4. All requirements of the selected policy are still fully enforced.

## Session Behavior
- A prompt appears about 10 minutes before expiry, only if the user is actively using the Resource.
- Re-authenticating with a valid IdP session happens without redirect and resets all timers; an expired IdP session redirects to the IdP.
- Ignoring or dismissing the prompt ends the session and cuts off access until the user re-authenticates.

## Gotchas
- Group overrides persist even if the Resource-level policy changes; they must be explicitly reset.
- If a user belongs to any Group with an override, the Resource-level policy is not evaluated unless another of their Groups inherits it.
- The "easiest policy" logic means a lenient Group policy can be selected over a stricter one for multi-Group users.
- Authentication in one Resource resets timers for all Resources.

## Related Docs
- Multi-Factor Authentication
- Device Profiles
- Location Requirements
- Device-only Resource Policies
- How Sessions Work