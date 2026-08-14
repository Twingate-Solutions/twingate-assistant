---
source: https://www.twingate.com/docs/authentication
type: docs
fetched: 2026-08-14
source_version: 463f9ea739368196dbf19b2cbf6c621c9985d1e21dced10197999b98530c472a
---

# Twingate Authentication Rule

## Page Title
Authentication (Security Policy Rule)

## Summary
The Authentication rule controls how frequently users must re-authenticate to access Resources. It can be applied to Resource Policies or Minimum Authentication Requirements, but not the Admin Console's authentication policy.

## Key Information
- Sets a time window (e.g., 6 hours) within which a prior authentication is considered valid
- If a user authenticated within the window, they won't be re-prompted—even across different Security Policies
- Twingate cannot control IdP behavior; some providers may silently re-authenticate without requiring user credentials
- Authentication windows are evaluated against the user's last sign-in time, not per-policy

## Prerequisites
- Resource Policies or Minimum Authentication Requirements configured in Admin Console
- Identity provider (IdP) connected to Twingate

## Configuration Values
| Field | Description |
|-------|-------------|
| Authentication frequency | Time duration (e.g., 1 hour, 6 hours, 1 day) after which re-authentication is required |

**Applicable to:**
- Resource Policies
- Minimum Authentication Requirements

**Not applicable to:**
- Admin Console authentication policy (cannot be edited)

## Behavior / Gotchas

- **Silent IdP re-auth**: Twingate cannot force your IdP to prompt for credentials. If active re-authentication matters, configure your IdP to require passwords on every authentication event.
- **Cross-policy deduplication**: A user authenticated within *any* valid window won't be prompted again, even if a stricter policy applies. Example: Minimum Requirement = 1 day, Resource Policy = 6 hours → user who just logged in accesses resource without re-auth, but will be prompted after 6 hours of inactivity.
- **Window is not per-session-start**: The clock runs from the user's last authentication time, not from when they first attempt resource access.

## Step-by-Step (Applying the Rule)
1. Navigate to Admin Console → Security Policies
2. Select or create a Resource Policy or Minimum Authentication Requirement
3. Add the Authentication rule
4. Set the desired time frequency
5. Save and apply the policy to relevant Resources or Groups

## Related Docs
- Resource Policies
- Minimum Authentication Requirements
- Security Policies overview
- Identity Provider configuration