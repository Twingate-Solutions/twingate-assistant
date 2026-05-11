# Twingate Authentication Policy Rule

## Page Title
Authentication (Rule Reference)

## Summary
The Authentication rule controls how frequently users must re-authenticate to access Resources. It applies to Resource Policies or Minimum Authentication Requirements, but not the Admin Console's authentication policy. Re-authentication behavior depends partly on IdP configuration.

## Key Information
- **Scope**: Applies to Resource Policies and Minimum Authentication Requirements only; Admin Console auth policy is not editable
- **Mechanism**: If a user hasn't authenticated within the configured time window, they are prompted to re-authenticate on Resource access
- **Session reuse**: A valid authentication session satisfies all policies within that window—users are not prompted multiple times for different policies
- **IdP dependency**: Twingate cannot control whether the IdP actually requires credential re-entry; some providers silently re-authenticate without prompting the user

## Prerequisites
- Resource Policy or Minimum Authentication Requirement configured in Admin Console
- Identity provider (IdP) integrated with Twingate

## Configuration Values
| Parameter | Description | Example |
|-----------|-------------|---------|
| Authentication frequency | Time window before re-authentication is required | 6 hours, 1 day |

## Behavior Logic
- User attempts Resource access → check last authentication timestamp
- If time since last auth **exceeds** the policy window → prompt for re-authentication
- If time since last auth **is within** the policy window → access granted, no prompt
- **Interaction between policies**: The most recently satisfied auth timestamp is used across all policies. Example: Minimum Auth Requirement = 1 day, Resource Policy = 6 hours — user who authenticated at T=0 accesses the resource at T=5h (no prompt); accessing at T=7h triggers re-auth

## Gotchas
- **IdP silent re-auth**: If your IdP uses SSO session cookies, users may be "re-authenticated" without entering credentials. Configure your IdP to require passwords on each authentication if active verification is required
- **Cross-policy session sharing**: A single authentication event satisfies multiple overlapping policies simultaneously — a stricter Resource Policy does not force re-auth if the user recently authenticated for a less strict policy
- **Admin Console excluded**: You cannot modify authentication policy for the Admin Console itself

## Related Docs
- Resource Policies
- Minimum Authentication Requirements
- Security Policies
- Identity Provider Integration