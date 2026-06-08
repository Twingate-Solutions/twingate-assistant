# Twingate Administration Overview

## Page Title
Administration

## Summary
Top-level administration hub covering Admin Console security configuration, reporting options, and subscription/billing management. Serves as a navigation index to three core administrative areas.

## Key Information
- **Admin Console Security**: Controls authentication policy for admins accessing the Admin Console, including optional 2FA enforcement
- **Reporting**: Provides network-level and user activity reporting across the account
- **Subscription Management**: FAQ-based billing and licensing management

## Sub-Sections

### Admin Console Security
- Admins are governed by a **special authentication policy** separate from standard users
- 2FA can be set as required or optional for Admin Console access
- Configured independently from network access policies

### Reporting
- Covers both **network-level activity** and **user activity**
- Multiple reporting options available (details in dedicated reporting doc)

### Subscription Management
- Billing and licensing handled via subscription management section
- FAQ format for common billing questions

## Prerequisites
- Must have Admin role to access Admin Console settings
- Account must exist on Twingate platform

## Configuration Values
- **2FA enforcement**: Enabled or disabled per Admin Console security policy (boolean toggle)

## Gotchas
- Admin Console authentication policy is **separate** from policies applied to regular network users — changes here only affect admins
- 2FA requirement applies specifically to Admin Console access, not necessarily to general Twingate network access

## Related Docs
- [Reporting](https://www.twingate.com/docs/reporting)
- [Admin Console Security](https://www.twingate.com/docs/admin-console-security)
- [Subscription Management](https://www.twingate.com/docs/subscription)