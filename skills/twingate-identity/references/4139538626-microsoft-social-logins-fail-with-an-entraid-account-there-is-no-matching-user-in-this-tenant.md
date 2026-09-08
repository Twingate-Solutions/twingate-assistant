---
source: https://help.twingate.com/articles/4139538626-microsoft-social-logins-fail-with-an-entraid-account-there-is-no-matching-user-in-this-tenant
type: help
fetched: 2026-09-06
source_version: 92d372231ab912069c29c70505d0326e1fba99eec41e9f3f6d0a0a8776a78935
---

# Microsoft Social Logins Fail: "There is no matching user in this tenant"

## Page Title
Microsoft social logins fail with an EntraID account — There is no matching user in this tenant

## Summary
Entra ID accounts (particularly admin/service accounts) can exist without a populated `Mail` attribute, even though they have a UPN-format username. Twingate requires a valid email address for Microsoft social logins, so users with unpopulated `Mail` attributes will fail authentication with "There is no matching user in this tenant."

## Key Information
- **Affected component**: Identity Provider - Microsoft (social) via Entra ID account
- Email is **required** for Microsoft social logins but **not** required for tenant-configured Entra ID IdP logins
- Entra ID UPN (`user@domain.tld`) does not guarantee the `Mail` attribute is populated
- Admin and service accounts are most commonly affected
- Error occurs even if the user appears to have an email address in the directory

## Prerequisites
- User must be invited to the Twingate network
- User must be signing in to the correct tenant URL (`https://<network>.twingate.com`)
- The `Mail` attribute in Entra ID must be populated

## Troubleshooting Steps

**For Twingate Admins:**
1. Confirm the user has been invited to the Twingate network

**For Twingate Users:**
1. Verify you are signing in to the correct Twingate network URL
2. Confirm the email used matches the one registered with Twingate

## Resolution
The Entra ID administrator must populate the `Mail` attribute for the affected account:

1. Open **Entra ID (Azure Active Directory)** admin portal
2. Navigate to the affected user's profile
3. Set/update the **Mail** attribute with a valid email address
4. Ensure this email matches the address invited in Twingate
5. Retry Microsoft social login

## Configuration Values
| Attribute | Location | Required For |
|-----------|----------|--------------|
| `Mail` | Entra ID user profile | Microsoft social login |
| UPN | Entra ID user profile | Not sufficient alone |

## Gotchas
- UPN format (`user@domain.tld`) is **not** the same as the `Mail` attribute — do not assume UPN presence means email is set
- This issue does **not** affect users authenticating via a configured Entra ID IdP (only social login)
- Admin/service accounts are commonly provisioned without the `Mail` attribute

## Related Docs
- Twingate Identity Provider configuration (Entra ID/Azure AD)
- Microsoft social login setup