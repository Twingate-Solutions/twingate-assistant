# Twingate Authentication Rule

## Page Title
Authentication (Rule Configuration)

## Summary
The Authentication rule controls how frequently users must re-authenticate to access Resources. It can be applied to Resource Policies or Minimum Authentication Requirements. Twingate delegates actual credential verification to the configured identity provider.

## Key Information
- Sets a time window for how often users must re-authenticate
- Applies to: **Resource Policies** or **Minimum Authentication Requirements**
- Admin Console authentication policy is **not editable**
- Authentication is scoped to a time window — if already authenticated within the window, no re-prompt occurs
- A single authentication satisfies multiple policies simultaneously (no double-prompting)
- Twingate cannot control IdP behavior — some IdPs may silently re-authenticate without prompting for credentials

## Configuration Values
| Setting | Description |
|---|---|
| Authentication window | Time duration (e.g., 6 hours, 1 day) after which re-authentication is required |

## Behavior Logic
- User accesses Resource → checks if authenticated within the configured window
- If **within** window → access granted, no re-auth
- If **outside** window → re-authentication prompt triggered via IdP
- One authentication satisfies all policy checks simultaneously:
  - Example: Minimum Auth Requirement = 1 day, Resource Policy = 6 hours → user who just logged in is **not** double-prompted, but will be prompted if accessing the resource >6 hours after sign-in

## Prerequisites
- Identity provider (IdP) configured with Twingate
- Resource Policies or Minimum Authentication Requirements configured in Admin Console

## Gotchas
- **IdP passthrough behavior**: Twingate triggers re-authentication, but the IdP controls whether the user actually sees a credential prompt. Silent SSO re-auth may occur without user interaction.
- **Recommended IdP config**: If active re-authentication is required, configure your IdP to require passwords on every authentication event.
- **Admin Console policy is fixed**: Cannot be modified via authentication rules.
- **Cross-policy satisfaction**: A stricter Resource Policy window does not force a second auth if the user already authenticated within that window — timing from initial sign-in is what matters.

## Related Docs
- Resource Policies
- Minimum Authentication Requirements
- Security Policies
- Identity Provider Configuration