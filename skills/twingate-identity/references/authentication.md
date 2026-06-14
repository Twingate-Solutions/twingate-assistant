# Twingate Authentication Policy Rule

## Page Title
Authentication (Policy Rule)

## Summary
Controls how frequently users must re-authenticate to access Resources. Applies to Resource Policies or Minimum Authentication Requirements. The authentication window is checked against the user's last authentication time, not per-policy.

## Key Information
- Authentication frequency is measured from the user's **last authentication time**, not session start
- A single recent authentication satisfies multiple policies simultaneously — no double-prompting
- Twingate cannot control IdP behavior during re-authentication (user may not be prompted for credentials)
- Admin Console authentication policy is **not editable**

## Prerequisites
- Access to Twingate Admin Console
- Configured Identity Provider (IdP)
- Resource Policies or Minimum Authentication Requirements to attach rules to

## Configuration Values
| Setting | Description |
|---|---|
| Authentication frequency | Time window (e.g., 6 hours, 1 day) after which re-authentication is required |

## Step-by-Step
1. Navigate to Admin Console → Security Policies
2. Select or create a **Resource Policy** or **Minimum Authentication Requirement**
3. Add an Authentication rule
4. Set the desired re-authentication frequency (time window)
5. Save and apply to relevant Resources or groups

## Gotchas
- **IdP passthrough**: Twingate triggers the authentication flow, but the IdP may silently re-authenticate without prompting the user for credentials. To enforce active credential entry, configure your IdP to require passwords on every authentication.
- **Cross-policy satisfaction**: If Minimum Authentication Requirement = 1 day and a Resource Policy = 6 hours, a user who authenticated within 6 hours satisfies **both** — no second prompt. Only the strictest time window matters for triggering re-auth.
- **Admin Console policy is fixed** — cannot be customized via authentication rules.

## Related Docs
- Resource Policies
- Minimum Authentication Requirements
- Security Policies overview
- Identity Provider configuration