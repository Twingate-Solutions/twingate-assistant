# Twingate Authentication Rule

## Summary
The Authentication rule controls how frequently users must re-authenticate to access Resources. It applies to Resource Policies or Minimum Authentication Requirements, but not the Admin Console authentication policy.

## Key Information
- Sets a time-based re-authentication frequency for resource access
- If user hasn't authenticated within the configured window, they're prompted to re-authenticate
- Authentication sessions are shared across policies — a single login satisfies multiple policy checks within the time window
- Twingate cannot control IdP behavior during re-authentication (IdP may silently re-auth without prompting credentials)

## Applicability
- **Resource Policies** ✓
- **Minimum Authentication Requirements** ✓
- **Admin Console authentication policy** ✗ (not editable)

## Configuration Values
| Setting | Description |
|---|---|
| Authentication window | Duration (e.g., 6 hours, 1 day) since last authentication before re-prompt is triggered |

## Behavior Logic
- User accesses a Resource → Twingate checks time since last authentication
- If time elapsed > policy window → user prompted to re-authenticate
- If time elapsed < policy window → no re-authentication required, regardless of other active policies

**Cross-policy example:**
- Minimum Authentication Requirement = 1 day
- Resource Policy = 6 hours
- User who just logged in: **not** prompted twice
- Same user after 6+ hours: **prompted** when accessing the Resource

## Gotchas
- **IdP passthrough**: Twingate triggers the auth flow, but the IdP may complete it silently without requiring password entry. If active credential re-entry is required, configure the IdP to force password prompts on every authentication
- **Shared session clock**: The authentication timer is based on the user's last actual authentication event, not per-policy. A recent login satisfies stricter policies temporarily
- One authentication event satisfies all concurrent policy checks — there is no double-prompting within a single session window

## Related Docs
- Resource Policies
- Minimum Authentication Requirements
- Security Policies