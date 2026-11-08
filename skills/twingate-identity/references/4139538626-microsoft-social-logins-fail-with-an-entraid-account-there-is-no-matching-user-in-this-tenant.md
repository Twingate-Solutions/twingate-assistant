---
source: https://help.twingate.com/articles/4139538626-microsoft-social-logins-fail-with-an-entraid-account-there-is-no-matching-user-in-this-tenant
type: help
fetched: 2026-11-08
source_version: 291232bd4e277aadce9868253e58a7fcf4bb998e5820c221567a583705d9b672
trust: official
---

# Microsoft Social Logins Fail: "There is no matching user in this tenant"

## Summary
Microsoft social logins via Entra ID fail when the user's `Mail` attribute is not populated in Entra ID. Twingate requires an email address for all social logins, but Entra ID permits accounts without an associated email. This does not affect logins through a configured Entra ID IdP.

## Key Information
- **Affected component:** Identity Provider — Microsoft (social login) via Entra ID account
- Entra ID allows accounts (admin/service accounts) with a UPN-format username but no `Mail` attribute set
- Twingate **requires** the `Mail` attribute for Microsoft social logins
- Logging in via a tenant's configured Entra ID IdP does **not** require the `Mail` attribute

## Symptoms
- User attempts Microsoft social login from an Entra ID account
- Error returned: `There is no matching user in this tenant`

## Prerequisites
- User must be invited to the Twingate network before login can succeed
- Login URL must be the correct network: `https://<network-name>.twingate.com`

## Troubleshooting Steps

**For Twingate Admins:**
1. Confirm the user has been invited to the Twingate network

**For Twingate Users:**
1. Confirm you are logging into the correct Twingate network URL
2. Confirm the email used for login matches the one registered with Twingate

## Resolution
1. In Entra ID, locate the user account
2. Set the **`Mail`** attribute to a valid email address
3. Ensure this email matches the address the user was invited with in Twingate
4. Retry Microsoft social login

## Gotchas
- An account may appear to have an email (via UPN format) but the `Mail` attribute can still be empty — these are distinct fields in Entra ID
- This issue only affects **social logins**; Entra ID IdP-based logins are unaffected
- Service/admin accounts without email inboxes are common sources of this issue

## Related Docs
- Twingate Identity Provider configuration (Entra ID / Azure AD)
- Microsoft social login setup