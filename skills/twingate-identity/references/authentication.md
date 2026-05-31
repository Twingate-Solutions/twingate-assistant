# Twingate Authentication Policy

## Summary
Controls how frequently users must re-authenticate to access Resources. Can be applied to Resource Policies or Minimum Authentication Requirements, but not the Admin Console's authentication policy.

## Key Information
- Sets a time-based re-authentication window for Resource access
- Authentication prompts trigger if user's last auth exceeds the configured time threshold
- Twingate cannot control IdP behavior during re-authentication (IdP may silently re-auth without prompting credentials)
- Authentication windows are **not** additive — a single valid auth session satisfies multiple policies simultaneously

## Prerequisites
- Resource Policy or Minimum Authentication Requirement configured in Admin Console
- Identity provider connected to Twingate

## Configuration Values
| Setting | Scope |
|---|---|
| Authentication frequency (time window) | Resource Policy or Minimum Authentication Requirement |

## Behavior Details
- **Single auth session honors multiple policies**: If Minimum Auth Requirement = 1 day and Resource Policy = 6 hours, a user who just authenticated will not be double-prompted — they only re-authenticate if >6 hours have passed since last auth
- **Policy interaction**: The most restrictive time window in effect determines when re-auth is triggered

## Gotchas
- **IdP passthrough**: Twingate triggers the auth flow, but the IdP may complete it silently (no password re-entry). If active credential re-entry is required, configure the IdP to always prompt for passwords
- Admin Console authentication policy is **not editable**
- Users are not prompted twice even when multiple overlapping policies exist — the single most recent auth timestamp is checked against each policy's window

## Recommendations
- If strict re-authentication (with credential entry) is required, configure your IdP session policy to require passwords on every authentication event
- Test IdP behavior with your specific provider to confirm whether silent re-auth occurs

## Related Docs
- Resource Policies
- Minimum Authentication Requirements
- Security Policies