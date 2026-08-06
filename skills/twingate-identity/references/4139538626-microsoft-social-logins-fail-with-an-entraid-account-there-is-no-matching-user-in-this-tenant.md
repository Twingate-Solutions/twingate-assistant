---
source: https://help.twingate.com/articles/4139538626-microsoft-social-logins-fail-with-an-entraid-account-there-is-no-matching-user-in-this-tenant
type: help
fetched: 2026-08-06
source_version: b26510ef7fd78aaec53930949370b9f237436135a0bfaf91265395eb287366c5
---

# Microsoft Social Logins Fail: "There is no matching user in this tenant"

## Page Title
Microsoft social logins fail with an EntraID account — There is no matching user in this tenant

## Summary
Entra ID accounts can exist without a populated `Mail` attribute, but Twingate requires an email address for all Microsoft social logins. When the `Mail` attribute is empty in Entra ID, authentication fails with "There is no matching user in this tenant." This does not affect logins through a configured Entra ID IdP integration.

## Key Information
- **Affected component**: Identity Provider — Microsoft (social login) via Entra ID account
- **Root cause**: Entra ID `Mail` attribute is not populated on the user account
- **Scope**: Only affects Microsoft social login flow; Entra ID IdP (tenant-configured) login is unaffected
- **Common affected accounts**: Admin accounts and service accounts that lack an email inbox but have a UPN (`user@domain.tld`)

## Prerequisites
- User must be invited to the Twingate network before login will succeed
- User's email address in Twingate invite must match the `Mail` attribute in Entra ID

## Troubleshooting Steps

**For Twingate Admins:**
1. Confirm the user has been invited to the Twingate network

**For Twingate Users:**
1. Verify you are signing into the correct network: `https://<network>.twingate.com`
2. Confirm the email used matches the one registered in Twingate

## Resolution
An Entra ID administrator must populate the `Mail` attribute on the affected user account:
1. Navigate to the user in Entra ID (Azure AD)
2. Set the **Mail** attribute to a valid email address
3. Ensure this email matches the address used in the Twingate invitation

## Gotchas
- A UPN in `user@domain.tld` format does **not** mean the `Mail` attribute is set — these are separate fields
- The error message "There is no matching user in this tenant" can appear even if the user exists in both Entra ID and Twingate, solely due to the missing `Mail` attribute
- Social login and IdP-configured login have different attribute requirements; missing `Mail` only blocks social login

## Related Docs
- Twingate Identity Provider configuration (Microsoft/Entra ID)
- Twingate user invitation workflow