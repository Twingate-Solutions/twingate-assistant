---
source: https://help.twingate.com/articles/4139538626-microsoft-social-logins-fail-with-an-entraid-account-there-is-no-matching-user-in-this-tenant
type: help
fetched: 2026-11-01
source_version: 6a1b61c9bab6093490e2ccfaf1254c237a1b8a62d770366ce6f03352c2a48951
trust: official
---

# Microsoft Social Logins Fail: "There is no matching user in this tenant"

## Summary
Entra ID accounts can exist without a populated `Mail` attribute, but Twingate requires an email address for all Microsoft social logins. When the `Mail` attribute is missing in Entra ID, login fails with "There is no matching user in this tenant."

## Key Information
- Entra ID supports accounts (admin/service accounts) without an associated email address
- Twingate **requires** the `Mail` attribute for Microsoft social logins
- This issue does **not** affect logins via a configured Entra ID IdP — only social login path
- The error message "There is no matching user in this tenant" is the symptom

## Prerequisites
- Affects: Microsoft (social) login via an Entra ID account
- Does **not** affect: Entra ID configured as a tenant IdP

## Troubleshooting Steps

**For Twingate Admins:**
1. Confirm the user has been invited to the Twingate network

**For Twingate Users:**
1. Verify you are signing into the correct Twingate network (`https://<network>.twingate.com`)
2. Confirm the email used for login matches the one registered in Twingate

## Resolution
An Entra ID administrator must populate the `Mail` attribute on the user's account in Entra ID:

1. Open **Entra ID (Azure AD) admin portal**
2. Navigate to the affected user's profile
3. Set/update the **Mail** attribute with a valid email address
4. Ensure this email matches the address invited in Twingate

## Configuration Values
| Attribute | Location | Required For |
|-----------|----------|-------------|
| `Mail` | Entra ID user profile | Microsoft social login |

## Gotchas
- The UPN (`user@domain.tld`) format does **not** substitute for the `Mail` attribute — they are separate fields
- An account can visually appear to have an email in Entra ID while the `Mail` attribute remains unpopulated
- Social login and IdP-based login have different attribute requirements; this issue is specific to social login

## Related Docs
- Twingate Identity Provider configuration (Entra ID)
- Twingate user invitation workflow