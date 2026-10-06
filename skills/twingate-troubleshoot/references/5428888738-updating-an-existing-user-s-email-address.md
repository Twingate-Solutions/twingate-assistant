---
source: https://help.twingate.com/articles/5428888738-updating-an-existing-user-s-email-address
type: help
fetched: 2026-10-04
source_version: 89a2dec84a88267cf079d847ba4973c83afe4884f14965508b0d4be2082bc6ca
trust: official
---

# Updating an Existing User's Email Address

## Summary
Twingate does not support changing the email address on an existing user account because email is tied directly to the Identity Provider (IdP). Neither users nor Twingate support can modify it. The workaround is to create a new user with the new email.

## Key Information
- Email address is bound to the IdP identity — it cannot be changed in-place
- Twingate support has no backend access to modify user emails
- Only viable path is creating a new user account with the new email

## Prerequisites
- Admin access to Twingate to add new users
- Access to manage users in your IdP

## Step-by-Step Workaround
1. Add the new email address as a new user in Twingate
2. Assign the new user to the same Groups/Resources as the original user
3. Have the user log in with the new account
4. Remove or deactivate the old user account when no longer needed

## Gotchas
- No in-place migration of group memberships, resource access, or history — must be manually reassigned to the new user
- The old account will continue to exist and consume a license seat until explicitly removed
- Any device registrations under the old account do not carry over

## Related Docs
- Adding users to Twingate
- Managing Groups and Resource access
- Identity Provider integration setup