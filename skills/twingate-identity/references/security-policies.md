---
source: https://www.twingate.com/docs/security-policies
type: docs
fetched: 2026-11-13
source_version: 8f39d7df3d043a4f87c0789fb19d306037087d4562278b99e9bcdc04113b5c58
trust: official
---

# Security Policies

## Summary
Twingate access control is configured in the Admin Console under the **Policies** tab, which has three sections: Resource Policies, Sign In Policy, and Device Profiles. A user must satisfy all applicable layers (device, sign-in, resource) to access a Resource.

## Key Information
- **Resource Policies**: per-Resource requirements, with up to three types:
  - Authentication: re-auth frequency and MFA.
  - Device Security: Trusted Profiles or approved OSes.
  - Location: country-level geoblocking (Enterprise only).
- A **Default Policy** is auto-assigned to new Resources.
- Policies are assigned at the Resource level and apply to all Groups with access. Groups can have **overrides**.
- **Sign In Policy**: baseline for signing in to the Client. Requires device security, authentication frequency, and optional native MFA.
- **Device Profiles**:
  - *Trusted Profiles*: one platform each. Verification methods: Manual, CrowdStrike, Intune, Jamf, Iru, SentinelOne, 1Password. Can add posture checks.
  - *Approved Operating Systems*: enable or disable each platform. Native posture checks include disk encryption, screen lock, firewall, and minimum OS version (varies by platform).
- **Evaluation order**:
  1. Device Profiles, checked at sign-in and about every 5 minutes.
  2. Sign In Policy.
  3. Resource Policy.
- A successful Resource Policy re-auth resets the Sign In session timer if its requirements are a superset of the Sign In Policy's.
- Authentication can be disabled on a Resource Policy to make it device-only. The user's Sign In session must still be valid.

## Prerequisites
- Admin Console access.
- For Trusted Profiles beyond manual verification: an MDM/EDR integration (CrowdStrike, Intune, Jamf, Iru, SentinelOne, or 1Password).
- Enterprise plan for geoblocking.

## Step-by-Step (recommended pattern)
1. Define Device Profiles (Trusted Profiles and Approved OSes).
2. Set a lenient Sign In Policy (e.g., 30-day auth frequency).
3. Create stricter Resource Policies for sensitive Resources.
4. Assign the strictest policy at the Resource level.
5. Add Group-level overrides only where relaxation is needed.

## Configuration Values
- Example policy name: `1D-MFA-AllTrusted` (1-day session, MFA required, Trusted devices only).
- Device re-check interval: ~5 minutes.
- Admin Console sign-in: fixed at 1 hour (static, not rolling, not configurable).
- No env vars, CLI flags, or API params are given on this page.

## Gotchas
- A Group override always beats the Resource-level policy. If any of a user's Groups has an override, Twingate compares only the policies tied to the user's Groups. A Group without an override contributes the Resource-level policy to that comparison.
- Overrides persist after the Resource-level policy changes until explicitly reset.
- Blocking a platform in Approved Operating Systems prevents sign-in unless the device matches a Trusted Profile for that platform.
- Twingate stores the IdP session expiry captured at sign-in. It redirects to the IdP only once that stored expiry has passed, so IdP session lifetime affects re-auth behavior.
- The Sign In session timer is rolling and resets on qualifying Resource Policy re-auth.

## Related Docs
- Resource Policies
- How Twingate resolves multiple policies
- Device-only Resource Policies
- How Sessions Work
- Device Profiles
- Approved Operating Systems
- Device Posture Checks
- Admin Console Security