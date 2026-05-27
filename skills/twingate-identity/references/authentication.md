# Twingate Authentication Policy

## Summary
Controls re-authentication frequency for users accessing Resources. Applies to Resource Policies or Minimum Authentication Requirements. Authentication behavior depends on IdP configuration since Twingate cannot control how the IdP handles the actual authentication challenge.

## Key Information
- Sets time window requiring users to re-authenticate before accessing Resources
- Single authentication satisfies multiple policies if within the time window (no double-prompting)
- Twingate cannot force IdPs to require password re-entry; some IdPs may silently re-authenticate
- Admin Console authentication policy **cannot be edited**

## Applicability
- Resource Policies
- Minimum Authentication Requirements
- ~~Admin Console authentication policy~~ (not configurable)

## Behavior Details
- If user last authenticated **within** the configured window → no re-auth prompt
- If user last authenticated **outside** the configured window → re-auth prompted
- A single login satisfies overlapping policies: authentication timestamp is shared across policies
  - Example: Minimum Auth Requirement = 1 day, Resource Policy = 6 hours → user who just logged in is **not** double-prompted, but will be prompted if accessing the Resource 6+ hours after login

## Configuration Values
| Setting | Description |
|---|---|
| Authentication window | Duration (e.g., 6 hours, 1 day) since last authentication before re-auth is required |

## Gotchas
- **IdP passthrough**: Twingate triggers an IdP authentication flow, but the IdP may complete it silently (SSO session still valid). If active credential re-entry is required, configure the IdP to force password prompts on each authentication.
- **Shared auth timestamp**: The most recent authentication time applies across all policies — the stricter time window governs when the next prompt occurs, but won't cause duplicate prompts within the same session.
- Admin Console policy is fixed and cannot be modified via authentication rules.

## Prerequisites
- Identity provider configured with Twingate
- Resource Policies or Minimum Authentication Requirements set up in Admin Console

## Related Docs
- Resource Policies
- Minimum Authentication Requirements
- Security Policies
- Identity Provider configuration