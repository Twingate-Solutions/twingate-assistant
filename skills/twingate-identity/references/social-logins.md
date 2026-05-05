## Social Logins

When no enterprise IdP is configured, Twingate supports four social login providers for end-user authentication. Admins manage users directly in the Admin Console.

### Supported Providers

- Google
- Microsoft
- LinkedIn
- GitHub

Users can sign in with **any** of these as long as the email address on the social account matches the email registered in Twingate.

### Inviting Users

1. **Team page** -> Users tab
2. Click **Add User**
3. Enter the user's email address
4. Click **Send Invite Email**

The user receives an email with:
- Link to download the Twingate Client
- Instructions to sign in for the first time

The user must accept the invite via email before signing in.

### Managing Users

User row -> three-dot menu:

| Action | Effect |
|---|---|
| **Edit** | Update display name |
| **Manage Role** | Set Admin / DevOps / Support / Access Reviewer (see /docs/admins) |
| **Disable** | Block sign-in; user remains in Twingate (still billable) |
| **Remove** | Permanently delete user (no longer billable) |

### Decision Notes

- **Social logins are for small teams or trial deployments** -- production deployments should use a real IdP (Okta, Entra ID, Google Workspace, etc.) for SCIM-driven user lifecycle management
- For mixed environments: Twingate supports multiple IdPs (e.g., Google Workspace + GitHub social) -- see /docs/identity-providers
- Email-matching is the binding mechanism -- users with multiple email addresses can sign in via different social providers as long as one matches their Twingate-registered email

### Gotchas

- **Users with non-matching emails cannot sign in** -- enforce a single canonical email per user
- **Disabled users still cost money** -- delete unused users to reduce billing
- Social provider availability depends on user's existing accounts -- not every user has a Google or GitHub account
- Social login does not provide SCIM provisioning -- onboarding/offboarding is fully manual via Admin Console

### Related Docs

- /docs/users -- User management overview
- /docs/admins -- Admin role assignment
- /docs/offboarding-users -- Disable vs. delete for social-login users
- /docs/identity-providers -- Enterprise IdP alternatives (Okta, Entra ID, etc.)
