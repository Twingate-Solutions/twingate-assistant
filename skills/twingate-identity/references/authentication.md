# Authentication Rule – Twingate

## Summary
Controls how frequently users must re-authenticate to access Resources. Applied via Resource Policies or Minimum Authentication Requirements. Authentication frequency is enforced by Twingate, but the actual credential challenge depends on IdP configuration.

## Key Information
- Sets a time window requiring re-authentication (e.g., every 6 hours)
- Applies to: **Resource Policies** or **Minimum Authentication Requirements**
- Admin Console authentication policy is **not editable**
- Authentication state is shared across policies — a user authenticated within the window won't be prompted again, even for a stricter policy
- Twingate cannot force IdPs to prompt for credentials; some providers silently re-authenticate

## Prerequisites
- Resource Policy or Minimum Authentication Requirement configured in Admin Console
- Identity provider (IdP) connected to Twingate

## Configuration Values
| Setting | Description |
|---|---|
| Authentication frequency | Time window (e.g., 1 hour, 6 hours, 1 day) after which re-authentication is required |

## Gotchas
- **IdP silent auth**: If your IdP has SSO sessions, users may be "re-authenticated" without entering credentials. Configure your IdP to require passwords on every auth if active re-authentication is required.
- **Cross-policy auth sharing**: Authentication satisfies all concurrent policies. Example — if Minimum Auth Requirement = 1 day and Resource Policy = 6 hours, a user logged in at T=0 can access the resource at T=5h without re-authenticating, but will be prompted after T=6h.
- Stricter Resource Policy does **not** override a recent authentication from a looser policy within the same session window.

## Related Docs
- Resource Policies
- Minimum Authentication Requirements
- Security Policies