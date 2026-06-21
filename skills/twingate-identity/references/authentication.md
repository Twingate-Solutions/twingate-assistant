# Twingate Authentication Rule

## Summary
The Authentication rule controls how frequently users must re-authenticate to access Resources. It applies to Resource Policies or Minimum Authentication Requirements, but not the Admin Console's authentication policy.

## Key Information
- Sets a time window after which users must re-authenticate before accessing a Resource
- Twingate cannot control how the IdP handles the actual authentication challenge (provider may silently re-authenticate without prompting credentials)
- Authentication sessions are shared across policies — a valid session satisfies multiple policy checks within the time window
- The most restrictive time window governs when a user is actually prompted

## Prerequisites
- Resource Policy or Minimum Authentication Requirement configured in Admin Console
- Identity provider connected to Twingate

## Configuration Values
| Setting | Scope |
|---|---|
| Authentication frequency (time window) | Resource Policy or Minimum Authentication Requirement |

Examples: `6 hours`, `1 day`

## Behavior / Logic

**Session reuse across policies:**
- If Minimum Authentication Requirement = 1 day and Resource Policy = 6 hours:
  - User authenticates → accesses Resource immediately → **no second prompt**
  - User tries to access Resource >6 hours after last auth → **prompted to re-authenticate**

## Gotchas
- **IdP silent re-auth**: Twingate triggers re-authentication but cannot force the IdP to prompt for credentials. If active credential entry is required, configure the IdP to require passwords on every authentication.
- **Admin Console policy is not editable** via this rule.
- A single authentication event satisfies all concurrent policy windows — users won't be double-prompted within the same session.

## Related Docs
- Resource Policies
- Minimum Authentication Requirements
- Security Policies