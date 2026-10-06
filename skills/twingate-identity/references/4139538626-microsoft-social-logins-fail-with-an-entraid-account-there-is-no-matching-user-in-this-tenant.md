---
source: https://help.twingate.com/articles/4139538626-microsoft-social-logins-fail-with-an-entraid-account-there-is-no-matching-user-in-this-tenant
type: help
fetched: 2026-10-04
source_version: 5f9ce11faea8d3c9a7d457eb62fa685e863ba6b8d5be9e0fa919095e0ea58818
trust: official
---

# Microsoft Social Logins Fail: "There is no matching user in this tenant"

## Summary
Entra ID accounts can exist without a populated `Mail` attribute, but Twingate requires an email address for all Microsoft social logins. When the `Mail` attribute is missing in Entra ID, authentication fails with "There is no matching user in this tenant."

## Key Information
- **Affected component:** Identity Provider — Microsoft (social login) via Entra ID account
- Admin/service accounts in Entra ID often have a UPN (`user@domain.tld`) but no associated email (`Mail` attribute)
- This distinction does **not** affect Entra ID IdP (tenant-configured) logins — only social logins
- Twingate matches social login users by email; missing `Mail` attribute causes lookup failure

## Prerequisites
- Twingate Admin access to invite/manage users
- Entra ID admin access to update user attributes

## Troubleshooting Steps

**For Twingate Admins:**
1. Confirm the user has been invited to the Twingate network

**For Twingate Users:**
1. Verify you are signing into the correct network: `https://<network-name>.twingate.com`
2. Confirm the email used matches the one registered in Twingate

## Resolution

An Entra ID administrator must populate the `Mail` attribute for the affected user account:

1. Open **Microsoft Entra admin center** (or Azure AD portal)
2. Navigate to the affected user's profile
3. Set/update the **Mail** attribute with the user's email address
4. Retry the Microsoft social login in Twingate

## Configuration Values
| Attribute | Location | Required for Social Login |
|-----------|----------|--------------------------|
| `Mail` | Entra ID user profile | Yes |
| UPN (`user@domain.tld`) | Entra ID user profile | Not sufficient alone |

## Gotchas
- UPN format does **not** substitute for the `Mail` attribute — both can exist independently in Entra ID
- This issue only affects **social logins**; Entra ID IdP (federated/tenant) logins do not require the `Mail` attribute
- Admin and service accounts are most commonly affected since they often lack a real mailbox

## Related Docs
- Twingate Identity Provider configuration — Microsoft Entra ID
- Twingate user invitation workflow