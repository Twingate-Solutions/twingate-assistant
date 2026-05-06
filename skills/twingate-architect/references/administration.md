# Twingate Administration Overview

## Page Title
Administration

## Summary
Top-level administration page covering Admin Console security configuration, reporting options, and subscription/billing management. Serves as a navigation hub linking to three core administrative areas.

## Key Information
- **Admin Console Security**: Controls authentication policy for admins accessing the Admin Console, including optional 2FA enforcement
- **Reporting**: Provides network-level and user activity reporting across the account
- **Subscription Management**: Covers billing, licensing FAQs, and plan changes

## Sub-sections

### Admin Console Security
- Admins are governed by a **special authentication policy** separate from regular users
- 2FA can be configured as required or optional for Admin Console access

### Reporting
- Available options cover both **network-level activity** and **user activity**
- See dedicated reporting docs for full option details

### Subscription Management
- Handles billing and licensing model questions
- Plan/subscription changes managed here

## Prerequisites
- Must have Admin role to access Admin Console settings
- Account must exist on Twingate

## Gotchas
- Admin Console authentication policy is **separate** from standard user authentication policies — changes here only affect admin access, not end-user access
- 2FA enforcement for admins is configurable (not on by default — verify current default in sub-pages)

## Related Docs
- [Reporting](https://www.twingate.com/docs/reporting)
- [Admin Console Security](https://www.twingate.com/docs/admin-console-security)
- [Subscription Management](https://www.twingate.com/docs/subscription-management)