---
source: https://help.twingate.com/articles/5428888738-updating-an-existing-user-s-email-address
type: help
fetched: 2026-08-06
source_version: af5c2036d9cf29259264429064e92e17f2c8b36dd9680678855caa60dc562881
---

# Updating an Existing User's Email Address

## Summary
Twingate does not support email address changes for existing user accounts because email is tied directly to the Identity Provider (IdP). Neither users nor Twingate support can modify email addresses on existing accounts.

## Key Information
- Email address is bound to the IdP used for authentication — it cannot be decoupled
- Twingate support has no backend ability to change a user's email
- Self-service email updates are not available to users

## Workaround: Add New User Account
The only supported solution is to create a new user with the updated email address:

1. Add the new email address as a new user in Twingate
2. Assign the same Groups/Resources as the original account
3. Have the user begin logging in with the new account
4. Remove or deactivate the old user account when no longer needed

## Gotchas
- No migration of existing account history or sessions to the new account
- Group memberships and Resource access must be manually reassigned to the new account
- If using SSO/IdP sync (e.g., Okta, Azure AD), the new email must exist in the IdP first before it can authenticate

## Related Docs
- Adding users to Twingate
- Identity Provider integration setup
- Managing user Groups and Resource access