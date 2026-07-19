# Twingate Administration

## Page Title
Administration Overview

## Summary
This page serves as a top-level navigation hub for Twingate administration topics. It covers Admin Console security configuration, reporting options, and subscription/billing management.

## Key Information
- **Reporting**: Network-level and user activity reporting available within the account
- **Admin Console Security**: Special authentication policy governs admin access; 2FA can be required or made optional
- **Subscription Management**: Billing and licensing FAQ and management tools available

## Prerequisites
- Admin-level access to the Twingate Admin Console

## Core Administration Areas

### Admin Console Security
- Admins accessing the Admin Console are subject to a dedicated authentication policy
- 2FA enforcement is configurable (required vs. optional)
- See: Admin Console Security docs for configuration steps

### Reporting
- Provides visibility into network-level activity and user activity
- See: Reporting docs for available report types

### Subscription Management
- Covers billing model and licensing questions
- See: Subscription Management docs for plan changes and FAQs

## Gotchas
- Admin Console authentication policy is **separate** from standard user authentication policies — changes here only affect admin access, not end-user access
- 2FA settings for the Admin Console must be configured explicitly; default behavior may not enforce 2FA

## Related Docs
- [Reporting](https://www.twingate.com/docs/reporting)
- [Admin Console Security](https://www.twingate.com/docs/admin-console-security)
- [Subscription Management](https://www.twingate.com/docs/subscription-management)