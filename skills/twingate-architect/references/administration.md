# Twingate Administration Overview

## Page Title
Administration

## Summary
The Administration section covers configuration of Admin Console security settings, reporting options, and subscription/billing management. It serves as a hub linking to three core administrative functions within Twingate.

## Key Information
- **Three primary administrative areas:**
  - Reporting (network-level and user activity)
  - Admin Console Security (2FA enforcement)
  - Subscription Management (billing and licensing)

## Admin Console Security
- Admins accessing the Admin Console are governed by a **special authentication policy** separate from regular users
- Configurable option to **require or not require 2FA** for Admin Console access
- Setting applies account-wide for all admin users

## Reporting
- Provides both **network-level** and **user activity** reporting
- Details available in dedicated reporting documentation

## Subscription Management
- FAQ-based resource for billing and licensing questions
- Managed via dedicated subscription management page

## Prerequisites
- Admin role with access to the Twingate Admin Console
- Account must be active on a Twingate plan

## Gotchas
- Admin Console authentication policy is **distinct** from user authentication policies — changes here only affect admin access, not end-user access
- 2FA enforcement for admins is a separate control from 2FA settings applied to regular network users

## Related Docs
- [Reporting](https://www.twingate.com/docs/reporting)
- [Admin Console Security](https://www.twingate.com/docs/admin-console-security)
- [Subscription Management](https://www.twingate.com/docs/subscription)