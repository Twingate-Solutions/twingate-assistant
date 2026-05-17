# Twingate Administration

## Page Title
Administration Overview

## Summary
Top-level administration hub covering Admin Console security configuration, reporting options, and subscription/billing management. Serves as a navigation index to three core admin areas.

## Key Information
- **Admin Console Security**: Controls authentication policy for admins accessing the Admin Console, including optional 2FA enforcement
- **Reporting**: Provides network-level and user activity reporting across the account
- **Subscription Management**: FAQ-based billing and licensing information

## Prerequisites
- Admin role with access to Twingate Admin Console

## Sub-Sections

### Admin Console Security
- Admins are governed by a **special authentication policy** separate from regular users
- 2FA can be set as **required or optional** for Admin Console access
- Configuration is distinct from user-facing authentication policies

### Reporting
- Covers both **network-level activity** and **user activity**
- Multiple reporting options available (details in dedicated reporting docs)

### Subscription Management
- Billing and licensing handled via subscription management section
- FAQ format for common billing questions

## Configuration Values
- 2FA enforcement: toggle required/not required per admin policy

## Gotchas
- Admin Console authentication policy is **separate** from standard user authentication policies — changes here only affect admin access, not end-user access
- 2FA settings for admins must be configured explicitly; do not assume they inherit user policy settings

## Related Docs
- [Reporting](https://www.twingate.com/docs/reporting)
- [Admin Console Security](https://www.twingate.com/docs/admin-console-security)
- [Subscription Management](https://www.twingate.com/docs/subscription-management)