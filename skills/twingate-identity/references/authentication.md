# Twingate Authentication Policy Rule

## Page Title
Authentication (Policy Rule)

## Summary
The Authentication rule controls how frequently users must re-authenticate to access Resources. It applies to Resource Policies or Minimum Authentication Requirements, but cannot be applied to the Admin Console's authentication policy.

## Key Information
- Sets re-authentication frequency (time window) for resource access
- Twingate does not control IdP behavior during re-authentication — the IdP may not require password re-entry
- Authentication is shared across policies: a valid session satisfies multiple policy checks within the same time window
- If authenticated within the window, users won't be prompted again even if different Security Policies apply

## Prerequisites
- At least one Resource Policy or Minimum Authentication Requirement configured
- Identity provider (IdP) connected to Twingate

## Configuration Values
| Parameter | Description |
|-----------|-------------|
| Time window | Duration since last authentication (e.g., 6 hours, 1 day) |

## How It Works (Step-by-Step)
1. User attempts to access a Resource with an Authentication rule applied
2. Twingate checks when the user last authenticated
3. If last authentication is **within** the defined window → access granted, no prompt
4. If last authentication is **outside** the window → user is prompted to re-authenticate via IdP
5. Re-authentication delegates to the IdP (Twingate does not enforce credential entry)

## Gotchas
- **IdP passthrough**: Twingate cannot force the IdP to require passwords. Some IdPs silently re-authenticate users without credential prompts — configure your IdP to require passwords each session if active re-authentication is critical
- **Session reuse across policies**: A single authentication satisfies all policy checks within that time window. Example: Minimum Authentication Requirement = 1 day, Resource Policy = 6 hours — a user who authenticated 5 hours ago passes the 6-hour resource check without a second prompt, but would be blocked after 6 hours
- **Admin Console policy is not editable** via this rule

## Related Docs
- Resource Policies
- Minimum Authentication Requirements
- Security Policies
- Identity Provider configuration