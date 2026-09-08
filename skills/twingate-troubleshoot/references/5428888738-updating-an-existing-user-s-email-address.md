---
source: https://help.twingate.com/articles/5428888738-updating-an-existing-user-s-email-address
type: help
fetched: 2026-09-06
source_version: 3f2f99451fe08519dbbc03c66d55aa6ba75ab20a1d433065c2de915f192ba15f
---

# Updating an Existing User's Email Address

## Summary
Twingate does not support changing the email address on an existing user account because email is tied directly to the Identity Provider (IdP). Neither users nor Twingate support can modify this on the backend. The workaround is to create a new user with the new email address.

## Key Information
- Email address is bound to the IdP identity — it cannot be changed in Twingate
- Twingate support has **no backend ability** to modify user email addresses
- This is a hard limitation, not a permissions/role issue

## Workaround: Replace User Account

1. Add the new email address as a new user in Twingate
2. Assign the new user to the appropriate Groups and Resources
3. Have the user begin logging in with the new account
4. Remove/deactivate the old user account once transition is complete

## Gotchas
- No in-place email migration path exists — treat it as a new user provisioning task
- Group memberships and resource access from the old account must be manually reassigned to the new account
- If using SCIM/automated provisioning, the new email user may be auto-provisioned from the IdP side; ensure the old account is also deprovisioned via IdP

## Related Docs
- User management / adding users
- Identity Provider integration setup
- SCIM provisioning