---
source: https://help.twingate.com/articles/5428888738-updating-an-existing-user-s-email-address
type: help
fetched: 2026-11-01
source_version: e38f0a6ce242368edcf3777f7d08fbc73424daf9c8e0b97a4d1d12ad6fb6980c
trust: official
---

# Updating an Existing User's Email Address

## Summary
Twingate does not support changing the email address on an existing user account because email is tied directly to the Identity Provider (IdP). Neither users nor Twingate support can modify it. The workaround is to create a new user account with the new email.

## Key Information
- Email addresses are immutable on existing Twingate accounts
- The constraint is at the IdP integration level, not a UI limitation
- Twingate backend support cannot override this restriction
- No in-place migration of permissions/groups from old to new account

## Workaround: New Account Creation

1. Add the new email address as a new user in Twingate admin console
2. Assign the new user to the appropriate Groups and Resources
3. Have the user log in with the new account
4. Deactivate or remove the old account once transition is complete

## Gotchas
- The new account will **not** inherit group memberships, resource access, or any settings from the old account — these must be reassigned manually
- If using automated provisioning (SCIM), the new email must exist in the IdP and be provisioned through the normal sync process
- Ensure the old account is explicitly disabled/removed to avoid license seat waste and security gaps

## Related Docs
- User management / adding users
- Identity Provider (SSO) configuration
- SCIM provisioning setup